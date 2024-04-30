def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if len(arr[j]) < len(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    strings = ["manzana", "banana", "pera", "uva", "kiwi", "naranja"]

    selection_sort(strings)
    print("Lista ordenada por longitud:")
    print(strings)

if __name__ == "__main__":
    main()

