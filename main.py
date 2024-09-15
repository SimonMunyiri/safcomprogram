#ussd app

print(
    """ 
                                                                                    iiii
       sssss                          ffffff                                        iiii       
     ssssssss                       ff      ff    
    sss            aaaaaaa          ff           aaaaaaaa    rrrr     rrrrrrr       iiii     ccccccc        ooooooooo     mmm         mmm
    sss           aaaaaaaaa         ff          aaaaaaaaaa  rrrrrr   rrrrrrrrr      iiii    ccccccccc      ooooooooooo    mmm mm   mm mmm
     sssssss             aa    ffffffffffffff           aa rrr   rrr rrr     rrr    iiii   ccc      ccc    ooo     ooo    mmm  mm mm  mmm
     ssssssss            aa         ff                  aa        rrrrr             iiii   ccc             ooo     ooo    mmm    mm   mmm
           ssss   aaaaaaaaa         ff          aaaaaaaaaa        rrrr              iiii   ccc             ooo     ooo    mmm         mmm
           ssss   aa     aa         ff          aa      aa        rrrr              iiii   ccc             ooo     ooo    mmm         mmm
    sssssssss     aa     aa         ff          aa      aa        rrrr              iiii    cccccccccc     ooooooooooo    mmm         mmm 
      sssss       aaaaaaaa aa       ff          aaaaaaaa aa       rrrr              iiii     ccccccc        ooooooooo     mmm         mmm
    """
)


airtimeBalance = 20
mpesaBalance = 10000
okoaJahaziBalance = 0
okoaJahaziDeptBalance = 0
totalAirtime = okoaJahaziBalance + airtimeBalance
bundleBalance = 0
topUpPins = "123456789"

def invalid():
    print("Invalid option selected")

def lessAirtime():
    print("Insufficient airtime to purchase this offer.")

def line():
    print("=====================================================")

def okoaSuccess(okoaJahaziBalance):
    print(f"You have received an okoa jahazi of {okoaJahaziBalance}")

def bundleSuccess(bundlePurchased, bundleBalance):
    print(f"You have successfully purchased {bundlePurchased}. Your new data balance is {bundleBalance}MB.")

def lessMpesa(mpesaBalance):
    print(f"You have insufficient mpesa balance to complete this offer. Your M-pesa balance is {mpesaBalance}")


