DS and Algo in Python:

Algorithm:
Algorithms are steps taken to execute a task. It's basically the way to implement a task. Comes from computer science algorithms are instructions to execute a task. There are number of ways to implement any task, bascially having number of algorithms. The goal is to not only learn what algorithm there exists but also which one to use. Choosing among different alogrithms is basically donw on the basis of efficiency:

Efficiency:
Efficiency in CS is defined in terms of speed and space. Speed is measured using time complexity and space measured using space complexity. Both of these measures are represented using Big-O notation.

Big-O notation:
This notation is is used to represent the complexity of algorithm as function of input size 'n'. 

Time Complexity:
Time complexity represented using this Big-O notation talks about the time taken by an algorithm as a function of input size(n).

Space Complexity:
Space complexity represented using this Big-O notation talks about the space taken by an algorithm as a function of input size(n).

There are different types of runtimes for existing algorithms like linear time: O(n), logarithmic time: O(logn), Quasilinear time: O(nlogn), quadratic time: O(n^2), cubic time: O(n^3), polynomial time: O(n^k), exponential time: O(k^n), factorial time: O(n!), etc. Below are couple of examples:

Linear time: O(n) - Searching for a number in a list can be done using Linear search and has a runtime of O(n), i.e. it linearly increases with n.

Logarithmic time: O(logn) - Searching for a number in a sorted list can be done using Binary search and has a runtime of O(logn), i.e. it increases with logn.

Quasilinear: O(nlogn) -  Sorting a list can be done using merge sort which whose runtime is proportional to nlogn.

Exponential: O(k^n) - If input n represent the no. of dials on a lock. The runtime varies as function of k^n where k rpesented the number of values for each dial.

Factorial time: O(n!) -  Travelling salesman problem is done in factorial time which is basically insolvable.

We mostly look at algorithms solvable in polynomial time. All these runtimes are measured for the worst case scenario. Comparing the worst case scenario makes sense as there's no room for surprise. These Big-O notation runtime are compared across same problem tasks but implemented using different algorithms in worst case for each n. In this way, there are also best case scenario and avg case scenario for each algorithm.