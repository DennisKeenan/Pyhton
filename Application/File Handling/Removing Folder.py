import os

fileinput=input("Name of folder you want to remove: ")
if os.path.exists(fileinput):
    os.rmdir(fileinput)
else:
    print("Folder not exist")