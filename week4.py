# File: week4.py
def modify_text(text):

    # converts to uppercase.
    return text.upper()


def read_file(filename):
  
    try:
        # Open the file in read mode.
        with open(filename, 'r') as file:
            content = file.read()  # Read entire content of the file.
            print(f"Successfully read file: {filename}")
            return content
    except FileNotFoundError as fnf_error:
        # Handle error if file does not exist.
        print(f"Error: The file '{filename}' was not found.")
        raise fnf_error
    except IOError as io_error:
        # Handle other I/O errors.
        print(f"Error: Unable to read the file '{filename}'.")
        raise io_error


def write_file(filename, content):
   
    try:
        # Open the file in write mode which creates the file if it doesn't exist.
        with open(filename, 'w') as file:
            file.write(content)  # Write modified content to the file.
            print(f"Successfully wrote modified content to file: {filename}")
    except IOError as io_error:
        # Handle errors related to writing the file.
        print(f"Error: Unable to write to the file '{filename}'.")
        raise io_error


def main():
    print("Lets manipulate files now, hehe")
    # Prompt the source file name.
    source_filename = input("what is the name of the fie you want to read? ")
    
    # Attempt to read from the specified source file.
    try:
        original_content = read_file(source_filename)
    except Exception as read_error:
        # If reading fails, exit the program.
        print("Exiting program due to the above error during file reading.")
        return

    # Modify the content using the modify_text function.
    modified_content = modify_text(original_content)
    
    # Prompt user for the destination filename.
    destination_filename = input("Enter the destination filename to write the modified content: ")
    
    # Attempt to write the modified content to the destination file.
    try:
        write_file(destination_filename, modified_content)
    except Exception as write_error:
        # If writing fails, exit the program.
        print("Exiting program due to the above error during file writing.")
        return

    print("File processing completed successfully!")


if __name__ == "__main__":
    # Ensure that main() is called when the script is executed.
    main()
