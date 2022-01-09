from tkinter import *
from tkinter import ttk
from tkinter import font
from typing import Sized
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_top=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//detect1.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photo_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photo_top)
        f_lb1.place(x=0,y=55,width=650,height=700)

        img_bottom=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//detect2.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photo_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(self.root,image=self.photo_bottom)
        f_lb1.place(x=650,y=55,width=950,height=700)

        #Button
        b1_1=Button(f_lb1,text="Face Recognition",command=self.face_recognition,cursor="hand2",font=("times new roman",17,"bold"),bg="White",fg="darkblue")
        b1_1.place(x=365,y=625,width=200,height=40)

#=====================Attendance================================
    def mark_attendance(self,i,r,n,d):
        with open("neil.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt_string=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dt_string},{d1},Present")




#=========================Face Recognizer=======================
    def face_recognition(self):
        def draw_boundary(img,classifer,scale_factor,min_neighbors,color,text,clf):
            #print(img)
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #print(img)
            featres=classifer.detectMultiScale(gray_image,scale_factor,min_neighbors)

            coord=[]

            for (x,y,w,h) in featres:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Neil@2001",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        ret,img=video_cap.read()

        while ret:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
