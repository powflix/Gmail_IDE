from tkinter import filedialog
from tkinter import *
import smtplib   
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


    
class gmail:
    
    def __init__(self,master):
        self.master=master
        master.title('GMAIL')
        RWidth=master.winfo_screenwidth()
        RHeight=master.winfo_screenheight()
        frame1=Frame(master,width=RWidth, height = 40,bg='#ffe6e6')
        frame2=Frame(master,width=RWidth, height = 60,bg='#ffe6e6')
        frame3=Frame(master,width=RWidth, height = 20,bg='#ffe6e6')
        frame4=Frame(master,width=RWidth, height = RHeight-230,bg='#ffe6e6')
        frame5=Frame(master,width=RWidth, height = 100,bg='#ffe6e6')
        frame1.place(x=0,y=0)
        frame2.place(x=0,y=40)
        frame3.place(x=0,y=100)
        frame4.place(x=0,y=120)
        frame5.place(x=0,y=RHeight-110)
        self.L1=Label(frame1, text="from",bg='#ffe6e6').place(x=0,y=0)
        self.L2=Label(frame1, text="Password",bg='#ffe6e6').place(x=0,y=20)
        self.L3=Label(frame2, text='To',bg='#ffe6e6').place(x=0,y=0)
        self.L4=Label(frame2, text='Cc',bg='#ffe6e6').place(x=0,y=20)
        self.L5=Label(frame2, text='Bcc',bg='#ffe6e6').place(x=0,y=40)
        self.L6=Label(frame3, text='Subject',bg='#ffe6e6').place(x=0,y=0)
        self.L7=Label(frame4, text='Body',bg='#ffe6e6').place(x=0,y=0)
        
        self.sender=Entry(frame1,width=250,bd=0,bg='#ffe6e6')
        self.password=Entry(frame1,show='*',width=250,bd=0,bg='#ffe6e6')
        self.to=Entry(frame2,width=250,bd=0,bg='#ffe6e6')
        self.Cc=Entry(frame2,width=250,bd=0,bg='#ffe6e6')
        self.Bcc=Entry(frame2,width=250,bd=0,bg='#ffe6e6')
        self.subject=Entry(frame3,width=250,bd=0,bg='#ffe6e6')
        self.body=Text(frame4,width=250,height=200,bd=0,bg='#ffe6e6')
        
        self.send=Button(frame5,text='Send',width=5,bg='#ffe6e6',relief=FLAT,command=lambda: self.mail()).place(x=0,y=20)
        self.formating=Button(frame5,text='A',width=5,bg='#ffe6e6',relief=FLAT).place(x=60,y=20)
        self.Attach=Button(frame5,text='B',width=5,bg='#ffe6e6',relief=FLAT,command=lambda: self.attach()).place(x=120,y=20)
        self.insertLink=Button(frame5,text='C',bg='#ffe6e6',width=5,relief=FLAT).place(x=180,y=20)
        self.insertEmoji=Button(frame5,text='D',bg='#ffe6e6',width=5,relief=FLAT).place(x=240,y=20)
        self.insertfile=Button(frame5,text='E',bg='#ffe6e6',width=5,relief=FLAT).place(x=280,y=20)
        self.insertPhoto=Button(frame5,text='F',bg='#ffe6e6',width=5,relief=FLAT).place(x=320,y=20)
        self.delete=Button(frame5,text='G',width=5,bg='#ffe6e6',relief=FLAT).place(x=360,y=20)
        
  
        
        self.sender.place(x=70,y=0)
        self.password.place(x=70,y=20)
        self.to.place(x=70,y=0)
        self.Cc.place(x=70,y=20)
        self.Bcc.place(x=70,y=40)
        self.subject.place(x=70,y=0)
        self.body.place(x=70,y=0)

    def mail(self):
        msg=MIMEMultipart()
        msg['From']=self.sender.get()
        msg['To']=self.to.get()
        msg['Subject']=self.subject.get()
        msg.attach(MIMEText(str(self.body.get('1.0',END)),'plain'))

            #filename='/home/avianjjai/Downloads/Fuzzy_logic_paper.pdf'
        attachment=open(self.attachment,'rb')
        
        p=MIMEBase('application','octet-stream')

        p.set_payload((attachment).read())
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % self.attachment)
        msg.attach(p)
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(self.sender.get(),self.password.get())
        text=msg.as_string()
        s.sendmail(self.sender.get(),self.to.get(),text)
        s.quit()
        
    def attach(self):
        self.master.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.attachment=str(self.master.filename)
        print(self.attachment)
root= Tk()
mygui=gmail(root)
root.mainloop()



