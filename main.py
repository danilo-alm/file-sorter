import filetype
import os
import argparse


def main():
    # Path with files to be sorted
    path = '/storage/emulated/0/Download/'

    # Creating all directories
    for folder in folders.keys():
        full_path = os.path.join(path, folder)
        folders[folder] = full_path
        if not os.path.exists(full_path):
            os.mkdir(full_path)
    
    files = get_files(path)

    for file in files:
        kind = filetype.guess(file)
        decide_and_move_file(file, kind)


def get_files(path):
    files = [os.path.join(path, i) for i in os.listdir(path)]
    return [i for i in files if os.path.isfile(i)]


def get_destination_path(filename, kind):
    if kind is None:
        return os.path.join(folders['Other'], filename)
    
    ftype = kind.mime.split('/')
    
    # Matching the top-level media type
    match ftype[0]:
        case 'image':
            destination = os.path.join(folders['Pictures'], filename)

        case 'video':
            destination = os.path.join(folders['Videos'], filename)
        
        case 'audio':
            destination = os.path.join(folders['Audio'], filename)
        
        case 'application':
            # Checking the subtype
            if ftype[1] in archives_subtypes:
                destination = os.path.join(folders['Archives'], filename)
            elif ftype[1] in documents_subtypes:
                destination = os.path.join(folders['Documents'], filename)
            elif ftype[1] in fonts_subtypes:
                destination = os.path.join(folders['Fonts'], filename)
        
        case _:
            return
        
    return destination


def rename_if_exists(path):
    count = 1
    filename, extension = os.path.splitext(path)
    new_path = path
    
    while os.path.exists(new_path):
        new_filename = f"{filename}({count})"
        new_path = f"{new_filename}{extension}"
        count += 1

    return new_path


def decide_and_move_file(file_path, kind):
    filename = os.path.split(file_path)[-1]
    destination = get_destination_path(filename, kind)
    destination = rename_if_exists(destination)
    os.rename(file_path, destination)

    if args.verbose:
        print(f'File {filename} moved to {destination}')


# Folder names and their full paths (populated in main)
folders = {
    'Documents': None,
    'Pictures': None,
    'Videos': None,
    'Archives': None,
    'Audio': None,
    'Fonts': None,
    'Other': None
}

# The top-level media type 'application' has many subtypes, and each
# one should be moved to a different directory. The subtypes possibilities
# are going to be stored in lists namedc after the directories they belong

archives_subtypes = ['x-brotli', 'x-rpm', 'dicom', 'epub+zip', 'zip', 'x-tar',
                     'x-rar-compressed', 'gzip', 'x-bzip2', 'x-7z-compressed',
                     'x-xz', 'pdf', 'x-msdownload', 'x-shockwave-flash', 'rtf',
                     'octet-stream', 'postscript', 'x-sqlite3', 'x-nintendo-nes-rom',
                     'x-google-chrome-extension', 'vnd.ms-cab-compressed', 'x-deb',
                     'x-unix-archive', 'x-compress', 'x-lzop', 'x-lzip', 'x-lz4', 'zstd']

documents_subtypes = ['msword', 'vnd.openxmlformats-officedocument.wordprocessingml.document',
                      'vnd.oasis.opendocument.text', 'vnd.ms-excel',
                      'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                      'vnd.oasis.opendocument.spreadsheet', 'vnd.ms-powerpoint',
                      'vnd.openxmlformats-officedocument.presentationml.presentation',
                      'vnd.oasis.opendocument.presentation']

fonts_subtypes = ['font-woff', 'font-woff', 'font-sfnt', 'font-sfnt']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='Verbose', action='store_true')
    args = parser.parse_args()

    main()