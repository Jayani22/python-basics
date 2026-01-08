# in python we declare functions like def keyword and function name

# def func_name():
#     print("Hello")

# func_name()# we call a function

# def mult(a: int, b: int) -> int:
#     return a * b # default is none
# res = mult(2, 3) # store the value which we got
# print(res)

# def mult(a: int, b: int) -> int:
#     return a * b # default is none
# res = mult('3.0', 3)
# print(res)

# #a=4, b=5 are keyword arguments, as they contain keys and values
# #'3.0', 3 are called as positional arguments

# def mult(a, b, *args, **kwargs):
#     print(f"a:{a}, b:{b}, args:{args}, kwargs:{kwargs}")
#     return a * b

# res=mult('3.0', 3, 4, 5, c=10, d=20)
# print(res)

"""
When we specify data type in function but if we give different data type when passing the values what happen
"""
# def abc(a:int, b:float) -> float:
#     return a+b
# print(abc(1,2.0)) # 3.0
# print(abc(2,2)) # 4

def calc(a, b, operation):
    if operation == "add":
        return a + b
    if operation == "sub":
        return a - b
    if operation == "mult":
        return a * b
    if operation == "div":
        return a % b
    
values = input("Enter 2 numbers:")
operation=input("Enter operation to perform:")
