# STEP-hw2

Problem 1

Codes file is matmul.py. Since I was not sure how to make the function more cache-friendly, I tried four different versions of matrix multiplication.

The resulting "time vs sizeN" plot is "result.png"



Problem 2

I think these two are some of the reasons why choosing BST instead of hashtable.

1. In BST, the keys are sorted in a particular order. A simple traversal can helps to get the order. Finding extremum or a particular 
  range of the data is easier.
  
2. It is mathematically difficult to self define a hashing function, while in BST the ordering reasoning can be modified 
  according to the need.



Problem 3

My idea is to create a doubly linked list for the entries of hashtable, such that the head is the website going to be deleted, 
and the tail is the newest one.

Also memo the number of inserted entries-- say, M-- all the time.



Let the number of websites allowed in cache is N and it is fixed. Use hashtable in hashtable to ensure that everytime the complexit
y is almost O(1). 

When there has been N websites saved in the hashtable, the inserting function fails and returns False, and needs some more work.
~~~
Everytime inserting one website W, check the number of occupied entries M.

  If M < N, simply insertly the new website(O(1)). M += 1, and also append it to the tail of 	doubly 	linked list (O(1))

  If M = N, search it to find if it is already here in the hashtable.

	  If so, stop inserting. Redirect the pointers pointed to it and from it,to make W to be the tail of the doubly linked list(O(1), 
      as the in doubly linked list, previous tail can be accessed in O(1))
    
	  If not, delete the last accessed website in the hashtable, which is also the head of linked list. Delete the head(O(1)).  
      Insert it the new element to the tail of doubly linked list(O(1)
~~~
