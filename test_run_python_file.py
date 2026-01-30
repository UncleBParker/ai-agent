# test_run_python_file.py

from functions.run_python_file import run_python_file

def main():
	print(f'\nResult for "main.py"')
	print(run_python_file("calculator", "main.py"))

	print(f'\nResult for "main.py ["3 + 5"]"')
	print(run_python_file("calculator", "main.py", ["3 + 5"]))

	print(f'\nResult for "tests.py"')
	print(run_python_file("calculator", "tests.py"))

	print(f'\nResult for "../main.py"')
	print(run_python_file("calculator", "../main.py"))

	print(f'\nResult for "nonexistent.py"')
	print(run_python_file("calculator", "nonexistent.py"))

	print(f'\nResult for "lorem.txt"')
	print(run_python_file("calculator", "lorem.txt"), "\n")



if __name__ == "__main__":
	main()