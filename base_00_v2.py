#Importing useful repositories just in case
import re #Not fully sure if I used this but keeping just in case - I added it at the start
import pandas #Def used a lot.

#Is an input blank or not? - read more about this in Talking About Making This.md
def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    # If name is not blank, program continues
    if response != "":
      return response

    # If name is blank, show error (& repeat loop)
    else:
      print("Sorry - this can’t be blank, please enter a product name.")

#Checking if interger - read more about this in Talking About Making This.md
def int_check(question, error, minnum, blank_0):

    valid = False
    while not valid:

      # ask user for number and check it is valid
      try:
        if blank_0 == "y":
          responsebase = input(question)
          if responsebase == "":
            return 0
          else:
            response = int(responsebase)
        else:
          response = int(input(question))
      
        #minnum is 1 less than your minimum value.
        if response <= minnum:
            print(error)
        else:
            return response

      # if an integer is not entered, display an error message
      except ValueError:
        print(error)
        return "error"

#String checking - read more about this in Talking About Making This.md
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full name of the snack
        if choice in var_list:

            # Get full name of snack and put it in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"

#A "yes" and a "no"
yesno = [
  ["yes", "y", "ye"], 
  ["no", "n"]
]

#Getting Dollars and Cents - read more about this in Talking About Making This.md
def dolcen(question, error, cur_yn):
  dolcen_error = ""
  #Loop in case of bad input
  while dolcen_error != "good":
    print(question)
    #Ask for dollars
    dolcen_dol = int_check("Dollars = $", numerror, -1, "y")
    if dolcen_dol == "error":
      dolcen_error = "error"
    else:
      print(question)
      #Ask for cents
      dolcen_cent = int_check("Cents = ¢", numerror, -1, "y")
      if dolcen_cent == "error":
        dolcen_error = "error"
      else:
        dolcen_error = "good"
  #Convert to decimals
  dolcen_bal = dolcen_dol + (dolcen_cent / 100)
  #In dollars formatting or not?
  if cur_yn == 1:
    dolcen_bal_cur = currency(dolcen_bal)
    return dolcen_bal_cur
  else:
    return dolcen_bal
  
#Currency - converting a number to 2 dp and adding a dollar sign in front
def currency(x):
  return "${:.2f}".format(x)
  
#Weight - putting 2 items right next to each other
def weight(a, b):
  return "{}{}".format(a, b)
  
# *** Main Code ***

print("Note that this prints in dollars and cents like this: $x.ab, with cents going from 0-99 (100 = 1 dollar). If you can't act like it is your currency as it doesn't use cents, sorry.")
#Budget for shopping
bal_dolcen_check = 0
numerror = "Error: Either not in grams, is lower than the minimum for this input, has decimal, or not a number."

while bal_dolcen_check == 0:
  bal_dolcen = dolcen("Please enter your budget.", numerror, 1)
  print(bal_dolcen)
  if bal_dolcen == "$0.00":
    print("You can't have a balance of $0.00")
  else:
    bal_dolcen_check = 1

#Lists to make the dictionary work.
products = []
grams = []
kilograms = []
cost_dolcen_lista = []
cost_dolcen_listb = []
cost_dolcen_listg = []
cost_dolcen_listgc = []
comparingstuff_list = [products, grams, kilograms, cost_dolcen_lista, cost_dolcen_listgc]

#What will eventually become the table, in dictionary form.
comparing_dict = {
  'Product': products,
  'Grams': grams,
  'Kilograms': kilograms,
  'Cost': cost_dolcen_lista,
  'Cost (NF)': cost_dolcen_listb,
  'PPG': cost_dolcen_listgc,
  'PPG (NF)': cost_dolcen_listg
}

endloopa = ""
endloopb = ""
listnum = 0
listnuma = 1
while endloopb != "Yes":
  product = ""
  gram = ""
  kilogram = ""
  #Ask for if user wants to stop adding to list if more than 2 items are in.
  if listnum >= 2:
    endloopa = not_blank("Do you want to stop looping the code? ").lower()
    endloopb = string_check(endloopa, yesno)
    print(endloopb)
  #If either saying no to stopping the looping code or it isn't meant to be prompted yet, do rest of the asking code.
  if endloopb == "No" or listnum <= 1:
    print("Product number", listnum)
    
    #Asking for name of product.
    product = not_blank("Please enter the name of a product that you wish to add to the list. \n")
    products.append(product)

    gramcheck = ""
    while gramcheck != "good":
      #Asking weight in grams.
      gram = int_check("Please enter, in grams, the weight of the product. Full number only. \n", numerror, 0, "n")

      #Checking if input is valid and if it is, converts and prints out in grams and kilograms.
      gramcheck = ""
      if gram == "error":
        gramcheck = "error"
      if gramcheck != "error":
        kilogram = gram / 1000
        print("Grams:", gram)
        print("Kilograms:", kilogram)
        gramcheck = "good"
        continue

    #Adding g and kg to the end of the weights + adding to eventual table.
    gframe = weight(gram, "g")
    kgframe = weight(kilogram, "kg")
    grams.append(gframe)
    kilograms.append(kgframe)

    #Inputting cost in dollars then cents.
    cost_dolcen_b = dolcen("Please enter the cost of that product in that weight.", numerror, 0)
    #Converting in a copy the above input to dollars and cents.
    cost_dolcen_a = currency(cost_dolcen_b)
    #Adding to the eventual table.
    cost_dolcen_lista.append(cost_dolcen_a)
    cost_dolcen_listb.append(cost_dolcen_b)
    print()

    #Price Per Gram
    cost_dolcen_g = cost_dolcen_b / gram
    cost_dolcen_gc = currency(cost_dolcen_g)
    cost_dolcen_listg.append(cost_dolcen_g)
    cost_dolcen_listgc.append(cost_dolcen_gc)
    print("Price of the product per gram:", cost_dolcen_gc)
    #Increasing shown list number
    listnum = listnum + listnuma

#Making dataframes - both long and short
comparing_frame = pandas.DataFrame(comparing_dict)
comparing_frame = comparing_frame.sort_values(axis=0, by='PPG (NF)')
comparing_frame_print = comparing_frame.drop('Cost (NF)', axis=1)
comparing_frame_print = comparing_frame_print.drop('Grams', axis=1)
comparing_frame_print = comparing_frame_print.drop('PPG (NF)', axis=1)

#Table Printing
print('The top row below the titles is the one that is best value per dollar. Please note that in the output folder is both the table below and a bigger one as .csv files.')
print(comparing_frame_print)
print('PPG = Price Per Gram.')

#Exporting 2 csv files with both short and long tables.
comparing_frame.to_csv("output/comparing_full.csv")
comparing_frame_print.to_csv("output/comparing_short.csv")