import os
import sys
from pyspark import SparkContext


def matrix_multiply(matrixfile, vectorfile):
    """
    compute matrix multiply by vector
    :param: first para is the matrix file; second para is the vector file
    :returns: RDD object of matrix*vector
    """
    #read file and save to local storage
    Matrix = sc.textFile(matrixfile).cache()
    Vector = sc.textFile(vectorfile).cache()
    
    #split by "," for each line and read element as str
    Matrix = Matrix.map(lambda l: l.split(',')).map(lambda l: [str(x) for x in l])

    #create row index
    Matrix = Matrix.zipWithIndex().map(lambda l: (int(l[1]), l[0]))

    #create col index: (i,((Ai1, 1), (Ai2,2),.. (Ain, n)))
    Matrix = Matrix.map(lambda l: (l[0], [(i,j) for (i,j) in enumerate(l[1])]))

    #change row&col index position: (j, (Aij,i))
    Matrix = Matrix.flatMap(lambda l: [(x[0],(l[0],x[1])) for x in l[1]])

    #group by col index
    Matrix_col = Matrix.groupBy(lambda l: l[0])
    
    #split by "," for each line and read element as str
    Vector = Vector.map(lambda l: l.split(',')).map(lambda l: [str(x) for x in l])

    #create row index: (i, Vi)
    Vector= Vector.map(lambda l: ([(i,j) for (i,j) in enumerate(l)]))

    #group by row index
    Vector = Vector.flatMap(lambda l: [(x[0], x[1]) for x in l]).groupBy(lambda l: l[0])

    #join index by j for (j, (Aij,i)) & (j, Vj)
    join_Av =  Matrix_col.join(Vector)
    join_Av = join_Av.map(lambda x : (x[0], list(x[1][0]), list(x[1][1])))

    #for each group compute:(j, (i, Aijvj))
    col_multiply = join_Av.map(lambda l: [(x[1][0],float(x[1][1])*float(l[2][0][1])) for x in l[1]])
    col_multiply = col_multiply.flatMap(lambda l: l)

    #reduce by key j, sum over column yield the sum of each row
    result = col_multiply.reduceByKey(lambda x, y: x + y).map(lambda l: l[1])
    return result

if __name__ == '__main__':
    sc = SparkContext(appName = "matrix")
    matrix_file = sys.argv[1]
    vector_file = sys.argv[2]
    res =  matrix_multiply(matrix_file, vector_file)
    print(res.collect())
