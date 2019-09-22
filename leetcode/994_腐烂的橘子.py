class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if 2 not in grid[0] and grid[1] and grid[2]: return -1
        k = 0

        def rot(grid, k):
            if 2 not in grid[0] and grid[1] and grid[2]: return
            pos, i, j = [], 0, 0

            # 终止条件，当没有1或都是2时终止
            check = 0
            for col in grid:
                if 2 in col: check += 2.0
                if 1 in col: check += 0.001
            if check % 2 == 0: return k
            # 获得腐烂的橘子的位置
            while i < len(grid):
                if 2 in grid[i]:
                    pos.append([grid[i].index(2), i])
                i += 1

            # 根据pos改变grid
            new_pos = []
            new_pos_x, new_pos_y = [], []
            for j in pos:
                # find new rot positions
                x, y = j[0], j[1]
                if x == 0 or x == 2:
                    new_pos_x.append(1)
                elif x == 1:
                    new_pos_x.append(0)
                    new_pos_x.append(2)
                if y == 0 or y == 2:
                    new_pos_y.append(1)
                elif y == 1:
                    new_pos_y.append(0)
                    new_pos_y.append(2)
                for pos_x in new_pos_x: new_pos.append([pos_x, y])
                for pos_y in new_pos_y: new_pos.append([x, pos_y])

                # generate the new positions
                # and change grid based on this
                for a in range(3):
                    for b in range(3):
                        if grid[a][b] == 1 and [a, b] in new_pos: grid[a][b] = 2
                print(pos, k, new_pos)
            k += 1
            rot(grid, k)
            # print(pos)
            return k

        rot(grid, 0)
