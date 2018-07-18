import game
from node import Node
import time
from config import input_file, output_file, tree_depth


def MiniMax(node, flag):
    if flag:
        return MaxMin(node, None)
    else:
        return MinMax(node, None)


def MaxMin(node, temp_node):
    if node.children == []:
        return static(node), None
    else:
        v = -10000000
        for child in node.children:
            temp = MinMax(child, temp_node)[0]
            if v < temp:
                v = temp
                temp_node = child
        return v, temp_node


def MinMax(node, temp_node):
    if node.children == []:
        return static(node), None
    else:
        v = 10000000
        for child in node.children:
            temp = MaxMin(child, temp_node)[0]
            if v > temp:
                v = temp
                temp_node = child
        return v, temp_node


def static(node):
    # print('Output:', node.value)
    return game.StaticEstimation(node.value, 'Opening')


def create_tree(node, depth, flag):
    if flag:
        # pos_w = game.MovesOpening(node.value)
        if depth > 0:
            pos_w = game.MovesOpening(node.value)
            for child_w in pos_w:
                node.children.append(create_tree(Node(child_w), depth-1, False))
    else:
        # pos_b = game.MoveGenerator(node.value, 'Opening')
        if depth > 0:
            pos_b = game.MoveGenerator(node.value, 'Opening')
            for child_b in pos_b:
                node.children.append(create_tree(Node(child_b), depth-1, True))
    return node


if __name__ == '__main__':
    position = []
    fp = open(input_file, 'r')
    for ch in fp.read():
        position.append(ch)
    fp.close()

    t_b = time.time()
    root = create_tree(Node(position), tree_depth, False)
    leaf = MiniMax(root, False)
    print('MINIMAX estimate:', leaf[0])
    print('Output:', leaf[1].value)
    t_e = time.time()
    print('Time:', t_e - t_b)
    print('Positions evaluated by static estimation:', game.leaves_count)

    fp = open(output_file, 'w')
    str0 = ''
    for e in leaf[1].value:
        str0 += e
    fp.write(str0)
    fp.close()