# raw input
name = input('enter a name: ')
print('{}'.format(name.title()))

# files

file_obj = open('/Users/tc045537/gitRepo/python/resources/data.txt','r')
file_data = file_obj.read()
file_obj.close()
print('data: {}'.format(file_data))

with open('/Users/tc045537/gitRepo/python/resources/data.txt','r') as f:
    file_data = file_obj.read()

print('data: {}'.format(file_data))