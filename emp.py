EMPNAME=[]

EMPNAME.append("samir")
EMPNAME.append("manish")
EMPNAME.append("sagar")

print("list of employee name:")
for name in EMPNAME:
    print(name)

EMPNAME.remove("sagar")

print("list after remove employee:")
for name in EMPNAME:
    print(name)
    
EMPNAME.append("manoj")
print("list after append the employe:")
for name in EMPNAME:
    print(name)