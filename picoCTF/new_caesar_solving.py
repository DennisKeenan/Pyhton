import string

alphabhet= string.ascii_lowercase[:16]
print(alphabhet)

def b16decode(secret):
    plain=""
    for i in secret:
       print(alphabhet.index(i))

b16decode("mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj")
        