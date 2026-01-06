def compare_numbers(first_number, second_number):
    
    if (first_number > 100 and second_number > 100) and (first_number < second_number):
        is_true = "True"
    else:
        is_true = "False"
    return is_true
    

first_number = int(input())
second_number = int(input())

is_true = compare_numbers(first_number, second_number)

print(is_true)