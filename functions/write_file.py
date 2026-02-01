# functions/write files.py

import os
import sys
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Write a specified string to a specified file at a specified directory relative to the working directory. Create the specified file and parent directories if they do not exist, and overwrite the entire contents of the specified file if it does already exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
					"Directory path of the target file, relative to the working directory (providing only a file name will search for a file of that name in the working directory)."
				),
            ),
			"content": types.Schema(
                type=types.Type.STRING, 
				description=(
					"A string that will be written to the target file."
				),
            )
        },
		required=["file_path", "content"]
    ),
)


def write_file(working_directory, file_path, content):
	try:
		working_dir_abs = os.path.abspath(working_directory)
		target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

		if not os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs:
			raise Exception(f'Cannot write to "{file_path}" as it is outside the permitted working directory')
		
		if os.path.isdir(target_file):
			raise Exception(f'Cannot write to "{file_path}" as it is a directory')
		
		os.makedirs(os.path.dirname(target_file), exist_ok=True)

		with open(target_file, "w") as file_obj:
			file_obj.write(content)

		return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
	
	except Exception as e:
		return f"Error: {e}"
		


if __name__ == "__main__":
	
	print(f"\n*** {sys.argv[0]} running as __main__")
	print(f'*** Arguments: working_dir="{sys.argv[1]}" file_path="{sys.argv[2]}" content="{sys.argv[3]}"\n')

	print(f"Result for file:")
	print(f"{write_file(sys.argv[1], sys.argv[2], sys.argv[3])}\n")