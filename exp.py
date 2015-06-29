import pexpect
import sys
import pdb

child = pexpect.spawn("python numExp.py")
fout = open('log.txt','ab')
child.logfile = fout

child.expect('Enter a number: ')
child.sendline('10')
#child.expect("number")

# This will output what is printed in the lines after the found
#   regular experession.  I will use this for the tables of data
#   that I want to be added to the file. 
#fout.write(child.after)

#pdb.set_trace()
child.expect('What is your name? ')
child.sendline('Joseph')
#child.expect("name")

child.close()
fout.close()

#child.interact()
