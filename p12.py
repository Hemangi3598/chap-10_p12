# p12) delete an existing flie

import os
filename = input("enter filename to be deleted ")
if os.path.exists(filename):
	os.remove(filename)
	print(filename, " file deleted ")
else:
	print(filename, "does not exist ")