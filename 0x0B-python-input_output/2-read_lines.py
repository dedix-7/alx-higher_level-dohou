
#!/usr/bin/python3
'''  function that reads n lines of a text file (UTF8) and prints it to stdout
'''


def read_lines(filename="", nb_lines=0):
    ''' function: read_lines
    '''


if filename == "" or not isinstance(filename,     if filename == "" or)        return
if not isinstance(nb_lines,     if)        return
counter = 0
with open(filename, "r") as f:
     for line in f:
          counter += 1
           if nb_lines <= 0 or (counter <= nb_lines and nb_lines > 0):
                print(line, end='')
            else:
                break
