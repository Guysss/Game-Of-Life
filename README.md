## Game-Of-Life

This is the Game Of Life. There is a cell grid and the cell have two state : alive or dead. The rules are simple, every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
+ Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
+ Any live cell with two or three live neighbours lives on to the next generation.
+ Any live cell with more than three live neighbours dies, as if by overpopulation.

**You can change defaults values if you want to change the simulation :**
- ```TABLE_SIZE``` : The size of the grid (number of cells).
- ```CELL_SIZE``` : The size of one cell (px).
- ```PERIODICITY``` : The simulation's update frequency (msec).

However, the size of the window depends on the length of the table and the cells.
- ```POPULATION_THRESHOLD``` : Number of living neighboring cells needed to be populate.
- ```STABILITY_THRESHOLD``` : Number of living neighboring cells needed to not change.

**In-game's keyboard :**
- ```Space Bar``` : Pause and unpause the game
- ```Mouse left click``` : Set the cell alive
- ```Mouse right click``` : Kill the cell


> [!WARNING]
> If you don't have the pygame library, type ```pip3 install pygame``` on Linux or ```python3 -m pip install pygame``` on Windows.

- Guys_s
