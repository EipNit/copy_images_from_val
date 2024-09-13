# Image Copier for Validation Dataset

This script copies image files listed in a `val.txt` file to a target directory for validation purposes. It ensures that only the images existing in the source directory are copied to the target directory, while logging any missing images.

## Features

- Automatically reads image names from `val.txt`.
- Copies images from a specified source folder to a target folder.
- Checks if the images exist in the source directory.
- Logs the images that were successfully copied and warns about missing files.

## Requirements

- Python 3.x
- Ensure the following Python standard libraries are installed:
  - `os`
  - `shutil`

## Directory Structure

Make sure your project folder is structured as follows:

```
project_folder/
│
├── data_mouse_labels/
│   ├── images/           # Folder containing the image files
│   └── val.txt           # Text file containing the list of image filenames
├── detecttest/            # The target folder where images will be copied
└── script.py              # Your Python script (name it appropriately)
```

## Usage

1. Clone the repository or download the script.
2. Ensure your project structure matches the above.
3. Place the images you want to validate into the `data_mouse_labels/images` directory.
4. Add the image filenames (one per line) in the `data_mouse_labels/val.txt` file.
5. Run the script.

### Running the Script

To execute the script, use the following command in your terminal or command line:

```bash
python script.py
```

The script will:

- Read the image filenames from `val.txt`.
- Copy the existing images from `data_mouse_labels/images` to the `detecttest` folder.
- Print out the log of copied files and any missing ones.

### Example `val.txt`

Your `val.txt` file should contain the image names, one per line, like this:

```
image1.jpg
image2.png
image3.bmp
```

## Notes

- The target directory `detecttest` will be created automatically if it does not exist.
- Ensure the image names in `val.txt` exactly match the names in the `images` folder (case-sensitive, no extra spaces).
- The script will skip any images that are not found in the source directory and print a warning.
