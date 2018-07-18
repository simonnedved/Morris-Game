# orin_board = {'a0': 0, 'g0': 1, 'b1': 2, 'f1': 3, 'e2': 5, 'a3': 6, 'b3': 7, 'c3': 8, 'e3': 9, 'f3': 10,
#               'g3': 11, 'c4': 12, 'd4': 13, 'e4': 14, 'b5': 15, 'd5': 16, 'f5': 17, 'a6': 18, 'd6': 19, 'g6': 20}

board = {0:[1,2,6], 1:[0,11], 2:[0,3,4,7], 3:[2,10], 4:[2,5,8], 5:[4,9], 6:[0,7,18],
         7:[2,6,8,15], 8:[4,7,12], 9:[5,10,14], 10:[3,9,11,17], 11:[1,10,20], 12:[8,13],
         13:[12,14,16], 14:[9,13], 15:[7,16], 16:[13,15,17,19], 17:[10,16], 18:[6,19],
         19:[16,18,20], 20:[11,19]}


leaves_count = 0


def Add(position):
    L = []
    for loc in range(len(position)):
        if position[loc] == 'x':
            copy_pos = position[:]
            copy_pos[loc] = 'W'
            if CloseMill(loc, copy_pos):
                Remove(copy_pos, L)
            else:
                L.append(copy_pos)
    return L


def Hopping(position):
    L = []
    for i in range(len(position)):
        if position[i] == 'W':
            for j in range(len(position)):
                if position[j] == 'x':
                    copy_pos = position[:]
                    copy_pos[i] = 'x'
                    copy_pos[j] = 'W'
                    if CloseMill(j, copy_pos):
                        Remove(copy_pos, L)
                    else:
                        L.append(copy_pos)
    return L


def Move(position, board):
    L = []
    for i in range(len(position)):
        if position[i] == 'W':
            neighbors = board[i][:]
            for j in neighbors:
                if position[j] == 'x':
                    copy_pos = position[:]
                    copy_pos[i] = 'x'
                    copy_pos[j] = 'W'
                    if CloseMill(j, copy_pos):
                        Remove(copy_pos, L)
                    else:
                        L.append(copy_pos)

    return L


def Remove(position, L):
    changed = 0
    for loc in range(len(position)):
        if position[loc] == 'B':
            if not CloseMill(loc, position):
                copy_pos = position[:]
                copy_pos[loc] = 'x'
                L.append(copy_pos)
                changed = 1
    if not changed:
        L.append(position)
    return L


def CloseMill(location, position):
    c = position[location]
    if c == 'W' or 'B':
        if location == 0:
            if (position[6] == c and position[18] == c) or (position[2] == c and position[4] == c):
                return True
            else:
                return False
        if location == 1:
            if position[11] == c and position[20] == c:
                return True
            else:
                return False
        if location == 2:
            if (position[0] == c and position[4] == c) or (position[7] == c and position[15] == c):
                return True
            else:
                return False
        if location == 3:
            if position[10] == c and position[17] == c:
                return True
            else:
                return False
        if location == 4:
            if (position[0] == c and position[2] == c) or (position[8] == c and position[12] == c):
                return True
            else:
                return False
        if location == 5:
            if position[9] == c and position[14] == c:
                return True
            else:
                return False
        if location == 6:
            if (position[0] == c and position[18] == c) or (position[7] == c and position[8] == c):
                return True
            else:
                return False
        if location == 7:
            if (position[6] == c and position[8] == c) or (position[2] == c and position[15] == c):
                return True
            else:
                return False
        if location == 8:
            if (position[6] == c and position[7] == c) or (position[4] == c and position[12] == c):
                return True
            else:
                return False
        if location == 9:
            if (position[5] == c and position[14] == c) or (position[10] == c and position[11] == c):
                return True
            else:
                return False
        if location == 10:
            if (position[9] == c and position[11] == c) or (position[3] == c and position[17] == c):
                return True
            else:
                return False
        if location == 11:
            if (position[9] == c and position[10] == c) or (position[1] == c and position[20] == c):
                return True
            else:
                return False
        if location == 12:
            if (position[4] == c and position[8] == c) or (position[13] == c and position[14] == c):
                return True
            else:
                return False
        if location == 13:
            if (position[12] == c and position[14] == c) or (position[16] == c and position[19] == c):
                return True
            else:
                return False
        if location == 14:
            if (position[12] == c and position[13] == c) or (position[5] == c and position[9] == c):
                return True
            else:
                return False
        if location == 15:
            if (position[2] == c and position[7] == c) or (position[16] == c and position[17] == c):
                return True
            else:
                return False
        if location == 16:
            if (position[15] == c and position[17] == c) or (position[13] == c and position[19] == c):
                return True
            else:
                return False
        if location == 17:
            if (position[15] == c and position[16] == c) or (position[3] == c and position[10] == c):
                return True
            else:
                return False
        if location == 18:
            if (position[0] == c and position[6] == c) or (position[19] == c and position[20] == c):
                return True
            else:
                return False
        if location == 19:
            if (position[18] == c and position[20] == c) or (position[13] == c and position[16] == c):
                return True
            else:
                return False
        if location == 20:
            if (position[18] == c and position[19] == c) or (position[1] == c and position[11] == c):
                return True
            else:
                return False


def MovesOpening(position):
    return Add(position)


def MovesMidgameEndgame(position, board):
    w_count, b_count, x_count = 0, 0, 0
    for loc in position:
        if loc == 'W':
            w_count += 1
        elif loc == 'B':
            b_count += 1
        elif loc == 'x':
            x_count += 1
    if w_count == 3:
        return Hopping(position)
    else:
        return Move(position, board)


def Swap(position):
    # print('SWAP!!!!!')
    for loc in range(len(position)):
        if position[loc] == 'W':
            position[loc] = 'B'
        else:
            if position[loc] == 'B':
                position[loc] = 'W'
    return position


def MoveGenerator(position, game_status):
    L0, L1 = [], []
    cp_pos = position[:]
    swap_pos = Swap(cp_pos)
    if game_status == 'Opening':
        L0 = Add(swap_pos)
    else:
        L0 = MovesMidgameEndgame(swap_pos, board)
    for pos in L0:
        pos = Swap(pos)
        L1.append(pos)
    return L1


def StaticEstimation(position, game_status):
    # print('-- StaticEstimation --')
    global leaves_count
    leaves_count += 1
    w_count, b_count = 0, 0
    for loc in range(len(position)):
        if position[loc] == 'W':
            w_count += 1
        if position[loc] == 'B':
            b_count += 1
    if game_status == 'Opening':
        return w_count - b_count
    else:
        move = len(MoveGenerator(position, 'MidgameEndgame'))
        if b_count <= 2:
            return 10000
        else:
            if w_count <= 2:
                return -10000
            else:
                if move == 0:
                    return 10000
                else:
                    return 1000 * (w_count - b_count) - move


def Decision(L, game_status):
    dic = {}
    for idx in range(len(L)):
        dic[idx] = StaticEstimation(L[idx], game_status)
    max_id = sorted(dic, key=lambda key: dic[key])[-1]
    return L[max_id]


# def choose_min_or_max(position):
#     w_count, b_count = 0, 0
#     for loc in position:
#         if loc == 'W':
#             w_count += 1
#         if loc == 'B':
#             b_count += 1
#     if w_count <= b_count:
#         return True
#     else:
#         return False