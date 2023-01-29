import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')
print(pattern)

# Sara doesn't have anything in C\Users\saesb so we are forcing the path for her :)
if "saesb" in pattern:
    pattern = sara_pattern = "D:\Code\sky\coding\homework\week2\Wk2_Exercise9and10\Exercise9\*"

# TODO: Use the glob.glob() function to obtain the list of filenames
print("\nTask 5")
# Python doc: glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)
filenames = glob.glob(pattern)  # this outputs a list with the FULL PATH of files in the pattern
print(f'List of file paths using glob.glob(pattern): {filenames}')
print(f'Type of output: {type(filenames)}')

# TODO: use os.path.getsize to find each file's size
print("\nTask 6")
for file in filenames:  # looping through all file paths of the paths list
    # print(file)  ## uncomment to check each file in filename
    # print(type(file))  ## uncomment to check the type of each file in filename
    size = os.path.getsize(file)  # Returns the size of the file, in bytes
    print(f'size {size} - file name: {file}')

# TODO: Add a test to only display files that are not zero length
print("\nTask 7")
for file in filenames:  # looping through all file paths of the paths list
    size = os.path.getsize(file)  # Return the size, in bytes
    if size != 0:  # Checks if the size of the file is not zero, so it prints it
        print(f'size {size} - file name: {file}')
    else:  # it's redundant as if it doesn't meet the if statement it will jump onto next file
        continue

# TODO: Remove the leading directory name(s) from each filename before you print it - 
print("\nTask 8")
for file in filenames:  # looping through all file paths of the paths list
    # os.path.basename(file_path_string) returns a string with the file name (without the whole path!)
    print(f'Print file name using os.path.basename(file): {os.path.basename(file)}')
