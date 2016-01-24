from pcapng import FileScanner

with open('4.pacpng') as fp:
    scanner = FileScanner(fp)
    for block in scanner:
        pass  # do something with the block...