def read_file(): 
    with open("./DataFiles/data.txt", "r", encoding='utf-8') as f:
        words = [word.rstrip("\n") for word in f]
    
    print(words)

###read_file()