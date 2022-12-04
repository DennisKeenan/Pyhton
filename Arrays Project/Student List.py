print()
studentList=["Harun Cahya","Ratna Danial","Susila Aditya","Muhamad Harun","Putri Lestari"]
print("Daftar murid kelas 10A:")
count=1
for i in studentList:
    print(str(count)+".",i)
    count+=1
print("="*35)
while(True):
    print("1. Add a student!")
    print("2. Find a student number")
    print("3. Check duplicate student")
    print("4. Print student list")
    print("5. Remove student")
    print("6. Close App")
    choices=input()
    if choices=="1":
        newStudent=input("Add a new student: ").title()
        studentList.append(newStudent)
    elif choices=="2":
        studentName=input("What's the student name: ")
        print("Number of", studentName,":", studentList.index(studentName)+1)
    elif choices=="3":
        duplicate=(True)
        for i in studentList:
            if studentList.count(i)==1:
                duplicate=(False)
            else:
                print("Duplicated name detected!", i)
                duplicate=(True)
                break
        if not duplicate:
            print("Duplicated name not detected")
    elif choices=="4":
        count=1
        for i in studentList:
            print(str(count)+".",i)
            count+=1
        print("-"*40)
    elif choices=="5":
        studentNumber=int(input("Insert the student number: "))
        choicesRemove=input("Are you sure to remove"+ " "+studentList[studentNumber-1]+ " y/n?")
        if choicesRemove=="y":
            studentList.remove(studentList[studentNumber-1])
    else:
        break

