# test_write_file.py

from functions.write_file import write_file

def main():
	print(f'\nResult for "lorem.txt":')
	print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

	print(f'\nResult for "pkg/morelorem.txt":')
	print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
	
	print(f'\nResult for "/tmp/temp.txt":')
	print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"), "\n")



if __name__ == "__main__":
	main()