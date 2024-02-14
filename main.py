f = open('students.txt')
arr = [str(x) for x in f]
nw_arr = []
for i in range(len(arr) - 1):
    if len(arr[i]) == 3:
        nw_arr.append(arr[i][-3])
    nw_arr.append(arr[i][-2])
nw_arr.remove('e')
print(nw_arr)
intarr = [int(x) for x in nw_arr]

d