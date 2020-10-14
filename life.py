import sys,pygame, random

# declare constants
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 5
ALIVE_COLOR = 0, 255, 255
DEAD_COLOR = 0, 0, 0
BG = 0, 0, 0
GRID_COLOR = 255, 255, 255
MAX_FPS = 30


# Create class and call init 
class GameLife():
    pygame.init()

    def __init__(self):
        # set screen with give varibels and title
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Conways Game of Life')
        self.screen.fill(BG)
        self.grids = []
        self.initGrid()
  
        pass

    

    def clearGrid(self):
        # clear screen of all cells
        self.screen.fill(BG)
        pass



    def initGrid(self):
        # define grid cols, rows and arrays for cordinates 
        self.num_cols = int(WIDTH / CELL_SIZE)
        self.num_rows = int(HEIGHT / CELL_SIZE)
        self.active_grid = []
        self.gen_grid = []

        # create matrix 
        for i in range(self.num_cols):
            self.active_grid.append([0]* self.num_rows)
            self.gen_grid.append([0]* self.num_rows)
        
        self.randomize(None,self.active_grid)
        self.randomize(0, self.gen_grid)
        self.grids.append(self.active_grid)
        self.grids.append(self.gen_grid)
        pass




    def randomize(self, value=None, grid = 0):
         # fill array with alive cells randomly
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                if(value == None):
                    cell_val = random.randint(0,1)
                else:
                    cell_val = value
                grid[i][j] = cell_val
    
        return grid


    # helper function to check current cell if null return 0 
    def check_cell(self, row, col):
        try:
            value = self.active_grid[row][col]
        except:
            value = 0
        return value

    # check neighbour function
    def check_neighbour(self, row, cols):
        live_neigh = 0
            # check all possible neighbours
        live_neigh += self.check_cell(row - 1, cols - 1)
        live_neigh += self.check_cell(row - 1, cols)
        live_neigh += self.check_cell(row - 1, cols + 1)
        live_neigh += self.check_cell(row, cols + 1)
        live_neigh += self.check_cell(row, cols - 1)
        live_neigh += self.check_cell(row + 1, cols - 1)
        live_neigh += self.check_cell(row + 1, cols )
        live_neigh += self.check_cell(row + 1, cols + 1)

        # apply conways rules
        try:
            if(self.active_grid[row][cols] == 1):
                if(live_neigh > 3):
                    return 0
                elif(live_neigh < 2):
                    return 0
                elif(live_neigh == 2 or live_neigh == 3):
                    return 1
            elif(self.active_grid[row][cols] == 0):
                if(live_neigh == 3):
                    return 1
            return self.active_grid[row][cols]
        except:
            pass
            
    # function to creating next grid generation         
    def next_gen(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                try:
                    next_update = self.check_neighbour(i,j)
                    self.gen_grid[i][j] = next_update
                except:
                    pass
        self.active_grid = self.gen_grid  
    pass

    def drawGrid(self):
        # loop through matrix and draw a cell for every "live" cell
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                if(self.active_grid[i][j] == 1):
                    color = ALIVE_COLOR
                else:
                    color = DEAD_COLOR
                pygame.draw.circle(self.screen, color, (int(i * CELL_SIZE + (CELL_SIZE / 2)),
                                                        int(j * CELL_SIZE + (CELL_SIZE / 2))),  
                                                        int(CELL_SIZE / 2),
                                                        0)
        #display window
        pygame.display.flip()
        pass



    def run(self):    
        self.clearGrid()
        clock = pygame.time.Clock()

        # loop until user exits program
        running = True
        while running:
            self.next_gen()
            self.drawGrid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(MAX_FPS)



if __name__ == '__main__': 
    game = GameLife()
    game.run()