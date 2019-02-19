#!/usr/bin/env python
# coding: utf-8

# In[114]:


#Hash Table implementation in Python
class PHash:
    def __init__(self):
        self.size=11
        self.slot=[None]*self.size
        self.data=[None]*self.size
    

    def hashFunc(self,key,size):
        return ord(key)%size
                     

    def reHashFunc(self,oldHash,size):
        return (oldHash+1)%size
#get() return the value of key item if found
    def get(self,key,size):
        for i in range(0,size):
            
            if self.slot[i]== key:
                return self.data[i]
        return None
    
#put() insert an item pair into the hash table
    def put(self,key,data):
        hashIndex=self.hashFunc(key,int(len(self.slot)))
        if self.slot[hashIndex]==None:
            self.slot[hashIndex]=key
            self.data[hashIndex]=data
        else:
            nextSlot=self.reHashFunc(hashIndex,int(len(self.slot)))
            while self.slot[nextSlot]!=None and self.data[nextSlot]!=key:
                    if self.slot[nextSlot]==None:
                        self.slot[nextSlot]=key
                        self.data[nextSlot]=data
                    elif self.slot[nextSlot]==key:
                        self.data[nextSlot]=data
                
                    nextSlot=self.reHashFunc(hashIndex,len(self.slot))
    
        

#delPair() function delete key-pair value if found
    def delPair(self,key):
        flag=False
        for i in range(0,self.size):
            if self.slot[i]==key:
                self.slot[i]=None
                self.data[i]=None
                flag=True
        if flag==True:
            print('\nItem pair found and deleted')
        else:
            print('\nNot found')


#lenTable() return the number of key-vlue pair in hash table
    def lenTable(self):
        l=0
        for i in range(0,self.size):
            if self.slot[i]!=None:
                l=l+1
        return l       

#display() display the entire table in key-value format
    def display(self):
        for i in range(0,self.size):
            if self.slot[i]!= None and self.data[i]!=None:
                print(self.slot[i]+':',self.data[i])
                


# In[ ]:




