print("Welcome to the tip calculator.")
total = input("What was the total bill? ")
while not total.isdigit():
    total = input("Please insert the bill amount: ")
percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
while not percent.isdigit():
    percent = input("Please insert the percent amount: ")
people = input("How many people to split the bill? ")
while not people.isdigit():
    people = input("Please insert the person amount: ")
total_res = float(total) / 100 * int(percent)
with_tip = float(total_res) + float(total)
split = with_tip / 7
final_amount = round(split, 2)
# final amound with rounding up to 2 decimal zeros (e.g 24.00 instead of 24)
final_amount = "{:.2f}".format(split)
message = f"Each person should pay: ${final_amount}"
print(message)