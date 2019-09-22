# Notes for [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/static/pythonds/index.html#)  

## __Trees and Tree Algorithms__  

. What is a _Tree_ data structure?  
. How a _Tree_ can be used to build a _Map_!.  
. Build a _Tree_ using a List.  
. Build a _Tree_ using classes and references.  
. Recursion to build a _Tree_.  
. __Final trick!__: Build a _Priority Queue_ using a _Heap_ (Yo, where's the _Tree_ at?).  

### __Tree Definition__  

    Oddly, trees in the virtual world start at the root (duh!) but the branches propagate downwards till they eventually end in leaves. Yes, all the nodes in the last layer are leaves!

#### _Applications_

- OS File System Hierarchy  
- Sentence Parsing for language comprehension
- Webpage Parsing  

### __Parts of Tree__

While the _virtual Tree_ is similar to it's biological cousin, w.r.t its look and structure, the constituent elements have distinct names and roles.

- __Node__  
  - A node is an element in the tree. Typically it contains a unique name (also called _key_). This is enough to do the central job of a tree, which is hierachical organization of data.
  - Note that, it is possible to store extra information in each node (we call this _payload_). This payload information is critical for evaluating space complexity.  

- __Edge__
  - An edge is the connecting element of a tree. It connects nodes and establishes a relationship between them.
  - Each node has a unique incoming edge (called a _Parent_ node). At the same time, each node can give out multiple edges (called _Children_).

- __Root__
  - Root is a distinguished node in a tree. It is the first node from where the tree grows (downwards, into the _virtual_ ground!).
  - Since its the first node, it has one exception to the typical Node rules. It doesn't not have an incoming node or Parent node (_Adam_ or _Eve_ or _Satan_ of the tree, depending on which way you lean).  

- __Path__
  - A path is an ordered set/list of nodes that are connected by edges. Note that, there is always a unique path from the root to any other node in the tree.  

- __Children__
  - A set of nodes having the same incoming edge (Parent) are called Children of that node.

- __Parent__
  - A node is the Parent of all such nodes connected to it through its outgoing edges.

- __Sibling__
  - Children of the same parents are siblings (it's elementary).

- __Subtree__
  - Pick any _Parent_ node and pluck it out of Tree, along with all its children. Notice that with the Parent node as a root, you get a new tree structure! This is called a Subtree.

- __Leaf__
  - Leaf nodes are terminal nodes in a Tree structure. That is, they dont have any outgoing edges (and Children).

- __Level__
  - Level determines how far a node is from the Root node. This can be determined by counting the number of edges one needs traverse on to get to the said node from the Root.
  - Naturally, the _Level_ of the Root node is _0_.

- __Height__
  - It is the maximum level for any node in the Tree. Put differently, its the distance from the root to its farthest leaf.

### __Binary Tree__

    A Tree where every Parent node has a maximum of two children is a Binary Tree.

### __Tree as a List of Lists (`TaaLL Tree`)__

Here's a simple _Binary Tree_ Structure implemented using List of Lists in Python.

```python
TaaLLTree = ['a',
                ['a1',
                    ['a11',
                        ['a111'], []
                    ],
                    ['a12',
                        ['a121'], []
                    ]
                ],
                ['a2',
                    ['a21'], []
                ]
            ]

```

In here, `a` is the _root_ node, `a111`,`a121` and `a21` are _leaf_ nodes. The _level_ of `a111` is __3__, while the _level_ to `a21` is __2__. The _height_ of the Tree is __3__, the maximum level. Finally, `a1` and `a2` are _siblings_ as they are _children_ of the same _parent_ `a`. Pick the sub-list, say `a1` (call using `TaaLLTree[1]`) and notice its a tree within a tree, aka _subtree_.