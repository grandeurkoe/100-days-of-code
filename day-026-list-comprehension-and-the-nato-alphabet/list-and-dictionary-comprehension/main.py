# List Comprehension
# new_list = [new_item for item in list]
# If you wish to specify a condition when creating a new list.
# new_list = [new_item for item in list if test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Print all the names whose length is greater than 5 in uppercase.
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# Dictionary Comprehension
# Creates a dictionary using existing items from a list.
# new_dict = {new_key:new_value for item in list}
# Creates a dictionary using (key,value) pairs from an existing dictionary.
# new_dict = {new_key:new_value for (key,value) in old_dict.items() if test}

# from random import randint

# student_scores = {student:randint(1,100) for student in names}
# passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
# print(passed_students)

# Iterate over a Pandas DataFrame.
student_dict = {
    "student": ["Meowya", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# # Loop through student_data_frame
# for (key,value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame.
for (index, row) in student_data_frame.iterrows():
    print(row)
