from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        #=============variables========================

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=IntVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=IntVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=IntVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #Image 1

        img1=Image.open(r"E:\images\student5.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #Image 2

        img2=Image.open(r"E:\images\student6.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=460,y=0,width=500,height=130)

        #Image 3

        img3=Image.open(r"E:\images\student7.jpg")
        img3=img3.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=960,y=0,width=400,height=130)


        # Bg Image

        img4=Image.open(r"E:\images\image12.jpg")
        img4=img4.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=790)

        title_lbl = Label(bg_img,text = "STUDENT MANAGEMENT SYSTEM",font = ("algerian",30,"bold"),bg = "white",fg = "dark green")
        title_lbl.place(x = 0,y = 0,width = 1370,height = 35)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=12,y=45,width=1330,height=680)

        def time():
            string=strftime("%H:%M:%S %p") #Hours Minutes Second AM/PM
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="red")
        lbl.place(x=0,y=0,width=120,height=30)
        time()


        #Left Label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=0,width=660,height=520)

        img_left=Image.open(r"E:\images\student8.jpg")
        img_left=img_left.resize((650,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=110)

        #current course

        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course  information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=110,width=645,height=110)

        #Department
        
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg='white')
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Science","Commerce","Arts")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course

        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","BSc.IT","B.Com","B.A")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year

        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg='white')
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","FY","SY","TY")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester

        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg='white')
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Sem I","Sem II","Sem III","Sem IV","Sem V","Sem VI")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # Class Student information
        
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=220,width=645,height=275)

        #student id

        studentId_label=Label(class_student_frame,text="StudentId:",font=("times new roman",12,"bold"),bg='white')
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entery=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entery.grid(row=0,column=1,padx=10,sticky=W)

        
        #student name

        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg='white')
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entery=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entery.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division

        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg='white')
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=18,font=("times new roman",12,"bold"),state="readonly")
        div_combo["values"]=("A","B","C","D","E")
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Roll No

        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg='white')
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entery=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entery.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
 
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg='white')
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        

        
        #DOB

        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg='white')
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entery=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entery.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email

        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg='white')
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entery=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entery.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #Phone no
 
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg='white')
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entery=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entery.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Addresss

        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg='white')
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entery=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entery.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher name

        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg='white')
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entery=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entery.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #button frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=640,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
 
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take photo sample",font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4)

        #Right Label frame
        
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=0,width=635,height=520)

        img_right=Image.open(r"E:\images\student11.jpg")
        img_right=img_right.resize((650,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=625,height=110)

        #================search system=============================

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="View Student Details & Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=110,width=620,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg='red',fg='white')
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #search
        
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll","Phone","Student_id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        search_entery=ttk.Entry(search_frame,textvariable=self.var_search,width=17,font=("times new roman",12,"bold"))
        search_entery.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
       
        search_btn=Button(search_frame,command=self.search_data,text="Search",width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #===============table frame============================

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=185,width=620,height=310)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Division")
        self.student_table.heading("roll",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
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
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=120)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
     #===============function declaration=================================

    def add_data(self): 
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kinjalpatel",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(



                                                                                                               self.var_dep.get(),
                                                                                                               self.var_course.get(),
                                                                                                               self.var_year.get(),
                                                                                                               self.var_semester.get(),
                                                                                                               self.var_std_id.get(),
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
                messagebox.showinfo("Sucess","Student details has been added sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                                         
      #================fetch data========================================                                                                      
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kinjalpatel",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
                
     # =================get cursor=============================
    def get_cursor(self,event=""):
         cursor_focus=self.student_table.focus()
         content=self.student_table.item(cursor_focus)
         data=content["values"]

         self.var_dep.set(data[0]),
         self.var_course.set(data[1]),
         self.var_year.set(data[2]),
         self.var_semester.set(data[3]),
         self.var_std_id.set(data[4]),
         self.var_std_name.set(data[5]),
         self.var_div.set(data[6]),
         self.var_roll.set(data[7]),
         self.var_gender.set(data[8]),
         self.var_dob.set(data[9]),
         self.var_email.set(data[10]),
         self.var_phone.set(data[11]),
         self.var_address.set(data[12]),
         self.var_teacher.set(data[13]),
         self.var_radio1.set(data[14])
     
    #update function
         
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="kinjalpatel",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                    
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
                messagebox.showinfo("Success","student details sucessfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #delete function
                
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="kinjalpatel",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
   #reset

    def reset_data(self):
        self.var_dep.set("Select Departmant")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
 #============= Generate data set or Take photo sample ===================
        
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="kinjalpatel",database="face_recognition")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from student")
               myresult=my_cursor.fetchall()
               id=0
               for x in myresult:
                   id+=1
               my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                    
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
            
              #====== Load predefined data on face frontals from opencv======
               face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

               def face_cropped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                   faces=face_classifier.detectMultiScale(gray,1.3,5)
                   #scaling factor=1.3
                   #minimum neighbour=5

                   for(x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped
                    
               cap=cv2.VideoCapture(0)
               img_id=0
               while True:
                   ret,my_frame=cap.read()
                   if face_cropped(my_frame)is not None:
                       img_id+=1
                       face=cv2.resize(face_cropped(my_frame),(450,450))
                       face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                       file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                       cv2.imwrite(file_name_path,face)
                       cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       cv2.imshow("Cropped Face",face)

                   if cv2.waitKey(1)==13 or int(img_id == 100):
                       break
               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Result","generating data sets completed",parent=self.root)
               
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        
    
    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="kinjalpatel",database="face_recognition")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
               data=my_cursor.fetchall()
               if len(data)!=0:
                   self.student_table.delete(*self.student_table.get_children())
                   for i in data:
                       self.student_table.insert("",END,values=i)
                   conn.commit()
               conn.close()                     

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            

                                 
                                 
                                 



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

