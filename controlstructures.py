# Simple ATM program
# Initialize variable to store balance
initbal = 1000
print("Welcome to our ATM machine")
#use while to output menu
# Use a loop to repeatedly output the menu
while True:
    print("\nMenu")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    #removed the break

    # prompt the user to enter option
    options = int(input("\nEnter your option: "))

    # Check if the input is a valid number
    # if-elif-else
    if options == 1:
        print("\nCurrent balance: Ksh", initbal)  # output current balance

    elif options == 2:
        dep = float(input("\nHow much do you want to deposit: Ksh "))
        initbal+=dep#operation for calculating total amount after depositing
        print("\nNew balance: Ksh", initbal)

    elif options == 3:
        withd = float(input("\nHow much do you want to withdraw: Ksh "))
        if withd<=initbal:#checks whether the inital balance is greater than the amount to be withdrawn
          initbal-=withd#voperation for calculating total amount after withdraw
          print("\nNew balance: Ksh ",initbal)
        else:#withd>initbal
         print("\nInsufficient balance!!")
    elif options == 4:  # exit
        print("\nTHANK YOU!")
        break  # break out of the loop to stop displaying the menu

    else:
        print("\nInvalid option. Please try again.")
    #end of the process

