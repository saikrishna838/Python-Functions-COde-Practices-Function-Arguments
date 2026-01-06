def message(arg_1, arg_2):
    result = arg_1 + " is " + str(arg_2) + " years old."
    return result

name = input()
age = int(input())
result = message(arg_1 = name, arg_2 = age)
print(result)

