len=int(input("enter len:"))
for i in range(len):
    name=input("enter string:")
    height=float(input("enter height:"))
    weight=float(input("enter weight:"))
    bmi=round((weight/((height)**2)),2)
    print(f"{name}'s bmi is {bmi}")
    if height>0 and weight>0:
        if bmi<=18.5:
            print(f"{name} is under weight ")
        elif bmi>=18.5 and bmi<=24.9:
            print(f"{name} is normal weight")
        elif bmi>=25 and bmi<=29.9:
            print(f"{name} is over weight")
        else:
            print(f"{name} is obesity")
    else:
        print("enter height and weight in positive  values")



            

