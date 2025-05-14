def main():
    print("Phase 1: Create a list of files to add.")
    file_list = []

    while True:
        filename = input("Enter the filename to add (or type 'done' to finish adding files): ").strip()
        if filename.lower() == 'done':
            if not file_list:
                print("No files added yet. Please add at least one file.")
                continue
            else:
                break
        # Accept file names without checking for existence at this stage
        if filename not in file_list:
            file_list.append(filename)
            print(f"Added '{filename}'.")
        else:
            print(f"'{filename}' is already in the file list.")

    print("\nPhase 2: Select a file from the list to read and process.")
    while True:
        print("\nFiles available:")
        for idx, fname in enumerate(file_list, 1):
            print(f"{idx}. {fname}")

        choice = input("Enter the number or name of the file to read (or type 'exit' to quit): ").strip()

        if choice.lower() == 'exit':
            print("Exiting the program.")
            break

        selected_file = None
        if choice.isdigit():
            index = int(choice)
            if 1 <= index <= len(file_list):
                selected_file = file_list[index - 1]
            else:
                print("Invalid file number. Please try again.")
                continue
        else:
            if choice in file_list:
                selected_file = choice
            else:
                print("File not found in the list. Please try again.")
                continue

        try:
            with open(selected_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: The file '{selected_file}' does not exist.")
            continue
        except IOError:
            print(f"Error: Could not read the file '{selected_file}'.")
            continue

        # Modify content: convert to uppercase as an example
        modified_content = content.upper()

        new_filename = selected_file.rsplit('.', 1)
        if len(new_filename) == 2:
            new_filename = f"{new_filename[0]}_modified.{new_filename[1]}"
        else:
            new_filename = f"{selected_file}_modified"

        try:
            with open(new_filename, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"Modified content written to '{new_filename}'.")
        except IOError:
            print(f"Error: Could not write to file '{new_filename}'.")

if __name__ == "__main__":
    main()


