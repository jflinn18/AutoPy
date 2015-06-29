import pexpect
import sys
import pdb

child = pexpect.spawn("python numExp.py")
fout = open('log.txt','wb')
child.logfile = fout

child.expect('Enter a number: ')
child.send('10\n')
child.expect("Your")
fout.write(child.after)

child.close()
fout.close()

#child.interact()
