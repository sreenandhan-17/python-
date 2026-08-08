name=input("enter the name:")
name=str(name)
age=input("enter the age:")
age=int(age)
if age<=18:
    print("child")
elif age<=20:
    print("teenager")
elif age<=25:
    print("young adult")
elif age<=30:
    print("adult")
else:
    print("old")
