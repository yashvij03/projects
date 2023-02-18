import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="anjali",database="project")
if mycon.is_connected():
    cursor1=mycon.cursor()

    #Creating Table to store Customer deatils
    comm1="Create table if not exists cus_details(C_id varchar(5) Primary key,Name varchar(30),  Age varchar(3), Phone varchar(12), Email varchar(20), Address varchar(30),Aadhar varchar(12));"
    cursor1.execute(comm1)
    #Creating Table to store room details
    comm2="Create table if not exists Rooms(C_id varchar(5) Primary key, RoomNo varchar(5), Room_type varchar (20), Days int (5), Checkin date, checkout date, Room_bill float(8,2));"
    cursor1.execute(comm2)
    #Creating Table to store restaurant data
    comm3="Create table if not exists restaurant(C_id varchar(5), Thaali varchar (20), Quantity int(3), Food_Bill float(7,2));"
    cursor1.execute(comm3)

    def newbooking():
        print("Enter New Customer Data")
        cid=input("Customer ID:")
        name=input("Enter Name:")
        age=input("Age:")
        phone=input("Contact No.:")
        mail=input("Email:")
        addr=input("Address:")
        aadh=input("Aadhar No.:")
        detail="'"+str(cid)+"','"+str(name)+"',"+str(age)+","+str(phone)+",'"+str(mail)+"','"+str(addr)+"',"+str(aadh)
        comm1="insert into cus_details values("+detail+");"
        cursor1.execute(comm1)

        print("    ")
        print("Select room type")
        print("1. Ultra Royal ----> Rs. 10,000 per day")
        print("2. Royal         ----> Rs. 5,000 per day")
        print("3. Elite            ----> Rs. 3,500 per day")
        print("4. Budget       ----> Rs. 2,500 per day")
        print("   ")
        roomchoice=int(input("Enter room choice:"))
        days=int(input("Duration of stay:"))
        checkin=input("Date of check-in (YYYY-MM-DD):")
        checkout=input("Date of check-out (YYYY-MM-DD):")
        roomno=input("Room No.:")
        roomtype=0
        roombill=0
        if roomchoice==1:
            roomtype="Ultra Royal"
            roombill= days*10000
            print("Ultra Royal room no.", roomno, "booked for",days,"days.")
            print("Enjoy your stay.")
        elif roomchoice==2:
            roomtype="Royal"
            roombill=days*5000
            print("Royal room no.", roomno, "booked for",days,"days.")
            print("Enjoy your stay.")
        elif roomchoice==3:
            roomtype="Elite"
            roombill=3500*days
            print("Elite room no.", roomno, "booked for",days,"days.")
            print("Enjoy your stay.")
        elif roomchoice==4:
            roomtype="Budget"
            roombill=2500*days
            print("Budget room no.", roomno, "booked for",days,"days.")
            print("Enjoy your stay.")
        else:
            print("Incorrect Input! Please try again")
        str(roombill)
        room= str(cid)+"','"+str(roomno)+"','"+str(roomtype)+"',"+str(days)+",'"+str(checkin)+"','"+str(checkout)+"',"+str(roombill)
        comm2="insert into rooms values('"+room+");"
        cursor1.execute(comm2)

        mycon.commit()
        return

    def oldbooking():
        cname=input("Enter customer name:")
        cid=input("Enter customer ID:")
        print(" ")
        print("1. View Customer details")
        print("2. Viwe Customer stay details")
        print("3. View Customer Bill")
        print(" ")
        option=int(input("Enter choice:"))
        data=()
        if option==1:
            comm="Select * from cus_details where c_id='"+str(cid)+"';"
            cursor1.execute(comm)
            data=cursor1.fetchone()
            print("Name:",data[1])
            print("Age:",data[2])
            print("Phone:",data[3])
            print("Mail:",data[4])
            print("Address:",data[5])
            print("Aadhar no.:",data[6])
        elif option==2:
            comm="select * from rooms where c_id='"+str(cid)+"';"
            cursor1.execute(comm)
            data=cursor1.fetchone()
            print("Room no.:",data[1])
            print("Room type:",data[2])
            print("Duration of stay:",data[3])
            print("Check-in date:",data[4])
            print("Check-out date:",data[5])
        elif option==3:
            comm1="select * from rooms where c_id='"+str(cid)+"';"
            cursor1.execute(comm1)
            data1=cursor1.fetchone()
            comm2="select * from restaurant where c_id='"+str(cid)+"';"
            cursor1.execute(comm2)
            data2=cursor1.fetchone()
            print("Room bill:",data1[6])
            print("Food bill:",data2[3])
            print("Total bill:",float(data1[6])+float(data2[3]))
           
        else:
            print("Incorrect input! Try again.")
        return

    def Bill():
        cid=input("Enter Customer ID:")
        comm1="select * from rooms where c_id='"+str(cid)+"';"
        cursor1.execute(comm1)
        data1=cursor1.fetchone()
        comm2="select * from restaurant where c_id='"+str(cid)+"';"
        cursor1.execute(comm2)
        data2=cursor1.fetchone()
        print("Room bill:",data1[6])
        print("Food bill:",data2[3])
        print("Total bill:",float(data1[6])+float(data2[3]))
        return
        
    def Restaurant():
        cid=input("Enter Customer ID:")
        print("Select a meal")
        print("1. Veg Regular Thaali               ----> Rs. 300")
        print("2. Veg Exclusive Thaali           ----> Rs. 450")
        print("3. Non-Veg Regular Thaali     ----> Rs. 500")
        print("4. Non-Veg Exclusive Thaali  ----> Rs.700")
        dish=int(input("Enter choice:"))
        qty=int(input("Enter quantity:"))
        resbill=0
        meal=0
        if dish==1:
            meal="Veg Regular"
            resbill=300*qty
            print("Order for",qty,"Veg Regular Thaali(s) placed.")
        elif dish==2:
            meal="Veg Exclusive"
            resbill=450*qty
            print("Order for",qty,"Veg Exclusive Thaali(s) placed.")
        elif dish==3:
            meal="Non-Veg Regular"
            resbill=500*qty
            print("Order for",qty,"Non-Veg Regular Thaali(s) placed.")
        elif dish==4:
            meal="Non-veg Exclusive"
            resbill=700*qty
            print("Order for",qty,"Non-Veg Exclusive Thaali(s) placed.")
        else:
            print("Incorrect Input! Try again.")

        res="'"+str(cid)+"','"+str(meal)+"','"+str(qty)+"','"+str(resbill)+"'"
        comm="Insert into Restaurant values("+res+");"
        cursor1.execute(comm)

        mycon.commit()
        return
        
    #Main Page
    print("****** WELOME TO HOTEL            ******")
    while True:
        print(" ")
        print(" ")
        print("1 ----> Create New Booking")
        print("2 ----> View Old Booking")
        print("3 ----> Restaurant Services")
        print("4 ----> Customer Bill")
        print("5 ----> Exit")
        print("    ")
        choice=int(input("Enter choice:"))
        if choice==1:
            newbooking()
        elif choice==2:
            oldbooking()
        elif choice==3:
            Restaurant()
        elif choice==4:
            Bill()
        elif choice==5:
            break
        else:
            print("Incorrect input! Try again")
    
newbooking()

    
    
