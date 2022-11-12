x = 10 
print(x)
y = 6 
print(y)
print( x+ y)
name = 'Harshita'
print(name)
print( name + 'Raghav')
print( name + ' Raghav')
print( name[0]+name[1]+name[2]+name[3])

'''
indexing form front -> 0,1,2,3,4,5,6,7....
indexing form end ->   ...-7,-6,-5,-4,-3,-2,-1 

'''
val = 'Modinagar'
print(val[0])
print ( val[1])
print(val[1:4])
print( val[1:])
print(val[:4])
 #strings are immutable
'''
 num = 5
id(num)
140724565103528
name= 'Dee'
id(name)
2401270323120
a= 10   // address-1 assigned
b = 12   //address-2 assigned
ans = a+b   //address-3 assigned
print( ans )
22
id(a)
140724565103688
id(b)
140724565103752
id(ans)
140724565104072
x = 10   //add-1 assigned
y = 10 //add-2 assigned , but add-2 == add-2 ,when same values are declared same add is given to both the variables 
id(x)
140724565103688
id(y)
140724565103688

 '''