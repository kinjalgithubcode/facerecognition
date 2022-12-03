from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
from train import Train
from time import strftime
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #Image 1

        img1=Image.open(r"E:\images\image1.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #Image 2

        img2=Image.open(r"E:\images\image8.jpg")
        img2=img2.resize((500,220),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #Image 3

        img3=Image.open(r"E:\images\image5.jpg")
        img3=img3.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=400,height=130)


        # Bg Image

        img4=Image.open(r"E:\images\image12.jpg")
        img4=img4.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=790)

        title_lbl = Label(bg_img,text = "FACE RECOGNITION SYSTEM SOFTWARE",font = ("algerian",30,"bold"),bg = "white",fg = "red")
        title_lbl.place(x = 0,y = 0,width = 1370,height = 35)

        def time():
            string=strftime("%H:%M:%S %p") #Hours Minutes Second AM/PM
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="red")
        lbl.place(x=0,y=0,width=120,height=30)
        time()

        # Student Details Button
        
        img5=Image.open(r"E:\images\student1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor = "hand2")
        b1.place(x=130,y=50,width=220,height=220)

        b1_1=Button(bg_img,text = "Student Details",command=self.student_details,cursor = "hand2",font = ("times new roman",15,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x=130,y=265,width=220,height=40)

        #Detect Face

        img6=Image.open(r"E:\images\image13.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image = self.photoimg6,cursor = "hand2",command=self.face_data)
        b1.place(x = 430,y = 50,width = 220,height = 220)

        b1_1 = Button(bg_img,text = "Face Detectore",cursor = "hand2",command=self.face_data,font = ("times new roman",15,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 430,y = 265,width = 220,height = 40)

        #Attendance button

        img7=Image.open(r"E:\images\image15.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image = self.photoimg7,cursor = "hand2",command=self.attendance_data)
        b1.place(x = 730,y = 50,width = 220,height = 220)

        b1_1 = Button(bg_img,text = "Attendance",cursor = "hand2",command=self.attendance_data,font = ("times new roman",15,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 730,y = 265,width = 220,height = 40)
        
        #ChatBot button

        img8=Image.open(r"E:\images\chatboat1.png")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image = self.photoimg8,cursor = "hand2",command=self.help_data)
        b1.place(x = 1030,y = 50,width = 220,height = 220)

        b1_1 = Button(bg_img,text = "ChatBoat",cursor = "hand2",command=self.help_data,font = ("times new roman",15,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 1030,y = 265,width = 220,height = 40)
        
        #Train Face button

        img9=Image.open(r"E:\images\traindata1.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image = self.photoimg9,cursor = "hand2",command=self.train_data)
        b1.place(x = 130,y = 330,width = 220,height = 220)

        b1_1 = Button(bg_img,text = "Train Data",cursor = "hand2",command=self.train_data,font = ("times new roman",15,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 130,y = 530,width = 220,height = 40)

        #Photos Face button

        img10=Image.open(r"E:\images\dataset.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image = self.photoimg10,cursor = "hand2",command=self.open_img)
        b1.place(x = 430,y = 330,width = 220,height = 220)

        b1_1 = Button(bg_img,text = "Photos",cursor = "hand2",command=self.open_img,font = ("times new roman",15,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 430,y = 530,width = 220,height = 40)
        
        #Devloper Face button

        img11=Image.open(r"E:\images\devloper.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image = self.photoimg11,cursor = "hand2",command=self.developer_data)
        b1.place(x = 730,y = 330,width = 220,height = 220)

        b1_1 = Button(bg_img,text = "Devloper",cursor = "hand2",command=self.developer_data,font = ("times new roman",15,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 730,y = 530,width = 220,height = 40)

        #Exit button

        img12=Image.open(r"E:\images\exit_button.jpg")
        img12=img12.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1 = Button(bg_img,image = self.photoimg12,cursor = "hand2",command=self.iexit)
        b1.place(x = 1030,y = 330,width = 220,height = 220)

        b1_1 = Button(bg_img,text = "Exit",cursor = "hand2",command=self.iexit,font = ("times new roman",15,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 1030,y = 530,width = 220,height = 40)

    def open_img(self):
        os.startfile("data")

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return

        #=============function button========================

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

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        
        
    

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()



