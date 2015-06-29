import pexpect


i = 0

while i < 5:
  child = pexpect.spawn('python numExp.py')
  fout = open('log.txt', 'ab')
  child.logfile = fout
  child.expect("Enter a number: ")

  if i < 3:
    child.send("10")

  else:
    child.send("20")

  child.expect("Your")
#  child.expect("number")
#  child.expect("What is your name?")
#  print child.after
#  child.send("Joseph")
#  child.expect("name")

#  fout.write("\n")
  fout.write("-"*25)
  fout.write("\n")

  child.close()
  fout.close()
  i = i + 1
