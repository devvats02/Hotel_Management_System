from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")
        
        #=======variables===========
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_cust_mother=StringVar()
        self.var_cust_gender=StringVar()
        self.var_cust_post=StringVar()
        self.var_cust_mobile=StringVar()
        self.var_cust_email=StringVar()
        self.var_cust_nationality=StringVar()
        self.var_cust_address=StringVar()
        self.var_cust_idproof=StringVar()
        self.var_cust_idnumber=StringVar() 
        
        #title
        lbl_title = Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
       
        #logo
        img2=Image.open(r"C:\Users\YASH\Documents\Hotel management project 3rd year\Images\logo.jpg")
        img2=img2.resize((100,48),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lablimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lablimg.place(x=0,y=0,width=100,height=48)
        
        #label Frame
        lablframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        lablframeleft.place(x=5,y=50,width=425,height=490)
        
        # Labels and Entries
        #cust_ref
        labl_cust_ref = Label(lablframeleft,text="Customer Ref:",font=("arial",12,"bold"),padx=2,pady=6)
        labl_cust_ref.grid(row=0,column=0,sticky=W)
        
        enty_ref=ttk.Entry(lablframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)
        #cust_name
        cname = Label(lablframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        
        txtcname=ttk.Entry(lablframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)
        #Mother name
        lablmname = Label(lablframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lablmname.grid(row=2,column=0,sticky=W)
        
        txtmname=ttk.Entry(lablframeleft,textvariable=self.var_cust_mother,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)
        #gender combobox
        labl_gender = Label(lablframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        labl_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(lablframeleft,textvariable=self.var_cust_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        #postcode
        labl_postcode = Label(lablframeleft,text="Postcode:",font=("arial",12,"bold"),padx=2,pady=6)
        labl_postcode.grid(row=4,column=0,sticky=W)
        txtpostcode=ttk.Entry(lablframeleft,textvariable=self.var_cust_post,width=29,font=("arial",13,"bold"))
        txtpostcode.grid(row=4,column=1)
        #mobilenumber
        labl_mobnumber = Label(lablframeleft,text="Mobile No.:",font=("arial",12,"bold"),padx=2,pady=6)
        labl_mobnumber.grid(row=5,column=0,sticky=W)
        txtmobile=ttk.Entry(lablframeleft,textvariable=self.var_cust_mobile,width=29,font=("arial",13,"bold"))
        txtmobile.grid(row=5,column=1)
        #email
        labl_email = Label(lablframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        labl_email.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(lablframeleft,textvariable=self.var_cust_email,width=29,font=("arial",13,"bold"))
        txtemail.grid(row=6,column=1)
        #nationality combobox
        labl_nationality = Label(lablframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        labl_nationality.grid(row=7,column=0,sticky=W)
        combo_nation=ttk.Combobox(lablframeleft,textvariable=self.var_cust_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nation["value"]=("Indian","American","Japanese","British","Others")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)
        
        #idproof combobox
        labl_idproof = Label(lablframeleft,text="ID Proof:",font=("arial",12,"bold"),padx=2,pady=6)
        labl_idproof.grid(row=8,column=0,sticky=W)
        combo_id=ttk.Combobox(lablframeleft,textvariable=self.var_cust_idproof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Aadhar Card","Driving Licence","Passport","Pan Card","Voter ID")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
        
        #id number
        labl_idnumber = Label(lablframeleft,text="ID Number:",font=("arial",12,"bold"),padx=2,pady=6)
        labl_idnumber.grid(row=9,column=0,sticky=W)
        txtidnumber=ttk.Entry(lablframeleft,textvariable=self.var_cust_idnumber,width=29,font=("arial",13,"bold"))
        txtidnumber.grid(row=9,column=1)
        #address
        labl_address = Label(lablframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        labl_address.grid(row=10,column=0,sticky=W)
        txtaddress=ttk.Entry(lablframeleft,textvariable=self.var_cust_address,width=29,font=("arial",13,"bold"))
        txtaddress.grid(row=10,column=1)
        #==========buttons Frame=====================
        btn_frame=Frame(lablframeleft,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        #Add button
        btn_add=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_add.grid(row=0,column=0,padx=1)
        #
        btn_update=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_update.grid(row=0,column=1,padx=1)
        #
        btn_delete=Button(btn_frame,text="DELETE",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_delete.grid(row=0,column=2,padx=1)
        #
        btn_reset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_reset.grid(row=0,column=3,padx=1)
        #==========table Frame===============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=50,width=860,height=490)
        
        labl_searchby = Label(table_frame,text="Search By:",bg="red",fg="black",font=("arial",12,"bold"))
        labl_searchby.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txt_search.grid(row=0,column=2,padx=2)
        
        btn_search=Button(table_frame,text="SEARCH",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_search.grid(row=0,column=3,padx=1)
        
        btn_showall=Button(table_frame,text="SHOW ALL",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_showall.grid(row=0,column=4,padx=1)
        
        #shoW data table ========================
        detail_frame = Frame(table_frame,bd=2,relief=RIDGE)
        detail_frame.place(x=0,y=50,width=860,height=350)
        
        scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
        
        self.cust_details_table=ttk.Treeview(detail_frame,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)
        
        self.cust_details_table.heading("ref",text="Ref No.")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("mother",text="Mother Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("post",text="PostCode")
        self.cust_details_table.heading("mobile",text="Mobile No.")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="ID Proof")
        self.cust_details_table.heading("idnumber",text="ID Number")
        self.cust_details_table.heading("address",text="Address")
        
        self.cust_details_table["show"]="headings"
        
        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("mother",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("post",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_cust_mobile.get()==""or self.var_cust_mother.get()=="": 
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                self.var_ref.get(),
                                                self.var_cust_name.get(),
                                                self.var_cust_mother.get(),
                                                self.var_cust_gender.get(),
                                                self.var_cust_post.get(),
                                                self.var_cust_mobile.get(),
                                                self.var_cust_email.get(),
                                                self.var_cust_nationality.get(),
                                                self.var_cust_idproof.get(),
                                                self.var_cust_idnumber.get(),
                                                self.var_cust_address.get()
                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_cust_mother.set(row[2])
        self.var_cust_gender.set(row[3])
        self.var_cust_post.set(row[4])
        self.var_cust_mobile.set(row[5])
        self.var_cust_email.set(row[6])
        self.var_cust_nationality.set(row[7])
        self.var_cust_idproof.set(row[8])
        self.var_cust_idnumber.set(row[9])
        self.var_cust_address.set(row[10])
        
    def update(self):
        if self.var_cust_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                
                                                self.var_cust_name.get(),
                                                self.var_cust_mother.get(),
                                                self.var_cust_gender.get(),
                                                self.var_cust_post.get(),
                                                self.var_cust_mobile.get(),
                                                self.var_cust_email.get(),
                                                self.var_cust_nationality.get(),
                                                self.var_cust_idproof.get(),
                                                self.var_cust_idnumber.get(),
                                                self.var_cust_address.get(),
                                                self.var_ref.get()
                                                                                               ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)
    
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_cust_mother.set("")
        #self.var_cust_gender.set("")
        self.var_cust_post.set("")
        self.var_cust_mobile.set("")
        self.var_cust_email.set("")
        #self.var_cust_nationality.set("")
        #self.var_cust_idproof.set("")
        self.var_cust_idnumber.set("")
        self.var_cust_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
    
    def search(self):
        conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
            conn.close()
if __name__ == "__main__":
    root=Tk()
    obj = cust_Win(root)
    root.mainloop()