/* CSC 236 Example of creating and using binary search trees in C++.

   Shows how to use a tree to store information, and in particular how to
   search through a binary search tree. This program both creates a binary
   search tree given an array, searches the tree given a target value, and
   deletes the tree before the program ends.
   */

#include<iostream>
#include <assert.h>
#include <string>

using namespace std;

struct Node //This is a Node with the integer type as the data type
{
    int data;
    Node *leftLink; //link is a pointer to another Node
    Node *rightLink;
}; 
/*---
Given a pointer to a root of a tree, it will populate it with values
from the array numbers. This function will continually split the array into
left and right pieces that will be used to populate the subtree to
the right and to the left, respectively. The root of the subtree will
have the value at the index where the array was split.
It also does the node creation.
precondition: arraySize accurately states the number of items in numbers,
    numbers refers to an allocated space for storing numbers,
    thisNode points to an existing node (and not some random point in
    memory)
postcondition: thisNode will point to a tree that has as its children
    and leaves the balanced binary search tree with values from numbers.
--- */
void populate_from_array(Node* currentNode, int* numbers, int arraySize)
{
    int index = arraySize/2;    // bifurcate the list to call this function recursively
    int value = numbers[index]; // have the value at the middle of the array as the value of
                                // of this node, and then work on the left and right subtree.

    assert( currentNode != NULL ); // There is something REALLY wrong if this node is NULL.

    // BASE CASE: There is only one element, so it is a leaf!
    currentNode->data = numbers[index];
    currentNode->leftLink = NULL;   // Make sure that this leaf points to nothing.
    currentNode->rightLink = NULL;  // Make sure that this leaf points to nothing.
    if(arraySize == 1) {
        return;
    }

    // Coming to this point in the code means that this "leaf" actually is the root of
    // a subtree, so we need to create the left and right children if necessary and
    // continue the process of creating subtrees recursively.

    // Ok, create the left array and recursively call this function to
    // build the leftmost subtree (i.e. currentNode is an internal node
    currentNode->leftLink = new Node;
    int* leftArray = new int[index];// temporarily create the subarray
    // Copy the values of the left half of the array to a another version to
    // pass into the recursive call.
    for( int i = 0; i<index; i++ ) {
        leftArray[i] = numbers[i];
    }
    populate_from_array(currentNode->leftLink, leftArray, index);
    delete leftArray;   // delete the array that was used to make the left subtree

    int rightSize = arraySize - index - 1;
    if( rightSize == 0 ) return; // the child in the right size does not exist!

    // create the right subtree and then process the right array into the right tree.
    currentNode->rightLink = new Node;
    int* rightArray = new int[rightSize];
    for( int i = index+1; i<arraySize; i++ ) {
        rightArray[i-(index+1)] = numbers[i];
    }
    populate_from_array(currentNode->rightLink, rightArray, rightSize);
    delete rightArray;  // delete the array that was used to make the right subtree
}

/*---
delete the tree rooted at currentNode. It checks to make sure that
the children are gone first, so it does a reverse deletion from the
leaves back up to the root.
precondition: currentNode is either pointing to a valid tree node or
    is NULL
postcondition: the tree rooted at currentNode has been deallocated.
---*/
void delete_node( Node* currentNode )
{
    // BASE CASE: Reached beyond the leaf, must return to
    // delete it.
    if( currentNode == NULL ) {
        return;
    }

    // RECURSION: Make sure that the children are gone first before
    // this node is deleted.
    if( currentNode->leftLink != NULL ) {
        delete_node( currentNode->leftLink );
    }
    if( currentNode->rightLink != NULL ) {
        delete_node( currentNode->rightLink );
    }
    // We only get here when both children are gone, so it is a leaf. DELETE!
    delete currentNode;
}

/*---
This function recursively searches for the value targetValue in the subtree rooted at
currentNode.
precondition: currentNode refers to a valid node
postcondition: if the value is in the tree, it will return true, otherwise,
    if it "falls off" the tree, it means that it did not encounter the value
    so it returns false.
---*/
bool find_value( Node* currentNode, int targetValue ) {

    // BASE CASE 1: The value is not in the tree, so we "fell off"
    if( currentNode == NULL ) {
        return false;
    }
    // BASE CASE 2: The value is found, so STOP LOOKING!
    else if( currentNode->data == targetValue ) {
        return true;
    }

    // RECURSION: Depending on the value, travel to the right or left.
    if( targetValue < currentNode->data )
        return find_value( currentNode->leftLink, targetValue );
    else
        return find_value( currentNode->rightLink, targetValue );

}

// This main function calls the function to create a tree.
int main()
{
    int numItems = 7;
    int* numberList = new int[numItems];
    int searchValue = 0;

    // create an array of the sequence 0 followed by 6 even numbers
    for( int i=0; i<numItems; i++ ) {
        numberList[i] = i*2;
    }

    // create the root node and then the entire tree, rooted
    // at the root.
    Node* rootNode = new Node;
    populate_from_array( rootNode, numberList, numItems);

    // ask the user for a value to find in the tree, then search
    // for it.
    cout << "value to find? ";
    cin >> searchValue;
    if( find_value( rootNode, searchValue ) ) {
        cout << "Found " << searchValue << endl;
    }
    else {
        cout << searchValue << " is not in the tree!" << endl;
    }

    // Recursively delete the tree (deallocate all the nodes)
    delete_node(rootNode);
    return 0;
}
