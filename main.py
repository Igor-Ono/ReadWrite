# Read, write and organize directories
# Basics of file IO

if __name__ == '__main__':
    # READ file and print only the lines with 'P' on the 3rd element
    f = open('inputFile.txt', 'r')
    # WRITE pass file
    passFile = open('PassFile.txt', 'w')
    failFile = open('FailFile.txt', 'w')
    # Running through every line in the 'inputFile.txt'
    for line in f:
        # Split to get the Pass or Fail element (3rd element)
        line_split = line.split()
        if line_split[2] == 'P':
            passFile.write(line)
        else:
            failFile.write(line)

    f.close()
    passFile.close()
    failFile.close()

    print('\nProcess finished.\n')
