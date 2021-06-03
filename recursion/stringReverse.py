def printReverse(str):
    helper(0, str)

def helper(index, str):
    if str is None or index >= len(str):
        return 
    helper(index+1, str)
    print(str[index], end='')

#printReverse('123')


# string reverse in place with o(1) extra memory

    
def reverseString(s):
    def reverseStringHelper(left, right):
        if left >= right:
            return
        reverseStringHelper(left+1,right-1)
        s[left], s[right] = s[right], s[left]
    
    reverseStringHelper(0, len(s)-1)

s = ['a','b','c','d','e']
reverseString(s)
for val in s:
    print(val)