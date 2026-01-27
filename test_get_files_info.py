# test_get_files_info.py

from functions.get_files_info import get_files_info

def main():
	print("\nResult for current directory:")
	print(get_files_info("calculator", "."))

	print("\nResult for 'pkg' directory:")
	print(get_files_info("calculator", "pkg"))

	print("\nResult for '/bin' directory:")
	print(get_files_info("calculator", "/bin"))

	print("\nResult for '../' directory:")
	print(get_files_info("calculator", "../"), "\n")



if __name__ == "__main__":
	main()