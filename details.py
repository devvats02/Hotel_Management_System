from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class detailsRoom:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")
        #==============title============
        lbl_title = Label(self.root,text="ROOM ADDING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
       
        #===========logo======================
        img2=Image.open(r"C:\Users\YASH\Documents\Hotel management project 3rd year\Images\logo.jpg")
        img2=img2.resize((100,48),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lablimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lablimg.place(x=0,y=0,width=100,height=48)
        
        lablframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",padx=2,font=("times new roman",12,"bold"))
        lablframeleft.place(x=5,y=50,width=540,height=350)
        #=============Floor============
        labl_floor = Label(lablframeleft,text="Floor:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_floor.grid(row=0,column=0,sticky=W,padx=20)
        
        self.var_floor=StringVar()
        enty_floor=ttk.Entry(lablframeleft,width=20,textvariable=self.var_floor,font=("arial",13,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)
        #==============room No============
        labl_RoomNo = Label(lablframeleft,text="Room No.:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)
        self.var_roomNo=StringVar()
        enty_RoomNo=ttk.Entry(lablframeleft,width=20,textvariable=self.var_roomNo,font=("arial",13,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)
        #==========Room type============
        labl_RoomType = Label(lablframeleft,text="Room Type:-",font=("arial",12,"bold"),padx=2,pady=6)
        labl_RoomType.grid(row=2,column=0,sticky=W,padx=20)
        self.var_roomType=StringVar()
        enty_RoomType=ttk.Entry(lablframeleft,width=20,textvariable=self.var_roomType,font=("arial",13,"bold"))
        enty_RoomType.grid(row=2,column=1,sticky=W)
        #===========buttons============
        btn_frame=Frame(lablframeleft,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)
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
        #==================table frame=============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"))
        table_frame.place(x=600,y=55,width=600,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(table_frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")
        
        self.room_table["show"]="headings"
        
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    #=======add data fun.============
    def add_data(self):
        if self.var_floor.get()==""or self.var_roomType.get()=="": 
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                self.var_floor.get(),
                                                self.var_roomNo.get(),
                                                self.var_roomType.get()
                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    #============fetch data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close() 
    #=========get cursor=============
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_roomType.set(row[2])
    #============update function===========
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                
                                                self.var_floor.get(),
                                                self.var_roomType.get(),
                                                self.var_roomNo.get(),
                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)
    #========delete function========
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this room details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host='localhost',user='root',passwd="devvats657@",database='management')
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 
    #==========reset function===========
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_roomType.set(""),
if __name__ == "__main__":   
    root=Tk()
    obj = detailsRoom(root)
    root.mainloop()