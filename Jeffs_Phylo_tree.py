#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 17:19:25 2017

@author: Crane

Modified Tue Feb 7th 20:10 2017
@author: Jeff Silverman, HMC '80

========================================================================

Created on Wed Jul  6 17:55:31 2016
                 C:\Python34\PhylogeneticTrees.py
@author: Crane
"""

# This is from https://www.cs.hmc.edu/twiki/bin/view/CFB/PhylogeneticTrees

import sys


"""
leafCount(Tree)

>>> leafCount(Groodies)
4
>>> leafCount((5,(3,("A", (), ()),("B", (), ())),("C", (), ())))
3
find(node, Tree)

This function returns True if the given node is in the given Tree and returns False otherwise. Some examples of find:

>>> find('W',Groodies)
True
>>> find('A',Groodies)
False
>>> find('E',Groodies)
True
subtree(node, Tree)

Returns the subtree of the given Tree rooted at the given node. Said another way, this function returns the tree beginning at node. This function can be very short, and may have as few as four lines in its body. It will be recursive, but can also call the find function for help. In particular, if the root of the Tree matches node then we just return that Tree. If not, we can use find to determine whether the species is in the left subtree or the right subtree, and then proceed from there. You can assume that node is present in Tree. Here are some examples:

>>> subtree("W", Groodies)
('W', (), ())
>>> subtree("Y", Groodies)
('Y', ('W', (), ()), ('Z', ('E', (), ()), ('L', (), ())))
>>> subtree("Z", Groodies)
('Z', ('E', (), ()), ('L', (), ()))
nodeList(Tree)

Takes a Tree as input and returns a list of all of the nodes in that tree (including both leaves and ancestral nodes). This function can be done in three lines of code, but you are welcome to make it longer if you like. Here is an example:

>>> nodeList(Groodies)
['X', 'Y', 'W', 'Z', 'E', 'L', 'C']
descendantNodes(node, Tree)

Returns the list of all descendant nodes of the given node in the Tree. This function will not be recursive itself, but it will call the nodeList and subtree functions for help. This function can be written in two lines of code (not counting the def line and the docstring).

Here are some examples of descendantNodes:

 >>> descendantNodes("X", Groodies)
 ['Y', 'W', 'Z', 'E', 'L', 'C']
 >>> descendantNodes("Y", Groodies)
 ['W', 'Z', 'E', 'L']
 >>> descendantNodes("Z", Groodies)
 ['E', 'L']

parent(node, Tree) returns the parent of the given node in the Tree. If the node has no parent in the tree, the function should return the special value None.

>>> parent("Y", Groodies)
'X'
>>> parent("W", Groodies)
'Y'
>>> parent("Z", Groodies)
'Y'
>>> parent("E", Groodies)
'Z'
>>> parent("X", Groodies)
>>> parent("X", Groodies) == None
True
scale(Tree,scaleFactor)

As we've discussed, internal nodes represent the most recent common ancestor of the species which descend from them. In the example tree above, we've labelled these nodes using letters, the same way we've labeled the leaf nodes. However sometimes biologists like to include other kinds of information at these nodes, for example, information on when that most recent common ancestor lived. Here is a tree where the internal nodes are labeled with numbers.

Tree = (4.3,
         ('C', (), () ),
         (3.2,
           ('A',(), ()),
           ('B',(),()))
        )
Perhaps we're measuring time in millions of years before present. In that case, this tree would tell us that species A and B had a most recent common ancestor which lived 3.2 million years ago, and that all three species (A, B and C) had a most recent common ancestor that lived 4.3 million years ago.

Your task now is to write a function scale which takes a Tree as input, and multiplies the numbers at its internal nodes by scaleFactor and returns a new tree with those values. Here are some examples:

>>> Tree = (4.3, ('C', (), () ),(3.2, ('A',(), ()), ('B',(),())) )
>>> scale(Tree,2.0)
(8.6, ('C', (), ()), (6.4, ('A', (), ()), ('B', (), ())))
We will later use this function to calibrate trees so we can better estimate dates in human evolution.



"""

TRACE=True

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

def leafCount ( tree ):
    """This counts the number of leaves in Tree tree.  A tree is a leaf
    if and only if both children are empty tuples"""
    if TRACE :
        print( "In leaf count at {}".format( tree[0] ), file=sys.stderr )
    assert len(tree) == 3, "In leafCount, at {}: the length of tree is {} but should be 3".format( tree[0], len(tree) )
    if tree[1] != () and tree[2] != () :
        return leafCount ( tree[1]) + leafCount ( tree[2])
    elif tree[1] != () :
        return leafCount ( tree[1])
    elif tree[2] != () :
        return leafCount ( tree[2])
    else :
# This tree is a leaf, both children are empty
        return 1

def find ( target, tree ):
    """This function returns True if the given node is in the given Tree and returns False otherwise. """
    if TRACE :
        print( "In find, at {}. ".format(tree[0]), file=sys.stderr )
    assert len(tree) == 3, "In find, at {}: the length of tree is {} but should be 3".format( tree[0], len(tree) )
# If this tree is what we're looking for, then we're done.
    if tree[0] == target :
        return True
# if this tree is not the tree we're looking for and this tree has no children, then it is hopeless.
    elif tree[1] == () and tree[2] == () :
        return False
# If this tree is not the tree we're lookikng for AND it has children, then maybe one of its descendents is the
# tree we're looking for.
    else :
        if tree[1] != () and tree[2] != ()  :
            return find ( target, tree[1]) or find ( target, tree[2])
        elif tree[1] != () :
            return find ( target, tree[1])
        elif tree[2] != () :
            return find ( target, tree[2])
        else :
            raise AssertionError ("At {}: for some reason, we're here".format(tree[0]) )




if __name__ == "__main__" :
# Do some unit testing
    def my_test ( actual, nominal, label):
        print ( label + " {} should be {}".format( actual,  nominal ) )
        assert actual == nominal, "At {}, {} should be {}".format( label, actual, nominal)

    my_test ( leafCount(Groodies), 4, "Groodies" )

    my_test ( leafCount((5,(3,("A", (), ()),("B", (), ())),("C", (), ()))), 3, "Instructor provided" )

    my_test ( leafCount (
        ( "Alice",
          ("Ben",      # Ben has 2 children
           ( "Charles", (), ()
             ),
           ( "David", (),
             ("Eric", (),
              ("Fred", (), ())
              )
            )
           ), ( 'George', (), () )
        )
       ),
        nominal=3, label="Jeff did it" )




    my_test ( find('W',Groodies), True, "W in Groodies" )
    my_test ( find('A',Groodies), False, "A in Groodies" )
    my_test ( find('E',Groodies), True, "E in Groodies" )

