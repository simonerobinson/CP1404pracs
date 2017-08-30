"""
Program to calculate and display uer's bonus based on sales.
If sales are under $1,000, the user gets 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter Sales: $"))
while sales > 0:
    if sales < 1000:
            bonus = sales * .10
            print("$", bonus)
    if sales >= 1000:
        bonus = sales * .15
        print("$", bonus)
    sales = float(input("Enter Sales: $"))
print("No sales bonus")