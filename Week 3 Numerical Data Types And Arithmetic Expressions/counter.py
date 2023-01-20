print("Please enter the number of coins:")
num_quarters = int(input("# of quarters: "))
num_dimes = int(input("# of dimes: "))
num_nickels = int(input("# of nickels: "))
num_pennies = int(input("# of pennies: "))
total = num_pennies + num_nickels * 5 + num_dimes * 10 + num_quarters * 25
num_dollars = total // 100
num_cents = total % 100
print("The total is {} dollars and {} cents".format(num_dollars, num_cents))
