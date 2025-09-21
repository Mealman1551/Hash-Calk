from hashlib import md5
from hashlib import sha1
from hashlib import sha224
from hashlib import sha256
from hashlib import sha384
from hashlib import sha512
from hashlib import sha3_224
from hashlib import sha3_256
from hashlib import sha3_384
from hashlib import sha3_512
from hashlib import blake2s
from hashlib import blake2b
from hashlib import shake_128
from hashlib import shake_256

print("Hash Calk")
print("This tool calculates the hashes of a file using various algorithms.")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("")

try:
	input_file = input("Enter the file path: ").strip('"')
	with open(input_file, 'rb') as file:
		file_content = file.read()
		print("")
		print("MD5:", md5(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("SHA 1:", sha1(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("SHA 224:", sha224(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("SHA 256:", sha256(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("SHA 384:", sha384(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("SHA 512:", sha512(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("SHA3 224:", sha3_224(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("SHA3 256:", sha3_256(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("SHA3 384:", sha3_384(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("SHA3 512:", sha3_512(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("Blake2s:", blake2s(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("Blake2b:", blake2b(file_content).hexdigest())
		print("")
		print("**************************************************************")
		print("")
		print("Shake 128 (32):", shake_128(file_content).hexdigest(32))
		print("")
		print("**************************************************************")
		print("")
		print("Shake 256 (32):", shake_256(file_content).hexdigest(32))
		print("")
		print("**************************************************************")
		print("")
		print("Shake 128 (64):", shake_128(file_content).hexdigest(64))
		print("")
		print("**************************************************************")
		print("")
		print("Shake 256 (64):", shake_256(file_content).hexdigest(64))
		print("")
except PermissionError:
	print("Error: Permission denied. Please check your file permissions.")
except IsADirectoryError:
	print("Error: Expected a file but found a directory. Please provide a file path.")
except FileNotFoundError:
	print("Error: File not found. Please check the file path.")
except Exception as e:
	print(f"An error occurred: {e}")
finally:
	print("")
	print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
	print("")
	print("Hash Calk - End of Program")
