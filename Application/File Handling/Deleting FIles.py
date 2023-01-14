import os

if os.path.exists("AI.txt"):
    os.remove("AI.txt")
else:
    print("File not found")