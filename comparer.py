print("""enter a number for the following.
we are going to compare them.
 """)

X = float(input("X:"))
Y = float (input("Y:"))

if X > Y:
    print(f"{X} > {Y}")
elif X == Y:
    print(f"{X} = {Y}")
else:
    print(f"{X} < {Y}")


