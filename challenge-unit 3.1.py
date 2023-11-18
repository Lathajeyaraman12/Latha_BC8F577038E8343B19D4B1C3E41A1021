def linear_search_product(products, target_product):
  indices = []

  for index, product in enumerate(products):
      if product == target_product:
          indices.append(index)

  return indices

# Example usage:
product_list = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target_product_name = "Apple"

result = linear_search_product(product_list, target_product_name)

if result:
  print(f"The product '{target_product_name}' is found at indices: {result}")
else:
  print(f"The product '{target_product_name}' is not found.")
