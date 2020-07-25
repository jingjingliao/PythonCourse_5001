my_fruit_counter = {}
my_fruit_counter["banana"] = 5
my_fruit_counter["fig"] = 1
my_fruit_counter["orange"] = 10
my_fruit_counter["apple"] = 1

print(my_fruit_counter)
print((my_fruit_counter.keys()))
print((my_fruit_counter.values()))
print((my_fruit_counter.items()))

print(list(my_fruit_counter.keys())[0:2])  # This is important

print(sorted(my_fruit_counter.items()))  # Create a sorted list
print((my_fruit_counter.items()))

fruit_by_count = sorted(my_fruit_counter.items(),
                        key=lambda x: x[1], reverse=True)  # sorted function

print(fruit_by_count)


my_food_type = {
    "vegetables": [],
    "meats": [],
    "fruits": []
}

my_food_type["vegetables"].append("celery")
my_food_type["vegetables"].append("carror")
my_food_type["vegetables"].append("spinch")

print(my_food_type)

for food in my_food_type["vegetables"]:
    food = "bubble"  # do not change the list
    print(food)


for i in range(len(my_food_type["vegetables"])):
    # my_food_type["vegetables"][i] = "bubble"  # change the list
    print(my_food_type["vegetables"][i])


# SET

my_veg_set = set()  # create empty set

my_fruit_set = {"banana", "fig", "grapefruite"}


# def check_for_fruit(fruit, fruit_set):
#     if fruit in fruit_set:
#         print("We have a {}".format(fruit))
#     else:
#         print("We don't have a {}".format(fruit))


# check_for_fruit("banana", my_fruit_set)
# check_for_fruit("peach", my_fruit_set)

# my_fruit_set.add("peach")
# my_fruit_set.remove("banana")

print(my_fruit_set)
