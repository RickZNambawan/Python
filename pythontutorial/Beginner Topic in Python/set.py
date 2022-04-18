""" Sets - are values thar are unordered and have no duplicates """

courses = {"History", "Math", "Physics", "CompSci"}  # the values are always in random order
print(courses)  # the values are not in order

""" Declaration """
mySet = ()  # creates empty set
newSet = set()

""" Throwing Duplicate Values """
names = {"Frederick", "Lyka", "Florante", "Lyka", "Clarence"}
print(names)  # only one "Lyka" prints inside a set

""" Membership Test """
nums = {1, 2, 3, 4, 5, 7, 8, 8, 9}
print(6 in nums)  # testing if the values are on the set

""" Methods of Set """
# intersection() method
itCourses = {"Programming", "Databases", "Networking", "Algorithm"}
csCourses = {"Programming", "Robotics", "Databases", "Algorithm"}
print(itCourses.intersection(csCourses))  # return the common values between 2 sets

# difference() method
itCourses = {"Programming", "Databases", "Networking", "Algorithm"}
csCourses = {"Programming", "Databases", "Robotics", "Algorithm"}
print(itCourses.difference(csCourses))  # return the different values on the first set in the second set

# union() method
itCourses = {"Programming", "Databases", "Networking", "Algorithm"}
csCourses = {"Programming", "Databases", "Robotics", "Algorithm"}
print(itCourses.union(csCourses))  # combines the values of second set into the first set without duplicates