'''
datatypes in py are------------------- 
none-> when nothing is assigned
numberic-> int, float, complex, bool
sequences---------
tuples
lists
set
string 
range...till here are seq 
dictionary
'''
num = 2.5
print(type(num))
num= 1
print(type(num))
num = 6+9j
print(type(num))
a = 5.6
b = int(a)
type(b)
k = float(b)
print(k)
bool = 100<6
print(bool)
print(bool)

lst = [1,3,5,9,11,13,17,23,29]
print(type(lst))
s = {1,3,5,9,11,13,17,23,29}
print(type(s))
tup = (1,3,5,9,11,13,17,23,29)
print(type(tup))

str = 'Harshita Raghav'
print(type(str))

print(list(range(10,20)))
print( tuple(range(100,110)))
