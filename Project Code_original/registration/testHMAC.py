import hashlib
import hmac



with open('section3-staff.key','rb') as file:
    key = file.read()

test = str.encode("test")


hmac1 = hmac.new(key, test, digestmod=hashlib.sha256)
#Create MD from hmac1
md1 = hmac1.hexdigest()
print(md1)