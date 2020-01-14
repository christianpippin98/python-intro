# SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
#             1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# # Instead of the word `function`, in Python, you use `def`
# def approximate_size(size, a_kilobyte_is_1024_bytes=True):

#     '''Convert a file size to human-readable form.
#     Keyword arguments:
#     size -- file size in bytes
#     a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
#                                 if False, use multiples of 1000
#     Returns: string
#     '''
#     if size < 0:
#         raise ValueError('number must be non-negative')

#     multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
#     for suffix in SUFFIXES[multiple]:
#         size /= multiple
#         if size < multiple:
#             return '{0:.1f} {1}'.format(size, suffix)

#     raise ValueError('number too large')

# if __name__ == '__main__':
#     print(approximate_size(16384, False))
#     print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
#     print(approximate_size(-16384))

name = "Fred"
def say_name():
    global name
    name = "Bubba"
#     print("internal", name)

say_name()
# print("external", name)

# # if/else
# name = "Joe"
# if name == "Steve":
#     print("I feel great")
# elif name == "Joe":
#     print("you got the better instructor")
# else:
#     print("I have a cold")

# # string concatenation

# # Still have dynamic typing (but no implicit coercion!)
# print(f"My name is { name }")

# # Collections
# # List
junk = ["Me", True, [1,2,3], 234]
# print(junk)

junk.append("uh-oh")
junk.insert(3, "wow")
junk.extend(["Mary", "Joseph", "Bob"])
# print(junk)

names = ["Mary", "Joseph", "Bob"]
# print(", ".join(names))

# Dictionaries
my_pairs = {
    123: "number",
    "name": "Brunhilda"
}

my_pairs["last"] = "Jones"
my_pairs["address"] = {"number": 123, "street": "Sesame St"}
# print(my_pairs.keys())
# print(my_pairs.values())
# print(my_pairs.items())

street_name = my_pairs["address"]
# # print(street_name)


# # Sets
my_stuff = ["Fred", True, 123, "Jones", "Fred"]
# print(list(set(my_stuff)))

my_set = {1, 2, 3}
my_set.add("Feed me")
# print(my_set)

# Tuple
my_tuple = (1, 2, 3, 3, "hello")
# print(my_tuple)
# print(my_tuple[0])

# Loops
my_tuple = (1, 2, 3, 3, "hello")
my_set = {1, 2, 3}
junk = ["Fred", True, [1,2,3], 234]
my_pairs = {
    123: "number",
    "name": "Broomhilda"
}

# for foo in my_pairs.values():
    # print(f"Why do I still have {foo} in this drawer?")

my_list = [1, 2, 4, "hello", "monkey"]
# my_subset = my_list[0:3]
# my_subset = my_list[1:3]
# my_subset = my_list[:3]
# my_subset = my_list[2:]
my_subset = my_list[2:34]
# my_subset = my_list[2:-1]
print(my_subset)
print(my_list)