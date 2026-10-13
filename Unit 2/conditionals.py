# Conditional if/else logic- these are keywords that instruct your
# program to do specific instructions based on specific data
# or conditions

# condititional syntax (how it is written)
bill_amount = int(input("Please type in a bill tender (1s ,5s, or 10s):"))

# if usually indicates that something is a possible option
if bill_amount == 1:
    print("here are 4 quarters")

# elif allows uo to indicate that there are more possible options
# you can have as many elif as you want
elif bill_amount == 5:
    print("here are 20 quartes")
elif bill_amount == 10:
    print("here are 40 quarters")


# else is ALWAYS your last option.
else:
    print("Sorry that type of bill is not accepted. ")

