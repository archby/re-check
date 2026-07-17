import os

def scan_directory(target_folder):
    print(f"Scanning directory: {target_folder}\n")
    for root_dir, subfolders, filenames in os.walk(target_folder):
        for filename in filenames:
            full_path = os.path.join(root_dir, filename)
            print(f"Found file: {full_path}")


if __name__ == "__main__":
    test_path = "./testfolder"
    if os.path.exists(test_path):
        scan_directory(test_path)
    else:
        print(f"Error: The path '{test_path}' does not exist. Please create it or update the script.")