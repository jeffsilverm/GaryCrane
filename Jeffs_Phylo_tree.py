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

from __future__ import print_function   # Makes the code work equally well on python 2 or python 3
import sys
import pprint
import pdb


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
# Set this flag to True for debugging purposes.  Clear this flag for production.
DEBUG_FLAG=True

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
    if DEBUG_FLAG :
# See https://docs.python.org/3.6/library/string.html#custom-string-formatting for more information on the format method
        print( "In leaf count at {}".format( tree[0] ), file=sys.stderr )
# This is a test to make sure that I haven't done something stupid.  In general, when I find a bug, I fix it, and then
# I add a test to make sure that it stays fixed.
    assert len(tree) == 3, "In leafCount, at {}: the length of tree is {} but should be 3.  tree is {}".format( tree[0], len(tree), \
                                                str( tree ) )
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
    if DEBUG_FLAG :
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
# raise AssertionError does the same thing as the assert statement, but without the test.  We know that if we got here,
# Then something is wrong with the program because an earlier test dealt with the case where both tree[1] and tree[2]
# are both empty tuples.
            raise AssertionError ("At {}: for some reason, we're here".format(tree[0]) )

def nodeList(tree):
    '''returns the list of nodes in a given tree'''
    nodes = [tree[0]]
    if len(tree[1]) > 1:
        nodes = nodes + nodeList(tree[1])
    if len(tree[2]) > 1:
        nodes = nodes + nodeList(tree[2])
    return nodes

def subtree(node_name, tree):
    """ Returns the subtree of the given Tree rooted at the given node.
    Said another way, this function returns the tree beginning at node.
    This function can be very short, and may have as few as four lines in
    its body. It will be recursive, but can also call the find function
    for help. In particular, if the root of the Tree matches node then
    we just return that Tree. If not, we can use find to determine whether
    the species is in the left subtree or the right subtree, and then proceed
    from there. You can assume that node is present in Tree. Here are some examples:

>>> subtree("W", Groodies)
('W', (), ())
>>> subtree("Y", Groodies)
('Y', ('W', (), ()), ('Z', ('E', (), ()), ('L', (), ())))
>>> subtree("Z", Groodies)
('Z', ('E', (), ()), ('L', (), ()))

"""
# Verify that were given a tuple
    assert type(tree) == type( () ), "In subtree: the type of tree should be tuple, but is {}".format(str(type(tree)))
# If we're given an empty tree, then return an empty tree
    if len(tree) == 0 :
        return ( () )
    # This is a test to make sure that I haven't done something stupid.  In general, when I find a bug, I fix it, and then
    # I add a test to make sure that it stays fixed.
    assert len(tree) == 3, "In subtree, at {}: the length of tree is {} but should be 3.  tree is {}".format(tree[0],
                                                                            len(tree), str(tree) )
    if DEBUG_FLAG :
        print("node_name=", node_name, "tree is ", tree, file=sys.stderr )
        if tree[1] != () and tree[2] != () :
            print ( "In subtree at node {}.  One of the children is {} and the other child is {}".format \
                    ( tree[0], tree[1][0], tree[2][0] ), file=sys.stderr )
        elif tree[1] != ()  :
            print ( "In subtree at node {}.  Child 1 is {} and there is no child 2".format \
                    ( tree[0], tree[1][0] ), file=sys.stderr)
        elif tree[2] != ()  :
            print ( "In subtree at node {}.  There is no child 1 and child 2 is {} ".format \
                    ( tree[0], tree[2][0] ), file=sys.stderr)
        else :
            print ( "In subtree at node {}.  There are no children ".format ( tree[0]  ), file=sys.stderr )
# THIS IS HORRENDOUS DEBUG CODE
        if tree[0] == "Ben" :
            print("in subtree at Ben.  Hitting a breakpoint.  HORRENDOUS DEBUG CODE")
            print("node_name=", node_name, file=sys.stderr )
            pp.pprint(tree)
            pdb.set_trace()

    try:
# This block of code should be refactored to test to see if we found what we are looking first.
        if tree[1] == () and tree[2] == ():
    # this node has no children, so it has no subtrees, this tree is a leaf.  The node_name
    # is in tree[0].  If this node is not the node we are looking for, then return an empty
    # tuple, because the node_name was not found
            if tree[0] != node_name :
                print("At {}: there are no children and did not find {} so can not search further".format(tree[0], \
                                node_name), file=sys.stderr)
