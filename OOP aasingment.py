def read_and_modify_file():
    input_filename = input("Please enter the filename to read: ")
    output_filename = "modified_" + input_filename

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Modify the content (convert to uppercase)

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()
