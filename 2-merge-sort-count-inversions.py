inversions = 0


def count_inversions(num_list):
    global inversions
    middle = int(len(num_list) / 2)

    left = num_list[:middle]
    right = num_list[middle:]

    if len(num_list) > 1:
        count_inversions(left)
        count_inversions(right)

        i = 0
        j = 0
        m = left
        n = right

        for k in range(len(m) + len(n) + 1):
            if m[i] <= n[j]:
                num_list[k] = m[i]
                i += 1
                if i == len(m) and j != len(n):
                    while j != len(n):
                        k += 1
                        num_list[k] = n[j]
                        j += 1
                    break
            elif m[i] > n[j]:
                num_list[k] = n[j]
                inversions += (len(m) - i)
                j += 1
                if j == len(n) and i != len(m):
                    while i != len(m):
                        k += 1
                        num_list[k] = m[i]
                        i += 1
                    break

    return inversions


file = open("/files/merge_sort_integers.txt")
lines = file.readlines()
file.close()

num_array = []
for n in range(0, len(lines)):
    lines[n] = lines[n].strip()
    num_array.append(int(lines[n]))

num_array = count_inversions(num_array)
print(num_array)
