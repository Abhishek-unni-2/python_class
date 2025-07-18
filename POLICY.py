print("------COMPANY INSURES POLICY-------")
name=input("enter your name: ")
status=input("Are you marrried or unmarried: ").lower()
age=int(input("enter you age: "))
gender=input("gender: Male or Female: ").lower()
print("----------------------------------")
if status=="married":
  print("company can provide a insures")
elif status=="unmarried" and gender=="male"and age>30:
  print("company can provide a insures")
elif status=="unmarried" and gender=="female"and age>25:
  print("company can provide a insures")
else:
  print("You are not eligible for insures or enter the correct details")