import os

base_dir = os.path.dirname(os.path.abspath(__file__))
inp = int(input('Hány resultot töröljön: '))
print(base_dir)
for i in range(inp):
    with open(f'./results/result{i+1}.txt', 'w') as w:
        w.write('')
print('A fájlok sikeresen ürítve!')
