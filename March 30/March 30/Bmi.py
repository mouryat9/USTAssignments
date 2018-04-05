student = int(input("Please enter the no of students"))
tuple1= ()

for i in range(0,student):
    height= int (input("Enter height"))
    weight = int (input("Enter Weight"))
    bmi=weight / height**2
    tuple1 += (bmi,)

print(tuple1)