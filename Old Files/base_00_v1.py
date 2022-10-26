#Importing just in case
import re
import pandas

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

def int_check(question, error, minnum):

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
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
      
yesno = [
  ["yes", "y", "ye"], 
  ["no", "n"]
]

#Currency
def currency(x):
  return "${:.2f}".format(x)
  
# *** Main Code ***

#Budget for shopping
numerror = "Error: Either not in grams, is lower than the minimum for this input, has decimal, or not a number."

balerror = ""
while balerror != "good":
  baldol = int_check("Please enter your budget. Dollars = $", numerror, 0)
  if baldol == "error":
    balerror = "error"
  else:
    balcen = int_check("Please enter your budget. Cents = ¢", numerror, -1)
    if balcen == "error":
      balerror = "error"
    else:
      balerror = "good"
baldolcen = baldol + (balcen / 100)
baldolcencur = currency(baldolcen)
print(baldolcencur)


products = []
grams = []
kilograms = []
comparingstuff = [products, grams, kilograms]

comparing_dict = {
  'Product': products,
  'Weight (Grams)': grams,
  'Weight (Kilograms)': kilograms
}

endloopa = ""
endloopb = ""
while endloopb != "Yes":
  listnum = 1
  product = ""
  gram = ""
  kilogram = ""
  #Ask for if user wants to stop adding to list if more than 2 items are in.
  if listnum >= 3:
    endloopa = not_blank("Do you want to stop looping the code? ").lower()
    endloopb = string_check(endloopa, yesno)
    print(endloopb)
  if endloopb == "No" or listnum <= 2:
    print("Product number", listnum - 1)
    product = not_blank("Please enter the name of a product that you wish to add to the list. \n")
    products.append(product)
    
    gram = int_check("Please enter, in grams, the weight of the product. Full number only. \n", numerror, 0)
    if gram != "error":
      kilogram = gram / 1000
      print("Kilograms:", kilogram)
    
      grams.append(gram)
      kilograms.append(kilogram)
  
    listnum = listnum + 1
    
print(product)
print(grams)
print(kilograms)