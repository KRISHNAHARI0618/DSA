# DSA : 
- #[ Dsa Notes:](https://github.com/Deeksha2501/Data-Structures-and-Algorithms-Notes/tree/main)
- Data Structures and Algorithms:
  - Structuring the data in a useful manner
- *Complexity Analysis*
  - By Counting the number of simples operations that computer has to do to solve any problem
  - As input grows in what proportion does the number of operations grow
  - How Run Time Grows as Input Grows
- *Asympototic Analysis*
  - As an illustration, suppose that we are interested in the properties of a function f (n) as n becomes very large. If f(n) = n2 + 3n, then as n becomes very large, the term 3n becomes insignificant compared to n2. The function f(n) is said to be "asymptotically equivalent to n2, as n → ∞". This is often written symbolically as f (n) ~ n2, which is read as "f(n) is asymptotic to n2".
#### Big O Notation:

- A Mathematical Notation that describes the limiting behaviour for function tends towards a particular value or infinity
- As Input order increases propotion also get increases

#### Common Complexities:

- Big O `worst case find out how to optimize`
- Big O(n) `Linear Structure`
- Drop Constants ` Constants does have much impact on program`
- Big(n^2) `Loop Inside Loop`
- Drop Non-Dominants ` O(n^2 + n) we will drop single n`
- Big O(1) `Simple Operations like addition etc ..`
- O(log n) ` Divide and Conquor - Sorting Algorithms`
- O(a+b) ` if iterations are different`
- O(a*b) ` if the lop iteratees inside for multiple times`

#### Array/List Data Structures:

- Accessing An element ---> `O(1)` Time ---> `O(1)` Space
- Set an Element ---> `O(1)` Time ---> `O(1)` Space
- Traversing an element ---> `O(n)` ---> `O(1)` Space
- Searching An element ---> `O(n)` Time ---> `O(1)` Space
- Copy Array ---> `O(n)` Time ---> `O(n)` Space
- Inserting an Element
  - At the Begining ---> `O(n)` Time ---> `O(1)` Space
  - At the end ---> `O(1)` Time ---> `O(1)` Space
  - Somewhere in midde ---> `O(n)` Time ---> `O(1)` Space
- Removing an Element 
  - At the Begining ---> `O(n)` Time ---> `O(1)` Space
  - At the end ---> `O(1)` Time ---> `O(1)` Space
  - Somewhere in midde ---> `O(n)` Time ---> `O(1)` Space

#### Recursion Notes:`[used](DP,Back-Tracking,BST)`

- *What is Recursion*
  - Function Calling By Itself until the specified condition met or based condition met is called **Recursion**
- *Recursive Leap of Faith* `How to Use Recursion`
  - 1: Understand The problem
  - 2: Identify the Sub-Problem
  - 3: Trust/Faith
  - 4: Link 1 & 2
  - 5: Base Condition
- Recurrance Relation 
  - Express the solution of porblem using solutions of teh subproblems

## Back-Tracking:

1. What is Back-Tracking?
   1. Logarithimic Approach to solve problem in a multiple ways with controlled recursion method
   2. Solutions are Build Step By Step
   3. If one path of solution dont give correct answer violates that path
   4. Modifications are done in-place
2. How is Backtracking is different from Recursion?
3. Pseudo Code for Back-Tacking
```
def helper():
  if valid:
    print
    return
  for choice in choices:
    if isValid(choice):
    choose
    helper()
    revert choice

helper()
```
4. How to find permutations is almost equal to factorial for numbers 
   1. - - - == 3! == 6 ways 3 characters word or number can rotate 6 ways
#### 8 Patterns to Solve 80% Leetcode problems

1. 2 pointer
2. Binary Tree BFS
3. Topological Sort
4. Binary Tree DFS
5. Top K Elements
6. Modified Binary Search
7. Subset
8. Sliding window
9. Backtracking[Recursion]
10. Dynamic Programming
11. HashMaps

### Linked List
- Linked list does not have indexes
- it will not store in contiguous locations
- it will have head and tail on is connecetd to another in the memory
- it is connected between the nodes

- **What is Linked List**
- Linked list Is a Form of sequential collection and it does not have to be in order. A linked list is made up of independent nodes that may contain any type of data and each node has a reference of next node in the link
- Linked List is not contigious

- Types of Linked Lists:
  - Singly Linked List : Reference of last node is Null
  - Double Linked List : It contains the reference of previous node and next node
  - Circular Singly Linked list : reference of last node is First Node
  - Circularly Double Linked List: reference of last node is First node value
  
### Hash Tables
- Collisions :
  - Seperate Chaining
    - 
- Linear Probing
```
class HashTable
```
### A Recipe for Problem Solving:
- **Understand the Problem**:
  - Can we restate the problem in our own words?
  - What are inputs that go into the problem?
  - What are output that come from the problem?
  - Can the outputs determined from the inputs provided
  - Do we have enough info to solve the problem?
  - what should i label the important piece of data that are part of a problem?
- **Explore the concrete examples**
  - start with simple examples
  - progress to more complex examples
  - explore with empty inputs
  - explore with invalid inputs
- **BreakDown the Problem**
  - Write out the steps that you need to take
- **Solve and Simplify**
  - Simplify the problem and write the simple steps
- **Look Back Refactor**
  - Improve the code and reduce the time complexity
  - Check result
  - try different ways
  - understand it a glance
  - how other poeple solve this problem

