#Basic List Operations
#. Create a list of five numbers and append a new number to it. Print the updated list.
#. Extend a list [1, 2, 3] with another list [4, 5, 6]. Print the result.
#. Insert the string "Python" at index 2 in the list ["Java", "C++", "JavaScript",
#"Ruby"].
#. Remove the first occurrence of the number 10 from the list [10, 20, 30, 10, 40].
#. Use the pop() method to remove the last element from [100, 200, 300, 400] and
#print the modified list.
#1. Append a new number to a list

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)


#2. Extend a list with another list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)


#3. Insert a string at a specific index

languages = ["Java", "C++", "JavaScript", "Ruby"]
languages.insert(2, "Python")
print(languages)


#4. Remove the first occurrence of an element

numbers = [10, 20, 30, 10, 40]
numbers.remove(10)
print(numbers)


#5. Remove the last element using pop()

numbers = [100, 200, 300, 400]
numbers.pop()
print(numbers)

#Intermediate List Operations
#6. Count how many times the number 5 appears in the list [5, 10, 5, 20, 5, 30].
#7. Sort the list [9, 1, 8, 3, 5] in ascending and descending order.
#8. Reverse the list [“apple”, “banana”, “cherry”] using the reverse() method.
#9. Create a copy of the list [1, 2, 3, 4, 5] and store it in another variable. Modify the
#copied list and print both lists.
#10. Clear all elements from a list [“hello”, “world”, “python”] using the clear()method.


#6. Count the occurrences of a number

numbers = [8, 10, 8, 20, 8, 30]
count = numbers.count(8)
print("The number 5 appears", count, "times.")


#7. Sort a list in ascending and descending order

numbers = [9, 1, 8, 3, 5]
numbers.sort()
print("Ascending order:", numbers)
numbers.sort(reverse=True)
print("Descending order:", numbers)


#8. Reverse a list using the reverse() method

fruits = ["pomogranate", "mango", "pear"]
fruits.reverse()
print("Reversed list:", fruits)


#9. Create a copy of a list and modify the copied list

numbers = [1, 2, 3, 4, 5]
copied_numbers = numbers.copy()
copied_numbers.append(6)
print("Original list:", numbers)
print("Copied list:", copied_numbers)


#10. Clear all elements from a list using the clear() method

words = ["hello", "its me", "kounain"]
words.clear()
print("Cleared list:", words)

#Tuple-Based Questions
#11. Create a tuple with 5 different fruits and print the third fruit.
#12. Convert the tuple (10, 20, 30, 40, 50) into a list, remove the number 30, and convert
#it back into a tuple.
#13. Try to append an element to the tuple (“A”, “B”, “C”). What happens? How can you
#modify a tuple indirectly?
#14. Unpack the tuple (100, 200, 300) into three separate variables and print them.
#15. Count the occurrences of 7 in the tuple (7, 1, 7, 3, 7, 5).

#11. Create a tuple with 5 different fruits and print the third fruit

fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(fruits[2])


#12. Convert a tuple to a list, remove an element, and convert back to a tuple

numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)
numbers_list.remove(30)
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)


#13. Try to append an element to a tuple and modify it indirectly

# Trying to append an element to a tuple will raise an error
fruits = ("A", "B", "C")
try:
    fruits.append("D")
except AttributeError:
    print("Tuples are immutable and cannot be appended.")

# Modifying a tuple indirectly by converting it to a list
fruits_list = list(fruits)
fruits_list.append("D")
fruits = tuple(fruits_list)
print(fruits)


#14. Unpack a tuple into separate variables

numbers = (300, 400, 500)
a, b, c = numbers
print(a, b, c)


#15. Count the occurrences of an element in a tuple

numbers = (7, 1, 7, 3, 7, 5)
count = numbers.count(7)
print(count)

#Advanced Problems
#16. Write a function that takes a list and returns a new list with all even numbers removed.
#17. Create a function that accepts a list and returns a new list with elements sorted in
#descending order without using the sort() method.
#18. Given a list of numbers, write a program to remove all duplicate elements and print the
#unique elements.
#19. Given a tuple of names (“Alice”, “Bob”, “Charlie”, “Alice”, “David”), convert
#it into a list, remove duplicates, and convert it back to a tuple.
#20. Create a program that takes a list of mixed data types (int, str, float) and separates
#integers into one list, strings into another, and floats into another.


#16. Remove even numbers from a list

def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

numbers = [1, 2, 3, 4, 5, 6]
print(remove_even_numbers(numbers))


#17. Sort a list in descending order without using sort()

def bubble_sort_descending(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

numbers = [5, 2, 8, 1, 9]
print(bubble_sort_descending(numbers))


#18. Remove duplicates from a list

def remove_duplicates(numbers):
    return list(set(numbers))

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(remove_duplicates(numbers))


#19. Remove duplicates from a tuple

def remove_duplicates_from_tuple(names):
    return tuple(set(names))

names = ("Alice", "Bob", "Charlie", "Alice", "David")
print(remove_duplicates_from_tuple(names))


#20. Separate mixed data types into different lists

def separate_data_types(mixed_list):
    integers = [x for x in mixed_list if isinstance(x, int)]
    strings = [x for x in mixed_list if isinstance(x, str)]
    floats = [x for x in mixed_list if isinstance(x, float)]
    return integers, strings, floats

mixed_list = [1, "hello", 3.4, 2, "kounain", 4.5]
integers, strings, floats = separate_data_types(mixed_list)
print("Integers:", integers)
print("Strings:", strings)
print("Floats:", floats)


#***Completed by Kounain Aftab***
