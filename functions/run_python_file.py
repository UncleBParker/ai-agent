# run_python_file.py

import os
import subprocess
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=f"Run a specified python (.py) file in a specified directory relative to the working directory with any specified arguments, returning any non-zero exit code, any stdout, and any stderr.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
					"Directory path of the target python file, relative to the working directory (providing only a file name will search for a file of that name in the working directory)."
				),
            ),
			"args": types.Schema(
                type=types.Type.ARRAY, 
				items=types.Schema(type=types.Type.STRING), 
				description=(
					"An array of strings representing the arguments to be passed to the target python file at runtime (Default is None)."
				),
            )
        },
		required=["file_path"]
    ),
)


def run_python_file(working_directory, file_path, args=None):
	try:
		working_dir_abs = os.path.abspath(working_directory)

		target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

		if os.path.commonpath([working_dir_abs, target_file_path]) != working_dir_abs:
			raise Exception(f'Cannot execute "{file_path}" as it is outside the permitted working directory')

		if not os.path.isfile(target_file_path):
			raise Exception(f'"{file_path}" does not exist or is not a regular file')
		
		if not target_file_path.endswith(".py"):
			raise Exception(f'"{file_path}" is not a Python file')
		
		command = ["python", target_file_path]

		if args != None:
			command.extend(args)
		
		CompletedProcess = subprocess.run(command, capture_output=True, text=True, timeout=30)

		return_code = CompletedProcess.returncode
		stdout = CompletedProcess.stdout
		stderr = CompletedProcess.stderr

		output_parts = []

		if return_code != 0:
			output_parts.append(f'Process exited with code {return_code}')
		
		if stdout:
			output_parts.append(f'STDOUT: {stdout}')
		elif stderr:
			output_parts.append(f'STDERR: {stderr}')
		else:
			output_parts.append(f'No output produced')
		
		return "\n".join(output_parts)


	except Exception as e:
		return f"Error: executing Python file: {e}"