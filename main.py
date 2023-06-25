import filetype
import os

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
        move_file(file, kind)


def get_files(path):
    files = [os.path.join(path, i) for i in os.listdir(path)]
    return [i for i in files if os.path.isfile(i)]


def move_file(filepath, kind):
    filename = os.path.split(filepath)[-1]
    if kind is None:
        new_path = os.path.join(folders['Other'], filename)
        os.rename(filepath, new_path)
        return
    
    ftype = kind.mime.split('/')
    
    match ftype[0]:
        case 'image':
            new_path = os.path.join(folders['Pictures'], filename)

        case 'video':
            new_path = os.path.join(folders['Videos'], filename)
        
        case 'audio':
            new_path = os.path.join(folders['Audio'], filename)
        
        case 'application':
            if ftype[1] in archives:
                new_path = os.path.join(folders['Archives'], filename)
            elif ftype[1] in documents:
                new_path = os.path.join(folders['Documents'], filename)
            elif ftype[1] in fonts:
                new_path = os.path.join(folders['Fonts'], filename)
        
        case _:
            return
    
    os.rename(filepath, new_path)
    print(f'File {filename} moved to {new_path}')


folders = {
    'Documents': None,
    'Pictures': None,
    'Videos': None,
    'Archives': None,
    'Audio': None,
    'Fonts': None,
    'Other': None
}

archives = ['x-brotli', 'x-rpm', 'dicom', 'epub+zip', 'zip', 'x-tar',
            'x-rar-compressed', 'gzip', 'x-bzip2', 'x-7z-compressed',
            'x-xz', 'pdf', 'x-msdownload', 'x-shockwave-flash', 'rtf',
            'octet-stream', 'postscript', 'x-sqlite3', 'x-nintendo-nes-rom',
            'x-google-chrome-extension', 'vnd.ms-cab-compressed', 'x-deb',
            'x-unix-archive', 'x-compress', 'x-lzop', 'x-lzip', 'x-lz4', 'zstd']

documents = ['msword', 'vnd.openxmlformats-officedocument.wordprocessingml.document',
             'vnd.oasis.opendocument.text', 'vnd.ms-excel',
             'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
             'vnd.oasis.opendocument.spreadsheet', 'vnd.ms-powerpoint',
             'vnd.openxmlformats-officedocument.presentationml.presentation',
             'vnd.oasis.opendocument.presentation']

fonts = ['font-woff', 'font-woff', 'font-sfnt', 'font-sfnt']

if __name__ == '__main__':
    main()