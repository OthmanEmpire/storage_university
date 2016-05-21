print("Input the coefficients of your quadratic equation")


print("a: ", end = " ")
a = int( input() )
print("b: ", end = " ")
b = int( input() )
print("c: ", end = " ")
c = int( input() )

print("Now obtaining solutions. Please wait.")

x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print("The solutions are: ", x1, "& ", x2)
