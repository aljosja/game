class Board:
    def __init__(self, rows, columns, tile=None):
        self.grid = [[tile]*rows for n in range(columns)]

    def show(self):
        for index, row in enumerate(self.grid):
            print(self.grid[index])

    def show_pretty(self):
        horizontal_divisor = ''
        cell_space = ''
        cell_padding = ' '
        cell_value = cell_padding + str(self.grid[0][0]) + cell_padding
        for x in range(len(cell_value)):
            cell_space += '-'
        h_cell_border = ' ' + cell_space
        v_cell_border = '|'
        for x in range(len(self.grid)):
            horizontal_divisor += h_cell_border
        for index_row, row in enumerate(self.grid):
            print(horizontal_divisor)
            display_row = v_cell_border
            for index_col, col in enumerate(row):
                display_row += (cell_padding + str(self.grid[index_row][index_col]) + cell_padding + v_cell_border)
            print(display_row)
        print(horizontal_divisor)


if __name__ == "__main__":
    print('\n=== This Module Contains ==================')
    print('Board(rows, columns, tile = None)')
    print('===========================================')
    print(f"Board(6, 6).grid: {Board(6, 6).grid}")
    print(f"Board(6, 6).grid[0][3]: {Board(6, 6).grid[0][3]}")
    print("Board(6, 6).show():")
    print(Board(6, 6).show())
    print("Board(6, 6).show_pretty():")
    print(Board(6, 6).show_pretty())
    print("Board(6, 6, 0).show_pretty():")
    print(Board(6, 6, 0).show_pretty())
    print("===========================================\n")
