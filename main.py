import os
import pathlib

TARGET_EXPAND = '.swift'


class ClassFile:

    name: str
    path: str

    def __init__(self, name, path):
        self.name = name
        self.path = path


def main():
    # TODO: 動的に
    path = '/Users/tokizo/prg/sw/Pendula/Pendula'

    p = pathlib.Path(path)
    inherited_class_names = set()
    class_files: [ClassFile] = []

    file_paths = p.glob('**/*')
    for f in file_paths:
        file_path = str(f)

        if not os.path.isfile(file_path) or not has_expand(expand=TARGET_EXPAND, file_path=file_path):
            continue
        
        for line in  open(file_path, 'r'):
            words = line.split()

            if len(words) == 0 or words[0] != 'class':
                continue

            class_files.append(ClassFile(name=words[1][:-1], path=file_path))
            [inherited_class_names.add(i) for i in extract_inherited_class_names(words)]

    not_inherited_class_files = [class_name for class_name in class_files if class_name not in inherited_class_names]


def has_expand(expand: str, file_path: str) -> bool:
    return expand == file_path[-len(expand):]


def extract_inherited_class_names(line: str) -> [str]:
    return line[2:-1]


main()