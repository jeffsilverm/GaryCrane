#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 09:49:08 2016

@author: Crane
"""
####  VERSION 1
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
        print('B1  onemx=',onemax,'useit=',useit,'loseit=',loseit)   # note –there is a misspelling of onemax  (onemx) but that is in a print string so presents no logical problem or implication 
        return max(onemax,useit,loseit)
    for i in list(range(2,len(x))): 
        print('C  i=',i,'len(x)=',len(x),'x=',x,'x[0]=',x[0],'x[i]=',x[i])  #'x[0]=',x[0],'x[i]=',x[i],'x[1:]=',x[1:]) 
        if len(x)>3: 
            print('D  i=',i,'x=',x,'len(x)=',len(x),'x[0]=',x[0],'x[i]=',x[i])   #,'x[1:]=',x[1:]) 
            useit=max(x[0]+x[i],x[0]+test(x[1:])) 
            loseit=test(x[1:]) 
        '''elif len(x)==3: 
            useit=x[0]+x[2] 
            loseit=x[2] 
        elif len(x)<3: 
            useit=0 
            loseit=0''' 
    return max(onemax,useit,loseit) 


def test_test ( expected, x ):
    """This function tests the test function"""
    r = test(x)
    if r != expected :
        print "Failure in test_test.  Expected %d, got %d, argument was %s" % \
              ( expected, r, x )

if __name__ == "__main__" :
    test_test(6,  [ 3, 6])
    test_test(7,  [ 1, 7, 4])
    test_test(11, [ 7, 1, 4])
    test_test(11, [ 2, 3, 9])
    test_test(4,  [ 1, 2, 3])
    test_test(4,  [-7, 1, 4])
    test_test(11, [ 1, 2, 3, 9])
    test_test(3,  [-1, 2, 3])


''' examples of running the above code  for Version 1:
test([1,2,3,9])
A  9 [1, 2, 3, 9]
C  i= 2 len(x)= 4 x= [1, 2, 3, 9] x[0]= 1 x[i]= 3
D  i= 2 x= [1, 2, 3, 9] len(x)= 4 x[0]= 1 x[i]= 3
A  9 [2, 3, 9]
B1  onemx= 9 useit= 11 loseit= 9                   ## useit has correct answer            
A  9 [2, 3, 9]
B1  onemx= 9 useit= 11 loseit= 9                    ## useit has correct answer 
C  i= 3 len(x)= 4 x= [1, 2, 3, 9] x[0]= 1 x[i]= 9
D  i= 3 x= [1, 2, 3, 9] len(x)= 4 x[0]= 1 x[i]= 9
A  9 [2, 3, 9]
B1  onemx= 9 useit= 11 loseit= 9                    ## useit has correct answer 
A  9 [2, 3, 9]
B1  onemx= 9 useit= 11 loseit= 9                     ## useit has correct answer 
Out[6]: 12                            ##WRONG!! correct answer =11
#-----------------------------------------------------------------
test([1,2,3])
A  3 [1, 2, 3]
B1  onemx= 3 useit= 4 loseit= 3            ## useit has correct answer 
Out[7]: 4                                  ## correct answer
#-----------------------------------------------------------------
test([-1,2,3])
A  3 [-1, 2, 3]
B1  onemx= 3 useit= 2 loseit= 3          ## loseit has correct answer
Out[8]: 3                                ##Correct!! the max functin picked correctly
#-----------------------------------------------------------------
test([1,5,3])
A  5 [1, 5, 3]
B1  onemx= 5 useit= 4 loseit= 3         ##onemx( should be onemax) has correct answer
Out[9]: 5                               ##Correct!! the max functin picked correctly
'''
#

