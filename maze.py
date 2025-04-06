from window import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
    def _create_cells(self):
        for i in range(self._num_cols):
            cols = []
            for j in range(self._num_rows):
                cols.append(Cell(self._win))
            self._cells.append(cols)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            can_visit = []
            if i > 0 and not self._cells[i - 1][j]._visited:
                can_visit.append([i - 1, j])
            if i < self._num_cols - 1 and not self._cells[i + 1][j]._visited:
                can_visit.append([i + 1, j])
            if j > 0 and not self._cells[i][j - 1]._visited:
                can_visit.append([i, j - 1])
            if j < self._num_rows - 1 and not self._cells[i][j + 1]._visited:
                can_visit.append([i, j + 1])
            
            if len(can_visit) == 0:
                self._draw_cell(i, j)
                return
            
            random_index = random.randrange(len(can_visit))
            will_visit = can_visit[random_index]

            if will_visit[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            
            if will_visit[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            
            if will_visit[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            
            if will_visit[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(will_visit[0], will_visit[1])