# Construct a leaf node
            return ( ( tree[0], (), ()  )  )
        elif tree[1] != () and tree[2] != ():
            if tree[0] == node_name :
    # We found our node.  Both tree[1] and tree[2] are both subtrees
                return ( tree[0], subtree(node_name,tree[1]), subtree(node_name,tree[2]) )
            else :
                return ( (subtree(node_name, tree[1]), subtree(node_name, tree[2]) ) )
        elif tree[1] != () :
    # tree[1] is a subtree, tree[2] is a leaf
            if tree[0] == node_name :
    # Here, we are building a new node, with the name of the node, the subtree in child 1, an empty subtree in child 2
                return ( tree[0], subtree(node_name, tree[1], ()) )
            else :
    # Return a subtree, which is a tree, but do not create a new node
                return subtree(node_name, tree[1] )
    # tree[2] is a subtree, tree[1] is a leaf
        elif tree[2] != () :
            if tree[0] == node_name :
                return ( tree[0], (), subtree(node_name, tree[2] ) )
            else :
                return subtree(node_name, tree[2] )
        else :
            print("About to raise AssertionError", file=sys.stderr )


    except AssertionError as a:
        print("in subtree at {}: one of the children raised AssertionError.  Child 1 is {}.  Child 2 is {}" ).format(\
                tree[0], tree[1][0], tree[2][0] )
# Raise the AssertionException.  This will force the caller to run its AssertionError handler and output the values at
# its level
        raise
    raise AssertionError("Not sure how we got here, in subtree, but we did.\n  Tree is {}".format(str(tree)))


# This is a unit test.  If this module is imported into another module, then this test will fail and the following software
# will not be executed.  But if this module is NOT imported, the __name__ will be "__main__" and the software below will be
# executed
if __name__ == "__main__" :
# Do some unit testing
    pp = pprint.PrettyPrinter()

# Define my own test tree, which is different from but similar to Groodies
# Note that there are 4 test cases: no children, #1 child, #2 child, 2 children
    fred = ("Fred", (), () )         # Fred has no childer
    george = ("George", (), () )    # George has no children
    eric = ("Eric", fred, () )      # Fred is Eric's son (first child)
    david = ("David", (), eric )    # Eric is David's son (second child.  I know this is strange, but I need it for debugging
    charles = ( "Charles", (), () ) # Charles has no children
    ben = ( "Ben", charles, david)  # Ben has 2 children
    alice = ( "Alice", ben, george )
    jeffs_tree = alice              # Note that this is not a copy!  2 identifiers pointing to the same object
#    jeffs_tree =         ( "Alice",      # Alace's children are Ben and George
#          ("Ben",      # Ben has 2 children, Charles and David
#           ( "Charles", (), ()    # Charles has no children
#             ), \
#           ( "David", (),    # David has 1 son, Eric
#             ("Eric", (),     # Eric has a son, Fred.  Fred a second son, not because that means anything but it is a test case
#              ("Fred", (), ())       # Fred has no children
#              ),
#             () \
#            ), \
#           ), \
#          ( 'George', (), () )       # George is the son of Alice
#        )
    pp.pprint( jeffs_tree )

    def my_test ( actual, nominal, label):
        """This is a generic test subroutine.  actual is the result of the function.  nominal is the "correct" answer
        label is a message to print """

        if actual == nominal :
            print( "CORRECT: {}".format(label) )
        else :
            if type(nominal) == type( () ) :
                print("ERROR at {} is a tuple.  Nominal is:".format(label) )
                pp.pprint(nominal)
                print("Actual is:")
                pp.pprint(actual)
            else :
                print ( "ERROR at {}: {} should be {}".format( label, actual,  nominal ) )
        return ( actual, nominal )

    my_test ( leafCount(Groodies), 4, "Groodies" )

    my_test ( leafCount((5,(3,("A", (), ()),("B", (), ())),("C", (), ()))), 3, "Instructor provided" )

    my_test ( leafCount ( jeffs_tree ), nominal=3, label="Jeff's tree" )




    my_test ( find('W',Groodies), True, "W in Groodies" )
    my_test ( find('A',Groodies), False, "A in Groodies" )
    my_test ( find('E',Groodies), True, "E in Groodies" )


    my_test ( subtree( node_name='W', tree=(('W', (), () )) ), nominal=('W', (), () ), label="Testing subtree with W" )

    my_test ( subtree( node_name="David", tree=jeffs_tree), david, "Testing subtree with david" )

    my_test ( subtree( node_name="Ben", tree=jeffs_tree), ben, "Testing subtree with ben" )


