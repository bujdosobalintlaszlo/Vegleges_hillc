def main():
    map_name = input("Add meg a map nevét (pl. map 1): ").strip()
    map_number = map_name.replace('map', '').strip()
    file_path = f'./results/result{map_number}.txt'

    try:
        with open(file_path, 'r') as f:
            data = f.readline().strip().split(',')
            if len(data) == 2:
                print(f"Átlagos lépésszám: {data[0]} Futtatásszám: {data[1]}")
            else:
                print("Hibás fájlformátum.")
    except Exception as e:
        print(f"Hiba történt a fájl beolvasása közben: {e}")

if __name__ == "__main__":
    main()



