from tkinter import*
from PIL import Image,ImageTk
from customer import cust_Win
from room import room_booking
from details import detailsRoom

class HotelManagement:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        #image 1
        img1=Image.open(r"C:\Users\YASH\Documents\Hotel management project 3rd year\Images\image1.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lablimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lablimg.place(x=0,y=0,width=1550,height=140)
        #image2
        img2=Image.open(r"C:\Users\YASH\Documents\Hotel management project 3rd year\Images\logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lablimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lablimg.place(x=0,y=0,width=230,height=140)
        #title
        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        #mainframe
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        #menu
        labl_menu = Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        labl_menu.place(x=0,y=0,width=230)
        #buttonframe
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=42,width=228,height=190)
        
        cust_btn = Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn = Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn = Button(btn_frame,text="DETAILS",command=self.detailsroom,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn = Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn = Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        #image
        img3=Image.open(r"C:\Users\YASH\Documents\Hotel management project 3rd year\Images\image2.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lablimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lablimg1.place(x=225,y=0,width=1310,height=590)
        
        #down image
        img4=Image.open(r"C:\Users\YASH\Documents\Hotel management project 3rd year\Images\food1.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lablimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lablimg1.place(x=0,y=225,width=230,height=210)
        
        img5=Image.open(r"C:\Users\YASH\Documents\Hotel management project 3rd year\Images\food2.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lablimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lablimg1.place(x=0,y=420,width=230,height=190)
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = cust_Win(self.new_window)  
    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = room_booking(self.new_window) 
    def detailsroom(self):
        self.new_window = Toplevel(self.root)
        self.app = detailsRoom(self.new_window) 
     
if __name__ == "__main__": 
    root=Tk()
    obj=HotelManagement(root)
    root.mainloop()
    