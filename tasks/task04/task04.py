tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [4, 5]
       },
       "node12": [6],
       "node13": [13]
   },
   "node2": [7, 8, 9]
}

def collect_leaves(tree):
  result = []
  if isinstance(tree, list):
    for x in tree:
      result.append(x)
  if isinstance(tree, dict):
    for value in tree.values():
      array = (collect_leaves(value))
      for item in array:
        result.append(item)
  return result

result = collect_leaves(tree)
print(result)  
test_array = [0, 7, 13]

assert collect_leaves(tree) == [1, 2, 3, 4, 5, 6, 13, 7, 8, 9]
assert collect_leaves(test_array) == test_array