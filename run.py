 
import subprocess  
  
def run_subprocess(command):
    try:
        # Create a subprocess, capture output, and use input if provided
        process = subprocess.Popen(
            command ,  # Append parameters to the command
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Merge stdout and stderr
            stdin=subprocess.PIPE,
            text=True
        )

        # # Provide input data to the subprocess, if available
        # if input_data is not None:
        #     process.stdin.write(input_data)
        #     process.stdin.close()

        # Capture and print the combined output (stdout + stderr)
        for line in process.stdout:
            print(line, end='') # too add (\n)if is a question! 

        # Wait for the subprocess to complete
        process.wait()

        # Check the return code and raise an exception if it's non-zero
        if process.returncode == 0:
            return True
        else:
            error_message = f"Subprocess returned non-zero exit status {process.returncode}\n"
            error_message += "Combined Output (stdout + stderr):\n"
            error_message += process.stdout.read()
            raise subprocess.CalledProcessError(
                returncode=process.returncode,
                cmd=command,
                output=error_message,
                stderr=""
            )

    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}")
    except Exception as e:
        print(f"Error running the subprocess: {e}")

# Example usage:
 
# result =run_subprocess(["python", "your_script.py",'1','2'])
result =run_subprocess(f'python your_script.py 1 2')
print(123,result)

# import subprocess

# def run_subprocess(command, parameters):
#     try:
#         # Create a subprocess, capture output, and use input if provided
#         process = subprocess.Popen(
#             command + parameters,  # Append parameters to the command
#             stdout=subprocess.PIPE,
#             stderr=subprocess.STDOUT,  # Merge stdout and stderr
#             stdin=subprocess.PIPE,
#             text=True
#         )

#         # # Provide input data to the subprocess, if available
#         # if input_data is not None:
#         #     process.stdin.write(input_data)
#         #     process.stdin.close()

#         # Capture and print the combined output (stdout + stderr)
#         for line in process.stdout:
#             print(line, end='\n')

#         # Wait for the subprocess to complete
#         process.wait()

#         # Check the return code and raise an exception if it's non-zero
#         if process.returncode != 0:
#             error_message = f"Subprocess returned non-zero exit status {process.returncode}\n"
#             error_message += "Combined Output (stdout + stderr):\n"
#             error_message += process.stdout.read()
#             raise subprocess.CalledProcessError(
#                 returncode=process.returncode,
#                 cmd=command,
#                 output=error_message,
#                 stderr=""
#             )

#     except subprocess.CalledProcessError as e:
#         print(f"Subprocess error: {e}")
#     except Exception as e:
#         print(f"Error running the subprocess: {e}")

# # Example usage:
# command = ["python", "your_script.py"]
# input_data = "input_data_to_be_passed_to_subprocess"
# parameters = ['12', '24', '48']
# result =run_subprocess(command,parameters)
# print(123,result)
