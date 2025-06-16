import os

def list_directory_contents(path):
    try:
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
directory_path = input("Enter the path of the directory: ")
list_directory_contents(directory_path)
