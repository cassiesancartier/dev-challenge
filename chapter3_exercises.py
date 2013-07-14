# Exercises for chapter 3:

# Name: Cassie Sancartier

# 3.1: When you move the repeat_lyrics call to the top of the program,
# you get the following error, because you are trying to call a function you
# haven't yet defined:

CassieSancartier:RampUp cms$ python exercise3.1.py
Traceback (most recent call last):
  File "exercise3.1.py", line 1, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined

-------------------------

# 3.2: When you move the function call back to the bottom, but then put the 
# repeat_lyrics definition above the print_lyrics definition, you get the 
# following:

"I'm a lumberjack, and I'm okay"
"I sleep all night and I work all day"
"I'm a lumberjack, and I'm okay"
"I sleep all night and I work all day"

# The repeat_lyrics() call works as it should because both the print_lyrics()
# and repeat_lyrics() functions were defined before calling it - it doesn't
# matter that they are 'out of order'.

-------------------------

# 3.3: Here is a function that moves a string's last letter to column 70:

def right_justify(s):
	spaces = (70 - len(s))
	print ((" " * spaces) + s)

	
right_justify('boat')
                                                                  boat

-------------------------

# 3.4:

# 1. Tested it, returned 'spam' twice

# 2. Modified do_twice:

def do_twice(f, v):
	f(v)
	f(v)

# 3. print_twice function:

def print_twice(string):
	print string
	print string

# 4. Called modified version of do_twice:

do_twice(print_twice, 'spam')
spam
spam
spam
spam

# 5. New function, do_four:

def do_four(f, v):
	do_twice(f, v)
	do_twice(f, v)


			

