apple_price = 20
orange_price = 25

apple_to_buy = int(input("How many apples will you buy?: "))
orange_to_buy = int(input("How many oranges will you buy?: "))

total_apple_price = apple_to_buy * apple_price
total_orange_price = orange_to_buy * orange_price
total_amount = total_apple_price + total_orange_price

print(f"\nThe total amount is {total_amount}.")