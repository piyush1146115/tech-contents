# Hash Table Internals

- [Internal structure of a Hash Table](https://youtu.be/jjW8w8ED3Ns?si=3xBjvXp9Me61i2Qp)
- [Conflict Resolution in Hash Tables with Chaining
](https://youtu.be/9rb8oILi4lU?si=KMWrI2U0nq-ldlav)
- [Conflict Resolution in Hash Tables with Open Addressing
](https://youtu.be/6_yFb7icd_c?si=dtf-txCoJneYdHhj)
    - With open addressing, we use a probing function to find the slot where the key should be placed
    - There are different probing function out there to solve this problem
    - A probing function is defined as p(k,i)=j; where k=key,i=attempt,j=index
- [Linear Probing for Conflict Resolution in Hash Tables
](https://youtu.be/5QKAXG25hig?si=SG1asWynisME93C4)
  - Probing function is defined as p(k,i) = (h(k) +i)%m, where i=attempt number and m=total slot
  - In average case, linear probing works in constant time
  - A good hash function is required in Linear probing, MurmurHash is preferred
  - If a hash function generates localized hashes, it will make linear probing inefficient
  - When we access a memory location, the page and it's neighbouring elements are cached in CPU. It makes Linear probing very efficient. It is called locality of reference
  - Challenges: Linear probing may suffer cascading collisions
- [Quadratic Probing for Conflict Resolution in Hash Tables](https://youtu.be/F-8pWiJv8ik?si=YsxhQti0l7G3JkWZ)
    - Instead of placing the collided key in the neighbouring slot, quadrating pribing adds successive value of an arbitrary quadrating polynomial. p(k,i) = h(k)+c1i+c2i^2. Sample sequence: h(k), h(k)+1, h(k)+2^2, h(k)+3^2
    - It reduces clustered collisions by distributing it quadratically
    - It has a good locality of reference but not as great as linear probing. Unless there are large collisions on same key, at least a couple of subsequent slots will be in cpu cache
- [Double Hashing for Conflict Resolution in Hash Tables
](https://youtu.be/wV4K6fo0T58?si=3dX-5YJbGlIqFmbC)
    - Double hashing is a probing technique used with open addressing, we use a probing function to find the slot where the key should be placed
    - Double hashing techniques use 2 hash functions to find the next slot
        - First hash function gives primary slot and upon collision, it uses second hash function as offset times attempt until an empty slot is reached
        - p(k,i) = (h1(k) + i*h2(k))%m
    - Given that we are using another hash function to offset, we are minimizing repeated collisions and effects of clustering
    - Follows no specific pattern and gives near-uniform yet random offset from the index
    - Choosing the second has function:
        - It should never return 0
        - It should cycle through entire table
        - Fast to compute and ~ to a random number generator
    - Advantages of Double Hashing:
        - Uniform spread upon collision
        - Follows no specific offset pattern
            - purely depends on the key
        - Least prone to clustering problem
- [Understanding the performance of a Hash Table](https://youtu.be/oD2yaTtu69w?si=_JlCK6UjR5uT7Wha)
    - Hash table gives constant time performace when there are zero collisions
    - load factor = n/m, where n=number of elements, m=slots in the hash table
    - Collisions on one slot will interfere with probe beginning on other
    - Depending on the probing strategy, the cost of each probe changes and it matters
        - Probing is costly in chained hashing
        - Double hashing requires us to evaluate 2 hash functions
    - Lookup time as a function of load
        - For your strategy identify how lookup time changes as a function of load factor against all strategies
    - To leverage cache in chained hashing, we can allocate pool for each slot so that the nodes of list are close to each other in memory
    - Chained hashing outperforms open addressing when tables are smaller
    - Open addressing outperforms chained hashing when tables are large enough
- [When full, why are Hash tables, ArrayList, and Vectors always doubled?](https://youtu.be/zt1E0akArqQ?si=R1elhm827gF_RITO)
    - Resizing is important to maintain performance
    - Resizing is costly operation
    - A typical strategy to resize is to always double the array. We re-allocate a new array of 2X size and rehash keys
    - If we always increase by 1, then the insertion complexity would be O(n^2)
    - When we grow by 2x, the complexity of expansion is O(n)
    - Mod m = AND(m-1), m=2^k(where m is a power of 2)
    - AND operation is significantly faster than division and hence performance gain
    - 2^k-1 has lower bits 1 and higher 0
    - Shrinking a hash table:
        - If keys are deleted from the hash table, then it does not make sense to keep them blocked 
        - We need to shrink when the number of elements are such that few insertions after shrink would not cause a resize
        - Hence we shrink when there are n/8 elements
    




