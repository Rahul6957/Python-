"""try:
    premium = int(input("Enter Premium amount:"))
    print("Premium:",premium)

except:
    print("Invalid Premium amount ") """
#************************************************************************************
try:
    age = float(input("Enter your age: "))
    vage = 18 - age

    if age <= 0:
        raise ValueError("Age must be greater than zero.")

    elif age >= 18:
        print("Allow to vote")

    else:
        print("Not allowed to vote")
        raise ValueError(f"Wait for {vage} years")     #give manu

except ValueError as e:
    print("Error:", e)
    

#***************************************************************

