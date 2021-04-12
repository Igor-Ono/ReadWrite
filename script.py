import subprocess as sp

n = 5
for i in range(0, n):
    sp.check_call(['python', 'main.py'])
    # To run use in the terminal: python script.py
