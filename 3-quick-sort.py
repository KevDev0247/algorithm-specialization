def generate_median(array, left_index, right_index):
    middle_index = 0 if right_index - left_index == 1 else (right_index - left_index) // 2 + left_index
    left = array[left_index]
    right = array[right_index]
    middle = array[middle_index]

    candidates = sorted([(left, left_index), (middle, middle_index), (right, right_index)])

    return candidates[1][1]


def choose_pivot(array, choice, left, right):
    if choice == 1:
        return left
    elif choice == 2:
        return right
    else:
        return generate_median(array, left, right)


def partition(array, choice, left, right):
    global count
    i = choose_pivot(array, choice, left, right)
    pivot = array[i]

    array[left], array[i] = array[i], array[left]

    i = left + 1
    for j in range(i, right + 1):
        count += 1
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    i -= 1
    array[i], array[left] = array[left], array[i]

    return i


def count_quick_sort(array, choice, left, right):
    if len(array) < 1:
        return
    if left <= right:
        pivot = partition(array, choice, left, right)

        count_quick_sort(array, choice, left, pivot - 1)
        count_quick_sort(array, choice, pivot + 1, right)


file = open("D:\\Algorithms-Specialization\\files\\quick_sort_integers.txt")
lines = file.readlines()
file.close()

num_array = []
for n in range(0, len(lines)):
    lines[n] = lines[n].strip()
    num_array.append(int(lines[n]))


count = 0
choice = int(input("input your choice of pivot (1: Leftmost, 2: Rightmost, 3: Median): "))

count_quick_sort(num_array, choice, 0, len(num_array) - 1)

print(num_array)
print(count)
