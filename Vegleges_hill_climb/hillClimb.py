import random
import numpy as np

#--------------------------------------------------------
# A map beolv. filebol
def read_map(file_name):
    global_maxes = []
    map_grid = []

    with open(file_name, 'r') as file:
        global_maxes = list(map(int, file.readline().strip().split(',')))
        for line in file:
            map_grid.append(list(map(int, line.strip().split())))

    global_max = max(global_maxes)  # global max
    return global_max, map_grid,len(global_maxes)
#--------------------------------------------------------

#--------------------------------------------------------
# A szomszedok elore kiszamitasa a terkep minden pontjara
def precompute_neighbors():
    neighbors_map = {}  # A szomszedok dic
    # Iranyok: fel, le, balra, jobbra, osszes keresztirany
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # A ,ap minden egyes poz.-hoz meghatarozzuk a szomszedokat
    for x in range(30):
        for y in range(30):
            neighbors = []
            # Minden iranyra kiszamitjuk a szomszedos koordinatákat
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 30 and 0 <= ny < 30:  # Csak akkor, ha a szomszed a terkepen belul van
                    neighbors.append((nx, ny))
            neighbors_map[(x, y)] = neighbors  # Taroljuk a szomszedokat
    return neighbors_map  # Visszaadjuk a szomszedok terkepet


#--------------------------------------------------------
# A szomszedos maximalis ertek keresese
def find_best_move(x, y, neighbors_map, map_grid):
    neighbors = neighbors_map[(x, y)]
    best_value = map_grid[x][y]
    best_move = (x, y)

    # Minden szomszedot kiertekelunk, és valasztunk a legjobb kozul
    for nx, ny in neighbors:
        if map_grid[nx][ny] > best_value:
            best_value = map_grid[nx][ny]
            best_move = (nx, ny)
    
    # Ha nincs jobb szomszed, random szomszed
    if best_move == (x, y):
        best_move = random.choice(neighbors)
    
    return best_move

#--------------------------------------------------------

#--------------------------------------------------------
# A jatek logikaja, szomszedos lepesek, greedy algo
def greedy_search(global_max, map_grid, neighbors_map, g_count, max_iterations=1000):
    # random kezdopont
    x, y = random.randint(0, 29), random.randint(0, 29)
    
    steps_taken = 0
    best_value = map_grid[x][y]  # A legjobb ertek (kezdetben a kezdo pozicio)
    best_position = (x, y)  # A legjobb poz
    gblc = 0  # Globalis maximum szamlalo
    
    # A szomszedos lepesek keresese
    for iteration in range(max_iterations):
        best_move = find_best_move(x, y, neighbors_map, map_grid)
        x, y = best_move
        steps_taken += 1  # N0veljuk a lepesek szamat

        # Ha jobb erteket talalunk, frissitjuk a legjobb erteket és poziciot
        if map_grid[x][y] > best_value:
            best_value = map_grid[x][y]
            best_position = (x, y)

        if best_value == global_max:
            gblc += 1
            if gblc == g_count:
                break


    return gblc, steps_taken, best_value  # Visszaadjuk a megtalalt maximumok szamat, a lepesek szamat és a legjobb erteket

#--------------------------------------------------------

#--------------------------------------------------------
# szimulaciok futtatas
def run_multiple_simulations(file_name, num_runs):
    global_max, map_grid, g_count = read_map(file_name)  # beolv.
    neighbors_map = precompute_neighbors()  # szomszedok megh.
    
    total_steps = 0
    for run_count in range(1, num_runs + 1):
        _, steps_taken, _ = greedy_search(global_max, map_grid, neighbors_map,g_count)  # futtatas
        total_steps = (total_steps * (run_count - 1) + steps_taken) / run_count 
    
    return total_steps
#--------------------------------------------------------

#--------------------------------------------------------
# fileba iras
def result_into_file(i,average_steps,runs):
    with open(f'./mapHandling/results/result{i}.txt','w') as writer:
        writer.write(f'{average_steps:.2f}, {runs}')
for i in range(1, 11):  # itt kell atirni 10re majd
    file_name = f'./mapHandling/maps/map{i}.txt'
    runs= 200
    average_steps = run_multiple_simulations(file_name,runs)
    result_into_file(i,average_steps,runs)
    print(f"Average steps after 200 runs: {average_steps:.2f}")
#--------------------------------------------------------


