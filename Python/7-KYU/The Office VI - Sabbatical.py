"""
Learning to code around you full time job is taking over your life. You realise that in order to make significant steps quickly, it would help to go to a coding bootcamp in London.

Problem is, many of them cost a fortune, and those that don't still involve a significant amount of time off work - who will pay your mortgage?!

To offset this risk, you decide that rather than leaving work totally, you will request a sabbatical so that you can go back to work post bootcamp and be paid while you look for your next role.

You need to approach your boss. Her decision will be based on three parameters:

val=your value to the organisation
happ=her happiness level at the time of asking and finally
The numbers of letters from 'sabbatical' that are present in string 'x'.

Note that if x contains three instances of the letter 'l', that still scores three points, even though there is only one in the word sabbatical.

If the sum of the three parameters (as described above) is > 22, return 'Sabbatical! Boom!', else return 'Back to your desk, boy.'.
"""

def sabb(s, value, happiness):
    char_count = 0
    for i in 'sbaticl':
        char_count += s.lower().count(i)
    return 'Sabbatical! Boom!' if char_count + value + happiness > 22 else 'Back to your desk, boy.'