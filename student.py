from tkinter import *
from tkinter import ttk
from tkinter import font
from typing import Sized
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System")

        #====================variables================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_teacher=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()



        #first image
        img=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//st1.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=-0,width=500,height=130)

        #second image
        img1=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//st2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//st3.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1020,y=0,width=500,height=130)

         #bacgorund image
        img3=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//background.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE, text="Student Details",font=("times new roman",12,"bold"),bg="white")
        Left_frame.place(x=10,y=10,width=720,height=580)

        img_left=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//img_left.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=730,height=130)

        #current course
        Current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE, text="Current Course Information",font=("times new roman",12,"bold"),bg="white")
        Current_course_frame.place(x=5,y=135,width=700,height=150)

        #Department Label
        department_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=0,column=0,padx=10,sticky=W)

        department_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        department_combo["values"]=("Select Department","Computers","IT","Civil","Mechanical","ENTC")
        department_combo.current(0)
        department_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(Current_course_frame,text="Course", font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(Current_course_frame,text="Year", font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(Current_course_frame,text="Semester", font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semster_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semster_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4")
        semster_combo.current(0)
        semster_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=700,height=300)

        #Student id
        student_id_label=Label(class_student_frame,text="Student ID", font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Student name
        student_name_label=Label(class_student_frame,text="Student Name", font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Class Division", font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo["values"]=("A","B","C","E","F","G")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Roll No
        roll_no_label=Label(class_student_frame,text="Roll Number:", font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Date of Birth
        dob_label=Label(class_student_frame,text="DOB:", font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:", font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Phone
        phone_label=Label(class_student_frame,text="Phone:", font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email:", font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        address_label=Label(class_student_frame,text="Address:", font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:", font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",variable=self.var_radio1, value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=5,column=1)

         #Buttons Student Information
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=690,height=40)

        #save button
        save_btn=Button(btn_frame,width=15,text="Save",command=self.add_data,font=("times new roman",12,"bold"),bg="Black",fg="white")
        save_btn.grid(row=0,column=0,padx=10)

        #update button
        update_btn=Button(btn_frame,width=15,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg="Black",fg="white")
        update_btn.grid(row=0,column=1,padx=10)

        #delete button
        delete_btn=Button(btn_frame,width=15,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="Black",fg="white")
        delete_btn.grid(row=0,column=2,padx=10)

        #reset button
        reset_btn=Button(btn_frame,width=15,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="Black",fg="white")
        reset_btn.grid(row=0,column=3,padx=10)

        #Buttons Student Information
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=690,height=40)

        #Take photo sample button
        take_photo_btn=Button(btn_frame1,width=30,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",12,"bold"),bg="Black",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=30,pady=5)

        #Update photo sample button
        update_photo_btn=Button(btn_frame1,width=30,text="Update Photo Sample",font=("times new roman",12,"bold"),bg="Black",fg="white")
        update_photo_btn.grid(row=0,column=1,padx=10,pady=5)



        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE, text="Student Details",font=("times new roman",12,"bold"),bg="white")
        Right_frame.place(x=750,y=10,width=700,height=580)

        img_right=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//student.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb1=Label(Right_frame,image=self.photoimg_right)
        f_lb1.place(x=5,y=0,width=730,height=130)

        #=====================================Search System=======================================================================
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=680,height=70)

        
        #Search 
        search_label=Label(search_frame,text="Search by:", font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        semester_label=Label(Current_course_frame,text="Semester", font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

         #Search button
        search_btn=Button(search_frame,width=12,text="Search",font=("times new roman",12,"bold"),bg="Black",fg="white")
        search_btn.grid(row=0,column=3,padx=2)
         
        #Search button
        showAll_btn=Button(search_frame,width=12,text="Show All",font=("times new roman",12,"bold"),bg="Black",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5)
    
        #=============================Table Frame======================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=680,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("id","dep","course","year","sem","name","div","roll","gender","dob","email","phone","address","teacher","photo"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        #=======================Function Declaration=====================
        
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Neil@2001",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_std_id.get(),
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_std_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()                                                                                    
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()    
                messagebox.showinfo("Success","Student details have been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #==========================Fetch function====================================
    def fetch_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Neil@2001",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()


            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())

                for i in data:
                    self.student_table.insert("",END,values=i)

                conn.commit()

            conn.close()

        except Exception as es:
            print()


    #================================Get cursor=======================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_std_id.set(data[0])
        self.var_dep.set(data[1])
        self.var_course.set(data[2])
        self.var_year.set(data[3])
        self.var_semester.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])
        

    #===============================Update Function=======================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student detials",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Neil@2001",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set  Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_ID=%s", (                                                 
                                                                                                                                                                                    
                                                                                                                                                                                    
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),  
                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                    ))    
                else:
                    if not Update:
                        return
                
                messagebox.showinfo("Success","student details updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #===================================Delete Function=========================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Student Page","Do you want to delete this student?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Neil@2001",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
            except Exception as es:
                if not delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete","student details deleted Successfully",parent=self.root)

    #=========================================Reset Function==================================================
    def reset_data(self):
        self.var_std_id.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #========================Generate Dataset or Take photo samples=============================================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Neil@2001",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set  Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_ID=%s", (                                                 
                                                                                                                                                                                
                                                                                                                                                                                    
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),  
                                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #==============Load Predefined data on face frontal from opencv=======
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)                        #1.3 - Scaling Factor and  5 = Minimum Neighbor

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                        

                cap=cv2.VideoCapture(0)
                img_id=0

                while(True):
                    
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(0,0),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0), 2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
