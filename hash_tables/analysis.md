Hash table
==========

It's data structure which maps keys to value. For given key algorithm calculates
hash function. This value is then used as a index where value associated with key
is kept.

# Pseudocode

```
table = {}
hash_table(key, value):
  hash = key % (prime_number)
  table[hash] = value

read_hash_table(key):
  hash = key % (prime_number)
  return table[hash]
```

# Complexity

Hash table it's data structure so space complexity (worst) is O(n). 

Search, insertion and deletion doesn't depends on number
of elements in hash table so all of them in average has Θ(1)
complexity. 

On the worst case (search, insertion & deletion) 
complexity is O(n).
