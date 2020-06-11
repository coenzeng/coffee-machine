water = 400
milk = 540
beans = 120
cups = 9
money = 550

def stock():
    print(f'''
The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
${money} of money
''')

exit = True
while (exit):

    action = input("Write action (buy, fill, take, remaining, exit):\n")

    if action == "buy":
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        
        if coffee == "back":
            continue
        elif coffee == "1":
            water -= 250
            beans -= 16
            money += 4
        elif coffee == "2":

            water -= 350
            if (water < 0):
                water += 350
                cups += 1
                print("Sorry, not enough water!\n")
            else:
                milk -= 75
                beans -= 20
                money += 7
                print("I have enough resources, making you a coffee!\n")
        elif coffee == "3":
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
        cups -= 1
    elif action == "fill":
        water += int(input("Write how many ml of water do you want to add:"))
        milk += int(input("Write how many ml of milk do you want to add:"))
        beans += int(input("Write how many g of coffee beans do you want to add:"))
        cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    elif action == "take":
        print("I gave you $" + str(money))
        money = 0
    elif action == "remaining":
        stock()
        continue
    elif action == "exit":
        break

