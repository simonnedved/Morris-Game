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
    return game.StaticEstimation(node.value, 'MidgameEndgame')


def create_tree(node, depth, flag):
    if flag:
        if depth > 0 and not end_game(node):
            pos_w = game.MovesMidgameEndgame(node.value, game.board)
            for child_w in pos_w:
                node.children.append(create_tree(Node(child_w), depth-1, False))
    else:
        if depth > 0 and not end_game(node):
            pos_b = game.MoveGenerator(node.value, 'MidgameEndgame')
            for child_b in pos_b:
                node.children.append(create_tree(Node(child_b), depth-1, True))
    return node


def end_game(node):
    w_count, b_count = 0, 0
    for c in node.value:
        if c == 'W':
            w_count += 1
        if c == 'B':
            b_count += 1
    if w_count <= 2 or b_count <= 2:
        return True
    else:
        return False


if __name__ == '__main__':
    position = []
    fp = open(input_file, 'r')
    for ch in fp.read():
        position.append(ch)
    fp.close()

    position = game.Swap(position)

    t_b = time.time()
    root = create_tree(Node(position), tree_depth, True)
    leaf = MiniMax(root, True)
    print('MINIMAX estimate:', leaf[0])
    print('Output:', game.Swap(leaf[1].value))
    t_e = time.time()
    print('Time:', t_e - t_b)
    print('Positions evaluated by static estimation:', game.leaves_count)

    fp = open(output_file, 'w')
    str0 = ''
    for e in leaf[1].value:
        str0 += e
    fp.write(str0)
    fp.close()