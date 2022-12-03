from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        #====================variables===============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        

        #Image 1

        img1=Image.open(r"E:\images\student14.jpg")
        img1=img1.resize((680,180),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=680,height=180)


        #Image 2

        img2=Image.open(r"E:\images\student13.jpg")
        img2=img2.resize((680,180),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=680,y=0,width=690,height=180)

        title_lbl = Label(self.root,text = "ATTENDANCE MANAGEMENT SYSTEM",font = ("algerian",30,"bold"),bg = "green",fg = "white")
        title_lbl.place(x = 0,y = 180,width = 1370,height = 35)
        
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=12,y=220,width=1330,height=480)

        #Left Label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=0,width=660,height=475)

        img_left=Image.open(r"E:\images\student8.jpg")
        img_left=img_left.resize((650,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=4,y=0,width=650,height=110)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=7,y=115,width=640,height=330)


        #label and entry
        #attendance id

        attendanceId_label=Label(left_inside_frame,text="Attendance Id:",font=("comicsansns 11 bold"),bg='white')
        attendanceId_label.grid(row=0,column=0,padx=15,pady=8,sticky=W)

        attendanceId_entery=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("comicsansns 11 bold"))
        attendanceId_entery.grid(row=0,column=1,pady=8,sticky=W)

        #Roll No
        rollLabel=Label(left_inside_frame,text="Roll No:",font=("comicsansns 11 bold"),bg='white')
        rollLabel.grid(row=0,column=2,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("comicsansns 11 bold"))
        atten_roll.grid(row=0,column=3,pady=8)

        #name
        nameLabel=Label(left_inside_frame,text="Name:",font=("comicsansns 11 bold"),bg='white')
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("comicsansns 11 bold"))
        atten_name.grid(row=1,column=1,pady=8)

        #Department
        depLabel=Label(left_inside_frame,text="Department:",font=("comicsansns 11 bold"),bg='white')
        depLabel.grid(row=1,column=2,padx=10)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("comicsansns 11 bold"))
        atten_dep.grid(row=1,column=3,pady=8)

        #Time
        timeLabel=Label(left_inside_frame,text="Time:",font=("comicsansns 11 bold"),bg='white')
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("comicsansns 11 bold"))
        atten_time.grid(row=2,column=1,pady=8)

        #Date
        dateLabel=Label(left_inside_frame,text="Date:",font=("comicsansns 11 bold"),bg='white')
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("comicsansns 11 bold"))
        atten_date.grid(row=2,column=3,pady=8)

        #Attendance
        attendanceLabel=Label(left_inside_frame,width=20,text="Attendance Status:",font=("comicsansns 11 bold"),bg='white')
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font=("comicsansns 11 bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,pady=8,sticky=W)

        #Butons frame

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=290,width=630,height=35)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)
 
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        
        #Right Label frame
        
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=0,width=645,height=475)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=630,height=440)

        #=========scroll bar table=============================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #==================fetch data======================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)    

    #export csv   
    def exportCsv(self):
       try:
           if len(mydata)<1:
               messagebox.showerror("No Data","No Data found to export",parent=self.root)
               return False
           fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root) 
           with open(fln,mode='w',newline="") as myfile:
               exp_write=csv.writer(myfile,delimiter=",")
               for i in mydata:
                   exp_write.writerow(i)
               messagebox.showinfo("Data Export","Your data exported to " +os.path.basename(fln)+ " Successfully")
               
       except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)       

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
