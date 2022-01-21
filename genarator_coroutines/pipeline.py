# processing pipe : tail -f | grep python

import follow
def grep(pattrn, lines):
    for line in lines:
        if pattrn in line:
            yield line
if __name__=="__main__":
    logfile = open('log.txt')
    loglines = follow.follow(logfile)
    pylines = grep("python",loglines)

    for line in pylines:
        print(line)