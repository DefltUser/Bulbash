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
'''
____sexy?Sexy
___?Sexy?Sexy?R
___?Sexy?Sexy?R
__?Sexy?Sexy?Se
_?Sexy?Sexy?Se
_?Sexy?Sexy?Se
_?Sexy?Sexy?Sexy?
?Sexy?Sexy?Sexy?Sexy
?Sexy?Sexy?Sexy?Sexy?Se
?Sexy?Sexy?Sexy?Sexy?Sex
_?Sexy?__?Sexy?Sexy?Sex
___?Sex____?Sexy?Sexy?
___?Sex_____?Sexy?Sexy
___?Sex_____?Sexy?Sexy
____?Sex____?Sexy?Sexy
_____?Se____?Sexy?Sex
______?Se__?Sexy?Sexy
_______?Sexy?Sexy?Sex
________?Sexy?Sexy?Sex
_______?Sexy?Sexy?Sexy?Se
_______?Sexy?Sexy?Sexy?Sexy?
_______?Sexy?Sexy?Sexy?Sexy?Sexy
_______?Sexy?Sexy?Sexy?Sexy?Sexy?R
________?Sexy?Sexy____?Sexy?Sexy?Se
_________?Sexy?Se_______?Sexy?Sexy?
_________?Sexy?Se_____?Sexy?Sexy?
_________?Sexy?R____?Sexy?Sexy
_________?Sexy?R_?Sexy?Sexy
________?Sexy?Sexy?Sexy
________?Sexy?Sexy?R
________?Sexy?Sexy
_______?Sexy?Se
_______?Sexy?
______?Sexy?
______?Sexy?
______?Sexy?
______?Sexy
______?Sexy
_______?Sex
_______?Sex
_______?Sex
______?Sexy?
______?Sexyy
_______|_?Sex
_______|__?Sex

'''
