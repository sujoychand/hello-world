# Code with Harry : Problem Solve 3

print("Enter Age of the person")
age = int(input())

if 18 < age <= 100:
    print("Person can drive the car")
elif age == 18:
    print("Not able to decide weather person can drive or not")
elif 7 <= age < 18:
    print("Too Young to think about driving")
else:
    print("Person cannot drive the car")