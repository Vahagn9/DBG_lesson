# === ex. 1 ===
def bubble_sort(in_list: list):
    """sorting list a by bubble. Updates the input list itself"""
    for i in range(1, len(in_list)):
        for j in range(len(in_list) - i):
            if in_list[j] > in_list[j + 1]:
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]


# === ex. 2 ===
def concatenate_two_lists_index_wise(list_1: list, list_2: list):
    """
    Concatenate two lists index-wise.
    Input:
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    returns ['My', 'name', 'is', 'Kelly']
    """
    return [i + j for i, j in zip(list_1, list_2)]


# === ex. 3 ===
def turn_list_items_to_square(in_list: list):
    """Given a Python list of numbers. Turn every item of a list into its square"""
    for i in range(len(in_list)):
        in_list[i] **= 2


# === ex. 4 ===
def calculate_sum_of_lists_members(list_in: list):
    """Write a program that will calculate sum of lists members."""
    members_sum = 0
    for i in list_in:
        members_sum += i
    return members_sum


# === ex. 5 ===
def remove_duplicates_from_a_list(list_a: list):
    """Write a Python program to remove duplicates from a list."""
    unique_items = []
    for i in list_a:
        if i not in unique_items:
            unique_items.append(i)
    list_a.clear()
    for i in unique_items:
        list_a.append(i)


# === ex. 6 ===
def get_unique_values_from_a_list(list_a: list):
    """Write a Python program to get unique values from a list."""
    unique_items = []
    for i in list_a:
        if i not in unique_items:
            unique_items.append(i)
    return unique_items


# === main ===
nums_list_ex = [6, 8, 9, 6, 7, 3, 5, 15, 654, 8, 8, 6, 6, 5]
str_list_ex = ["Anna", "anna", "Bob", "Alis", "anna", "Bob", "anna"]

print(nums_list_ex)
bubble_sort(nums_list_ex)
print(nums_list_ex)
print("=== next example ===")
print(str_list_ex)
remove_duplicates_from_a_list(str_list_ex)
print(str_list_ex)
