
import time

def highestProfit(numSupplierrs,  inventory, order):
	start = time.time()
	profit = 0
	inventory.sort(reverse=True)

	m = inventory[0]

	while order != 0:
		for x in inventory:
			if x == m:
				profit += m
				order -= 1
				inventory[0] -= 1

				if order == 0:
					break
			else:
				m -= 1
				break
				
	print(time.time() - start)
	return profit



inventory = [3,5]
orders = 6

print(highestProfit(2, inventory, orders))