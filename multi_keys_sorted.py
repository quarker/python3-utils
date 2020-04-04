from operator import itemgetter

student_tuples = [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

"""
Using sorted() will return a new list
"""
student_tuples = sorted(student_tuples, key=lambda student: student[2])   # sort by age
assert student_tuples == [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

student_tuples = sorted(student_tuples, key=itemgetter(1, 2))    # sort by grade then by age
assert student_tuples == [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

"""
Using list.sort() will sort the list in-place
"""
student_tuples.sort(key=lambda student: student[2])
assert student_tuples == [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

student_tuples.sort(key=itemgetter(1, 2))
assert student_tuples == [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

student_tuples.sort(key=lambda student: (student[1], student[2]))
assert student_tuples == [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

"""
Sort students by descending grade and then ascending age, do the age sort first and then sort again using grade.
This is because when multiple records have the same key, their original order is preserved.
"""
student_tuples.sort(key=lambda student: student[2])
student_tuples.sort(key=lambda student: student[1], reverse=True)
assert student_tuples == [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
