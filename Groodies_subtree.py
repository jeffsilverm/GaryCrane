# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:09:10 2017

@author: Crane
"""

Groodies =  ( "X",
                ("Y",
                    ("W", (), ()),
                    ("Z",
                        ("E", (), ()),
                        ("L", (), ())
                    )
                ),
                ( "C", (), () )
            )
            
if False :
    def subtree(node,tree):
        '''Returns the subtree of the given Tree rooted at the given node.
        Presume the node is in the tree.'''
        if node==tree[0]:
            return tree
        else:
            subtree(node,tree[1])
            subtree(node,tree[2])
        
def subtree1(node,tree, level=1):
    '''Returns the subtree of the given Tree rooted at the given node.
    Presume the node is in the tree.'''
    if len( tree ) == 0 :
        print( "\nAt level", str(level), "Length of tree is 0, so node wasn't found")
        return None
    print( "\nAt level", str(level), 'Before comparison of node ', node, "left element", tree[0], "whole tree ",tree)
    if node==tree[0]:
        print("At level", str(level), 'SUCCESS!   tree=',tree,'tree[0]=',tree[0],'node=',node)
        return tree
    else :
        print("At level", str(level), 'NOT YET: ',node, ' is not = ',tree[0])
        print("At level", str(level), 'NEXT STEP:  testing middle element',node,' in ',tree[1])
        result = subtree1(node,tree[1], level+1)
        if result == None :
            print("At level", str(level), 'LAST STEP:  testing right element',node,' in ',tree[2])
            result = subtree1 (node,tree[2], level+1)
    return result
        
if __name__ == "__main__" :
    assert subtree1("X", Groodies ), "X was not found and should have been"
    print("\n***************")
    assert subtree1("Y", Groodies ), "Y was not found and should have been"
    print("\n***************")
    assert subtree1("L", Groodies ), "L was not found and should have been"
    print("\n***************")
    assert subtree1("C", Groodies ), "c was not found and should have been"
    print("\n***************")
    assert not subtree1("ql", Groodies ), "ql was found and should not have been"
    print("\n***************")
    assert not subtree1("z2", Groodies ), "z2 was found and should not have been"
    print("\n***************")

