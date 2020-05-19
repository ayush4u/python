a='heythisisastring'
print(a)
print(len(a))#remember its a funcion()
'''
lets dive into string indexing and slicing
'''
#indexing(starts from 0)
print(a[0])
print(a[-1])
#slicing
print(a[1:])#grab everything to the end
print(a[:3])#grab everything UPTO 3(ie without including)
'''
lets play
'''
print(a[1:8:2])#from one to 8 (ie to 7) print everthing taking the jump of two
print(a[::2])
print(a[::-1])
'''
fun
'''
print(a*2)