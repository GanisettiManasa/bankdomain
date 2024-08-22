#CRUDS program on bank domain

import os

def ShowMenu():
    Menu = [CreateAccount, ShowAllAccounts, UpdateAccount, DeleteAccount, SearchAccount, exit]

    while True:
        Choice = int(input("------BANK SYSTEM-------\n"
                           "          Menu\n"
                           "1. Add an account\n"
                           "2. Show all accounts\n"
                           "3. Update an account\n"
                           "4. Delete an account\n"
                           "5. Search an account\n"
                           "0. Exit\n"
                           "Enter your choice: "))

        if Choice < 0 or Choice > 5:
            print("Invalid choice. Please try again.")
            continue
        elif Choice == 0:
            break

        Menu[Choice - 1]()

def GetData():
    AccountNumber = input("Enter Account Number: ")
    AccountHolderName = input("Enter Account Holder Name: ")
    Balance = float(input("Enter Account Balance: "))
    NewData = [AccountNumber, AccountHolderName, Balance]
    return NewData

def LoadAccountRecords():
    if os.path.exists(ACCOUNTS_DATA_FILE) and os.path.getsize(ACCOUNTS_DATA_FILE) > 0:
        FpAccounts = open(ACCOUNTS_DATA_FILE, "r")
        AccountDetails = FpAccounts.read()
        return eval(AccountDetails)
    return {}

def SaveAccountRecords():
    FpAccounts = open(ACCOUNTS_DATA_FILE, "w")
    FpAccounts.write(str(Records))
    FpAccounts.close()

def CreateAccount():
    NewData = GetData()
    Records[NewData[0]] = [NewData[1], NewData[2]]
    SaveAccountRecords()
    print("Account details added successfully.")

def ShowAllAccounts():
    print("All Accounts:")
    for Record in Records:
        PrintAccountDetails(Record)

def AccountNotFound(EnteredAccountNumber):
    print("Account not found with Number: " + EnteredAccountNumber)

def UpdateAccount():
    EnteredAccountNumber = CheckRecord("update")
    if EnteredAccountNumber != -1:
        NewBalance = float(input("Enter new balance: "))
        Records[EnteredAccountNumber][1] = NewBalance
        SaveAccountRecords()
        print("Account details updated successfully.")
    else:
        AccountNotFound(EnteredAccountNumber)

def DeleteAccount():
    EnteredAccountNumber = CheckRecord("delete")
    if EnteredAccountNumber != -1:
        Records.pop(EnteredAccountNumber)
        SaveAccountRecords()
        print("Account details deleted successfully.")
    else:
        AccountNotFound(EnteredAccountNumber)

def SearchAccount():
    EnteredAccountNumber = CheckRecord("search")
    if EnteredAccountNumber != -1:
        PrintAccountDetails(EnteredAccountNumber)
    else:
        AccountNotFound(EnteredAccountNumber)

def CheckRecord(operation):
    EnteredAccountNumber = GetAccountNumber(operation)
    if EnteredAccountNumber in Records: 
        return EnteredAccountNumber
    return -1

def GetAccountNumber(operation):
    return input("Enter Account Number to " + operation + ":")

def PrintAccountDetails(AccountNumber):
    print("Account Number: " + AccountNumber)
    print("Account Holder Name: " + Records[AccountNumber][0])
    print("Account Balance: " + str(Records[AccountNumber][1]))

global ACCOUNTS_DATA_FILE
ACCOUNTS_DATA_FILE = "accounts.txt"
global Records
Records = LoadAccountRecords()
ShowMenu()
