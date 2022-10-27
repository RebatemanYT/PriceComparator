So how did I make this?

Due to it being better for me for productivity, I did all of it in the base file without having seperate files for making components on their own.

- [base_00_v1.py](old_files/base_00_v1.py) is the starting version that had been made in 1 or 2 sessions.
- [base_00_v2.py](base_00_v2.py) is what I continued and finished the program on.

You can read about other files in the [readme](readme.md).

**Individual Parts of base_00_v2.py:**
- Definitions:
  - def not_blank(question):
    - Asks a question and returns an error if blank. If not blank, it returns the input.
  def int_check(question, error, minnum, blank_0):
    - Checks if something is an interger and if blank_0 is set to "y", it will act like a blank answer is 0. If it isn't fully an interger, is 0 while blank_0 isn't "y" and is smaller than minnum, it gives an error.
  - def string_check(choice, options):
    - Checks if a string is within the options (used for a yes/no).
  - def dolcen(question, error, cur_yn):
    - Asks for dollars then cents then combines them. If cur_yn is set to 1 in the code, it turns it into a currency format via the next def. Then it returns either in or out of currency format.
  - def currency(x):
    - Turns whatever you put as x into a dollar format with $a.bc
  - def weight(a, b):
    - Puts right after each other the 2 things you set as a and b in that order. Used for easy weight letters setting with no space in between (e.g. 10kg).

Rest of the code is asking about your balance, your item's name, weight, cost and if you want to stop the code looping (after 2 uses). After you end the loop, it goes to finalizing, exporting and printing the tables for info about your inputs, including sorting the tables by PPG (Price Per Gram).

**About The Experience**

At first, I didn't have much of a plan for how to code this. I didn't even know how to do formatting on .md files, how to export to a different folder, combine pre-made text and input right next to each other or how to hide stuff in panda tables without making a semi-paragraph in the form of a singular line of code. I now know how to do lots of those things and did stuff with the code that I wouldn't have been likely to do with the help of a trello board or any real planning. I just did stuff on the fly. If I had this style as an option to me in the work I did before this, I wouldn't have taken like 7 months, it would have been at most 2 months. The coding was done in about 1 month. It would have been like 1 or 2 weeks if it wasn't for school holdays in the middle of the coding time and getting too distracted during the school holidays.

But at the beginning of making this, I had a bit of struggle in figuring out the groove of things. I hadn't done coding before without a tutorial (outside of Scratch, WarioWare DIY and very bad Unity attempts) and it was going to be my second ever code written in Python (the first being the previous work with the tutorial). However, I figured out how to do all of it and I never made a trello board or a slide show for it. That did mean that some of my thought process behind the coding wasn't ever written down. That isn't helped with me getting too distracted by coding and debugging to write comments. That would have been a big help but too late now to do them while making each part of the code. However, I can still comment post-coding.

And I just did that while writing this. I hope someone reads this. And if you do, here's a little thanks (a video of me using the program): https://youtu.be/mPxxKxzrH_w

Anyways, after all of that, I still don't know how to read from a csv file with the pandas repository so it doesn't fully meet the guidelines set by the task. If you were wanting the video for the briefing, here it is: https://www.youtube.com/watch?v=I5Qm8at-IEg. It's just a short video from a school teaching kit but without it, this wouldn't have been done. So yeah, I need a break... and to figure out if I have finished this.

Anyways, thanks for reading this.