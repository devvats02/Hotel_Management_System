from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class room_booking:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")
        
        #=============variables================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        
        #============title====================
        lbl_title = Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
       
        #===========logo======================
        img2=Image.open(r"C:\Users\YASH\Documents\Hotel management project 3rd year\Images\logo.jpg")
        img2=img2.resize((100,48),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lablimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lablimg.place(x=0,y=0,width=100,height=48)
        
        lablframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",padx=2,font=("times new roman",12,"bold"))
        lablframeleft.place(x=5,y=50,width=425,height=490)
        
        #=========customer contact==========
        labl_cust_contact = Label(lablframeleft,text="Customer Contact:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_cust_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(lablframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)
        #==========fetch data button===========
        btnfetchdata=Button(lablframeleft,command=self.fetch_contact,text="FETCH DATA",font=("arial",8,"bold"),bg="black",fg="gold",width=9)
        btnfetchdata.place(x=347,y=4)
        
        #================check in date==================
        check_in_date = Label(lablframeleft,text="Check_in Date:-",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        textcheck_in_date=ttk.Entry(lablframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        textcheck_in_date.grid(row=1,column=1)
        
        #=============check out date==============
        check_out_date = Label(lablframeleft,text="Check_out Date:-",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        textcheck_out_date=ttk.Entry(lablframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        textcheck_out_date.grid(row=2,column=1)
        #=================room type============
        labl_roomtype = Label(lablframeleft,text="Room Type:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_roomtype.grid(row=3,column=0,sticky=W)
        combo_roomtype=ttk.Combobox(lablframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_roomtype["value"]=("Single","Double","Luxury")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)
        #==================Available room===============
        labl_roomavailable = Label(lablframeleft,text="Available Room:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_roomavailable.grid(row=4,column=0,sticky=W)
        textroomavailable=ttk.Entry(lablframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        textroomavailable.grid(row=4,column=1)
        #=============Meal=======================
        labl_Meal = Label(lablframeleft,text="Meal:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_Meal.grid(row=5,column=0,sticky=W)
        textMeal=ttk.Entry(lablframeleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        textMeal.grid(row=5,column=1)
        #================No. of Days=================
        labl_NoOfDays = Label(lablframeleft,text="No. Of Days:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_NoOfDays.grid(row=6,column=0,sticky=W)
        textNoOfDays=ttk.Entry(lablframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        textNoOfDays.grid(row=6,column=1)
        #=============Paid Tax================
        labl_paidtax = Label(lablframeleft,text="Paid Tax:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_paidtax.grid(row=7,column=0,sticky=W)
        textpaidtax=ttk.Entry(lablframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        textpaidtax.grid(row=7,column=1)
        #=============Sub Total=================
        labl_subtotal = Label(lablframeleft,text="Sub Total:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_subtotal.grid(row=8,column=0,sticky=W)
        textsubtotal=ttk.Entry(lablframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
        textsubtotal.grid(row=8,column=1)
        #===============Total cost=================
        labl_totalcost = Label(lablframeleft,text="Total Cost:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_totalcost.grid(row=9,column=0,sticky=W)
        texttotalcost=ttk.Entry(lablframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        texttotalcost.grid(row=9,column=1) 
        #==================bill button============
        btn_bill=Button(lablframeleft,text="BILL",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_bill.grid(row=10,column=0,padx=1,sticky=W)
        #==================buttons=====================
        btn_frame=Frame(lablframeleft,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        #Add button
        btn_add=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_add.grid(row=0,column=0,padx=1)
        #update button
        btn_update=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_update.grid(row=0,column=1,padx=1)
        #delete button
        btn_delete=Button(btn_frame,text="DELETE",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_delete.grid(row=0,column=2,padx=1)
        #reset button
        btn_reset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_reset.grid(row=0,column=3,padx=1)
        #============right side image==============
        img3=Image.open(r"C:\Users\YASH\Documents\Hotel management project 3rd year\Images\room.jpg")
        img3=img3.resize((500,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lablimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lablimg.place(x=760,y=55,width=500,height=300)
        #==========table Frame===============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=280,width=860,height=260)
        
        labl_searchby = Label(table_frame,text="Search By:",bg="red",fg="black",font=("arial",12,"bold"))
        labl_searchby.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txt_search.grid(row=0,column=2,padx=2)
        
        btn_search=Button(table_frame,text="SEARCH",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_search.grid(row=0,column=3,padx=1)
        
        btn_showall=Button(table_frame,text="SHOW ALL",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_showall.grid(row=0,column=4,padx=1)
        
        #==============show data table=================
        
        detail_frame = Frame(table_frame,bd=2,relief=RIDGE)
        detail_frame.place(x=0,y=50,width=860,height=180)
        
        scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(detail_frame,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No.")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="NoOfDays")
        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()  
    # ================Add data function==================
    def add_data(self):
        if self.var_contact.get()==""or self.var_checkin.get()=="": 
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                self.var_contact.get(),
                                                self.var_checkin.get(),
                                                self.var_checkout.get(),
                                                self.var_roomtype.get(),
                                                self.var_roomavailable.get(),
                                                self.var_meal.get(),
                                                self.var_noofdays.get()
                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    #===========fetch data function=====================
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close() 
    #==========get cursor=============  
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    #=============update data function===========
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,Room=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                
                                                self.var_checkin.get(),
                                                self.var_checkout.get(),
                                                self.var_roomtype.get(),
                                                self.var_roomavailable.get(),
                                                self.var_meal.get(),
                                                self.var_noofdays.get(),
                                                self.var_contact.get(),
                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root) 
    #==============delete function=================
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this room details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()      
    #===========reset function==============
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
    #================All Data Fetch===============   
    
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This number not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=55,width=300,height=180)
                
                lablName=Label(showdataframe,text="Name:",font=("arial",12,"bold"))
                lablName.place(x=0,y=0)
                
                labl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                labl.place(x=90,y=0)
                #===============gender=============
                conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lablGender=Label(showdataframe,text="Gender:",font=("arial",12,"bold"))
                lablGender.place(x=0,y=30)
                
                labl2=Label(showdataframe,text=row,font=("arial",12,"bold"))
                labl2.place(x=90,y=30)
                #=============email===============
                conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lablGender=Label(showdataframe,text="Email:",font=("arial",12,"bold"))
                lablGender.place(x=0,y=60)
                
                labl3=Label(showdataframe,text=row,font=("arial",12,"bold"))
                labl3.place(x=90,y=60)
                #===========Nationality===============
                conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lablGender=Label(showdataframe,text="Nationality:",font=("arial",12,"bold"))
                lablGender.place(x=0,y=90)
                
                labl4=Label(showdataframe,text=row,font=("arial",12,"bold"))
                labl4.place(x=90,y=90)
                #=============Address============
                conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lablGender=Label(showdataframe,text="Address:",font=("arial",12,"bold"))
                lablGender.place(x=0,y=120)
                
                labl3=Label(showdataframe,text=row,font=("arial",12,"bold"))
                labl3.place(x=90,y=120)
    #===========search system=============
    def search(self):
        conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close() 
    #==============Bill functions=================
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days) 
        
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(700)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1)) 
            subtotal="Rs."+str("%.2f"%((q5)))   
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))    
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)  
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1)) 
            subtotal="Rs."+str("%.2f"%((q5)))   
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))    
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1)) 
            subtotal="Rs."+str("%.2f"%((q5)))   
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))    
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total) 
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1)) 
            subtotal="Rs."+str("%.2f"%((q5)))   
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))    
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1)) 
            subtotal="Rs."+str("%.2f"%((q5)))   
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))    
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
            q1=float(700)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1)) 
            subtotal="Rs."+str("%.2f"%((q5)))   
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))    
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1)) 
            subtotal="Rs."+str("%.2f"%((q5)))   
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))    
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1)) 
            subtotal="Rs."+str("%.2f"%((q5)))   
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))    
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)
        else:
            q1=float(700)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1)) 
            subtotal="Rs."+str("%.2f"%((q5)))   
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))    
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)
if __name__ == "__main__":   
    root=Tk()
    obj = room_booking(root)
    root.mainloop()