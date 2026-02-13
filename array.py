"""
Arrays are contiguous collection of values. 
These are collection of values stored contiguously in memory locations. In java, C, swift, arrays are 
homogenuous structures i.e with fixed data types and size. Hence memory allocation for each value and hence whole
array is fixed.

Contiguous vs Non-Contiguous block of values:
The advantage of storing a collection of values contigously is accessing. Accessing any index is done in 
constant time, start with first address, multiple by index value and data type allocated space. Instead if 
we decide to store the collection noncontiguously, each location needs to store the value and reference to 
next value. Because the basic property of arrays is to store values one after another in a particular order. 
Changing the order should change the array. Hence which value comes next is an important aspect in an array. 
This property of data structure array describes the relationship among the values which is an important aspect 
and needs to be stored along with the values.

List:
In Python, arrays are generally represented by list which are heterogenuous structures i.e with 
no fixed size and datatype. Storing in contiguous memory locations becomes difficult in such a case. Hence to 
resolve this, python stores addresses or pointers pointing to those values/objects. Addresses/Pointers have fixed 
size hence this way lists in python are able to store contiguous collection of values without fixed size and type.

The list stores pointers to objects, not the objects themselves!

✅ Pros:
1) Can store mixed types
2) Very flexible

❌ Cons:
1) Memory-heavy
2) Slower for numerical computation

To use OG array that stores continuous block of values instead of references, you can use array.array library 
in Python.


"""

#These values are stored elsewhere, the array stores only the references contiguously.
# Due to storage being contiguous, access is done in constant time instead of iteratively.
list = [1, 2, 3, 4, 'Aditya'] 

#Accessing a value in python list is done in constant time
val = list[3]

#Searching for a value in python list is done in linear time. Goes through each element sequentially
if 3 in list: print(True)

