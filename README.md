# File Sorter

This is a Python script that sorts files in a specified directory by their file type. It uses the `filetype` library to guess the file type and then moves the file to the appropriate directory based on its type.

## Usage

1. Clone or download the project files to your local machine.

2. Install the requirements by running the following command:

```
pip -r requirements.txt
```

3. Run the script:

```
python main.py [-v/--verbose]
```

Optional argument:
- `-v/--verbose`: Enables verbose output, which displays information about the files being moved.

## Default Directory Names

The script organizes files into several default directories based on their types. The following directories are provided by default:

- Documents
- Pictures
- Videos
- Archives
- Audio
- Fonts
- Other

These directories are automatically created by the script if they do not already exist. You can modify the directory names and their corresponding paths directly in the script if desired.
