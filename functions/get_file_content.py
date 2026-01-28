# get_file_content.py

import os
import sys
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
	try:
		working_dir_abs = os.path.abspath(working_directory)

		target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

		if not os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs:
			raise Exception(f'Cannot read "{file_path}" as it is outside the permitted working directory')
		
		if not os.path.isfile(target_file):
			raise Exception(f'File not found or is not a regular file: "{file_path}"')
		
		with open(target_file, "r") as file_obj:
			contents = file_obj.read(MAX_CHARS)
			if file_obj.read(1):
				contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

		return contents
	
	except Exception as e:
		return f"Error: {e}"
		


if __name__ == "__main__":
	
	print(f"\n*** {sys.argv[0]} running as __main__")
	print(f'*** Arguments: working_dir="{sys.argv[1]}" target_file="{sys.argv[2]}"\n')

	print(f"Result for file:")
	print(f"{get_file_content(sys.argv[1], sys.argv[2])}\n")