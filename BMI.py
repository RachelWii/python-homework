import sys
a=input('your weight(kg):')
b=input('your height(m):')
A=float(a)
B=float(b)
BMI=A/((B)*(B))
print('your BMI is'+str(BMI))
if BMI>20:
    if BMI<30:
        if BMI>=25:
           print("you\'re FAT")
        else:print('you\'re in good shape')
    else:print('you\'re TOO FAT')
else:print('you\'re TOO THIN')
user_input=input('print \'yes\' to exit the program:')
if user_input.lower()=="yes":
    exit()