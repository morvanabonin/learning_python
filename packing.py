# Call normal of date function passing three parameters - year, month, day
from datetime import date
d = (2013, 3, 15)
print (date(d[0], d[1], d[2]))

#Function date using packing to pass - year, month, day
from datetime import date
d = (2013, 3, 15)
print (date(*d))

#Other example using a dictionary data.
def new_user(active=False, admin=False, root=False):
	print(active)
	print(admin)
	print(root)

config = {"active" : False,
	  "admin" : True,
	  "root" : False}

new_user(config.get('active'), config.get('admin'), config.get('root'))

print ('Function using packing args')
def new_user(active=False, admin=False, root=False):
	print(active)
	print(admin)
	print(root)

config = {"active" : False,
	  "admin" : True,
	  "root" : True}

new_user(**config)
