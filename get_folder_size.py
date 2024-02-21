import os

def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.islink(file_path):  # Skip symbolic links
                total_size += os.path.getsize(file_path)
    return total_size / (1024**3)  # Convert bytes to gigabytes

def main():
    folder_path = r"..."
    folder_size_gb = get_folder_size(folder_path)
    print(f"The total size of the folder '{folder_path}' is {folder_size_gb:.2f} GB")

if __name__ == "__main__":
    main()
