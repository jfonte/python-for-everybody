
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()

# this works because the fn definitions don't alter flow of execution
# making definitions readily available everywhere EXCEPT if called 
# on before something is defined