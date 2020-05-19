file=open('testfile')
print(file.read())
print(file.read())#lets see the output ()blank becualse the curser is at the end
file=open('testfile','a+')
file.write('\nnew line is here')
print(file.read())
print(file.seek(0))
print(file.readlines())#return the list of the line
print(file.close())
'''
hey now lets take the shortcut
'''
with open('testfile') as file:
    print(file)

with open('testfile',mode='a') as file:
    file.write('\n ok thats the another method')

for file in open('testfile'):
    print(file)
