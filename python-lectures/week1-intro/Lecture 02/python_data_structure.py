my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(my_dict)
print(my_dict["a"])
print(my_dict["b"])
print(my_dict["c"])

my_dict["c"] = 300
print(my_dict)

# Reason to use dictionary – It can contain heterogeneous values.

student_object = {
    "full_name": "Divya Rai",
    "age": 30,
    "location": "Delhi",
    "favorite_food": "Dosa",
    "name": "Varun",
    "subjects": ["Hindi", "English", "Maths"],
    "marks": {
        "hindi_marks": 70,
        "english_marks": 80,
        "maths_marks": 90

    }
}
print(student_object["subjects"])
student = [15, "delhi", "Varun", "name"]
print(student_object["subjects"][0])
print(student)
print(student_object["marks"]["hindi_marks"])

# formating
my_messsage = "Hello Sir %s, thanks for signing up %d" %(student_object["full_name"],student_object["age"])
print(my_messsage)