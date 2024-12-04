## Lab Instructions

### Objective

Write a script that organizes files in a directory based on their file extensions (e.g., .txt, .jpg) into respective folders.


### Pre-task

Create some files with different file extensions in the target directory. For example:
- test.jpg
- test.txt
- test.exe

### Steps

1. **Create a new Python script**:

   - Open your code editor and create a new Python file named `organize_files.py`.

2. **Import necessary modules**:

   - Use the `os` and `shutil` modules to interact with the file system.

3. **Define the main function**:

   - Create a function `organize_files(directory)` that takes a directory path as an argument.

4. **List all files in the directory**:

   - Use `os.listdir(directory)` to get a list of all files in the specified directory.

5. **Organize files by extension**:

   - Loop through the list of files.
   - For each file, determine its extension using `os.path.splitext(file)[1]`.
   - Create a new directory for each extension if it doesn't already exist.
   - Move the file to the corresponding directory using `shutil.move`.

6. **Test your script**:
   - Run your script with a test directory containing various files.
   - Verify that files are correctly organized into folders based on their extensions.

### Example Code

```python
import os
import shutil

def organize_files(directory):
	 for filename in os.listdir(directory):
			if os.path.isfile(os.path.join(directory, filename)):
				file_extension = os.path.splitext(filename)[1][1:]  # Get the file extension
				if file_extension:  # Skip files without an extension
					 dest_dir = os.path.join(directory, file_extension)
					 if not os.path.exists(dest_dir):
							os.makedirs(dest_dir)
					 shutil.move(os.path.join(directory, filename), os.path.join(dest_dir, filename))

if __name__ == "__main__":
	 organize_files("/path/to/your/directory")
```

### Extensions for the Lab (Optional)


#### 1. **Add a Dry-Run Mode**
Before actually moving files, provide an option to print the changes that would be made. This is useful for reviewing the changes without executing them.

**Implementation:**
- Add a `dry_run` argument to `organize_files`.
- Print planned moves instead of executing them when `dry_run=True`.

```python
def organize_files(directory, dry_run=False):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1][1:]
            if file_extension:
                dest_dir = os.path.join(directory, file_extension)
                if dry_run:
                    print(f"Would move: {filename} -> {dest_dir}")
                else:
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    shutil.move(os.path.join(directory, filename), os.path.join(dest_dir, filename))
```

---

#### 2. **Handle Nested Directories**
Extend the script to traverse nested directories recursively and organize files in subdirectories.

**Implementation:**
- Use `os.walk` instead of `os.listdir`.

```python
def organize_files(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            file_extension = os.path.splitext(filename)[1][1:]
            if file_extension:
                dest_dir = os.path.join(directory, file_extension)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(os.path.join(root, filename), os.path.join(dest_dir, filename))
```

---

#### 3. **Generate a Report**
Create a summary report after organizing files, showing how many files were moved for each extension.

**Implementation:**
- Use a dictionary to count files by extension.
- Write the summary to a text file.

```python
def organize_files(directory):
    report = {}
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1][1:]
            if file_extension:
                dest_dir = os.path.join(directory, file_extension)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(os.path.join(directory, filename), os.path.join(dest_dir, filename))
                report[file_extension] = report.get(file_extension, 0) + 1
    with open(os.path.join(directory, "report.txt"), "w") as report_file:
        for ext, count in report.items():
            report_file.write(f"{ext}: {count} files\n")
```

---

#### 4. **Ignore Certain Extensions**
Add a feature to exclude specific file extensions from being moved (e.g., `.log`, `.tmp`).

**Implementation:**
- Use a list of ignored extensions and skip them during processing.

```python
def organize_files(directory, ignore_extensions=None):
    if ignore_extensions is None:
        ignore_extensions = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1][1:]
            if file_extension and file_extension not in ignore_extensions:
                dest_dir = os.path.join(directory, file_extension)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(os.path.join(directory, filename), os.path.join(dest_dir, filename))
```

---

#### 5. **Organize by File Size**
Instead of organizing by extensions, classify files into size-based folders (e.g., Small, Medium, Large).

**Implementation:**
- Define size thresholds (e.g., Small: <1MB, Medium: 1-10MB, Large: >10MB).

```python
def organize_by_size(directory):
    size_categories = {
        "Small": lambda size: size < 1 * 1024 * 1024,
        "Medium": lambda size: 1 * 1024 * 1024 <= size <= 10 * 1024 * 1024,
        "Large": lambda size: size > 10 * 1024 * 1024
    }
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)
            for category, condition in size_categories.items():
                if condition(file_size):
                    dest_dir = os.path.join(directory, category)
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    shutil.move(filepath, os.path.join(dest_dir, filename))
                    break
```

---

#### 6. **Add Undo Capability**
Keep track of original file locations in a separate log file and provide a script to reverse the changes.

**Implementation:**
- Save original paths in a JSON file before moving files.
- Create a script to restore files to their original locations.

---

#### 7. **CLI Interface**
Enhance the script with a command-line interface using `argparse`, allowing users to specify the directory, dry-run mode, ignored extensions, etc.

```python
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a directory by extension.")
    parser.add_argument("directory", help="The directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")
    parser.add_argument("--ignore", nargs="*", default=[], help="List of extensions to ignore")
    args = parser.parse_args()

    organize_files(args.directory, dry_run=args.dry_run, ignore_extensions=args.ignore)
```

