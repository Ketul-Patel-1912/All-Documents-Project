from csv import excel
from datetime import date
from distutils.util import execute
from multiprocessing import connection
from traceback import print_tb
from colorama import Cursor
import mysql.connector
from mysql.connector import Error
import pandas as pd

#def show_product_add()

print("""
__________________________________________
Welcome to Die inventory Management System
------------------------------------------
""")
mydb=mysql.connector.connect(host="127.0.0.1",
                                    port="3307",
                                    user="root",
                                    password="root")
mycursor = mydb.cursor()
mycursor.execute("Create database if not exists Die_Inventory_system")
mycursor.execute("use Die_inventory_system")
mycursor.execute("create table if not exists login(username varchar(25) not null, password varchar(25))")
mycursor.execute("create table if not exists Product_Add(ProductID int primary key auto_increment, Die_Name varchar(20) not null)")
mycursor.execute("Create table if not exists Transaction (Tran_ID int primary key auto_increment,Die_Name varchar(30) not null,Type1 varchar(30) not null,Type2 varchar(30) not null,Die_Number varchar(15) ,Qty int not null,Date date not null)")
mydb.commit()

##### -------- Adding Password------------

z=0
mycursor.execute("select * from login")
for i in mycursor:
    z+=1
if(z==0):
    mycursor.execute("insert into login values('username','k123')")
    mydb.commit()
    
