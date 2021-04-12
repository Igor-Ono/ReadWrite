# Read, write and organize directories

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    # READ file and print only the lines with 'P' on the 3rd element
    f = open('inputFile.txt', 'r')
    count = 0
    # Running through every line in the 'inputFile.txt'
    for line in f:
        # Split to get the Pass or Fail element (3rd element)
        line_split = line.split()
        if line_split[2] == 'P':
            print(str(count) + ' ' + line)
        count += 1
    f.close()
