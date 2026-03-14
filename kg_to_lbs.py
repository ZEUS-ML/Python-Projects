weight=(input("enter the unit of input weight (kg/lbs):"))
inp = float(input("enter the weight: "))
if weight =="kg":
    print("the weigth in pounds is: ", 2.20462*inp,"lbs")
elif weight == "lbs":
    print("the weight in  kilograms is : ",inp/2.20462,"kg")
else:
    print("invalid unit")