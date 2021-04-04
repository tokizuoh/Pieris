import os
import pathlib

TARGET_EXPAND = '.swift'

def main():
    # TODO: 動的に
    path = '/Users/tokizo/prg/sw/Pendula/Pendula'

    p = pathlib.Path(path)
    for f in p.glob('**/*'):
        file_path = str(f)

        if not os.path.isfile(file_path) or not isSameExpand(expand=TARGET_EXPAND, file_path=file_path):
            continue
        print(file_path)
        
        # TODO: ファイル内検索
        # with open(file_path, 'r') as file:
            # print(file)
            # exit()

# TODO: 命名がおかしい sameであるなら比較対象はどちらも同じ型であるべき？
def isSameExpand(expand: str, file_path: str) -> bool:
    return expand == file_path[-len(expand):]

main()