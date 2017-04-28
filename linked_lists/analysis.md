Linked lists
============

This is the data structure that takes advantage of references. Linked lists are made up of nodes. Each
node contains a reference to the next node in the list. What is more, each node contains a data.

A linked list is:

* the empty lists, represented by None
* a node that contains data object and a reference to a linked list

# Pseudocode

```
structure node:
  next_node = none
  data = none

structure linked_list:
  length = 0
  head = none
```

# Complexity

If you want to index linked list you have to go through every element. Based on that indexing complexity is Θ(n). The same is for accessing - Θ(n). Insertion only needs
to look at list once so Θ(1) for insertion. Deleting is similar Θ(1).

# References

* [Linked lists](http://greenteapress.com/thinkpython/html/chap17.html)
