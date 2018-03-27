import random

key = "r74io860-21"
random.seed(key * 997)
print random.randint(1,100)

key = "srghjtdoiukj-21"
random.seed(key * 997)
print random.randint(1,100)

print bytearray("fjksgh,aeufkjgh")

string = "jhg,sbrmnvd;vfbjoheklntrs"

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
for b in arr:
    print b