while True:
    ussd = input("Enter USSD:> ")

    #check the entered USSD code
    if ussd == "*544#":
        #buy bundles
        print("1) daily bundles")
        print("2) Weekly bundles")
        print("3) Monthly bundles")

        bundleOption = input(":> ")
        if bundleOption == "1":
            print("1) Sh 99(Giga 1GB)")
            print("2) Sh 10: 25MB + 25SMS")
            boughtDaily = input("> ")
            if boughtDaily == "1":
                #check airtime balance
                if totalAirtime < 99:
                    lessAirtime()
                    print("1) Buy from M-pesa")
                    print("2) Okoa jahazi")

                    airtimeAdd = input("> ")
                    if airtimeAdd == "1":
                        print("Buying from M-pesa")
                        #first check that the mpesa balance is greater than the amount you wanna use
                        if mpesaBalance >= 99:
                            #proceed to purchase data
                            #deduct ksh 99 from yr M-pesa
                            mpesaBalance -= 99
                            #increment your bundle balance
                            bundleBalance += 1024
                            #print a success message
                            bundleSuccess(99, bundleBalance)
                        else:
                            lessMpesa(mpesaBalance)

                    elif airtimeAdd == "2":
                        #check the okoa jahazi debt balance for the user
                        #if the user has a debt, do not allow him/her to okoa more
                        if okoaJahaziDeptBalance > 0:
                            print(f"Sorry, request not successful. You must pay your previous Okoa jahazi debt balance of {okoaJahaziDeptBalance}")
                        else:
                            print("Accessing okoa jahazi")
                            print("1) 10")
                            print("2) 20")
                            print("3) 50")
                            print("4) 100")
                            getOkoa = input("> ")
                            if getOkoa == "1":
                                okoaJahaziBalance += 9
                                totalAirtime = okoaJahaziBalance + airtimeBalance
                                okoaJahaziDeptBalance = 10
                                okoaSuccess(okoaJahaziBalance)
                            elif getOkoa == "2":
                                okoaJahaziBalance += 18
                                okoaJahaziDeptBalance = 20
                                totalAirtime = okoaJahaziBalance + airtimeBalance
                                okoaSuccess(okoaJahaziBalance)
                            elif getOkoa == "3":
                                okoaJahaziBalance += 45
                                okoaJahaziDeptBalance = 50
                                totalAirtime = okoaJahaziBalance + airtimeBalance
                                okoaSuccess(okoaJahaziBalance)
                            elif getOkoa == "4":
                                okoaJahaziBalance += 90
                                okoaJahaziDeptBalance = 100
                                totalAirtime = okoaJahaziBalance + airtimeBalance
                                okoaSuccess(okoaJahaziBalance)
                            else:
                                invalid()
                    else:
                        invalid()
                else:
                    #check if airtime is enough to purchase the data
                    #if airtime is enough, use it to purchase this data
                    #if airtime is not enough, check if there is enough okoa jahazi...
                    #if okoa jahazi isn't enough, use total airtime to purchase data
                    if airtimeBalance >= 99:
                        airtimeBalance -= 99
                        bundleBalance += 1024
                        print("Successfully purchased ")
                    elif airtimeBalance < 99:
                        if okoaJahaziBalance >= 99:
                            okoaJahaziBalance -= 99
                            bundleBalance += 1024
                            print("Successfully purchased")
                        else:
                            #use both airtime and okoa jahazi
                            if totalAirtime >= 99:
                                # first use all the airtime balance that is available
                                # the use okoa jahazi balance
                                newAirtimeBalance = airtimeBalance - 99
                                okoaJahaziBalance = newAirtimeBalance + okoaJahaziBalance
                                totalAirtime = okoaJahaziBalance
                                airtimeBalance = 0
                                bundleBalance += 1024
                                print("Successfully purchased")

                            else:
                               print("insufficient airtime!")


        else:
            invalid()
    elif ussd == "*144#":
        #check airtime balance
        print(f"Your airtime balance is {airtimeBalance}")
    elif ussd == "*131#":
        #okoa jahazi
        print("Accessing okoa jahazi")
        print("1) 10")
        print("2) 20")
        print("3) 50")
        print("4) 100")
        getOkoa = input("> ")
        if getOkoa == "1":
            okoaJahaziBalance += 9
            totalAirtime = okoaJahaziBalance + airtimeBalance
            okoaJahaziDeptBalance = 10
            okoaSuccess(okoaJahaziBalance)
        elif getOkoa == "2":
            okoaJahaziBalance += 18
            okoaJahaziDeptBalance = 20
            totalAirtime = okoaJahaziBalance + airtimeBalance
            okoaSuccess(okoaJahaziBalance)
        elif getOkoa == "3":
            okoaJahaziBalance += 45
            okoaJahaziDeptBalance = 50
            totalAirtime = okoaJahaziBalance + airtimeBalance
            okoaSuccess(okoaJahaziBalance)
        elif getOkoa == "4":
            okoaJahaziBalance += 90
            okoaJahaziDeptBalance = 100
            totalAirtime = okoaJahaziBalance + airtimeBalance
            okoaSuccess(okoaJahaziBalance)
        else:
            invalid()
    elif ussd == "*144*4#":
        if okoaJahaziBalance > 0:
            print(f"Your okoa jahazi balance is {okoaJahaziBalance} and your okoa jahazi debt balance is {okoaJahaziDeptBalance}.")
        elif okoaJahaziBalance == 0 and okoaJahaziDeptBalance > 0:
            print(f"You do not have oustanding okoa jahazi balance. Your existing okoa jahazi debt balance is {okoaJahaziDeptBalance}.")
        elif okoaJahaziBalance == 0 and okoaJahaziDeptBalance == 0:
            print("You do not have existing okoa jahazi debt. please dial *131# to okoa credo")
    elif ussd == "*544*4#":
        if bundleBalance >= 1000:
            bundleBalanceGb = bundleBalance/1000
            print(f"Data bundle balance is {bundleBalanceGb}GB")
        else:
            print(f"Data bundle balance is {bundleBalance}MB")
    elif ussd == "*141*"+ topUpPins +"#":
        airtimeBalance += 10
        totalAirtime = airtimeBalance + okoaJahaziBalance
        print(f"Received ksh 10 of airtime. Your airtime balance is {airtimeBalance}")
    else:
        invalid()







