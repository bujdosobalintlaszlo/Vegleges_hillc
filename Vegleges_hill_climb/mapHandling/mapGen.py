import numpy as np
from scipy.ndimage import gaussian_filter
import os

instance_count = 0
map_size = 0
min_height, max_height = 0, 150

def get_valid_int_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Kérlek, adj meg egy számot {min_value} és {max_value} között!")
            else:
                return value
        except ValueError:
            print("Érvényes egész számot adj meg!")

def initialize_inputs():
    global instance_count, map_size
    instance_count = get_valid_int_input('Hány map generálódjon?: ', 1, None)
    map_size = get_valid_int_input('Add meg a pályaméretet (min.: 10, max.: 100): ', 10, 100)

def generate_maps():
    for map_counter in range(1, instance_count + 1):
        # Létrehozunk egy alap térképet véletlenszerű magasságokkal
        map_data = np.random.randint(min_height, max_height + 1, (map_size, map_size))
        
        # Noise hozzáadása: véletlenszerű változások alkalmazása a domborzaton
        noise = np.random.normal(0, 10, (map_size, map_size))
        map_data = map_data + noise
        
        # A simítás csökkentése
        sigma = 0.5  # Kisebb szigma érték, hogy élesebb hegyeket kapjunk
        smoothed_map = gaussian_filter(map_data, sigma=sigma)
        
        # mentes fileba
        write_into_file(smoothed_map, map_counter)

def write_into_file(smoothed_map, map_counter):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    maps_folder = os.path.join(script_dir, 'maps')
    os.makedirs(maps_folder, exist_ok=True)
    file_name = os.path.join(maps_folder, f'map{map_counter}.txt')

    with open(file_name, 'w') as f:
        max_heights = CheckMultipleMaxes(smoothed_map)
        f.write(f'{", ".join(map(str, max_heights.astype(int)))}\n')
        for row in smoothed_map:
            f.write(' '.join(map(str, row.astype(int))) + '\n')

def CheckMultipleMaxes(smoothed_map):
    flattened_map = smoothed_map.flatten()
    max_val = flattened_map.max()
    return flattened_map[flattened_map == max_val]

initialize_inputs()
generate_maps()
print("Map(ok) legenerálva!")



