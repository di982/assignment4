#assignment4
#grading system(A,B,C,D)
#no negative values
#no values greater than 100
#0-30:D
#31-50:C
#51-70:B
#71-100:A

#Use average for the grading
#maths, physics, geo, chem
#the program to display "unrecognized marks/ avg" if a negative value or
#a value greater than 100 is keyed in

print('Enter marks obtained in the following subjects:')
maths = int(input("Enter your maths marks"))
physics = int(input("Enter your physics marks"))
geography = int(input("Enter your geography marks"))
chemistry = int(input("Enter your chemistry marks"))
total = maths + physics + geography + chemistry
avg = total / 4

if avg >= 71 and avg <= 100:
    print('Your Grade is A')
elif avg >= 51 and avg <=70:
    print("Your Grade is B")
elif avg >= 31 and avg <= 50:
    print("Your Grade is C")
elif avg >= 0 and avg <= 30:
    print("Your Grade is D")