#simple ATM  program
#initialize varaible to store balance
initbal=1000
print("Welcome to our ATM machine")
#use while to output menu
while True:
    print("Menu")
    print("\n1.Check balance")
    print("\n2.Deposit money")
    print("\n3.Witdraw money")
    print("\n4.Exit")
    #break exits this operation
    break
#prompts user to enter option
options=int(input("\nEnter your option:"))
#if-elif-else
if options==1:
    print("\nCurrent balance:Ksh ",initbal)#output current balance
   
elif options==2:
     dep=float(input("\nHow much do you want to deposit: Ksh "))
     depAmount=initbal+dep#operation for calculating total amount after depositing
     print("\nNew balance: Ksh ",depAmount)
elif options==3:
    withd=float(input("\nHow much do you want to withdraw: Ksh "))#operation for calculating total amount after withdraw
    if withd<initbal:#checks whether the inital balance is greater than the amount to be withdrawn
      withAmount=initbal-withd
      print("\nNew balance: Ksh ",withAmount)
    else:#withd>initbal
        print("\nInsufficient balance!!")
   
elif options==4:#exit
    print("\nTHANK YOU!")
    breakpoint
    
else:
    print("\nInvalid option.Please try again.")
#end of the process