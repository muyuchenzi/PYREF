def read_file():
    with open(r'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Basic\data\致橡树.txt',
              'r', encoding='utf-8') as f:
        while True:
            txt_line = f.readline()
            if not txt_line:
                break
            yield txt_line


file_res = read_file()
for line in file_res:
    print(line)

