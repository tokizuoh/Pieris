# Pieris
Extracts the names of classes that are not inherited but are not given 'final'.
  
## Usage

```bash
> python -V
Python 3.8.5
  
# args[1]: Xcode project path
> python main.py /Users/tokizo/prg/sw/Pendula/Pendula
[Warning] Not inherited but not given final qualifier.
/Users/tokizo/prg/sw/Pendula/Pendula/AppDelegate.swift
/Users/tokizo/prg/sw/Pendula/Pendula/SceneDelegate.swift
/Users/tokizo/prg/sw/Pendula/Pendula/View/Common/ComponentBaseViewController.swift
  
# If the input is incorrect, an error will be output.
> python main.py /Users/tokizo/prg/sw/Pendula/Pendul
ERROR: Please input Project Directory Path
```