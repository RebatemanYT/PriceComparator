Just for school.
Note that I don't have slides or a trello for this due to not having that good of an idea for the full plan.

Steps to use:
  0. Put in, dollar then cent, your budget. This won't loop later on.
  
  The next steps are in a loop.
  1. If you have put in at least 2 items, it will ask you if you want to stop looping the code. If you input "No", it will loop. If you input "Yes", it will stop looping and show your results. If you haven't put in 2 or more items, it won't show this prompt.
  2. It will ask you to put the product name in.
  3. Afterwards, it will ask you to input the product weight in grams. It will auto convert to kilograms.
  4. 

PARTS
main.py = Loads in the base.
base_00_vx.py = Base component, x = version number
  v1 = Has the budget, looping, exit looping, product name, weight, and that's basically it.
  v2 = Same as v1 but moved the buget to a seperate definition part and reused for product costs. Also adds figuring out price per kg and outputting to files.
output = Folder with outputted files.
  comparing_full.csv = Most of the stuff used for calculating the output.
  comparing_short.csv = The short version showed at the end of using the program.
Talking About Making This.md = A write up about each part of base_00_v2.py and about making the program.

Program includes test versions of the output folder stuff.