'''
list are mutable(changes can be done) just like strings and it is represented by[]
'''
l=[1,2,3,'a','b','c']

#indexing and slicing
print(l[0])
print(l[0:2])
print(l[::2])

'''
fun
'''
mylist=l+["hey"]
print(mylist)
mylist=mylist*2 #yess you can reassing things in python
print(mylist)
'''
Methods/functions
'''
l2=[1,4,3,5,7,3,5]
print(l2.sort()) #sort the list ,print none
print(l2)
print(l2.append('oh,hi'))
print(l2)
print(l2.pop(-1))
print(l2)
l2.reverse()
print(l2)

'''
now lil twist NESTED LIST

'''
l=[1,2,3]
l2=[4,5,6]
l3=[6,7,8]
mat=[l,l2,l3]
print(mat)

#we can use for loop to grab element
hate=[ik[0] for ik in mat]
print(hate)