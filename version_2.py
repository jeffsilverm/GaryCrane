#! /usr/bin/python2
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------
#----------------------------------------------------------------- 
#-----------------------------------------------------------------  
"""
Created on Mon Jun  6 09:49:08 2016

@author: Crane
"""
### VERSION 2
def test(x):
    onemax=max(x)
    print('A ',onemax,x)
    if len(x)<3:
        useit=0
        loseit=0 
    if len(x)==3:
        useit=x[0]+x[2]
        #print('B1  useit=',useit)
        loseit=x[2]  
        print('B1  onemax=',onemax,'useit=',useit,'loseit=',loseit,'answer=',max(onemax,useit,loseit))
        return 'Final Result from B1=',max(onemax,useit,loseit)
    print('KK  len(x)=',len(x),'x=',x)
    if len(x)>3:
        print('C  len(x)=',len(x),'x=',x,'x[0]=',x[0],'x[1:]=',x[1:])  #'x[0]=',x[0],'x[i]=',x[i],'x[1:]=',x[1:]) 
        for i in list(range(2,len(x))):
            if len(x)-i>=2:
                print('D  i=',i,'x=',x,'len(x)=',len(x),'x[0]=',x[0],'x[i]=',x[i])   #,'x[1:]=',x[1:])
                useit=max(x[0]+x[i],x[0]+test(x[1:]))
                loseit=test(x[1:])
        '''elif len(x)==3:
            useit=x[0]+x[2]
            loseit=x[2]
        elif len(x)<3:
            useit=0
            loseit=0'''
    return 'Final Result from end of function ',max(onemax,useit,loseit)

''' example of running the above code  for Version 2:

test([1,2,3,9])
A  9 [1, 2, 3, 9]
KK  len(x)= 4 x= [1, 2, 3, 9]
C  len(x)= 4 x= [1, 2, 3, 9] x[0]= 1 x[1:]= [2, 3, 9]
D  i= 2 x= [1, 2, 3, 9] len(x)= 4 x[0]= 1 x[i]= 3
A  9 [2, 3, 9]
B1  onemax= 9 useit= 11 loseit= 9 answer= 11      # note the correct answer
Traceback (most recent call last):

  File "<ipython-input-30-810303365aab>", line 1, in <module>
    test([1,2,3,9])

  File "<ipython-input-29-1a72ebc9f124>", line 19, in test
    useit=max(x[0]+x[i],x[0]+test(x[1:]))

TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
  ### it appears to me that Python is attempting to create useit when len(x)-i<2 ... 
when I know the formula won't work ... 
but - Python should not have even tried ... so what is going on here?

#-------------------------------------------------------------
Here is another example but one that shows an incorrect answer when len(x)=3 '''
'''
test([1,2,12,9])
A  12 [1, 2, 12, 9]
KK  len(x)= 4 x= [1, 2, 12, 9]
C  len(x)= 4 x= [1, 2, 12, 9] x[0]= 1 x[1:]= [2, 12, 9]
D  i= 2 x= [1, 2, 12, 9] len(x)= 4 x[0]= 1 x[i]= 12
A  12 [2, 12, 9]
B1  onemax= 12 useit= 11 loseit= 9 answer= 12   # correct answer =13, and that has not been computed
Traceback (most recent call last):

  File "<ipython-input-31-7107644dc176>", line 1, in <module>
    test([1,2,12,9])

  File "<ipython-input-29-1a72ebc9f124>", line 19, in test
    useit=max(x[0]+x[i],x[0]+test(x[1:]))

TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
'''
#
