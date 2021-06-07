#HASHMAP AND HASHTABLE ARE SAME = DICTIONARY

class HashTable:
    def __init__(self):
        self.max=100 #size of array
        self.arr=[None for i in range(self.max)] #initializing array
    
    #HASH FUNCTION
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max #RETURNING THE INDEX OF THE ARRAY BY USING MOD OD SUM OF ASCII VALUES
    
    def add_ele(self,key,value):
        k=self.get_hash(key)
        self.arr[k]=value
    
    def get_ele(self,key):
        k=self.get_hash(key)
        print(self.arr[k])
    
    def del_ele(self,key):
        k=self.get_hash(key)
        self.arr[k]=None
    
    #ALTHOUGH THIS IS ARE DICTIONARIES SO WE WANT TO USE THIS FOR MORE CONVIENENT
    # A['MARCH 1']=101 WILL SET THE VALUE
    # A['MARCH 1'] WILL GET THE VALUE
    # TO ENABLE THIS WE HAVE TO USE INDEX OPERATORS. | LUCKILY PYTHON SUPPORTS THIS
    # __getitem__ | __setitem__ | __delitem__

    def __setitem__(self,key,value):
        k=self.get_hash(key)
        self.arr[k]=value
    
    def __getitem__(self,key):
        k=self.get_hash(key)
        print(self.arr[k])
    
    def __delitem__(self,key):
        k=self.get_hash(key)
        self.arr[k]=None  #del t[] will delete



t=HashTable()
print(t.arr)
t.add_ele('march 1',101)
t.get_ele('march 1')
#Now using index operations
t['march 2']=102
t['march 2']
print(t.arr)