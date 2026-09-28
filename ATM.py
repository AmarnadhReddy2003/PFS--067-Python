# ATM Machine
card_valid='True'
if card_valid == 'True':
    print('Card Valid')
    pin=int(input('Enter the pin:'))
    if pin == 1902:
        print('Valid Pin')
        bal_ance=int(input('Enter Amount:'))
        if bal_ance<=100000:
            sufficient=bal_ance
            print("You have suuficient amount of funds")
            if sufficient:
                print(f"Here is you'r withdrawl amount of {sufficient}")
            else:
                pass
        else:
            print("You don't have sufficient funds")
            print('Plese check the amount once again')
    else:
        print('Your pin is wrong')
        print('Plese renter the correct pin')
else:
    print('Invalid Card')