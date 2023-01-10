# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:57:28 2023

@author: Surface
"""
#11.4
lst=[1,2,2,3,4,5,6,7,7,8,9]
new_list=[]
def has_duplicates():
    for i in lst:
        if i not in new_list:
            new_list.append(i)
            if new_list==lst:
               return False
            else:
               return True
        #这样能确保新的列表里包含原列表里所有种类的元素，且元素互不重复
print(has_duplicates())

#dict1={}
#for i in lst:
    #if i not in dict:
    #    dict1.append(i)
   # print(dict1)

def has_duplicates(t):
    
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

   
   
   
    