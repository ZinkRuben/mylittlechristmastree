from time import sleep
teststring = "test"
morse_dictionary = {"a" : "01",
                    "b" : "1000",
                    "c" : "1010",
                    "d" : "100",
                    "e" : "0",
                    "f" : "0010",
                    "g" : "110",
                    "h" : "0000",
                    "j" : "0111",
                    "k" : "101",
                    "l" : "0100",
                    "m" : "11",
                    "n" : "10",
                    "o" : "111",
                    "p" : "0110",
                    "q" : "1101",
                    "r" : "101",
                    "s" : "000",
                    "t" : "1",
                    "u" : "001",
                    "v" : "0001",
                    "w" : "011",
                    "x" : "1001",
                    "y" : "1011",
                    "z" : "1100",
                    " " : "space"
                    }
tree.color='white'
try:
    for character in teststring:
        bits = morse_dictionary[character]
        for bit in bits:
            if bit == "1":
                #print("hosszu")
                tree.color = Color('red')
                sleep(1)
                tree.color = Color('white')
            elif bit == "0":
                #print("rovid")
                tree.color = Color('red')
                sleep(3)
                tree.color = Color('white')
            else:
                print("gond")
            sleep(1)
except KeyboardInterrupt:
    tree.close()
