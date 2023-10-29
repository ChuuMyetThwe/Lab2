
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    y = x.split(",")
    z = list(map(float,y))
    return z

def calc_average(z):
    average = sum(z) / len(z)
    return average

def calc_min_max(z):
    minimum = min(z)
    maximum = max(z)
    return [minimum, maximum]

def sort_temperature(z):
    sorted_list = sorted(z)
    return sorted_list

def main():
    display_main_menu()
    num_list = get_user_input()
    min_val, max_val = calc_min_max(num_list)
    print("Minimum:", str(min_val))
    print("Maximum:", str(max_val))
    sorted_list = sort_temperature(num_list)
    print("Sorted Temperature: ", sorted_list)

if __name__ == "__main__":
    main()