# This is your first program of python.
# To write the code you need Python installed in your system and a source code editor or IDE.
# In my Case I am using VS Code.
# If you are also using this you need to install Python Extension by Microsoft to run the Python Code.
# If There's any issue you can search for the solution on google

# This is Your First Program.
# In This we will learn about some basic datatypes of Python.

# In Python to assign a variable there are some rules they are:
#   1. It Should Start with alphabet only.
#   2. It can be alphanumeric.
#   3. It can only have '_' ( Underscore ) as a special charecter.

# There are main :
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple
# Mapping Type:	   dict
# Boolean Type:	    bool
# Python Automatically detects which datatype it is.
# Initialising string :
string = 'Hello World'
print(type(string))
# Here we declared a variable "string" and  assigned it a value 'Hello World'.
# Initialising Integer :
# Here we declared a variable "a" and  assigned it a value 9.
a = 9
# To check its datatype we can write the following:
print(type(a)) # Here we use print statement to print the datatype of 'a' using a type func we will learn forward.
# Initialising Float :S
# Here we declared a variable "b" and  assigned it a value "9.0".
b = 9.0
print(type(b))
# Initialising Complex :
# Here we declared a variable "c" and  assigned it a value 3 + 5j.
c = 3 + 5j 
print(type(c))
# Initializing list :
# List is can be initialialized by "[]" (Square Brackets).
d = [] 
#                       OR 
# It can also be initialised by list() function.
e = list()
# Now lets Print the datatypes of the same.
print(type(d))
print(type(e))
# It is the same for Tuple.
# To initialise tuple you can use "()" (Parentheses)
f = ()
#                       OR
# It can also be initialised by tuple() function.
g = tuple()
# Now lets Print the datatypes of the same.
print(type(f))
print(type(g))
# Initialisng Dict:
# Dictionary contains Key:Value Pair which can be initialised by "{}" or dict() function.
h = {}
i = dict()
# Now lets print the datatype of h and i.
print(type(h))
print(type(i))
# Boolean Datatype is for the keywords True and False.
# If we assign it to any variable it will store a boolean value:
j = True # Here True is a boolean value.
print(type(j))