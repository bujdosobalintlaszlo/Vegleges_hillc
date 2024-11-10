import os

run_count = int(input('Hány futtatásból legyen a pont számolva: '))
point = 0
for i in range(run_count):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(f'./mapHandling/results/result{i+1}.txt')
    if os.path.exists(file_path):
        with open(file_path) as file:
            line = file.readline().strip()
            numbers = line.replace(',', '').split()
            point += float(numbers[0])
    else:
        print(f"Hiba: A {file_path} fájl nem található.")
        break 

if run_count > 0:
    print(f'Eredmény: {(point / run_count):.2f} pont')