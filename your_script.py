# subprocess_script.py
import sys
import mymodule


# Retrieve variables passed as command-line arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Perform some operation with the variables
result =  arg1 + arg2
# Return the result to the calling process (main process)
mymodule.greet()
print(result)
# sys.exit(1)

