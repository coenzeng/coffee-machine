import math
water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how much milk the coffee machine has:\n"))
beans = int(input("Write how many beans the coffee machine has:\n"))
coffee = int(input("Write how many cups of coffee you will need:\n"))
enough_water = (water - coffee * 200)
enough_milk = (milk - coffee * 50) 
enough_beans = (beans - coffee * 15)

new_water = water/200
new_milk = milk/50
new_beans = beans/15
m1 = min(new_water, new_milk, new_beans)

if (enough_water < 0 or enough_milk < 0 or enough_beans < 0):

    print("No, I can make only " + str(math.floor(m1)) + " cups of coffee")
else:
    print("Yes, I can make that amount of coffee (and even " + str(math.floor(m1 - 1)) + " more than that)")