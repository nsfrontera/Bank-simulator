New_Account = input('Enter name for account? ') #This grabs the account name
Opening_Balance = float(input('Enter starting balance? ')) #This Grabs the balance
Option = 0 #These are variables for counters and balance of totals
Deposite = 0
Amount_Deposite = 0
Withdrawal = 0
Error_Withdrawl = 0
Amount_Error_Withdrawl = 0
Fees = 0
Amount_Fees = 0
Amount_Withdrawl = 0
while Option != "3": #This loops the menu screen and options and ends the loop
    print(' Account: ', New_Account,'\n','Balance: $', Opening_Balance, '\n''You can:', '\n' '1)   Deposit some funds', '\n''2)   Withdraw some funds', '\n''3)   Quit')
    Option = input('Enter selection: ')
    if Option == "1": #code for option 1 that deposits
        Number_Added = abs(float(input('Amount to be deposited? ')))
        Opening_Balance += Number_Added
        Amount_Deposite += Number_Added
        Deposite += 1
    elif Option == "2": #code for option 2  that withdrawals
        Number_Withdrawl = abs(float(input('Amount to be withdrawal? ')))
        if Opening_Balance < Number_Withdrawl: #code for bad withdrawal
            Opening_Balance -= 5
            Error_Withdrawl += 1
            Fees += 1
            Amount_Fees += 5
            Amount_Error_Withdrawl += Number_Withdrawl
            print('Insufficient funds, an overdraft fee of $5 has been charged from your balance.')
        else: #code for good withdrawal
            Opening_Balance -= Number_Withdrawl
            Withdrawal += 1
            Amount_Withdrawl += Number_Withdrawl
print('Final Statement', "\n", 'Account: ', New_Account,"\n",'Balance: ', Opening_Balance,"\n",Deposite, 'deposits with a total of $', Amount_Deposite, "\n",  Withdrawl, 'withdrawl with a total of $', Amount_Withdrawl, "\n", Error_Withdrawl, 'bad withdrawls with a total of $', Amount_Error_Withdrawl, "\n", Fees, 'fees with cost total of $',Amount_Fees, "\n", 'Thank you come again!')
