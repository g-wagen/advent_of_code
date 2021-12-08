import helper
import copy
import pandas as pd
import numpy as np

data = """7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1

22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7"""
data = [x for x in data.split('\n')]


# data = helper.get_puzzle_input(y=2021, d=4)

splits = data.count('')
split_pos = []

for i, item in enumerate(data):
    if item == '':
        split_pos.append(i)

nums = [int(x) for x in data[0].split(',')]

chunk_size = 5
boards = {}

for i, pos in enumerate(split_pos):
    try:
        board = data[pos:split_pos[i+1]]
    except IndexError:
        board = data[pos:]
    combine = ' '.join([x for x in board]).split()
    combine = [int(x) for x in combine]
    boards[i] = [combine[i:i + chunk_size] for i in range(0, len(combine), chunk_size)]
    # boards[i] = combine

# print(boards)

# dfs = {k:pd.DataFrame(v) for (k, v) in boards.items()}
dfs = [pd.DataFrame(v) for k, v in boards.items()]

calcing = True

# while calcing:
for n in nums:
    for i, df in enumerate(dfs):
        for col in df.columns:
            df.loc[df[col] == n, col] = np.nan
        # dfs[i] = df[df != n]
            nan_cols = dfs[i].loc[:, dfs[i].isnull().all()]
            nan_rows = dfs[i][dfs[i].isna().all(axis=1)]
            if nan_cols.shape[1] == 1 or nan_rows.shape[0] == 5:
        #     print(dfs[i].sum() * n)
                break
            # calcing = False
            # else:
            #     calcing = True
            # print(nan_cols)
            # print(nan_cols.shape)
            # print(nan_rows)
            # print(nan_rows.shape)
            # print(n)
        # print(df)
    # for df in dfs
print(dfs)

