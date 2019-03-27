from django.test import TestCase

# Create your tests here.
s = '<input type="text" name="phone" maxlength="12" required id="id_phone">'



d = s.split('<input')

print(type(d))

for i in d:
	print(i, ' - ', len(i))