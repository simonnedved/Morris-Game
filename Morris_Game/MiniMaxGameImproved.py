import game
from node import Node
import time
from config import input_file, output_file, tree_depth


def diff_closeMill(position):
    count, count1 = 0, 0
    for location in range(len(position)):
        c = position[location]
        if c == 'W':
            if location == 0:
                if (position[6] == c and position[18] == c) or (position[2] == c and position[4] == c):
                    count += 1
            if location == 1:
                if position[11] == c and position[20] == c:
                    count += 1
            if location == 2:
                if position[7] == c and position[15] == c:
                    count += 1
            if location == 3:
                if position[10] == c and position[17] == c:
                    count += 1
            if location == 4:
                if position[8] == c and position[12] == c:
                    count += 1
            if location == 5:
                if position[9] == c and position[14] == c:
                    count += 1
            if location == 6:
                if position[7] == c and position[8] == c:
                    count += 1
            if location == 9:
                if position[10] == c and position[11] == c:
                    count += 1
            if location == 12:
                if position[13] == c and position[14] == c:
                    count += 1
            if location == 13:
                if position[16] == c and position[19] == c:
                    count += 1
            if location == 15:
                if position[16] == c and position[17] == c:
                    count += 1
            if location == 18:
                if position[19] == c and position[20] == c:
                    count += 1
        if c == 'B':
            if location == 0:
                if (position[6] == c and position[18] == c) or (position[2] == c and position[4] == c):
                    count1 += 1
            if location == 1:
                if position[11] == c and position[20] == c:
                    count1 += 1
            if location == 2:
                if position[7] == c and position[15] == c:
                    count1 += 1
            if location == 3:
                if position[10] == c and position[17] == c:
                    count1 += 1
            if location == 4:
                if position[8] == c and position[12] == c:
                    count1 += 1
            if location == 5:
                if position[9] == c and position[14] == c:
                    count1 += 1
            if location == 6:
                if position[7] == c and position[8] == c:
                    count1 += 1
            if location == 9:
                if position[10] == c and position[11] == c:
                    count1 += 1
            if location == 12:
                if position[13] == c and position[14] == c:
                    count1 += 1
            if location == 13:
                if position[16] == c and position[19] == c:
                    count1 += 1
            if location == 15:
                if position[16] == c and position[17] == c:
                    count1 += 1
            if location == 18:
                if position[19] == c and position[20] == c:
                    count1 += 1
    return count-count1


def blocked_piece(position):
    count, count1 = 0, 0
    for i in range(len(position)):
        temp, temp1 = 0, 0
        if position[i] == 'W':
            for neigb in game.board[i]:
                if position[neigb] == 'B':
                    temp += 1
            if temp == len(game.board[i]):
                count += 1
        elif position[i] == 'B':
            for neigb in game.board[i]:
                if position[neigb] == 'W':
                    temp1 += 1
            if temp1 == len(game.board[i]):
                count1 += 1
    return count-count1


def newStaticEstimation(position):
    # print('-- StaticEstimation --')
    global leaves_count
    game.leaves_count += 1
    w_count, b_count = 0, 0
    for loc in range(len(position)):
        if position[loc] == 'W':
            w_count += 1
        if position[loc] == 'B':
            b_count += 1
    move = len(game.MoveGenerator(position, 'MidgameEndgame'))
    if b_count <= 2:
        return 100000
    else:
        if w_count <= 2:
            return -100000
        else:
            if move == 0:
                return 100000
            else:
                return 1000*(w_count-b_count) - move + 4000*diff_closeMill(position) + 1000*blocked_piece(position)


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
    return newStaticEstimation(node.value)


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

    t_b = time.time()
    root = create_tree(Node(position), tree_depth, True)
    leaf = MiniMax(root, True)
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