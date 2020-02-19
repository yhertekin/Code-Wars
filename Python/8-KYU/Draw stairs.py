"""
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

For example n = 3 result in "I\n I\n I", or printed:

I
 I
  I
Another example, a 7-step stairs should be drawn like this:

I
 I
  I
   I
    I
     I
      I
"""

def draw_stairs(n):    
    return "".join([' '*i + 'I\n' for i in range(n)])[:-1]
    

#or 
def stairs(n):
    
    text = ''
    for i in range(n):        
        text += ' '*i
        text += 'I\n'
    return text[:-1]