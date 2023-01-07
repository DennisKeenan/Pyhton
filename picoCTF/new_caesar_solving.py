import string
import binascii

LOWERCASE_OFFSET = ord("a")
alphabhet= string.ascii_lowercase[:16]
print(alphabhet)

def b16decode(secret):
    plain=""
    count=0
    temp=""
    for i in secret:
        count+=1
        temp+="{0:04b}".format(alphabhet.index(i))
        if count==2:
            number=int(temp,2)
            plain+=(chr(number))
            temp=""
            count=0
    print(plain)
def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return alphabhet[(t1 - t2) % len(alphabhet)]

enc1=("mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj")
print(alphabhet)
for k in alphabhet:
  enc=""
  for i, c in enumerate(enc1):
    enc += unshift(c, k[i % len(k)])
  b16decode(enc)

        