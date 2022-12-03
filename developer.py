from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl = Label(self.root,text = "DEVELOPER",font = ("algerian",30,"bold"),bg = "white",fg = "blue")
        title_lbl.place(x =0,y =0,width =1370,height=35)
        
        img_top=Image.open(r"E:\images\bg.jpg")
        img_top=img_top.resize((1370,660),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1370,height=660)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=450,height=400)

        img_top1=Image.open(r"E:\images\devloper.jpg")
        img_top1=img_top1.resize((450,200),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=0,y=0,width=450,height=200)

        dev_label=Label(main_frame,text="We are two developer for this project",font=("times new roman",20,"bold"),bg='white')
        dev_label.place(x=0,y=200)


        dev_label=Label(main_frame,text="1) Kinjal",font=("times new roman",20,"bold"),bg='white')
        dev_label.place(x=0,y=240)

        dev_label=Label(main_frame,text="2) Mitali",font=("times new roman",20,"bold"),bg='white')
        dev_label.place(x=0,y=280)

        dev_label=Label(main_frame,text="We are full stack developer",font=("times new roman",20,"bold"),bg='white')
        dev_label.place(x=0,y=320)









if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
