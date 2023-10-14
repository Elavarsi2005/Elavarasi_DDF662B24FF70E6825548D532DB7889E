"""
Write a function called linear_search_product that takes the list of products and a target product
name as input. The function should perform a linear search to find the target product in the list and 
return a list of indices of all occurences of the product is not 
found.
"""


def linearsearchproduct(productlist, targetproduct):
  indices = []

  for index, product in enumerate(productLiist):
    if product == targetproduct:
      indices.append(index)

  return indices


# Example usage:
products = ["shoes", "boot", "loafer", "shoes","sandal", "shoes"]
target = "shoes"
result = linearsearchproduct(products, target)
print(result)
