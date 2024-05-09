WEIGHT=input("your weight(kg):")
HEIGHT=input("your height(m):")
BMI=float(WEIGHT)/(float(HEIGHT)*float(HEIGHT))
print(str(BMI))
if BMI>30:
    print("you\'re TOO FAT")
elif BMI>25:
    print("you\'re FAT")
elif BMI>=20:
    print("you\'re in GOOD shape")
else:
    print("you\'re TOO THIN")
command=input("input 'yes' to exit the program: ")
if command.lower()=="yes":
    exit()