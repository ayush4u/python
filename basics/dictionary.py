'''
dictionaries work on mapping object concept where we use key to mapping 
its reperesented by{}
'''
dict={'k1':"hey",'k2':1,'k3':4}
print(dict['k3'])

#fun begains

dict['k4']= [1,2,3]
print(dict)

#lets say if you want to print 2nd index of list k4
print(dict['k4'][2])

#methods
print(dict.keys())
print(dict.items())
print(dict.values())
