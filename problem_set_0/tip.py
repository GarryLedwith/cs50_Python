def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# dollars_to_float 
# accespts a string as an argument 
# formatted as $##.## 
# each # is a decimal digit 
# remove leading dollar sign
# return the amount as a float 
def dollars_to_float(d):
    if d.startswith("$"): # if the string starts with a dollar sign 
        d = d[1:] # remove the dollar sign
    return float(d)

   
# test dollars_to_float
# print(dollars_to_float("$10.50"))  # Expected output: 10.50
# print(dollars_to_float("$0.99"))   # Expected output: 0.99
# print(dollars_to_float("$100"))    # Expected output: 100.00
# print(dollars_to_float("$0"))      # Expected output: 0.00
    
    
# # percent_to_float
# accepts a string as an argument
# formatted as ##%
# each # is a decimal digit
# remove trailing percent sign
# return the amount as a float
def percent_to_float(p):
    if p.endswith("%"): # if the string ends with a percent sign
        p = p[:-1] # remove the percent sign
    return float(p) / 100  # convert to float and divide by 100


# test percent_to_float
# print(percent_to_float("15%"))  # Expected output: 0.15
# print(percent_to_float("20%"))  # Expected output: 0.20
# print(percent_to_float("100%")) # Expected output: 1.00
# print(percent_to_float("0%"))   # Expected output: 0.00

main()