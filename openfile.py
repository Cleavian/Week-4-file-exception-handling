def process_file():
    # Ask the user for a filename
    filename = "studentrecord.txt"  # Predefined filename

    try:
        # Open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        output_filename = "modified_" + filename
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)

        print(f"Success! Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read or write the file. Check permissions.")

# Run the function
process_file()