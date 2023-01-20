p1 = float(input("Enter price of the first item: "))
p2 = float(input("Enter price of the second item: "))
club_card_flag = input("Does customer have a club card? (Y/N): ")
club_card_flag = club_card_flag == "y" or club_card_flag == "Y"
tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))
base_price = p1+p2
after_discount = p1+p2/2 if p1 > p2 else p1/2+p2
if club_card_flag:
    after_discount *= 0.9
total_price = after_discount + after_discount*tax_rate/100
print("Base price = {:.2f}".format(round(base_price, 2)))
print("Price after discounts = {:.2f}".format(round(after_discount, 2)))
print("Total price = {:.2f}".format(round(total_price, 2)))
