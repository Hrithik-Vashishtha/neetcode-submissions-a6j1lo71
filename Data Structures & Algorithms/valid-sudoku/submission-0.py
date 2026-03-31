class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dict = {}
        grid_set = {}

        for row in range(9):
            row_set = set()
            for col in range(9):
                elem = board[row][col]

                if elem == ".":
                    continue

                box_id = (row // 3, col // 3)

                # check duplicates
                if (
                    elem in row_set
                    or elem in col_dict.get(col, set())
                    or elem in grid_set.get(box_id, set())
                ):
                    return False

                # add to row
                row_set.add(elem)

                # add to column
                if col not in col_dict:
                    col_dict[col] = set()
                col_dict[col].add(elem)

                # add to box
                if box_id not in grid_set:
                    grid_set[box_id] = set()
                grid_set[box_id].add(elem)

        return True