while True:
    print("""1.Login
2.Show Report Card 
3.Show Transaction
4. Exit
""")
    
    ch=int(input("Enter Your Choice :-> "))
    if ch==1:
        passwrd=input("Enter Password :-> ")
        mycursor.execute("select * from login")
        for i in mycursor:
            username,password=i
        if(passwrd==password):
            print("""
                  _______
                  Welcome
                  ------- """)
            loop2='y'
            while (loop2=='y' or loop2=='Y'):
                print("""
    _____________________________________________
    1.0 Add Die's Name In Catelogue
    1.1. Deleting the catelogue
    1.2. Display Catelogue Items
    _____________________________________________
    2.0 All Transaction -- Purchase Die, Die Usages, Add Recycle Die
    2.1 Update Transaction Table
    2.2 Delete Items from Transaction Table
    2.3 Display All the Transaction 
    _____________________________________________
    3.0 Show Purchase Transaction Only
    3.1 Show Die Usage Transaction Only
    3.2 Show Number of Die Running in Production
    _____________________________________________
    4. Change Password
    5. Log out
    """)       
                ch=float(input("Enter Your Choice :-> "))
                
    #1.0 Add Die's Name In Catelogue 
               
                if ch==1.0:
                    loop='y'
                    while(loop=='y' or loop=='Y'):
                        
                        Die_Name=input("Enter Types Of Dies i.e-Inner,Middle,Outer :-> ")
                        mycursor.execute("insert into Product_Add(Die_Name) values('"+str(Die_Name)+"')")
                        mydb.commit()
                        print("""
                        _________________________
                        Record Added Sucessfully
                        -------------------------""")
                        
                    ## show record after data inserted....
                     
                        mycursor.execute("select * from Product_Add")
                        print("Sr.No || Die Name")
                        for i in mycursor:
                            t_srno,Die_name=i
                            print(f"{t_srno} || {Die_name}")   
                        
                        loop=input("Do You Want to Enter More Items? (Y/N) :-> ")
                    loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")


    
    # 1.1. Deleting the catelogue 
    
              
                elif (ch==1.1):
                    
                    loop='y'
                    while(loop=='y' or loop=="Y"):
                        
                        # before delete Show record
                        mycursor.execute("select * from Product_Add")
                        print("Sr.No || Die Name")
                        for i in mycursor:
                            t_srno,Die_name=i
                            print(f"{t_srno} || {Die_name}")
                            
                        # start deleting code 
                        srno=int(input("Enter Die Serial Number :-> "))
                        mycursor.execute("delete from Product_Add where ProductID = '"+str(srno)+"'")
                        mydb.commit()
                        
                        print("""
                        _________________________
                        Record Deleted Sucessfully
                        -------------------------""")
                        
                        # after delete show the recored
                        mycursor.execute("select * from Product_Add")
                        print("Sr.No || Die Name")
                        for i in mycursor:
                            t_srno,Die_name=i
                            print(f"{t_srno} || {Die_name}") 
                            
                        loop=input("Do You Want to Delete Any Other Record ? (Y/N) :-> ")
                    loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")
    
    # 1.2. Display Catelogue Items  
                 
                elif (ch==1.2):
                                          
                        mycursor.execute("select * from Product_Add")
                        print("Sr.No || Die Name")
                        for i in mycursor:
                            t_srno,Die_name=i
                            print(f"{t_srno} || {Die_name}")         
                       
                        loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")
                        
    # 2.0 All Transaction -- Purchase Die, Die Usages, Add Recycle Die
                       
    
                elif (ch==2.0):
                    
                        # first See The record avilable 
                    mycursor.execute("select * from transaction")
                    print("Sr.No || Die Name || Trans Type1 || Trans Type2 || Die Number || Qty || Entered Date")
                    print("--------------------------------------------------------------------------------------")
                    for i in mycursor:
                           
                            t_srno,t_Die_name,t_type1,t_type2,t_dieNumber,t_qty,t_todaydate=i
                            print(f"{t_srno}     || {t_Die_name}    || {t_type1}||   {t_type2}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
                            print("---------------------------------------------------------------------------------------------------")
                            
                            
                            
                    loop='y'
                    while(loop=='y' or loop=='Y'):    
                        
                        # add new record
                        Die_name_=input("Enter Die Name (Add Die name according Catelogue)  :-> ")
                        type1_=input("Enter Transaction Type (order, Use, Add, Production) :-> ")
                        type2_=input("Enter Transaction Type (Fresh, Recycle, Cancel, Scrap ) :-> ")
                        die_Number = input("Enter Die Number if required :-> ")
                        qty=int(input("Enter Qty :-> "))
                        

                        mycursor.execute("insert into Transaction(Die_Name,Type1,Type2,Die_Number,Qty,Date) values('"+str(Die_name_)+"','"+str(type1_)+"','"+str(type2_)+"','"+str(die_Number)+"','"+str(qty)+"',now())")
                        mydb.commit()
                        print("""
                        _________________________
                        Record Added Sucessfully
                        -------------------------""")
                        
                    ## show record after data inserted....
                     
                        mycursor.execute("select * from transaction")
                        print("Sr.No || Die Name || Trans Type1 || Trans Type2 || Die Number || Qty || Entered Date")
                        print("--------------------------------------------------------------------------------------")
                        for i in mycursor:
                           
                            t_srno,t_Die_name,t_type1,t_type2,t_dieNumber,t_qty,t_todaydate=i
                            print(f"{t_srno}     || {t_Die_name}    || {t_type1}||   {t_type2}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
                            print("---------------------------------------------------------------------------------------------------")
                        
                        loop=input("Do You Want to Enter More Items? (Y/N) :-> ")
                    loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")
                    
    # 2.1 Update Transaction Table

                elif (ch==2.1):
                    
                    # first See avialble Transaction record in Transaction table

                    mycursor.execute("select * from transaction")
                    print("Sr.No || Die Name || Trans Type1 || Trans Type2 || Die Number || Qty || Entered Date")
                    print("--------------------------------------------------------------------------------------")
                    for i in mycursor:
                           
                            t_srno,t_Die_name,t_type1,t_type2,t_dieNumber,t_qty,t_todaydate=i
                            print(f"{t_srno}     || {t_Die_name}    || {t_type1}||   {t_type2}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
                            print("---------------------------------------------------------------------------------------------------")
                            
                            
                            
                    loop='y'
                    while(loop=='y' or loop=='Y'):    
                        
                        # Update record code
                        u_srno=int(input("Enter Transaction Number :-> "))
                        u_Die_name=input("Enter Die Name (Outer Die,Middle Die..) :-> ")
                        u_type1_=input("Enter Transaction Type (Purchase, Use, Add, Production) :-> ")
                        u_type2_=input("Enter Transaction Type (Fresh, Recycle, Cancel, Scrap ) :-> ")
                        u_die_Number = input("Enter Die Number if required :-> ")
                        u_qty=int(input("Enter Qty :-> "))
                        u_date=input("Enter Date (YYYY-MM-DD) :-> ")
                        
                        mycursor.execute("update Transaction set Die_Name='"+str(u_Die_name)+"',Type1='"+str(u_type1_)+"',Type2='"+str(u_type2_)+"',Die_Number='"+str(u_die_Number)+"',Qty='"+str(u_qty)+"',Date='"+str(u_date)+"' where Tran_ID = '"+str(u_srno)+"'")
                        mydb.commit()
                        
                
                        
                        print("""
                        _________________________
                        Record Updated Sucessfully
                        -------------------------""")
                        
                    ## show record after data Updated....
                     
                        mycursor.execute("select * from transaction")
                        print("Sr.No || Die Name || Trans Type1 || Trans Type2 || Die Number || Qty || Entered Date")
                        print("--------------------------------------------------------------------------------------")
                        for i in mycursor:
                           
                            t_srno,t_Die_name,t_type1,t_type2,t_dieNumber,t_qty,t_todaydate=i
                            print(f"{t_srno}     || {t_Die_name}    || {t_type1}||   {t_type2}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
                            print("---------------------------------------------------------------------------------------------------")
                        
                        loop=input("Do You Want to Update More Items? (Y/N) :-> ")
                    loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")


    # 2.2 Delete Items from Transaction Table
    
                elif (ch==2.2):
                    
                    # first See avialble Transaction record in Transaction table
                    
                    mycursor.execute("select * from transaction")
                    print("Sr.No || Die Name || Trans Type1 || Trans Type2 || Die Number || Qty || Entered Date")
                    print("--------------------------------------------------------------------------------------")
                    for i in mycursor:
                           
                            t_srno,t_Die_name,t_type1,t_type2,t_dieNumber,t_qty,t_todaydate=i
                            print(f"{t_srno}     || {t_Die_name}    || {t_type1}||   {t_type2}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
                            print("---------------------------------------------------------------------------------------------------")
                                    
                    loop='y'
                    while(loop=='y' or loop=='Y'):    
                        
                        # Delete record code
                        d_srno=int(input("Enter Transaction Number :-> "))
  
                        mycursor.execute("delete from transaction where Tran_ID = '"+str(d_srno)+"'")
                        mydb.commit()
                        
                        print("""
                        _________________________
                        Record Deleted Sucessfully
                        -------------------------""")
                        
                    ## show record after data Deleted....
                        mycursor.execute("select * from transaction")
                        print("Sr.No || Die Name || Trans Type1 || Trans Type2 || Die Number || Qty || Entered Date")
                        print("--------------------------------------------------------------------------------------")
                        for i in mycursor:
                           
                            t_srno,t_Die_name,t_type1,t_type2,t_dieNumber,t_qty,t_todaydate=i
                            print(f"{t_srno}     || {t_Die_name}    || {t_type1}||   {t_type2}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
                            print("---------------------------------------------------------------------------------------------------")
                        
                        
                        loop=input("Do You Want to Deleted More Items? (Y/N) :-> ")
                    loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")

    # 2.3 Display All the Transaction  

                elif (ch==2.3):
  
                    mycursor.execute("select * from transaction")
                    print("Sr.No || Die Name || Trans Type1 || Trans Type2 || Die Number || Qty || Entered Date")
                    print("--------------------------------------------------------------------------------------")
                    for i in mycursor:
                           
                            t_srno,t_Die_name,t_type1,t_type2,t_dieNumber,t_qty,t_todaydate=i
                            print(f"{t_srno}     || {t_Die_name}    || {t_type1}||   {t_type2}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
                            print("---------------------------------------------------------------------------------------------------")                                    
    # 3.0 Show Purchase Transaction Only

                elif (ch==3.0):
                   
                    print("""
                          _____________________________ 
                          Total Purchased Transaction.........
                          ------------------------------
                          """)
                        
                    mycursor.execute("select Tran_ID,Die_Name,type1,qty,Date from Transaction where type1='order'")
                    print("Tran.No || Die Name || Tran Type1 ||  Qty || Order Date")
                    print("--------------------------------------------------------------------")
                    for i in mycursor:
                                t_srno,t_Die_name,t_type1,t_qty,t_todaydate=i
                                print(f"{t_srno}     || {t_Die_name}    || {t_type1} || {t_qty}  || {t_todaydate}")
                                print("---------------------------------------------------------------------------------------------------")
                                         
                    loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")
    
    #3.1 Show Die Usage Transaction Only
    
                elif (ch==3.1):
                   
                    print("""
                          _____________________________ 
                          Die Usage Transaction.........
                          ------------------------------
                          """)
                        
                    mycursor.execute("select * from transaction where type1='use'")
                    print("Sr.No || Die Name || Trans Type1 || Trans Type2 || Die Number || Qty || Entered Date")
                    print("--------------------------------------------------------------------------------------")
                    for i in mycursor:
                           
                            t_srno,t_Die_name,t_type1,t_type2,t_dieNumber,t_qty,t_todaydate=i
                            print(f"{t_srno}  || {t_Die_name}  || {t_type1}||   {t_type2}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
                            print("---------------------------------------------------------------------------------------------------")
                                         
                    loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")
    
    
    
    #3.2 Show Number of Die Running in Production
    
                elif (ch==3.2):
                   
                    print("""
                          ___________________________________
                          Number of Die Running in Production.........
                          -----------------------------------
                          """)
                        
                    mycursor.execute("select Tran_ID,Die_Name,Die_Number,qty,date from Transaction where type1 in('use') and type2 in('fresh','recycle')")
                    print("Tran.No || Die Name || Die Number || Qty || Entered Date")
                    print("--------------------------------------------------------------------------------------")
                    for i in mycursor:
                           
                            t_srno,t_Die_name,t_dieNumber,t_qty,t_todaydate=i
                            print(f"{t_srno}  || {t_Die_name}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
                            print("---------------------------------------------------------------------------------------------------")
                                         
                    loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")
    
    #4. Change Password
    
                elif (ch==4.0):
                    changepass=input("Enter New Password :-> ")
                    mycursor.execute("update login set password='"+str(changepass)+"'")
                    mydb.commit()
                    
                    print("""
                          ___________________________________
                          Your Password Has been Changed....
                          -----------------------------------
                          """)
                    
                    loop2=input("Do You Want to Continue Editing Stock? (Y/N) :-> ")   
                    
    #5. Log out     
               
                elif (ch==5.0):
                    break                 
                    
        else:
            print("""
                  ______________________
                  Wrong Password Entered
                  ----------------------""")
    
    ######----------------Second command Start From Here -------------------------------------
    
    # 2.Show Report Card
    
    elif (ch==2):
        
        print("""
    ______________________________________________________________________________
    Number Of Fresh Outer Die , NUmber Of Recycle Die, Total Running In Production 
    -------------------------------------------------------------------------------
     """)
        
        
        mycursor.execute("with cte1 as (select Die_Name,sum(qty) as qty from transaction where type1='order' and type2='fresh' group by Die_Name),cte2 as (select Die_Name,sum(qty)as qty2 from Transaction where type1='use' and type2='fresh' group by Die_Name),cte3 as (select Die_Name,sum(qty) as qty from Transaction where type1='Add' and type2='recycle'group by Die_Name),cte6 as (select Die_Name,sum(qty) as qty from Transaction where type1='use' and type2='fresh' group by Die_Name),cte7 as (select Die_Name,sum(qty) as qty from Transaction where type1='use' and type2='recycle' group by Die_Name),cte8 as (select Die_Name,sum(qty) as qty from Transaction where type1='Production' and type2='cancel' group by Die_Name) select a.Die_Name,a.qty-b.qty2 as Fresh_Outer_Die,c.qty+h.qty-g.qty as Rycycle_Outer_Die,f.qty+g.qty-h.qty as Production_Outer_Die from cte1 as a inner join cte2 as b on a.Die_Name=b.Die_Name inner join cte3 as c on a.Die_Name=c.Die_Name inner join cte6 as f on a.Die_Name=f.Die_Name inner join cte7 as g on a.Die_Name=g.Die_Name inner join cte8 as h on a.Die_Name=h.Die_Name")
        
        print(" Die Name || Number Of Fresh Outer || Numer Of recycle Die || Currently Runnning In Production")
        print("--------------------------------------------------------------------------------------")
        
        for i in mycursor:
                           
            t_Die_name,t_Fresh,t_recycle,t_Production=i
            print(f"{t_Die_name}  || {t_Fresh}  ||  {t_recycle} || {t_Production}")
            print("---------------------------------------------------------------------------------------------------")
    
    
    elif (ch==3):
        
        print("""
                _____________________________ 
                Total Purchased Transaction.........
                ------------------------------
                """)
                        
        mycursor.execute("select Tran_ID,Die_Name,type1,qty,Date from Transaction where type1='order'")
        print("Tran.No || Die Name || Tran Type1 ||  Qty || Order Date")
        print("--------------------------------------------------------------------")
        for i in mycursor:
            t_srno,t_Die_name,t_type1,t_qty,t_todaydate=i
            print(f"{t_srno}     || {t_Die_name}    || {t_type1} || {t_qty}  || {t_todaydate}")
            print("---------------------------------------------------------------------------------------------------")
        
        print("""
                _____________________________ 
                Die Usage Transaction.........
                ------------------------------
                """)
                        
        mycursor.execute("select * from transaction where type1='use'")
        print("Sr.No || Die Name || Trans Type1 || Trans Type2 || Die Number || Qty || Entered Date")
        print("--------------------------------------------------------------------------------------")
        for i in mycursor:
                           
            t_srno,t_Die_name,t_type1,t_type2,t_dieNumber,t_qty,t_todaydate=i
            print(f"{t_srno}  || {t_Die_name}  || {t_type1}||   {t_type2}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
            print("---------------------------------------------------------------------------------------------------")
            
        print("""
                ___________________________________
                Production Cancelled History.......
                -----------------------------------
                """)
                        
        mycursor.execute("select Tran_ID,Die_Name,Die_Number,date from Transaction where type1 in('Production') and type2 in('Cancel')")
        print("Tran.No || Die Name || Die Number || Entered Date")
        print("--------------------------------------------------------------------------------------")
        for i in mycursor:
                           
            t_srno,t_Die_name,t_dieNumber,t_todaydate=i
            print(f"{t_srno}  || {t_Die_name}  ||  {t_dieNumber} || {t_todaydate}")
            print("---------------------------------------------------------------------------------------------------")
                            
        print("""
                ___________________________________
                Number of Die Running in Production.........
                -----------------------------------
                """)

                        
        mycursor.execute("select Tran_ID,Die_Name,Die_Number,qty,date from Transaction where type1 in('use') and die_number!=(select Die_number from transaction where type1='production' and type2='cancel')")
        print("Tran.No || Die Name || Die Number || Qty || Entered Date")
        print("--------------------------------------------------------------------------------------")
        for i in mycursor:
                           
            t_srno,t_Die_name,t_dieNumber,t_qty,t_todaydate=i
            print(f"{t_srno}  || {t_Die_name}  ||  {t_dieNumber} || {t_qty}  || {t_todaydate}")
            print("---------------------------------------------------------------------------------------------------")
            
    # Exit
            
    elif (ch==4):
        break