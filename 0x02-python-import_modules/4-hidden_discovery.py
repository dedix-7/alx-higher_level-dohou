#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as crackfile
    hidden_names = dir(crackfile)
    for i in hidden_names:
        # print(i)
        if i[:2] != "__":
            print(i)
