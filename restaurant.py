#restro bill printing
print('''
    _________________________________
            RESTAURANTS LIST
    _________________________________
        1. HALDIRAM 
        2. FUEL STATION
        3. FRULLATO
        4. EXIT
    ________________________________
''')
ch=int(input('SELECT THE CHOICE:-'))
match ch:
    case 1:
        def haldiram():
            qty1=0
            qty2=0
            qty3=0
            d1=0
            d2=0
            d3=0
            dish = ['RAJ KACHORI','CHOLA BHATORA','SAMOSA']
            price = [180,200,90]
            while True:
                print('''
                            _______________________
                              WELCOME TO HALDIRAM
                            ________________________
                             0. RAJ KACHORI   - 180/-
                             1. CHOLA BHATURA - 200/-
                             2. SAMOSA        - 90/-
                             3. BILL
                            _______________________
                            ''')
                ch=int(input('WHAT DO YOU WANT TO EAT?'))
                match ch:
                    case 0:
                        qty1=int(input('ENTER THE QUANTITY:-'))
                        d1=price[0] * qty1
                    case 1:
                        qty2=int(input('ENTER THE QUANTITY:-'))
                        d2=price[1] * qty2
                    case 2:
                        qty3=int(input('ENTER THE QUANTITY:-'))
                        d3=price[2] * qty3
                    case 3:
                        total_bill= qty1 * 180+ qty2 *200+ qty3*90
                        if total_bill==0:
                            print('PLEASE ADD AT LEAST ONE ITEM.')
                            continue
                        name=input('ENTER THE CUSTOMER NAME:-')
                        mob=int(input('ENTER THE CUSTOMER MOB NUM:-'))    
                        print('________________________________')
                        print('             BILL               ')
                        print('________________________________')
                        print(f'''NAME  :-    {name}''')
                        print(f'''MOB NUM:-   {mob}''')
                        print('_________________________________')
                        if qty1>0:
                            print(f'''RAJ KACHORI      X{qty1}    {d1}''')
                        if qty2>0:
                            print(f'''CHOLA BHATURA    X{qty2}    {d2}''')
                        if qty3>0:
                            print(f'''SAMOSA           X{qty3}    {d3}''')
                        print('________________________________')
                        print(f'''TOTAL BILL :-           {total_bill}''')
                        print('______________________________________')

                        import random
                        import math
                        def otp():
                            otps=math.floor(random.random() * 10000)
                            return otps
                        def pay():
                            while True:
                                print('''
                                ___________________________________
                                    CHOOSE PAYMENT METHOD
                                ____________________________________
                                    1. CASH
                                    2. CARD 
                                    3. UPI
                                    4. EXIT
                                ____________________________________
                                ''')
                                payment= int(input('SELECT THE PAYMENT METHOD:-'))
                                match payment:
                                    case 1:
                                        cash=int(input('ENTER THE CASH AMOUNT:-'))
        
                                        if cash > total_bill:
                                            more_cash= cash-total_bill
                                            print('___________________________________')
                                            print('PAYMENT SUCCESSFUL!')
                                            print(f'''{cash}    - {total_bill} = {more_cash}/-''')
                                            print('____________________________________')
                                            print('ORDER CONFIRMED!')
                                            print(f'''CHANGE RETURN  -->  {more_cash}/-''')
                                            print('_____________________________________')
                                            print('THANK YOU FOR VISITING HALDIRAM!')
                                            print('_________________________________')
                                            break
                                            
                                        if cash < total_bill:
                                            less_cash= total_bill - cash
                                            print('_____________________________________')
                                            print('INSUFFICIENT AMOUNT!')
                                            print(f'''REMAINING AMOUNT  --> {less_cash}/-''')
                                            print('________________________________________')
                                            extra = int(input("ENTER REMAINING CASH: "))
                                            cash=cash+extra
                                            if cash > total_bill:
                                                nbill= cash - total_bill
                                                print('___________________________________')
                                                print('PAYMENT SUCCESSFUL!')
                                                print(f'''{cash}    - {total_bill} = {nbill}/-''')
                                                print('____________________________________')
                                                print('ORDER CONFIRMED!')
                                                print(f'''CHANGE RETURN  -->  {nbill}/-''')
                                                print('_____________________________________')
                                                print('THANK YOU FOR VISITING HALDIRAM!')
                                                print('_____________________________________')
                                                break
                                            if cash< total_bill:
                                                print('_____________________________________')
                                                print('INSUFFICIENT AMOUNT!')
                                                print(f'''REMAINING AMOUNT  --> {less_cash}/-''')
                                                print('________________________________________')
                                            if cash==total_bill:
                                                print('_________________________')
                                                print('PAYMENT IS SUCCESSFUL!')
                                                print('ORDER CONFIRMED!')
                                                print('_________________________')
                                                print('THANK YOU FOR VISITING HALDIRAM!')
                                                print('__________________________')
                                                break
                                        if cash==total_bill:
                                            print('_________________________')
                                            print('PAYMENT IS SUCCESSFUL!')
                                            print('ORDER CONFIRMED!')
                                            print('_________________________')
                                            print('THANK YOU FOR VISITING HALDIRAM!')
                                            print('__________________________')
                                            break
                                    case 2:
                                        card_num=input('ENTER THE CARD NUM:-')
                                        if len(str(card_num))==16:
                                            cvv=input('ENTER THE CVV NUM:-')
                                            if len(str(cvv))==3:
                                                uotp=otp()
                                                print('YOUR OTP NO:-',uotp)
                                                eotp=int(input('ENTER THE OTP:-'))
                                            if uotp==eotp:
                                                print('________________________________')
                                                print('PAYMENT IS SUCCESSFULLY PAID!')
                                                print('ORDER CONFIRMED!')
                                                print('________________________________')
                                                break
                                            else:
                                                print('INVALID OTP!')
                                        else:
                                            print('INVALID CARD NUMBER!')
                                            break
                            
                                    case 3:
                                        uid=input('ENTER THE UPI ID:-')
                                        pin=input('ENTER THE PIN :-')
                                        print(f'''{total_bill}/-  PAID!''')
                                        print('____________________________________')
                                        print('PAYMENT SUCCESSFULLY PAID !')
                                        print('____________________________________')
                                        break
                                    
                                    case 4:
                                        print('THANK YOU FOR VISITING!')
                                        break
                                    case _:
                                        print('INVALID CHOICE')
                        pay()
                        break
                    case _:
                        print('INVALID CHOICE')
        haldiram()
    case 2:
        def fuelstation():
            qty1=0
            qty2=0
            qty3=0
            while True:
                dish = ['MARGHERITA PIZZA','MAC N CHEESE PASTA','GRILLED SANDWICH ']
                price = [150,200,170]
                print('''
                _______________________________________
                        WELCOME TO FUEL STATION
                _______________________________________
                     0. MARGHERITA PIZZA    :  150/-
                     1. MAC N CHEESE PASTA  :  200/-
                     2. GRILLED SANDWICH    :  170/-
                     3. BILL
                ________________________________________
                ''')
                ch=int(input('WHAT DO YOU WNAT TO EAT?'))
                match ch:
                    case 0:
                        qty1=int(input('ENTER THE QUANTITY:- '))
                        d1= price[0] *qty1
                    case 1:
                        qty2=int(input('ENTER THE QUANTITY:- '))
                        d2=price[1] * qty2
                    case 2:
                        qty3=int(input('ENTER THE QUANTITY:- '))
                        d3=price[2] * qty3
                    case 3:
                        total_bill= qty1 * 150+ qty2 *200+ qty3*170
                        if total_bill==0:
                            print('PLEASE ADD AT LEAST ONE ITEM.')
                            continue
                        name=input('ENTER THE CUSTOMER NAME:-')
                        mob=int(input('ENTER THE CUSTOMER MOB NUM:-'))
                        print('________________________________')
                        print('             BILL               ')
                        print('________________________________')
                        print(f'''NAME  :-    {name}''')
                        print(f'''MOB NUM:-   {mob}''')
                        print('_________________________________')
                        if qty1>0:
                            print(f'''MARGHERITA PIZZA     X{qty1}    {d1}''')
                        if qty2>0:
                            print(f'''MAC N CHEESE PASTA    X{qty2}    {d2}''')
                        if qty3>0:
                            print(f'''GRILLED SANDWICH      X{qty3}    {d3}''')
                        print('________________________________')
                        print(f'''TOTAL BILL :-           {total_bill}''')
                        print('______________________________________')
                        
                        import random
                        import math
                        def otp():
                            otps=math.floor(random.random() * 10000)
                            return otps
                        def pay():
                            while True:
                                print('''
                                ___________________________________
                                    CHOOSE PAYMENT METHOD
                                ____________________________________
                                    1. CASH
                                    2. CARD 
                                    3. UPI
                                    4. EXIT
                                ____________________________________
                                ''')
                                payment= int(input('SELECT THE PAYMENT METHOD:-'))
                                match payment:
                                    case 1:
                                        cash=int(input('ENTER THE CASH AMOUNT:-'))
        
                                        if cash > total_bill:
                                            more_cash= cash-total_bill
                                            print('___________________________________')
                                            print('PAYMENT SUCCESSFUL!')
                                            print(f'''{cash}    - {total_bill} = {more_cash}/-''')
                                            print('____________________________________')
                                            print('ORDER CONFIRMED!')
                                            print(f'''CHANGE RETURN  -->  {more_cash}/-''')
                                            print('_____________________________________')
                                            print('THANK YOU FOR VISITING FURL STATION!')
                                            print('_________________________________')
                                            break
                                            
                                        if cash < total_bill:
                                            less_cash= total_bill - cash
                                            print('_____________________________________')
                                            print('INSUFFICIENT AMOUNT!')
                                            print(f'''REMAINING AMOUNT  --> {less_cash}/-''')
                                            print('________________________________________')
                                            extra = int(input("ENTER REMAINING CASH: "))
                                            cash=cash+extra
                                            if cash > total_bill:
                                                nbill= cash - total_bill
                                                print('___________________________________')
                                                print('PAYMENT SUCCESSFUL!')
                                                print(f'''{cash}    - {total_bill} = {nbill}/-''')
                                                print('____________________________________')
                                                print('ORDER CONFIRMED!')
                                                print(f'''CHANGE RETURN  -->  {nbill}/-''')
                                                print('_____________________________________')
                                                print('THANK YOU FOR VISITING FUEL STATION!')
                                                print('_____________________________________')
                                                break
                                            if cash< total_bill:
                                                print('_____________________________________')
                                                print('INSUFFICIENT AMOUNT!')
                                                print(f'''REMAINING AMOUNT  --> {less_cash}/-''')
                                                print('________________________________________')
                                            if cash==total_bill:
                                                print('_________________________')
                                                print('PAYMENT IS SUCCESSFUL!')
                                                print('ORDER CONFIRMED!')
                                                print('_________________________')
                                                print('THANK YOU FOR VISITING FUEL STATION!')
                                                print('__________________________')
                                                break
                                        if cash==total_bill:
                                            print('_________________________')
                                            print('PAYMENT IS SUCCESSFUL!')
                                            print('ORDER CONFIRMED!')
                                            print('_________________________')
                                            print('THANK YOU FOR VISITING FUEL STATION!')
                                            print('__________________________')
                                            break
                                    case 2:
                                        card_num=input('ENTER THE CARD NUM:-')
                                        if len(str(card_num))==16:
                                            cvv=input('ENTER THE CVV NUM:-')
                                            if len(str(cvv))==3:
                                                uotp=otp()
                                                print('YOUR OTP NO:-',uotp)
                                                eotp=int(input('ENTER THE OTP:-'))
                                            if uotp==eotp:
                                                print('________________________________')
                                                print('PAYMENT IS SUCCESSFULLY PAID!')
                                                print('ORDER CONFIRMED!')
                                                print('________________________________')
                                                break
                                            else:
                                                print('INVALID OTP!')
                                        else:
                                            print('INVALID CARD NUMBER!')
                                            break
                            
                                    case 3:
                                        uid=input('ENTER THE UPI ID:-')
                                        pin=input('ENTER THE PIN :-')
                                        print(f'''{total_bill}/-  PAID!''')
                                        print('____________________________________')
                                        print('PAYMENT SUCCESSFULLY PAID !')
                                        print('____________________________________')
                                        break
                                    
                                    case 4:
                                        print('THANK YOU FOR VISITING!')
                                        break
                                    case _:
                                        print('INVALID CHOICE')
                        pay()
                        break
                    case _:
                        print('INVALID CHOICE')
        fuelstation()
    case 3:
        def frullato():
            qty1=0
            qty2=0
            qty3=0
            while True:
                dish = ['NUTELLA BROWNIE','KITKAT SHAKE','NUTELLA HAZELNUTS']
                price = [160,200,130]
                print('''
                __________________________________
                           FRULLATO
                ___________________________________
                     0.NUTELLA BROWNIE   : 160/-
                     1.KITKAT SHAKE      : 200/-
                     2.NUTELLA HAZELNUTS : 130/-
                     3.BILL
                ___________________________________    
                 ''')
                ch=int(input('WHAT DO YOU WANTS TO EAT?'))
                match ch:
                    case 0:
                        qty1=int(input('ENTER THE QUANTITY:- '))
                        d1= price[0] *qty1
                    case 1:
                        qty2=int(input('ENTER THE QUANTITY:- '))
                        d2= price[1] *qty2
                    case 2:
                        qty3=int(input('ENTER THE QUANTITY:- '))
                        d3= price[2] *qty3
                    case 3:
                        total_bill= qty1 * 160+ qty2 *200+ qty3*130
                        if total_bill==0:
                            print('PLEASE ADD AT LEAST ONE ITEM.')
                            continue
                        name=input('ENTER THE CUSTOMER NAME:-')
                        mob=int(input('ENTER THE CUSTOMER MOB NUM:-'))
                        print('________________________________')
                        print('             BILL               ')
                        print('________________________________')
                        print(f'''NAME  :-    {name}''')
                        print(f'''MOB NUM:-   {mob}''')
                        print('_________________________________')
                        if qty1>0:
                            print(f'''NUTELLA BROWNIE     X{qty1}    {d1}''')
                        if qty2>0:
                            print(f'''KITKAT SHAKE        X{qty2}    {d2}''')
                        if qty3>0:
                            print(f'''NUTELLA HAZELNUTS   X{qty3}    {d3}''')
                        print('________________________________')
                        print(f'''TOTAL BILL :-           {total_bill}''')
                        print('______________________________________')
                        
                        import random
                        import math
                        def otp():
                            otps=math.floor(random.random() * 10000)
                            return otps
                        def pay():
                            while True:
                                print('''
                                ___________________________________
                                    CHOOSE PAYMENT METHOD
                                ____________________________________
                                    1. CASH
                                    2. CARD 
                                    3. UPI
                                    4. EXIT
                                ____________________________________
                                ''')
                                payment= int(input('SELECT THE PAYMENT METHOD:-'))
                                match payment:
                                    case 1:
                                        cash=int(input('ENTER THE CASH AMOUNT:-'))
        
                                        if cash > total_bill:
                                            more_cash= cash-total_bill
                                            print('___________________________________')
                                            print('PAYMENT SUCCESSFUL!')
                                            print(f'''{cash}    - {total_bill} = {more_cash}/-''')
                                            print('____________________________________')
                                            print('ORDER CONFIRMED!')
                                            print(f'''CHANGE RETURN  -->  {more_cash}/-''')
                                            print('_____________________________________')
                                            print('THANK YOU FOR VISITING FRULLATO!')
                                            print('_________________________________')
                                            break
                                            
                                        if cash < total_bill:
                                            less_cash= total_bill - cash
                                            print('_____________________________________')
                                            print('INSUFFICIENT AMOUNT!')
                                            print(f'''REMAINING AMOUNT  --> {less_cash}/-''')
                                            print('________________________________________')
                                            extra = int(input("ENTER REMAINING CASH: "))
                                            cash=cash+extra
                                            if cash > total_bill:
                                                nbill= cash - total_bill
                                                print('___________________________________')
                                                print('PAYMENT SUCCESSFUL!')
                                                print(f'''{cash}    - {total_bill} = {nbill}/-''')
                                                print('____________________________________')
                                                print('ORDER CONFIRMED!')
                                                print(f'''CHANGE RETURN  -->  {nbill}/-''')
                                                print('_____________________________________')
                                                print('THANK YOU FOR VISITING FRULLATO!')
                                                print('_____________________________________')
                                                break
                                            if cash< total_bill:
                                                print('_____________________________________')
                                                print('INSUFFICIENT AMOUNT!')
                                                print(f'''REMAINING AMOUNT  --> {less_cash}/-''')
                                                print('________________________________________')
                                            if cash==total_bill:
                                                print('_________________________')
                                                print('PAYMENT IS SUCCESSFUL!')
                                                print('ORDER CONFIRMED!')
                                                print('_________________________')
                                                print('THANK YOU FOR VISITING FRULLATO!')
                                                print('__________________________')
                                                break
                                        if cash==total_bill:
                                            print('_________________________')
                                            print('PAYMENT IS SUCCESSFUL!')
                                            print('ORDER CONFIRMED!')
                                            print('_________________________')
                                            print('THANK YOU FOR VISITING FRULLATO!')
                                            print('__________________________')
                                            break
                                    case 2:
                                        card_num=input('ENTER THE CARD NUM:-')
                                        if len(str(card_num))==16:
                                            cvv=input('ENTER THE CVV NUM:-')
                                            if len(str(cvv))==3:
                                                uotp=otp()
                                                print('YOUR OTP NO:-',uotp)
                                                eotp=int(input('ENTER THE OTP:-'))
                                            if uotp==eotp:
                                                print('________________________________')
                                                print('PAYMENT IS SUCCESSFULLY PAID!')
                                                print('ORDER CONFIRMED!')
                                                print('________________________________')
                                                break
                                            else:
                                                print('INVALID OTP!')
                                        else:
                                            print('INVALID CARD NUMBER!')
                                            break
                            
                                    case 3:
                                        uid=input('ENTER THE UPI ID:-')
                                        pin=input('ENTER THE PIN :-')
                                        print(f'''{total_bill}/-  PAID!''')
                                        print('____________________________________')
                                        print('PAYMENT SUCCESSFULLY PAID !')
                                        print('____________________________________')
                                        break
                                    
                                    case 4:
                                        print('THANK YOU FOR VISITING!')
                                        break
                                    case _:
                                        print('INVALID CHOICE')
                        pay()
                        break
                    case _:
                        print('INVALID CHOICE')
        frullato()
    case 4:
        print('THANK YOU!! ')
    case _:
        print('INAVALID CHOICE')