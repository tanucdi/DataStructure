#User function Template for python3

def reverseWord(s):
    #your code here
    a=len(s)
    w=''
    while a>0:
        w=w+s[a-1]
        a-=1
    return w


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends