import os
import pathlib

TARGET_EXPAND = '.swift'

def main():
    # TODO: 動的に
    path = '/Users/tokizo/prg/sw/Pendula/Pendula'

    p = pathlib.Path(path)
    
    inherited_class_names = set()
    class_names = []

    file_paths = p.glob('**/*')
    for f in file_paths:
        file_path = str(f)

        if not os.path.isfile(file_path) or not isSameExpand(expand=TARGET_EXPAND, file_path=file_path):
            continue
        
        for line in  open(file_path, 'r'):
            words = line.split()

            if len(words) == 0 or words[0] != 'class':
                continue

            class_names.append(words[1][:-1])
            [inherited_class_names.add(i) for i in extract_inherited_class_names(words)]


# TODO: 命名がおかしい sameであるなら比較対象はどちらも同じ型であるべき？
def isSameExpand(expand: str, file_path: str) -> bool:
    return expand == file_path[-len(expand):]

def extract_inherited_class_names(line: str) -> [str]:
    return line[2:-1]

main()