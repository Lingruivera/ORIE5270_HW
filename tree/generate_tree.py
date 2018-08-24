class Tree(object):
    '''
    output tree object represented using a matrix structure
    :param: tree object constructed using Nodes
    '''
    def __init__(self, root):
        self.root = root

    def get_depth(self):
        """
        compute the depth of the tree recursively
        :param: tree instance
        :return: the depth of the tree
        """
        if self.root is None:
            return 0
        elif self.root.left is None and self.root.right is None:
            return 1
        else:
            left_node = Tree(self.root.left)
            right_node = Tree(self.root.right)
            return 1 + max(left_node.get_depth(), right_node.get_depth())

    def visualize_tree(self):
        """
        print the tree instance row by row
        use '|' as separator
        :param: tree instance
        :return: a list of lists representation of the tree
        """
        depth = self.get_depth()
        queue = [self.root]
        count = 1
        tree_matrix = []

        for j in range(depth):
            depth_row = []
            next_queue = []
            depth_row.append(['|'] * (2 ** (depth - count) - 1))
            for x in queue:
                if x is not None:
                    depth_row.append([x.value])
                    next_queue.append(x.left)
                    next_queue.append(x.right)
                else:
                    depth_row.append('|')
                    next_queue.append(None)
                    next_queue.append(None)
                if len(queue) > 1:
                    depth_row.append(['|'] * (2 ** (depth - count + 1) - 1))
                queue = queue[1:]
            depth_row.append(['|'] * (2 ** (depth - count) - 1))

            depth_row = [item for sublist in depth_row for item in sublist]
            queue = next_queue
            count = count + 1
            for i in depth_row:
                print(i),
            print(' ')
            tree_matrix.append(depth_row)
        print(' ')
        return tree_matrix


class Node(object):
    """
    construct a Node
    :param: node value, left child, right child
    """
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
