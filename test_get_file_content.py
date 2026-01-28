# test_get_file_content.py

from functions.get_file_content import get_file_content

def main():
	print(f'Result for "lorem.txt"')
	print(get_file_content("calculator", "lorem.txt"), "\n")

	print(f'\nResult for "main.py"')
	print(get_file_content("calculator", "main.py"))

	print(f'\nResult for "pkg/calculator.py"')
	print(get_file_content("calculator", "pkg/calculator.py"))

	print(f'\nResult for "/bin/cat"')
	print(get_file_content("calculator", "/bin/cat"))

	print(f'\nResult for "pkg/does_not_exist.py"')
	print(get_file_content("calculator", "pkg/does_not_exist.py"), "\n")



if __name__ == "__main__":
	main()