# John Nep Arcilla  06/06/2023

arr = [5, 1, 4, 6, 7, 3, 5, 7, 3]
duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate elements:", duplicates)
