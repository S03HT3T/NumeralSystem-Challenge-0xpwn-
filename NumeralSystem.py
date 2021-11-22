import base64
import base58
import base91
import binascii

num = open("NumeralSystem.txt","r").read()

for i in range(5):
	if num.startswith('keep'):
		num = num.split(": ")
		num = base64.b32decode(num[1]).decode()
		print("Base32 decoded!!")
	else:
		num = base64.b32decode(num).decode()
		print("Base32 decoded!!")

	num = num.split(": ")
	num = binascii.unhexlify(num[1]).decode()
	print("Hex decoded!!")

	num = num.split(": ")
	num = base64.b64decode(num[1]).decode()
	print("Base64 decoded!!")

	num = num.split(": ")
	num = binascii.unhexlify(num[1]).decode()
	print("Hex decoded!!")

	num = num.split(": ")
	num = base64.b85decode(num[1]).decode()
	print("Base85 decoded!!")

	num = num.split(": ")
	num = binascii.unhexlify(num[1]).decode()
	print("Hex decoded!!")

num = num.split(": ")
num = base58.b58decode(num[1]).decode()
print("Base58 decoded!!")

num = num.split(": ")
num = base91.decode(num[1]).decode()
print("Base91 decoded!!")


print("Flag : " + str(num))