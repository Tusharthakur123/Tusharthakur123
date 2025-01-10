import time 

print("please insert your CARD")

time.sleep(5) # here atm machine takes some time to process the card

password=1234

pin=int(input("enter your atm pin")) # here pin no is in integer format

balance=5000

if pin==password:
    while True:

        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """ 
            )
        try:
            option=int(input("please enter your choice"))
        except:
            print("please enter valid option")
                
            print("============================================")
            print("============================================")
            print("============================================")

        if  option ==1:
            print(f"your current balance is{balance}")

            print("============================================")
            print("============================================")
            print("============================================")

        if option ==2:
            
            withdraw_amount=int(input("please enter withdraw_amount"))

            print("============================================")
            print("============================================")
            print("============================================")

            balance=balance-withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            print("============================================")
            print("============================================")
            print("============================================")

            print(f"your current balance is{balance}")

            print("============================================")
            print("============================================")
            print("============================================")

        if option==3:

            deposit_amount=int(input("please enter deposit_amount"))

            balance=balance=deposit_amount

            print(f"{deposit_amount} is credited to your account")

            print("============================================")
            print("============================================")
            print("============================================")

            print(f"your  updated current balace is{balance}")

            print("============================================")
            print("============================================")
            print("============================================")

        if option==4:
            break
else:
    print("wrong pin please try again")
