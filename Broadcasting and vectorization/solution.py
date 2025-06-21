import numpy as np

prices = np.array([100,200,300])

discount = 10
final_prices = prices - (prices * discount / 100)
print(final_prices)
# Output: [ 90. 180. 270.]
# The code uses NumPy to apply a discount to an array of prices in a vectorized manner.
# This eliminates the need for a loop, making the code more efficient and concise.
# The final_prices array contains the discounted prices.