# Exercises for chapter 2:

# Name: Cassie Sancartier

# 2.1: Based on the linked article, it seems that because of the leading zero, 
# python is translating the 02132 number from the Octal system into another type 
# of number system. There was an 'invalid token' error message on the first number 
# (02492) because the Octal system only uses the digits 0 through 7.

-------------------------

# 2.2: When the original statements are run in a script, there is no output.  
# Here is the modified script, with print statement:

print 5
x = 5
print x + 1

# The new output is:
5
6

-------------------------

# 2.3: Value and type of expression:
# 1. 8, integer
# 2. 8.5, float
# 3. 4.0, float
# 4. 11, integer
# 5. '.....', string

-------------------------

# 2.4:

# 1. 523.6 (used the following expression, with floats instead of integers):

r = 5
4.0/3.0 * math.pi * r**3
523.5987755982989

#2. $945.45 (used the following):

discount_price = 24.95 * .60
shipping_first_copy = 3.00
shipping_additional_copy = .75

(discount_price * 60) + (shipping_first_copy + (shipping_additional_copy * 59))
945.4499999999999

#3. 7:30:02am  (used the following):

easy_pace = ((8 * 60) + 15)
tempo_pace = ((7 * 60) + 12)
start_time = ((6 * 3600) + (52 * 60))
start_time + (easy_pace * 2.0) + (tempo_pace * 3.0)
27006.0
breakfast_time = start_time + (easy_pace * 2.0) + (tempo_pace * 3.0)

breakfast_time/3600
7.501666666666667



