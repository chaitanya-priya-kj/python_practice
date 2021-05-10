print(2+5)

t = ("Norway",4.5673, 3) #tuple

for item in t:
    print(item)

t = t + (3783,32)

print(t)
print(t*3)

def minmax(items):
    print( min(items),max(items))

minmax([33,23,23,2])

a = "jelly"
b = "bean"

print(a,b,end = " ")

a,b = b,a 

print(a,b,end = " ")

if("Norway" in t):
    print("True")