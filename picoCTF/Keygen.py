from hashlib import *

username=b"PRITCHARD"
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

proccess=sha256(username).hexdigest()
dynamic=""

dynamic += proccess[4]
dynamic += proccess[5]
dynamic += proccess[3]
dynamic += proccess[6]
dynamic += proccess[2]
dynamic += proccess[7]
dynamic += proccess[1]
dynamic += proccess[8]
print(dynamic)

print(key_part_static1_trial+dynamic+key_part_static2_trial)