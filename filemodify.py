
# This function reads content from an input file, modifies it, and writes the modified version to a new file
def modify_and_save_file(input_filename, output_filename):
    try:
        # Open the input file in read mode and read its content
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read everything from the file
            
        # Modify the content (converting all text to uppercase in this example)
        modified_content = content.upper()  # You can change this modification as needed
        
        # Write the modified content to a new output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)  # Save the changes to a new file
        
        print(f"Modified content has been saved to {output_filename}")  # Notify the user
    
    except FileNotFoundError:
        # If the input file doesn't exist, inform the user
        print(f"Error: The file {input_filename} does not exist.")
    
    except IOError:
        # Handle other IO-related errors like permission issues
        print("Error: There was an issue with reading or writing the file.")

# This function prompts the user for a filename and attempts to read its content while handling errors
def read_file_with_error_handling():
    filename = input("Please enter the filename: ")  # Ask the user for a file name
    
    try:
        # Try opening the file and reading its content
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
        print("File content successfully read:")  # Inform the user the file was read successfully
        print(content)  # Display the content of the file
    
    except FileNotFoundError:
        # If the file is not found, show a user-friendly message
        print(f"Error: The file {filename} does not exist.")
    
    except IOError:
        # Catch other IO errors, like permission issues
        print("Error: There was an issue reading the file.")

# Example usage

# Modify the content of an existing file and save the new content to another file
input_file = "example.txt"  # Replace with your actual file
output_file = "modified_example.txt"  # This is the file where the modified content will be saved
modify_and_save_file(input_file, output_file)  # Call the function to modify and save the file

# Ask the user for a filename and try to read it
read_file_with_error_handling()  # Call the function to handle file reading and error checking
