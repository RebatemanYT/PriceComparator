So how did I make this?

Due to it being better for me for productivity, I did all of it in the base file without having seperate files for making components on their own.

base_00_v1.py is the starting version that had been made in 1 or 2 sessions.
base_00_v2.py is what I continued and finished the program on.

You can read about other files in the readme.

Individual Parts of base_00_v2.py:
Definitions:
  def not_blank(question):
    Asks a question and returns an error if blank. If not blank, it returns the input.
  def int_check(question, error, minnum, blank_0):
    Checks if something is an interger and if blank_0 is set to "y", it will act like a blank answer is 0. If it isn't fully an interger, is 0 while blank_0 isn't "y" and is smaller than minnum, it gives an error.
  def string_check(choice, options):
    Checks if a string is within the options (used for a yes/no).
  def dolcen(question, error, cur_yn):
    Asks for dollars then cents then combines them. If cur_yn is set to 1 in the code, it turns it into a currency format via the next def. Then it returns either in or out of currency format.
  def currency(x):
    Turns whatever you put as x into a dollar format with $a.bc
  def weight(a, b):
    Puts right after each other the 2 things you set as a and b in that order. Used for easy weight letters setting with no space in between (e.g. 10kg).

Rest of the code is asking about your balance, your item's name, weight, cost and if you want to stop the code looping (after 2 uses). After you end the loop, it goes to finalizing, exporting and printing the tables for info about your inputs, including sorting the tables by PPG (Price Per Gram).