# Coroutines
# call generator with parametr..
def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        next(cr, 'default') # must be call befor call send method...
        return cr
    return start
@coroutine
def grep(pattrn):
    while True:
        line = yield
        if pattrn in line:
            print(line)
g = grep("python")
#next(g, 'default') # must be call befor call send method...
g.send("python Yeah, but no, but yeah, but no")