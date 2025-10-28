print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    user_input=input("enter name: ")
    string_list = user_input.split(",")
    float_list = [float(num) for num in string_list]
    return float_list

def calc_average(num_list):
    print(sum(num_list) / len(num_list))

def find_min_max(num_list):
    print(min(num_list) , max(num_list))

def sort_temperature(num_list):
    print(sorted(num_list))

def calc_median_temperature(num_list):
    x = len(num_list)
    if x==0:
        return 0.0
    
    sorted_list = sorted(num_list)
    mid= x // 2
    if x % 2 == 0:
        median = ((sorted_list[mid -1] + sorted_list[mid]) / 2)
        print (median)

def calc_average_temp(num_list):
    total = sum(num_list)
    length = len(num_list)
    ave = total / length
    print(ave)

def calc_min_max_temp(num_list):
    min_temp = min(num_list)
    max_temp = max(num_list)
    print(min_temp, max_temp)

display_main_menu()
num_list = get_user_input()
calc_average(num_list)
find_min_max(num_list)
sort_temperature(num_list)
calc_median_temperature(num_list)
calc_average_temp(num_list)
calc_min_max_temp(num_list)