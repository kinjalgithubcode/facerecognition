from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("750x650+0+0")
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open(r'E:\images\chatboat1.png')
        img_chat=img_chat.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=610)
        btn_frame.pack()

        label=Label(btn_frame,text='Type Something',font=('arial',14,'bold'),fg='green',bg='white')
        label.grid(row=0,column=0,padx=5,sticky=W)    
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('arial',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',16,'bold'),width=8,bg='red')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear_func,font=('arial',14,'bold'),width=8,bg='green')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=''
        self.label_1=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='green',bg='white')
        self.label_1.grid(row=1,column=1,padx=5,sticky=W)

        
        #=====================function declaration======================

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear_func(self):
        self.text.delete('1.0',END)
        self.entry.set('')
        
        
    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg="Please enter some input"
            self.label_1.config(text=self.msg,fg='green')
        else:
            self.msg=''
            self.label_1.config(text=self.msg,fg='green')

        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
            
        elif (self.entry.get()=='how are you'):
              self.text.insert(END,'\n\n'+'Bot: fine and you')
               
        elif (self.entry.get()=='fantastic'):
              self.text.insert(END,'\n\n'+'Bot: nice to hear')

        elif (self.entry.get()=='more information'):
              self.text.insert(END,'\n\n'+'Bot: kinjalhp1990@gmail.com')

        elif (self.entry.get()=='what is your name'):
              self.text.insert(END,'\n\n'+'Bot: my name is mr.Hacker')

        elif (self.entry.get()=='how does face recognition work'):
              self.text.insert(END,'\n\n'+'Bot: face recognition is a way of\nrecognizing a human face through\ntechnology.A fecial recognition\nsystem uses biomatrics. to map')
              
        elif (self.entry.get()=='bye'):
              self.text.insert(END,'\n\n'+'Bot: Thank you for chatting')

        else:
            self.text.insert(END,'\n\n'+"Bot: sorry I didn't get it")
        
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
