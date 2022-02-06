# https://www.w3resource.com/python-exercises/list/

# 1. Write a Python program to sum all the items in a list
count = 0
n1 = range(10)

s1 = ["My name is Saurabh. Saurabh is learning Python"]

print(n1)
print(n1[0])


for numbers in n1:
    count += numbers
    # print(numbers)

print('Total Sum is ' + str(count))
# 3. Write a Python program to get the largest number from a list

print('Largest number in list ' + str(max(n1)))

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first
# and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

Sample_List = ['abc', 'xyz', 'aba', '1221']

cnt = 0
for s in Sample_List:
    if (len(s) >= 2) and (s[0] == s[-1]):
        cnt += 1
        # print(s)

print(cnt)

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple
# from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

Sample_List1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected_Result = []


def last(n):
    return n[-1]


def sort_list_last(tuples):
    return sorted(tuples, key=last)


print(sort_list_last(Sample_List1))

# 7. Write a Python program to remove duplicates from a list
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40, 10]

print(sorted(list(set(a))))

# OR

uniq_item = []
dup_items = set()

for x in a:
    if x not in uniq_item:
        uniq_item.append(x)
    else:
        dup_items.add(x)

print(uniq_item)
print(dup_items)

# 8. Write a Python program to check a list is empty or not
a = []

if not a:
    print("List is empty")

# Write a Python program to find the list of words that are longer than n from a given list of words.
# Output n 3 ['quick', 'brown', 'jumps', 'over', 'lazy']


def words_length(n, str1):
    words_list = []
    txt = str1.split(" ")
    for x2 in txt:
        if len(x2) > n:
            words_list.append(x2)
    return words_list


print(words_length(3, "The quick brown fox jumps over the lazy dog"))

# 11. Write a Python function that takes two lists and returns True if they have at least one common member


def text_include_any(li1, li2):
    for x3 in li1:
        if x3 in li2:
            return True
    return False


print(text_include_any([1, 2, 3, 4, 5], [3, 6, 9, 12, 15]))
print(text_include_any([1, 2, 3, 4, 5], [6, 9, 12, 15]))

# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


def concat_list_range(n, li5):
    list1 = []
    for i in range(1, n+1):
        for x7 in li5:
            list1.append(x7+str(i))
    return(list1)

print(concat_list_range(5, ["p", "q"]))
