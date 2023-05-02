# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp = [2200, 2350, 2600, 2130, 2190]

result_1 = exp[1] - exp[0]
print(f"{result_1} dollars")

result_2 = exp[0] + exp[1] + exp[2]
print(f"{result_2} dollars")

result_3 = 2000 in exp
print(f"you spent exactly 2000 dollars in any month?\n{result_3}")

result_4 = exp.append(1980)
print(exp)
# Ans --> [2200, 2350, 2600, 2130, 2190, 1980]

result_5 = exp[3] - 200
print(f"{result_5} dollars")

exp[3] = result_5
print(exp)