f=open("proto.txt","r")
print(f.read()) # Read all text in files
print(f.readline()) # Read text per-lines
print(f.readlines()) # Read all text by list
for i in f:
    print(i)
f.close()

f=open("mytext.txt","w")
f.write("Bye\n")
f.writelines(["Hello\n","World\n","Pyhton\n"])
f=open("mytext.txt","r")
print(f.read())
f.close()

f=open("D:\\Dennis Keenan Arkananta\\BrightChamps\\Pyhton\\Application\\File Handling\\new.txt","x")
f.close()