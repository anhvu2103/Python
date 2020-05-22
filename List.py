'''
Anh Vu
02/25/2020
Assignment 5
Write a program that asks the users to enter integer values for two lists.
Display whether the lists are of equal length or not,
whether the numbers in each list add up to the same value,
and then display a list of the numbers that are common to both lists.
'''
# creating an empty list
list1 = []
list2 = []
# number of elemetns as input
n = int(input("Enter number of elements: "))
# iterating till the range
for i in range(0, n):
    ele1 = int(input())

    list1.append(ele1)  # adding the element


k = int(input("Enter number of elements: "))
for j in range(0, k):
    ele2 = int(input())

    list2.append(ele2)  # adding the element

list1len = len(list1)
list2len = len(list2)
print("List 1: ",list1)
print("List 2: ",list2)
print("List 1 length is: ",list1len)
print("List 2 length is: ",list2len)
suml1 = sum(list1)
suml2 = sum(list2)
if list1len == list2len:
    print("The lists have equal length")
else:
    print("The lists do not have equal length")

if suml1 == suml2:
    print("The sum of list 1 and list 2 add up to the same result which is: ", suml1)
else:
    print("List 1 and List 2 doesn't add up to the same number")
    print("The sum of list 1: ",suml1)
    print("The sum of list 2: ",suml2)
for item in list1:
    for item1 in list2:
        if item == item1:
            print(item, "is in both list 1 and list 2")

