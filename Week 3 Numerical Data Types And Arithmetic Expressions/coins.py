num_dollars = int(input("# of dollars: "))
num_cents = int(input("# of cents: "))
total_cents = num_dollars*100+num_cents
num_quarter = total_cents//25
total_cents = total_cents%25
num_dime = total_cents//10
total_cents = total_cents%10
num_nickel = total_cents//5
total_cents = total_cents%5
num_penny = total_cents
print("The coins are {} quarters, {} dimes, {} nickels and {} pennies".format(num_quarter, num_dime, num_nickel, num_penny))
