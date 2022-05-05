
# translate = {
#     "red": "rojo",
#     "blue": "aloz",
#     "green": "verdi",
#     "white": "blanco"
# }

# alist = [
#     "rojo",
#     "aloz", 
#     "verdi",
#     "blanco" 
# ]
# # print("alist", alist[1]) 
# print("translate red", translate["white"])

# user = {
#     "first_name": "Robert",
#     "last_name": "Smith", 
#     "age": 19,
#     "school": {
#         "school_name": "Fresno State", 
#         "grade": "Senior",
#         "gpa": 3.5,
#         "completed_courses": [
#             "Programming Fund",
#             "Project Management"
#         ]
#     }
# }
# print("Length of dictionary: ", len(user)) 
# print(user["first_name"] + "'s age is: ", user["age"])
# print("courses", user["school"]["completed_courses"])
# num_courses = len(user["school"]["completed_courses"])
# output = user["first_name"] + "goes to" + user["school_name"] + "and is taking" + str(num_courses) 

# print(output) 

# if "completed_courses" in user: 
#     print("True")
# else: 
#     print("False") 

# print("Original user: ", user)
# user["school"] = None
# print("Mutated user: ", user)

# school = user.get("school", None)
# print("school", school.get("complete_courses"))

# print("keys: ", user.keys())
# print("Values: ", user.values())

# user_data = list(user)
# print("User dictionary converted into a list: ", user_data)
# print("User dictionary converted into a tuple of key value pairs: ", user.items())

# print("User", user)
# alist = [1, 2]
# set = set(alist)
# del user["school"]
# print("User with no school: ", user)

# user.clear()
# print("Cleared user object: ", user)
# original_dict = {}
# dict1 = {
#     "a": "A", 
#     "b": "B",
#     "c": "C",
# }

# dict2 = {
#     "c": "C",
#     "d": "D", 
#     "e": "E"
# }

# dict3 = {
#     "f": "F",
#     "g": "G",
#     "h": "H"
# }

# dict1.update(dict2)
# dict1.update(dict3)
# print("dict1", dict1)
# print("Merged Dictionary", original_dict.update(dict2)) #TOCO: check python version

# def main(): 
#     print("Main running...")
#     d = {}
#     print(d)

#     d.update(dict2)
#     print("d", d)

#     print("Keys", d.keys())
#     print("Values", d.values())
# main()

from tkinter import W


def main():
    textese_dict = create_dictionary("Textese.txt")
    prompt = "Enter a simple sentence in lowercase letters without any punctuations: "
    sentence = input(prompt)
    translate(sentence, textese_dict)

def create_dictionary(file_name):
    infile = open(file_name, "r") # "Textese.txt"
    text_list = [ line.rstrip() for line in infile ]  #creates a list of stringss from textese.txt
    infile.close()
    output = [ x.split(",") for x in text_list ] # .split is creating an array of arrays by using the (,)
    return dict(output)

def translate(sentence, textese_dict): 
    words = sentence.split()
    for word in words:
        print(textese_dict.get(word, word) + " ", end="")

main()
