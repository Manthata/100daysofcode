


year = int(input("Enter the year you want to check "))

if year%4 == 0:
    print("first if ")
    if year%100 == 0 :
        if year%400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not leap year")