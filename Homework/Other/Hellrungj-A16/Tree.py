#-------------------------------------------------------------------------------
# Name:        BinarySearchTree.py
# Purpose:  CSC 236 Example of creating and using binary search trees in Python.
#
#   Shows how to use a tree to store information, and in particular how to
#   search through a binary search tree. This program both creates a binary
#   search tree given an array, searches the tree given a target value, and
#   deletes the tree before the program ends.
#
#-------------------------------------------------------------------------------
# Put the definition of the Node structure after this line.
class Node():
    def __str__(self):
        """Constructs a Node."""
        self.Notedata = 0
        self.NodeleftLink = 0 #link is a pointer to another Node
        self.NoderightLink = 0
# Put the definition of the three recursive functions after this line.

def populate_from_array(currentNode, numbers, arraySize):
    """precondition: arraySize accurately states the number of items in numbers,
        numbers refers to an allocated space for storing numbers,
        thisNode points to an existing node (and not some random point in memory)
    postcondition: thisNode will point to a tree that has as its children
        and leaves the balanced binary search tree with values from numbers."""

    index = arraySize/2    # bifurcate the list to call this function recursively
    value = numbers[index] # have the value at the middle of the array as the value of of this node, and then work on the left and right subtree.

    assert( currentNode != None ) # There is something REALLY wrong if this node is NULL.

    # BASE CASE: There is only one element, so it is a leaf!
    currentNode.Notedata = numbers[index]
    currentNode.NodeleftLink = None  # Make sure that this leaf points to nothing.
    currentNode.NoderightLink = None  # Make sure that this leaf points to nothing.
    if arraySize == 1:
        return
    currentNode.NodeleftLink = Node()
    leftArray = index
    for i in index:
        leftArray[i] = numbers[i]
    populate_from_array(currentNode.NodeleftLink, leftArray, index)
    del leftArray   
    
    currentNode.NoderightLink = arraySize - index - 1
    rightSize = arraySize - index - 1
    if rightSize == 0: 
        return 

    currentNode.NoderightLink = Node()
    rightArray = rightSize
    index = 0
    for i in arraySize:
        rightArray[i-(index+1)] = numbers[i]
        index=+1
    populate_from_array(currentNode.NoderightLink, rightArray, rightSize)
    del rightArray 
    # Put the driver function definition; i.e. main() after this line

def find_value( currentNode, targetValue ):
    """precondition: currentNode is either pointing to a valid tree node or
        is NULL
    postcondition: the tree rooted at currentNode has been deallocated."""
    # BASE CASE 1: The value is not in the tree, so we "fell off"
    if currentNode == None:
        return False
    # BASE CASE 2: The value is found, so STOP LOOKING!
    elif currentNode.data == targetValue:
        return True

    # RECURSION: Depending on the value, travel to the right or left.
    if targetValue < currentNode.data:
        return find_value( currentNode.NodeleftLink, targetValue )
    else:
        return find_value( currentNode.NoderightLink, targetValue )
    #Recursively delete the tree (deallocate all the nodes)
def delete_node( currentNode ):

    # BASE CASE: Reached beyond the leaf, must return to
    # delete it.
    if( currentNode == None ):
        return
    # RECURSION: Make sure that the children are gone first before
    # this node is deleted.
    if currentNode.NodeleftLink != None:
        delete_node( currentNode.NodeleftLink )
    if currentNode.NoderightLink != None:
        delete_node( currentNode.NoderightLink )
    #We only get here when both children are gone, so it is a leaf. DELETE!
    del currentNode
    delete_node(Node)
    return 0

def main():
    """This main function calls the function to create a tree."""
    numItems = 7
    numberList = [None]*numItems #This is how you fix it.
    searchValue = 0
    #create an array of the sequence 0 followed by 6 even numbers
    for i in numItems:
        numberList[i] = i*2;
    #create the root node and then the entire tree, rooted at the root.
    rootNode = Node()
    populate_from_array( rootNode, numberList, numItems)

    #ask the user for a value to find in the tree, then search for it.
    searchValue = input("value to find? ")
    if find_value( rootNode, searchValue ):
        print("Found " + str(searchValue))
    else:
        print ( str(searchValue) + " is not in the tree!") 

if __name__ == '__main__':
    main()
