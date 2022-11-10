def name(*args):
    print(args)

print("Python", "Java", ".net", "C", "C++")

#Sum of all numbers

def Sum(*args):
    print(sum(args))

Sum(12,23,34,56)

#Max
def Max(*args):
    print(max(args))

Max(12,23,34,56)

#Min
def Min(*args):
    print(min(args))

Min(12,23,34,56)

print("*********************************************")

def print_names(**kwargs):
    print(type(kwargs))
    print(kwargs["lang"])

print_names(lang="Python", ver=3.0)

