def modify_and_write_file(input_filename, output_filename):
  
  try:
    with open(input_filename, 'r') as infile:
      data = infile.read()

    # Modify the data
    modified_data = data.upper() 

    with open(output_filename, 'w') as outfile:
      outfile.write(modified_data)

    print(f"File '{input_filename}' modified and saved as '{output_filename}'.")

  except FileNotFoundError:
    print(f"Error: Input file '{input_filename}' not found.")
  except PermissionError:
    print(f"Error: Permission denied while reading '{input_filename}'.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Get input filename from the user
input_filename = input("Enter the name of the input file: ")

# Create output filename (e.g., add "_modified" to the original name)
output_filename = input_filename + "_modified.txt"

# Call the function to process the file
modify_and_write_file(input_filename, output_filename)