"""def my_function(child3,child2,child1):#Arbitrary arguments
    print("Ailenin usagi:" + child3)


my_function(child1 = "Cavid" , child2 = "Aytac", child3 = "Jasmin")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")"""
"""def my_function(**kid):
    print("Sonuncu ad:" + kid["ana"])
my_function(usaq="Jasmin",ana="Aytac")
#def my_function(**kid):
 # print("His last name is " + kid["lname"])

#my_function(fname = "Tobias", lname = "Refsnes")"""
"""def my_function(**country):
  print("I am from " + country["olke1"])

my_function(olke1="Sweden",olke2="india")"""

"""def my_function(country="Azerbaycan"):
  print("I am from " + country)

my_function("Norway")
my_function()"""
"""def my_function(country = ""):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")"""
"""def my_function(x):
    return ("neyse")*5
print(my_function("454545"))"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
