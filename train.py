from tkinter import *
from tkinter import ttk
from tkinter import font
from typing import Sized
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Train Dataset",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_top=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//train.png")
        img_top=img_top.resize((1530,335),Image.ANTIALIAS)
        self.photo_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photo_top)
        f_lb1.place(x=0,y=50,width=1530,height=335)

        #=====================Button=====================

        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="black",fg="white")
        b1_1.place(x=0,y=385,width=1530,height=65)

        img_bottom=Image.open(r"D://TY COLLEGE//AI//CP_IMAGES//college_images//photos.jpg")
        img_bottom=img_bottom.resize((1530,335),Image.ANTIALIAS)
        self.photo_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(self.root,image=self.photo_bottom)
        f_lb1.place(x=0,y=450,width=1530,height=335)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]#list comprehension

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)
    
        #====================Train the classifier=============================
        #Self = pip install opencv-contrib-python
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed")



        


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
