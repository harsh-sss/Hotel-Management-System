import mysql.connector
import datetime
mydb=mysql.connector.connect(user='root',password='123456',host='localhost',database='hotel')
mycursor=mydb.cursor()
while True:
    print("\n\n\t\t WELCOME TO HOTEL RED VELVET")                                             
    print("\t    Place where Guests treated like God")  
    print("------------------------------------------------------------|")
    print("|Address: Marine Lines near Wankhede Stadium,MUMBAI         |")
    print("|PHNO.1: 9861212512           PHNO.2: 022254555             |")
    print("|S.T NO.: 3214454654544       PAN NO.: 5454565556554        |")
    print("|CIN NO.: ADD244564DF         GST NO.: 12154555DSF          |")
    print("|-----------------------------------------------------------|")
    print("***********************************************************")
    print("            WISHING YOU A GOOD STAY                        ")
    print("             FROM TEAM RED VELVET                          ")
    print("***********************************************************")
    print("\n1.Hotel")
    print("\n2.Restaurant")
    print("\n3.Wedding Halls For Rent")
    print("\n4.Exit")
    ch=int(input("\nENTER YOUR CHOICE FROM THE ABOVE MENU "))
    def hotel():
        ans='y'
        while(ans=='y' or ans=='Y'):
            h=input("\nDO YOU WANT TO PROCEED FURTHER.....Enter y/n ")        
            if (h=='y'):
                print("\n\tMENU")
                print("\n1.ROOM DETAILS ")
                print("\n2.REGISTRATION ")
                print("\n3.BOOKING ")
                print("\n4.LAUNDARY PRICES ")
                print("\n5.ROOM SERVICE PRICES ")
                ch1=int(input("\nENTER CHOICE FROM THE MENU ABOVE "))
                def roomdetail():
                    print("\n\n")
                    sql='select*from roomdetail'
                    mycursor.execute(sql)
                    rows=mycursor.fetchall()
                    for x in rows:
                        print(x)
                def registration():
                    nm=input("\nENTER YOUR NAME ")
                    add=input("\nENTER YOUR ADDRESS ")
                    phno=int(input("\nENTER YOUR PHONE NUMBER "))
                    chck_in=input("\nENTER CHECK-IN DATE(YYYY-MM-DD) ")
                    chck_out=input("\nENTER CHECK-OUT DATE(YYYY-MM-DD) ")
                    print("***************************************************")
                    print("YOUR FIRST STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                    print("***************************************************")
                    sql="insert into registcust(name,address,phno,CHECKIN,CHECKOUT)values('{}','{}','{}','{}','{}')".format(nm,add,phno,chck_in,chck_out)
                    mycursor.execute(sql)
                    mydb.commit()
                def booking():
                    print("__________________________________________________________________________")
                    print("\n\n\t ****ROOM BOOKING PROCEDURE****\n")
                    
                    print("__________________________________________________________________________")
                    
                    print("\n\tROOMS AVAILABLE")
                    print("\n1.  2-SINGLE BED NON-AC Room")
                    print("2.  1-DOUBLE BED NON-AC Room")
                    print("3.  2-SINGLE BED AC Room")
                    print("4.  1-DOUBLE BED AC Room")
                    ch1=int(input("\nENTER YOUR ROOM CHOICE "))
                    N=int(input("\nENTER NUMBER OF DAYS/NIGHTS TO STAY "))
                    
                    if ch1==1:
                        cst=1500*N
                        print("_____________________________________________________")
                        print("|\t******HOTEL RED VELVET******                 |")
                        print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                        print("|----------------------------------------------------|")
                        print("|ROOM\t\t\t\tPRICE(in Rs.)        |")
                        print("|--------\t\t\t-----------          |")
                        print("|2-SINGLE BED NON-AC Room\t 1500                |")
                        
                        print("|NUMBER OF DAYS LIVING-\t\t",N,"Days              |")
                        
                        print("|----------------------------------------------------|")
                        print("|FINAL AMOUNT\t\t\tRS.",cst,"            |")
                        print("|\t\tTHANKYOU:)!!!                        |")
                        print("_____________________________________________________")
                        print("\n****************************************************")
                        print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                        print("****************************************************")
                        print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                        
                    elif ch1==2:
                        cst=2000*N
                        print("_____________________________________________________")
                        print("|\t******HOTEL RED VELVET******                 |")
                        print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                        print("|----------------------------------------------------|")
                        print("|ROOM\t\t\t\tPRICE(in Rs.)        |")
                        print("|--------\t\t\t-----------          |")
                        print("|1-DOUBLE BED NON-AC Room\t 2000                |")
                        
                        print("|NUMBER OF DAYS LIVING-\t\t",N,"Days              |")
                        
                        print("|----------------------------------------------------|")
                        print("|FINAL AMOUNT\t\t\tRS.",cst,"            |")
                        print("|\t\tTHANKYOU:)!!!                        |")
                        print("_____________________________________________________")
                        print("\n****************************************************")
                        print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                        print("****************************************************")
                        print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                        
                        
                    elif ch1==3:
                        cst=2500*N
                        print("_____________________________________________________")
                        print("|\t******HOTEL RED VELVET******                 |")
                        print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                        print("|----------------------------------------------------|")
                        print("|ROOM\t\t\t\tPRICE(in Rs.)        |")
                        print("|--------\t\t\t-----------          |")
                        print("|2-SINGLE BED AC Room\t\t2500                 |")
                        
                        print("|NUMBER OF DAYS LIVING-\t\t",N,"Days              |")
                        
                        print("|----------------------------------------------------|")
                        print("|FINAL AMOUNT\t\t\tRS.",cst,"            |")
                        print("|\t\tTHANKYOU:)!!!                        |")
                        print("_____________________________________________________")
                        print("\n****************************************************")
                        print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                        print("****************************************************")
                        print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                        
                        
                    elif ch1==4:
                        cst=3000*N
                        print("_____________________________________________________")
                        print("|\t******HOTEL RED VELVET******                 |")
                        print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                        print("|----------------------------------------------------|")
                        print("|ROOM\t\t\t\tPRICE(in Rs.)        |")
                        print("|--------\t\t\t-----------          |")
                        print("|1-DOUBLE BED AC Room\t\t3000                 |")
                        
                        print("|NUMBER OF DAYS LIVING-\t\t",N,"Days              |")
                        
                        print("|----------------------------------------------------|")
                        print("|FINAL AMOUNT\t\t\tRS.",cst,"            |")
                        print("|\t\tTHANKYOU:)!!!                        |")
                        print("_____________________________________________________")
                        print("\n****************************************************")
                        print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                        print("****************************************************")
                        print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                        
                    else:
                        print("\nWRONG CHOICE")
                def laundary():
                    sql="select * from laundary"
                    mycursor.execute(sql)
                    rows=mycursor.fetchall()
                    for x in rows:
                        print(x)
                    p=0
                    q=0
                    r=0
                    ch7=int(input("Enter your choice "))
                    def ln1():
                        x=(p+1)*100
                        print("\nCOST FOR BLEACHING",x)
                    def ln2():
                        x=(q+1)*50
                        print("\nCOST FOR WASHING",x)
                    def ln3():
                        x=(r+1)*25
                        print("\nCOST FOR CLOTH IRON",x)
                    if ch7==1:
                        ln1()
                    if ch7==2:
                        ln2()
                    if ch7==3:
                        ln3()
                def rmsv():
                    sql="select * from roomservice"
                    mycursor.execute(sql)
                    rows=mycursor.fetchall()
                    for x in rows:
                        print(x)
                    p=0
                    q=0
                    r=0
                    d=0
                    ch7=int(input("Enter your choice "))
                    def ln1():
                        x=(p+1)*100
                        print("\nCOST FOR SWEEPING",x)
                    def ln2():
                        x=(q+1)*100
                        print("\nCOST FOR MOPPING",x)
                    def ln3():
                        x=(r+1)*150
                        print("\nCOST FOR DISH CLEANING",x)
                    def ln4():
                        x=(d+1)*35
                        print("\nCOST FOR BOTTLE IRON",x)
                    if ch7==1:
                        ln1()
                    if ch7==2:
                        ln2()
                    if ch7==3:
                        ln3()
                    if ch7==4:
                        ln4()
                if ch1==1:
                    roomdetail()
                if ch1==2:
                    registration()
                if ch1==3:
                    booking()
                if ch1==4:
                    laundary()
                if ch1==5:
                    rmsv()
            else:
                print("OK....NOTED")
                break
              
        

    def restaurantmenu():
        ans='y'
        while(ans=='y' or ans=='Y'):
            z=input("DO YOU WANT TO SEE RESTAURANT MENU.....ENTER y/n ")
            if (z=='y'):
                print("\n\tMENU")
                print("\n1.Beverages")
                print("\n2.Punjabi food")
                print("\n3.South Indian Food")
                print("\n4.Dessert")
                ans1='y'
                while(ans1=='y' or ans1=='Y'):
                    k=input("\nOrder....Delicious food (y/n) ")
                    if (k=='y'):
                        ch2=int(input("\nEnter Your food option "))
                       
                        if ch2==1:
                            sql="select * from beverages"
                            mycursor.execute(sql)
                            rows=mycursor.fetchall()
                            for x in rows:
                                print(x)
                
                            print("\nPLEASE SELECT THE ITEMS YOU WANT TO ORDER FROM BEVERAGES")
                            ch3=int(input("\nEnter Beverages item no. "))
                            m=int(input("\nEnter Quantity "))
                            print("\n*****************************")
                            print("ORDER NOTED !!")
                            print("WILL SERVE YOU IN FEW MINUTES")
                            print("THANKYOU!!")
                            print("Final BILL is being Processed")
                            if ch3==1:
                                x=20*m
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Regular tea\t\t\tRs.20                |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",m,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"              |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                                
                            elif ch3==2:
                                x=25*m
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|MASALA tea\t\t\tRs.25                |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",m,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"              |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch3==3:
                                x=25*m
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Coffee\t\t\t\tRs.25                |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",m,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"              |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch3==4:
                                x=25*m
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Cold drink\t\t\tRs.25                |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",m,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"              |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch3==5:
                                x=200*m
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|ALCOOLIC DRINK\t\t\tRs.200               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",m,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            else:
                                print("\nWrong Choice")
                        if ch2==2:
                            sql="select * from punjabi order by DISHNO ASC"
                            mycursor.execute(sql)
                            rows=mycursor.fetchall()
                            for x in rows:
                                print(x)
                            print("\nPLEASE SELECT THE ITEMS YOU WANT TO ORDER FROM PUNJABI DISHES")
                            ch4=int(input("\nEnter Punjabi item no. "))
                            b=int(input("\nEnter Quantity "))
                            print("\n**********************************************")
                            print("ORDER COMPLETED FOR PUNJABI DISHES!!")
                            print("YOUR FOOD WILL BE SERVED IN FEW MINUTES")
                            print("\t THANKYOU!")
                            print("************************************************")
                            if ch4==1:
                                x=110*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Shahi Paneer\t\t\tRs.110               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                                
                            elif ch4==2:
                                x=140*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Kadai Paneer\t\t\tRs.140               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch4==3:
                                x=150*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Handi Paneer\t\t\tRs.150               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch4==4:
                                x=140*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Palak Paneer\t\t\tRs.140               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch4==5:
                                x=100*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Chilli Paneer\t\t\tRs.100               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch4==6:
                                x=110*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Mix Veg\t\t\tRs.110               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch4==7:
                                x=130*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Aloo Matar\t\t\tRs.130               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch4==8:
                                x=150*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Dal Fry\t\t\tRs.150               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch4==9:
                                x=150*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Dal Tadka\t\t\tRs.150               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch4==10:
                                x=20*b
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Plain Roti\t\t\tRs.20                |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",b,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            else:
                                print("\nWrong Choice")
                        if ch2==3:
                            sql="select * from southindian"
                            mycursor.execute(sql)
                            rows=mycursor.fetchall()
                            for x in rows:
                                print(x)
                            print("\nPLEASE SELECT THE ITEMS YOU WANT TO ORDER FROM SOUTHINDIAN DISHES")
                            ch5=int(input("\nEnter southindian item no. "))
                            a=int(input("\nEnter Quantity "))
                            print("\n***********************************")
                            print("YOUR ORDER COMPLETED FOR SOUTHINDIAN DISHES")
                            print("YOUR FOOD WILL BE SERVED IN FEW MINUTES")
                            print("\tTHANKYOU!!")
                            print("*************************************")
                            if ch5==1:
                                x=100*a
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Plain Dosa\t\t\tRs.100               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",a,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch5==2:
                                x=130*a
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Rice Idli\t\t\tRs.130               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",a,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch5==3:
                                x=150*a
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Paneer Dosa\t\t\tRs.150               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",a,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch5==4:
                                x=120*a
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|VadaSambhar\t\t\tRs.120               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",a,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch5==5:
                                x=140*a
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Onion Dosa\t\t\tRs.140               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",a,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch5==6:
                                x=100*a
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Plain Rice\t\t\tRs.100               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",a,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch5==7:
                                x=100*a
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Rasam\t\t\tRs.100               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",a,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch5==8:
                                x=150*a
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Appam\t\t\tRs.150               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",a,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            else:
                                print("\nWrong Choice")
                        if ch2==4:
                            sql="select * from desert"
                            mycursor.execute(sql)
                            rows=mycursor.fetchall()
                            for x in rows:
                                print(x)
                            print("\nPLEASE SELECT THE ITEMS YOU WANT TO ORDER FROM DESSERTS") 
                            ch6=int(input("\nENTER DESSERT NUMBER "))
                            c=int(input("\nENTER QUANTITY "))
                            print("\n******************************************")
                            print("YOUR ORDER COMPLETED FOR DESSERTS")
                            print("YOUR FOOD WILL BE SERVED IN FEW MINUTES")
                            print("\tTHANKYOU!!")
                            print("********************************************") 
                            if ch6==1:
                                x=60*c
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Vanilla Ice Cream\t\t\tRs.60               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",c,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch6==2:
                                x=45*c
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Strawberry Ice Cream\t\t\tRs.45               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",c,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch6==3:
                                x=80*c
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Pineapple Ice Cream\t\tRs.80                |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",c,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch6==4:
                                x=80*c
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Chocolate Ice Cream\t\t\tRs.80          |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",c,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            elif ch6==5:
                                x=80*c
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|DISH\t\t\t\tPRICE(in Rs.)        |")
                                print("|--------\t\t\t-----------          |")
                                print("|Hot Chocolate\t\t\tRs.80               |")
                                print("|                                                    |")
                                print("|                                                    |")
                                print("|QUANTITY-\t\t\t",c,"                  |")
                                
                                print("|----------------------------------------------------|")
                                print("|FINAL AMOUNT\t\t\tRS.",x,"             |")
                                print("|\t\tTHANKYOU:)!!!                        |")
                                print("_____________________________________________________")
                                print("\n****************************************************")
                                print("YOUR SECOND STEP FOR MAGESTIC EXPERIENCE COMPLETED!!")
                                print("****************************************************")
                                print("\nPlease pay the following Amount to unlock the key for Magestic Expereince")
                            else:
                                print("\nWRONG CHOICE")
                    else:
                        print("OK NOTED")
                        break
            else:
                print("OK.....NOTED")
                break
            
    def weddinghall():
        sql='select*from hall'
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
        ans='y'
        while(ans=='y'):
            m=input("\nDO YOU WANT TO REGISTER.....y/n ")
            if (m=='y'):
                ch9=int(input("\nEnter Your Hall Category "))
                h=input("\nEnter Your Name ")
                g=input("\nEnter Your Address ")
                phno1=int(input("\nEnter Your Phone No."))
                dte=input("\nEnter Date of Hall Booking ")
                hr=int(input("\nEnter No. of Hours "))
                print("\n**********************************")
                print("HALL BOOKED!!!")
                print("Thankyou for booking the Hall!")
                print("************************************")
                sql="insert into registhall(NAME,ADDRESS,PHONE_NUMBER,DATE_OF_BOOKING)values('{}','{}','{}','{}')".format(h,g,phno1,dte)
                mycursor.execute(sql)
                mydb.commit()
                w=2000
                r=5000
                t=10000
                y=20000
                ans1='y'
                while(ans1=='y'):
                    n=input("\nDO YOU WANT CATERING FACILITY?.....y/n ")
                    if (n=='y'):
                        sql='select*from caterers'
                        mycursor.execute(sql)
                        rows=mycursor.fetchall()
                        for x in rows:
                            print(x)
                        print("\n**************************************")
                        print("YOU HAVE SELECTED THE CATERING FACILITY!")
                        print("****************************************")
                        ch8=int(input("\nENTER YOUR CHOICE OF CATERER "))
                        j=int(input("\nNumber of People "))
                        
                        if ch9==1:
                            if ch8==1:
                                d=550*j
                                print("\n**************************************")
                                print("You have selected SMALL HALL          ")
                                print("You have selected A1 CATERERS         ")
                                print("**************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   2000","               |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               550","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",w*hr+d,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==2:
                                e=520*j
                                print("\n*****************************************")
                                print("You have selected SMALL HALL             ")
                                print("You have selected FK CATERERS            ")
                                print("*****************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   2000","               |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               520","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",w*hr+e,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==3:
                                f=650*j
                                print("\n****************************************")
                                print("You have selected SMALL HALL            ")
                                print("You have selected MAHARAJA CATERERS     ")
                                print("****************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   2000","               |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               650","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",w*hr+f,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==4:
                                o=500*j
                                print("\n******************************************")
                                print("You have selected SMALL HALL              ")
                                print("You have selected UNIQUE CATERERS         ")
                                print("******************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   2000","               |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               550","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",w*hr+o,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            else:
                                print("Wrong Choice")
                        elif ch9==2:
                            if ch8==1:
                                d=550*j
                                print("\n********************************************")
                                print("You have selected MEDIUM HALL               ")
                                print("You have selected A1 CATERERS               ")
                                print("********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   5000","               |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               550","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",r*hr+d,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==2:
                                e=520*j
                                print("\n**********************************************")
                                print("You have selected MEDIUM HALL                 ")
                                print("You have selected FK caterers                 ")
                                print("**********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   5000","               |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               520","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",r*hr+e,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==3:
                                f=650*j
                                print("\n************************************************")
                                print("You have selected MEDIUM HALL                   ")
                                print("You have selected MAHARAJA CATERERS             ")
                                print("************************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   5000","               |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               650","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",r*hr+f,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break    
                            elif ch8==4:
                                o=500*j
                                print("\n***********************************************")
                                print("You have selected MEDIUM HALL                  ")
                                print("You have selected UNIQUE CATERERS              ")
                                print("***********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   5000","               |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               500","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",r*hr+o,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            else:
                                print("Wrong Choice")
                        elif ch9==3:
                            if ch8==1:
                                d=550*j
                                print("\n************************************************")
                                print("You have selected LARGE HALL                    ")
                                print("You have selected A1 CATERERS                   ")
                                print("************************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   10000","              |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               550","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",t*hr+d,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==2:
                                e=520*j
                                print("\n***********************************************")
                                print("You have selected LARGE HALL                   ")
                                print("You have selected FK CATERERS                  ")
                                print("***********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   10000","              |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               520","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",t*hr+e,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==3:
                                f=650*j
                                print("\n***********************************************")
                                print("You have selected LARGE HALL                   ")
                                print("You have selected MAHARAJA CATERERS            ")
                                print("***********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   10000","              |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               650","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",t*hr+f,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==4:
                                o=500*j
                                print("\n***********************************************")
                                print("You have selected LARGE HALL                   ")
                                print("You have selected UNIQUE CATERERS              ")
                                print("***********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   10000","              |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               500","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",t*hr+o,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            else:
                                print("\nWrong Choice")
                        elif ch9==4:
                            if ch8==1:
                                d=550*j
                                print("\n***********************************************")
                                print("You have selected LARGE HALL WITH LAWN         ")
                                print("You have selected A1 CATERERS                  ")
                                print("***********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   20000","              |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               550","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",y*hr+d,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==2:
                                e=520*j
                                print("\n***********************************************")
                                print("You have selected LARGE HALL WITH LAWN         ")
                                print("You have selected FK CATERERS                  ")
                                print("***********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   20000","              |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               520","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",y*hr+e,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==3:
                                f=650*j
                                print("\n***********************************************")
                                print("You have selected LARGE HALL WITH LAWN         ")
                                print("You have selected MAHARAJA CATERERS            ")
                                print("***********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   20000","              |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               650","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",y*hr+f,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            elif ch8==4:
                                o=500*j
                                print("\n***********************************************")
                                print("You have selected LARGE HALL WITH LAWN         ")
                                print("You have selected UNIQUE CATERERS              ")
                                print("***********************************************")
                                print("_____________________________________________________")
                                print("|\t******HOTEL RED VELVET******                 |")
                                print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                                print("|----------------------------------------------------|")
                                print("|Name: ",h,"                                         |")
                                print("|Address: ",g,"                                   |")
                                print("|Phone Number: ",phno1,"                           |             ")
                                print("|____________________________________________________|")
                                print("|COST OF LAWN:                   20000","              |")
                                print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                print("|COST OF CATERERS:               500","                |")
                                print("|No. of People","\t\t\t",j,"                |")
                                print("|----------------------------------------------------|")
                                print("|Final Cost:""\t\t\t",y*hr+o,"             |")
                                
                                print("|____________________________________________________| ")
                                print("\n*****************************************************")
                                print("\nBooked Successfully, Please pay the following amount")
                                break
                            else:
                                print("\nWrong Choice")
                                break
                        else:
                            print("\nWrong Choice")
                            break
                            
                            
                    elif (n=='n'):
                        print("\nOk...... No Caterers required")
                        if ch9==1:
                            print("_____________________________________________________")
                            print("|\t******HOTEL RED VELVET******                 |")
                            print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                            print("|----------------------------------------------------|")
                            print("|Name: ",h,"                                         |")
                            print("|Address: ",g,"                                   |")
                            print("|Phone Number: ",phno1,"                           |             ")
                            print("|____________________________________________________|")
                            print("|COST OF LAWN:                   2000","               |")
                            print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                            
                            print("|----------------------------------------------------|")
                            print("|Final Cost:""\t\t\t",w*hr,"               |")
                                
                            print("|____________________________________________________| ")
                            print("\n*****************************************************")
                            print("\nBooked Successfully, Please pay the following amount")
                            
                            break
                        elif ch9==2:
                            print("_____________________________________________________")
                            print("|\t******HOTEL RED VELVET******                 |")
                            print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                            print("|----------------------------------------------------|")
                            print("|Name: ",h,"                                         |")
                            print("|Address: ",g,"                                   |")
                            print("|Phone Number: ",phno1,"                           |             ")
                            print("|____________________________________________________|")
                            print("|COST OF LAWN:                   5000","               |")
                            print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                
                            print("|----------------------------------------------------|")
                            print("|Final Cost:""\t\t\t",r*hr,"              |")
                                
                            print("|____________________________________________________| ")
                            print("\n*****************************************************")
                            print("\nBooked Successfully, Please pay the following amount")
                            
                            break
                        elif ch9==3:
                            print("_____________________________________________________")
                            print("|\t******HOTEL RED VELVET******                 |")
                            print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                            print("|----------------------------------------------------|")
                            print("|Name: ",h,"                                         |")
                            print("|Address: ",g,"                                   |")
                            print("|Phone Number: ",phno1,"                           |             ")
                            print("|____________________________________________________|")
                            print("|COST OF LAWN:                   10000","                |")
                            print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                
                            print("|----------------------------------------------------|")
                            print("|Final Cost:""\t\t\t",t*hr,"              |")
                                
                            print("|____________________________________________________| ")
                            print("\n*****************************************************")
                            print("\nBooked Successfully, Please pay the following amount")
                            
                            break
                        elif ch9==4:
                            print("_____________________________________________________")
                            print("|\t******HOTEL RED VELVET******                 |")
                            print("|PAN NO.: 5454565556554\tGST NO.: 12154555DSF         |")
                            print("|----------------------------------------------------|")
                            print("|Name: ",h,"                                         |")
                            print("|Address: ",g,"                                   |")
                            print("|Phone Number: ",phno1,"                           |             ")
                            print("|____________________________________________________|")
                            print("|COST OF LAWN:                   20000","               |")
                            print("|No. of Hours:","\t\t\t" ,hr,"                  |")
                                
                            print("|----------------------------------------------------|")
                            print("|Final Cost:""\t\t\t",y*hr,"             |")
                                
                            print("|____________________________________________________| ")
                            print("\n*****************************************************")
                            print("\nBooked Successfully, Please pay the following amount")
                            
                            break
                    else:
                        print("\nWrong Choice Entered")
            elif(m=='n'):
                break
            else:
                print("\nWrong Choice")
                break
    def ext():
        exit()
                    
                    
                        
                
        
    if ch==1:
        hotel()
    if ch==2:
        restaurantmenu()
    if ch==3:
        weddinghall()
    if ch==4:
        ext()


    
 
        
        
    
    



    
    



