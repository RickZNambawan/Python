import os

print(dir(os))
print(os.getcwd())  # get current working directory

# os.chdir("C:/Users/RickZ/Desktop/3")  # change directory

# os.mkdir("Sample")  # make directory with top-level only
# os.makedirs("Sample1/Sample2")  # make dir with top-level and subdirectories

# os.rmdir("Sample1")  # remove directory not remove the subdirectory
# os.removedirs("Sample1/Sample2")  # remove directory remove the top-level with subdirectory

# os.rename("Sample1", "SAMPLE1")  # renaming directory
# print(os.stat("SAMPLE1"))  # show information about the file
# print(os.stat("SAMPLE1").st_size)  # print only the info you want about the file

# print(os.listdir())  # show list of directory

path = os.path.join("SAMPLE1", "hahaha.txt")  # to add path properly
print(path)
print(os.path.basename(path))  # to print the subdir of the folder
print(os.path.dirname(path))  # to print the top-level sub of the folder
print(os.path.split(path))  # to split in tuple of the name path
print(os.path.exists(path))  # to know if the file is exist
print(os.path.isdir(path))  # to know if something is directory
print(os.path.isfile(path))  # to know if something is file
print(os.path.splitext(path))  # to split the file name and file extension
