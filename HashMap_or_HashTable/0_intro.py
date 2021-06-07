# In hashmap we have STRING index
# IMPLEMENTING HASH FUNCTION USING ASCII VALUES

'''
lookup / insertion / deletion is = O(1) average
'''


#HASH FUNCTION
def get_hash(key):
    h=0
    for char in key:
        h+=ord(char)
    return h%100 #WEHERE 100 IS THE SIZE OF THE ARRAY/LIST