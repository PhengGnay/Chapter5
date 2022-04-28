
# file_name = "./infile.txt"
# infile = open(file_name, 'r')
# names = [line.rstrip() for line in infile]
# # print("names: ", names)

# #
# # infile.close()

# # def main():
# #     display_with_forloop(file_name)
# #     print()

# # def display_with_forloop(file_name):
# #     infile = open_file(file_name, 'r')
# #     for line in infile:
# #         print(line, end="") 
# #     infile.close() 

# # def display_with_list_comprehension(file_name):
# #     infile = open_file(file_name, 'r')
# #     items = [line.rstrip() for line in infile]
# #     print("items: ", items)
# #     infile.close()

# def open_file(file_name, mode):
#     return open(file_name, mode)


# def main():
#     save_to_outfile("./outfile.txt")

# # create a file object in write mode
# def open_file(file_name, mode):
#     return open(file_name, mode)

# def save_to_outfile(file_name):
#     outfile = open_file(file_name, "w")
#     for name in names:
#         if "Doe" not in name:
#             print("Name to be persisted: ", name)
#             outfile.write(name + "\n")
#     outfile.close()
# main()

# a_list = []
# a_set = {}
# a_list.append("A")
# a_set.add("A") 

# def main(): 
#     words = ["nudge", "nudge", "wink", "wink"]
#     terms = set(words)
#     print("terms", terms)
#     terms.add("wink")
#     terms.add("new wink")
#     terms.discard("nudge")
    
# main()

# arr1 = ["Alpha", "Bravo", "Charlie"]
# arr2 = ["Bravo", "Dalta"]
# set1 = set(arr1)
# set2 = set(arr2)

# print("set1", set1)
# print("set2", set2) 
# #Built-in Set methods: 1 .union, 2 .intersection, 3 . difference()

# print("union: ", set1.union(set2))
# print("intersection: ", set1.intersection(set2))
# print("difference: ", set1.difference(set2))
