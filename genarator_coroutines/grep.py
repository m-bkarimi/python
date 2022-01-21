# Coroutines
# call generator with parametr..
def grep(pattrn):
    while True:
        print('ok')
        line = yield
        if pattrn in line:
            print(line)
g = grep("python")
next(g, 'default') # must be call befor call send method...
g.send("python Yeah, but no, but yeah, but no")