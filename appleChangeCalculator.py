money = int(input("How much money do you have?: "))
applePrice = int(input("What's the current price of an apple?: "))
appleCanBuy = money//applePrice
appleChange = money%applePrice

print(f"You can buy {appleCanBuy} apples and your change is {appleChange} pesos.")