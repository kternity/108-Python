num1 = 2
num2 = 3

def sum(num1, num2):
   return num1+num2

result = sum(21,21)
print("the result of sum(num1, num2) is " +str(result))

# Create a list
def list():
   color = ["red", "green", "blue", "yellow"]
   print(color)
   color.append("white")
   print(len(color))
   color.remove("white")
   print("list")

#List 2
def list2():
   print("list 2")
   num=[12,34,21,35,37,87,24,-45,-1,1,2,3,5,-8,-7,88,32,65,-84]

   for n in num:
      if n < 0:
         print(n)

me = {
   "name":"Kenneth",
   "last":"Chung",
   "age":"42",
   "city":"Glendale",
}
print(me)
me["preferred color"]="blue"
print(me["name"])]

name = me["name"]
print(name)