a=int(input("enter the mark of subject 1(0-100) :-"))
b=int(input("entr the mark of subject 2(0-100):-"))
c=int(input("enter the mark of subject 3(0-100):-"))
d=int(input("enter the mark of subject 4(0-100):-"))
e=int(input("enter the mark of subject 5(0-100):-"))
i=a+b+c+d+e
print("total of subject ::",i)
everage=i/5
print("everage ::",everage)
if(everage>90):
    print("A+ grade")
elif(everage<=90 and everage>70):
    print("A grade")
elif(everage<=70 and everage>50):
    print("B grade")
elif(everage<=50 and everage>33):
    print("C grade")
else:
    print("Fail..!")