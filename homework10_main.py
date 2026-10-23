print("Завдання 1")
numbers_list = [10, 20, 10, 30, 20, 40, 10, 50]
numbers_set = set(numbers_list)
print(numbers_list)
print(numbers_set)
print(len(numbers_set))
print(30 in numbers_set)
print(100 in numbers_set)

print("Завдання 2")
data = [15, "Python", 15, True, "Python", 3.14, False, True]
data_set = set(data)
print(data_set)
data_set.add("Redis")
data_set.add(100)
data_set.discard("Python")
print(True in data_set)
print(False in data_set)

print("Завдання 3")
python_students = {"Anna", "Oleg", "Ivan", "Maria"}
redis_students = {"Oleg", "Maria", "Petro", "Sofia"}
union_operator = python_students | redis_students
union_method = python_students.union(redis_students)
print(union_operator)
print(union_method)
print(union_operator == union_method)

print("Завдання 4")
intersection_operator = python_students & redis_students
intersection_method = python_students.intersection(redis_students)
print(intersection_operator)
print(intersection_method)

print("Завдання 5")
all_students = {"Anna", "Oleg", "Ivan", "Maria", "Petro", "Sofia"}
python_students_set = {"Anna", "Oleg", "Ivan"}
diff_operator = all_students - python_students_set
diff_method = all_students.difference(python_students_set)
print(diff_operator)
print(diff_method)

print("Завдання 6")
numbers = {10, 20, 30}
numbers.add(40)
numbers.add(40)
numbers.update([50, 60, 70])
numbers.remove(20)
numbers.discard(100)
popped_element = numbers.pop()
print(popped_element)
print(numbers)
