from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter
import tkinter
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from time import strftime
from datetime import datetime

class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//vit_logo.png")
        img=img.resize((200,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=-0,width=200,height=130)

        #second image
        #img1=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//f_title.jpg")
        #img1=img1.resize((1000,130),Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)

        #f_lb1=Label(self.root,image=self.photoimg1)
        #f_lb1.place(x=200,y=0,width=1000,height=130)

        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",36,"bold","underline"),bg="white",fg="red")
        title_lbl.place(x=180,y=0,width=1200,height=130)

        #third image
        img2=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//vit_logo.png")
        img2=img2.resize((200,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1330,y=0,width=200,height=130)

        #bacgorund image
        img3=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//orange_bg.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,bg="white",fg="red")
        title_lbl.place(x=0,y=-10,width=1530,height=45)

        #==================Time================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',20,'bold'),background='white',foreground='blue')
        lbl.place(x=1350,y=0,width=150,height=50)
        time()

        #Student Button
        img4=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",command=self.student_details)
        b1_1.place(x=200,y=300,width=220,height=40)


        #Detect face Button
        img5=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//detect1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=650,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=300,width=220,height=40)

        #Attendance face Button
        img6=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #Help Button
        """img7=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//help_desk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)"""

        #Train Face Button
        img8=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//train_data.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)

        #Photos Face Button
        img9=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=650,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=600,width=220,height=40)

        #Developers Button
        """img10=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//developers.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Developers",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)"""

         #Exit Button
        img11=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.iExit,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)

    
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


        #=============================Function Buttons==============================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
            

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
            

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()
