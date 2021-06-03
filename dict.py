value = {'url1': 'abcd',
 'url2': 'efgh'}

def convert(s):
    try:
        x = int(s)
    except ValueError:
        print('conversion fsailed')
        x = -1
        return x

list = ['1a','2a','3a']
print(list)
tuple = ('1a','1a','1a')
print(tuple)