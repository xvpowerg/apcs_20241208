poem = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉'''

file = open("output.txt","x")
file.write(poem)
file.flush()
file.close()
