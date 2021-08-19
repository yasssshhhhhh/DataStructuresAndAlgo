maxProduct = 1
currentProduct = 1
nums = [6, -3, -10, 0, 2]
for value in nums:
    currentProduct = currentProduct*value
    if currentProduct > 0:
        currentProduct*=1
        maxProduct = max(maxProduct,currentProduct)
    else:
        currentProduct*=-1
        maxProduct = max(maxProduct,currentProduct)
print(maxProduct)


