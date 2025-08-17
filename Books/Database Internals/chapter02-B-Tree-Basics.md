# B-Tree Basics

Most of the mutable storage structures use an in-place update mechanism. During insert, delete, or update operations, data records are updated directly in their locations in the target file. 

B-Trees are not a recent invention: they were introduced by Rudolph Bayer and Edward M. McCreight back in 1971 and gained popularity over the years. By 1979, there were already quite a few variants of B-Trees. Douglas Comer collected and systematized some of them. 

## Binary Search Trees

A binary search tree (BST) is a sorted in-memory data structure, used for efficient key-value lookups. BSTs consist of multiple nodes. Each tree node is represented by a key, a value associated with this key, and two child pointers (hence the name binary).
BSTs start from a single node, called a root node. 

A naive on-disk BST implementation would require as many disk seeks as comparisons, since there’s no built-in concept of locality. This sets us on a course to look for a data structure that would exhibit this property.

## Trees for Disk-Based Storage

As previously mentioned, unbalanced trees have a worst-case complexity of O(N). Balanced trees give us an average O(log2 N). At the same time, due to low fanout (fanout is the maximum allowed number of children per node), we have to perform.balancing, relocate nodes, and update pointers rather frequently. Increased maintenance costs make BSTs impractical as on-disk data structures

### Disk-Based Structures

Data structures used in databases have to be adapted to account for persistent medium limitations. On-disk data structures are often used when the amounts of data are so large that keeping an entire dataset in memory is impossible or not feasible. Only a fraction of
the data can be cached in memory at any time, and the rest has to be stored on disk in a manner that allows efficiently accessing it.

### Hard Disk Drives

Head positioning is the most expensive part of an operation on the HDD. This is one of the reasons we often hear about the positive effects of sequential I/O: reading and writing contiguous memory segments from disk.


### Solid State Drives

Solid state drives (SSDs) do not have moving parts: there’s no disk that spins, or head that has to be positioned for the read. A typical SSD is built of memory cells, connected into strings (typically 32 to 64 cells per string), strings are combined into arrays, arrays are combined into pages, and pages are combined into blocks.

The smallest unit that can be written (programmed) or read is a page. However, we can only make changes to the empty memory cells (i.e., to ones that have been erased before the write). The smallest erase entity is not a page, but a block that holds multiple pages, which is why it is often called an erase block. Pages in an empty block have to be written sequentially.

Since in both device types (HDDs and SSDs) we are addressing chunks of memory rather than individual bytes (i.e., accessing data block-wise), most operating systems have a block device abstraction [CESATI05]. It hides an internal disk structure and buffers I/O operations internally, so when we’re reading a single word from a block device, the whole block containing it is read. This is a constraint we cannot ignore and should always take into account when working with disk-resident data structures.

### On-Disk Structures

In “Binary Search Trees”, we came to the conclusion that high fanout and low height are desired properties for an optimal on-disk data structure. We’ve also just discussed additional space overhead coming from pointers, and maintenance overhead from remapping these pointers as a result of balancing. B-Trees combine these ideas: increase node fanout, and reduce tree height, the number of node pointers, and the frequency of balancing operations.

## Ubiquitous B-Trees

B-Trees build upon the foundation of balanced search trees and are different in that they have higher fanout (have
more child nodes) and smaller height. B-Trees are sorted: keys inside the B-Tree nodes are stored in order. Because of that, to locate a searched key, we can use an algorithm like binary search.

### B-Tree Hierarchy

B-Trees consist of multiple nodes. Each node holds up to N keys and N + 1 pointers to the child nodes. These nodes are logically grouped into three groups:
- Root node
- Leaf nodes
- Internal nodes

B-Trees allow storing values on any level: in root, internal, and leaf nodes. B+-Trees store values only in leaf nodes. Internal nodes store only separator keys used to guide the search algorithm to the associated value stored on the leaf level.

### Separator Keys

Keys stored in B-Tree nodes are called index entries, separator keys, or divider cells. They split the tree into subtrees (also called branches or subranges), holding corresponding key ranges. Keys are stored in sorted order to allow binary search. A sub‐tree is found by locating a key and following a corresponding pointer from the higher to the lower level.

The first pointer in the node points to the subtree holding items less than the first key, and the last pointer in the node points to the subtree holding items greater than or equal to the last key. Other pointers are reference subtrees between the two keys: Ki-1≤ Ks < Ki, where K is a set of keys, and Ks is a key that belongs to the subtree.

Some B-Tree variants also have sibling node pointers, most often on the leaf level, to simplify range scans. These pointers help avoid going back to the parent to find the next sibling. Some implementations have pointers in both directions, forming a double-linked list on the leaf level, which makes the reverse iteration possible.

### B-Tree Lookup Complexity

B-Tree lookup complexity can be viewed from two standpoints: the number of block transfers and the number of comparisons done during the lookup.

In terms of number of transfers, the logarithm base is N (number of keys per node). There are K times more nodes on each new level, and following a child pointer reduces the search space by the factor of N. During lookup, at most logK M (where M is a total number of items in the B-Tree) pages are addressed to find a searched key. The number of child pointers that have to be followed on the root-to-leaf pass is also equal to the number of levels, in other words, the height h of the tree. From the perspective of number of comparisons, the logarithm base is 2, since searching a key inside each node is done using binary search. Every comparison
halves the search space, so complexity is log2 M.

### B-Tree Lookup Algorithm

The algorithm starts from the root and performs a binary search, comparing the searched key with the keys stored in the root node until it finds the first separator key that is greater than the searched value. This locates a searched subtree. As we’ve
discussed previously, index keys split the tree into subtrees with boundaries between two neighboring keys. 
During the point query, the search is done after finding or failing to find the searched key. During the range scan, iteration starts from the closest found key-value pair and continues by following sibling pointers until the end of the range is reached or the
range predicate is exhausted.

### B-Tree Node Splits

To insert the value into a B-Tree, we first have to locate the target leaf and find the insertion point.

After the leaf is located, the key and value are appended to it. Updates in B-Trees work by locating a target leaf node using a lookup algorithm and associating a new value with an existing key.

Splits are done by allocating the new node, transferring half the elements from the splitting node to it, and adding its first key and pointer to the parent node. When the split is done, we have two nodes and have to pick the correct one to finish insertion. For that, we can use the separator key invariants. If the inserted key is less than the promoted one, we finish the operation by inserting to the split node. Otherwise, we insert to the newly created one.

To summarize, node splits are done in four steps:
1. Allocate a new node.
2. Copy half the elements from the splitting node to the new one.
3. Place the new element into the corresponding node.
4. At the parent of the split node, add a separator key and a pointer to the new
node.

### B-Tree Node Merges

If neighboring nodes have too few values (i.e., their occupancy falls under a threshold), the sibling nodes are merged. This situation is called underflow. 

More precisely, two nodes are mergedif the following conditions hold:
- **For leaf nodes**: if a node can hold up to N key-value pairs, and a combined num‐
ber of key-value pairs in two neighboring nodes is less than or equal to N.
- **For nonleaf nodes**: if a node can hold up to N + 1 pointers, and a combined
number of pointers in two neighboring nodes is less than or equal to N + 1.

To do this, we move elements from one of the siblings to the other one. Generally, elements from the right
sibling are moved to the left one, but it can be done the other way around as long as the key order is preserved

To summarize, node merges are done in three steps, assuming the element is already
removed:
1. Copy all elements from the right node to the left one.
2. Remove the right node pointer from the parent (or demote it in the case of a non‐leaf merge).
3. Remove the right node.