## DSA Concepts:
- Tree/Binary Trees
- Binary Search Tree
- AVL Tree
- Binary Heap
- Trie
- Hashing
- Sort Algorithms
- Searching Algorithms
- Graph Algorithms
- Graph Traversal
- Topological Sorting
- All Pairs Shortest Path
- Greedy Algorithms
- Divide and Conquer
- Dynamic Programming
- Backtracking
- The Wild West (possibly a project or special topic)

# Data Structures and Algorithms (DSA) - Interview-Focused Roadmap

## Introduction
- Introduction to DSA
- Time & Space Complexity Analysis (Big O Notation)

## Arrays & Strings
- Arrays - Basics & Operations
- String Manipulation & Pattern Matching
- Sliding Window Technique
- Two Pointer Technique
- Kadane’s Algorithm (Maximum Subarray)

## Searching Algorithms
- Linear Search
- Binary Search (with Variants: First/Last Occurrence, Search in Rotated Sorted Array)

## Sorting Algorithms
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Counting Sort
- Radix Sort

## Recursion & Backtracking
- Recursion Basics
- Backtracking Basics
- N-Queens Problem
- Sudoku Solver
- Subsets, Permutations, Combinations
- **Recursion Concepts:**
  - A way of solving a problem by calling function itself
  - Same function calling multiple times with decreasing the input values 
  - Base Condition is needed to mention else infinite loop will occur
- **Why Recursion**
  - Recursion the important when you have  bigger problem need to divide sub-problems
  - The prominent usage of recursion in data structures like trees and graphs
  - interviews
  - It is used in many algorithims 
    - divide and conquer
    - Greedy
    - Dynamic Programming
  - **Recursion vs Iteration**
    - recursion will take stack space while iteration not
    - recursion will take time as input grows while iteration not
    - Iteration is better in some places 
  - **When to Use Recursion**
    - when we can easily breakdown larger problems into sub problems
    - when we are fine with extra spaces and extra time that comes with it
    - when we need quick working solution 
    - when we use traversal
    - when we use memoization in recursion

## Linked Lists
- Linked Lists - Basics & Operations
- Linked Lists - Reversal & Merge
- Detect Cycle (Floyd’s Algorithm)
- Intersection of Two Linked Lists

## Stack & Queue
- Stack - Basics & Applications
- Queue - Basics & Variants
- Next Greater Element
- Min Stack
- Implement Queue using Stacks / Stack using Queues
- LRU Cache (Design Problem)

## Trees
- Trees - Basics & Traversals (Inorder, Preorder, Postorder, Level Order)
- Binary Search Trees (BST)
- Lowest Common Ancestor (LCA)
- Diameter of a Binary Tree
- Balanced Binary Tree
- Serialize & Deserialize Binary Tree

## Heaps
- Heap & Priority Queue
- Heap Sort
- Top K Elements Problem
- Median in a Stream

## Tries
- Trie Data Structure & Applications
- Word Search Problems
- Auto-complete Feature

## Hashing
- Hash Maps & Sets
- Group Anagrams
- Two Sum / 3Sum / 4Sum
- Longest Consecutive Sequence

## Graphs
- Graph Basics & Representations
- Graph Traversals (BFS, DFS)
- Detect Cycles (Directed & Undirected)
- Topological Sort
- Graph Coloring Problem

## Graph Algorithms
- Shortest Path (Dijkstra, Bellman-Ford, Floyd-Warshall)
- Minimum Spanning Tree (Prim’s, Kruskal’s)
- Union-Find (Disjoint Set Union)

## Dynamic Programming (DP)
- Dynamic Programming Basics
- DP - 0/1 Knapsack Problem
- DP - Longest Common Subsequence
- DP - Longest Increasing Subsequence
- DP - Matrix Chain Multiplication
- DP - Subset Sum / Partition
- DP - Edit Distance
- DP - Coin Change
- DP - House Robber / Paint House

## Greedy Algorithms
- Activity Selection
- Fractional Knapsack
- Job Sequencing Problem
- Huffman Coding

## Bit Manipulation
- XOR Tricks
- Check if Power of 2
- Count Set Bits
- Single Number Problems

## Math & Logic
- Sieve of Eratosthenes
- GCD / LCM
- Modular Arithmetic
- Combinatorics (nCr, Pascal’s Triangle)

## System Design Intro (for advanced prep)
- Basic concepts (scalability, load balancers, caching)
- When to move from DSA to Low-Level Design (LLD) & High-Level Design (HLD)

## Final Steps
- Building a Simple DSA-Based App
- Problem-Solving with DSA
- Mock Interviews & Contest Practice
- Final Project Review
- Revision & Practice
- Project/Revision

7989342423


# Learning2025
Learning All In One in 2025

### Change the Color to Terminal Folder:

- vim ~/.bashrc
- PS1="\[\e[32m\]\W\[\e[0m\] \[\e[33m\]\$\[\e[0m\] "
- source ~/.bashrc

#### Activate Venv in Windows Environment
- source ../../Learning2025/venv/S
cripts/Activate

## Top 1 Percent Skills to learn as a DevOps Engineer. Please follow the timestamps below.
- 00:00 - Introduction
- 00:30 - Impact of AI on DevOps
- 01:30 - MLOps
- 02:28 - AIOps
- 03:29 - FinOps
- 04:45 - AI Assisted DevOps
- 05:20 - Secure Software Supply Chain
- 06:07 - eBPF
- 07:30 - WASM
- 08:38 - Kubernetes Management
