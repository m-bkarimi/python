# A Python version of Unix 'tail -f'
import time
def follow(file:str) -> str:
    file.seek(0,2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(.02)
            continue
        yield line


fp = open('log.txt')

for line in follow(fp):
    print(line)