#amirhossein
#40213160281828
import datetime as dt
#dt.datetime.now()
money = 5.0  #dollar$
password = input("enter your password to continue: ")
if(password == "123"):
    while(True):
    
        switching = input("type what do you want(deposit,withdraw,bankstatement) for each time this process has commission[0.01$]: ")
        if(switching == "bankstatement"):
            money -= 0.01
            print("your bankstatement is",money,"$")
        elif(switching == "withdraw"):
            withdraw = float(input("how much money for withdraw: "))
            money -= (withdraw + 0.01)
        elif(switching == "deposit"):
            deposit = float(input("how much money for deposit: "))
            money += (deposit - 0.01)
        print("your last logging for:" , dt.datetime.now())
        ex = input("for exit type q: ")
        if(ex == "q"):
            break