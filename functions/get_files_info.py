# functions/get_files_info.py

import os
import sys
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description=(
					"Directory path to list files from, relative to the working directory (default is 'the working directory itself' literally '.')"
				),
            ),
        },
    ),
)


def get_files_info(working_directory, directory="."):
	try:
		working_dir_abs = os.path.abspath(working_directory)
		target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

		if not os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
			raise Exception(f'Cannot list "{directory}" as it is outside the permitted working directory')
		
		if not os.path.isdir(os.path.normpath(target_dir)):
			raise Exception(f'"{directory}" is not a directory')
		
		dir_contents = os.scandir(target_dir)

		result = "\n".join((f"- {obj.name}: file_size={obj.stat().st_size} bytes, is_dir={obj.is_dir()}") for obj in dir_contents)

		return result
	
	except Exception as e:
		return f"Error: {e}"
		


if __name__ == "__main__":
	
	print(f"\n*** {sys.argv[0]} running as __main__")
	print(f'*** Arguments: working_dir="{sys.argv[1]}" target_dir="{sys.argv[2]}"\n')

	print(f"Result for directory:")
	print(f"{get_files_info(sys.argv[1], sys.argv[2])}\n")