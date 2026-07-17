import os
import hashlib

def calculate_256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for b_block in iter(lambda: f.read(4096), b""):
                sha256.update(b_block)
        return sha256.hexdigest()
    except (PermissionError, FileNotFoundError):
        return None


def scan_directory(target_folder):
    file_paths = []
    hashes = []

    print(f"--- Scanning directory: {target_folder} ---\n")
    for root_dir, _, filenames in os.walk(target_folder):
        for filename in filenames:
            full_path = os.path.join(root_dir, filename)
            file_hash = calculate_256(full_path)
            if file_hash:
                file_paths.append(full_path)
                hashes.append(file_hash)
    already_deleted = set()
    for i in range(len(hashes)):
        if i in already_deleted:
            continue
        for j in range(i + 1, len(hashes)):
            if j in already_deleted:
                continue
            if hashes[i] == hashes[j]:
                print(f"[!] Duplicate found!")
                print(f"   Original: {file_paths[i]}")
                print(f"   Duplicate: {file_paths[j]}\n")
                already_deleted.add(j)

if __name__ == "__main__":
    test_path = str(input("Enter the folder's path, both absolute and relative paths work: "))
    if os.path.exists(test_path) and os.path.isdir(test_path):
        scan_directory(test_path)
    else:
        print(f"Error: The path '{test_path}' does not exist.")