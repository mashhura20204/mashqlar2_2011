def remove_duplicates(lst):

    unique_list = list(set(lst))

    unique_list.sort()
    return unique_list


def get_ends(lst):
    if len(lst) == 0:
        return None, None
    return lst[0], lst[-1]


def count_elements(lst):
    return len(lst)


items = [1, 2, 2, 3, 3, 4, 1]

clean_list = remove_duplicates(items)
first, last = get_ends(clean_list)
count = count_elements(clean_list)

print("Takrorlarsiz ro'yxat:", clean_list)
print("Birinchi element:", first)
print("Oxirgi element:", last)
print("Elementlar soni:", count)

##########################################################

def merge_lists(lst1, lst2):
    return lst1 + lst2


def sort_merged(lst):
    return sorted(lst)


def get_evens(lst):
    return [x for x in lst if x % 2 == 0]


def sum_evens(lst):
    return sum(lst)


list1 = [1, 3, 5]
list2 = [2, 4, 6]


merged = merge_lists(list1, list2)
sorted_merged = sort_merged(merged)
evens = get_evens(sorted_merged)
evens_sum = sum_evens(evens)

print("Birlashtirilgan ro'yxat:", merged)
print("Tartiblangan ro'yxat:", sorted_merged)
print("Juft sonlar:", evens)
print("Juft sonlar yig'indisi:", evens_sum)
####################################################
def find_min_max(lst):
    return min(lst), max(lst)


def diff_min_max(lst):
    mn, mx = find_min_max(lst)
    return mx - mn


def index_max(lst):
    return lst.index(max(lst))


def remove_min(lst):
    lst.remove(min(lst))
    return lst



values = [12, 5, 8, 19, 3, 15]

mn, mx = find_min_max(values)
difference = diff_min_max(values)
max_index = index_max(values)

values_after_removal = remove_min(values.copy())


print("Eng kichik:", mn)
print("Eng katta:", mx)
print("Farqi:", difference)
print("Eng katta element indeksi:", max_index)
print("Eng kichik o'chirilgan ro'yxat:", values_after_removal)
