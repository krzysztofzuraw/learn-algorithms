# Tree (data structure)

From [wiki](https://en.wikipedia.org/wiki/Tree_(data_structure)):

> A tree is a data structure made up of nodes or vertices and edges without having any cycle. The tree with no nodes is called the null or empty tree. A tree that is not empty consists of a root node and potentially many levels of additional nodes that form a hierarchy.

## Complexity

In my example I implemented my algorithm for finding a path in naive way. I first get all possible
paths and then select only this one which contains my start or end values. I means that I have to do
at least n/2 operations. Based on that the best case time complexity is Ω(n), average: Θ(n), worst
O(n).

### References

* [Wikipedia](https://en.wikipedia.org/wiki/Tree_(data_structure))
