nums = [1,2,3,4,6,5]
print( nums )
print ( nums[1])
print(nums[2:])
print(nums[-1])
values = [1,4.5,'harshita',92928292992398239829382938298392839829389283928339283928398293829382938298928928392839238948,'dharti']
print(values)
names = [nums,values]
print(names)
nums.insert(3,'dee')
print(nums)

values.remove('harshita')
print(values)
values.pop(3)
print(values)
del nums[2:]
print(nums)
nums.extend([2,3,4,5,67,7,9])
print(nums)

print(min(nums))

print(sum(nums))