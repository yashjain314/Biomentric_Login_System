from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Variable Declarations
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        # BG IMAGE
        self.bg=ImageTk.PhotoImage(file=r"F:\Face Recognition Project\images\L3.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        
        # LEFT IMAGE
        self.bg1=ImageTk.PhotoImage(file=r"F:\Face Recognition Project\images\R1.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=500,height=550)

       # Main Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # Label and Entry

        #  ROW 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,))
        self.txt_lname.place(x=370,y=130,width=250)

        # ROW 2
        
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email Id",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # ROW 3
        
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Name of Your Home Town")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)




        security_A=Label(frame,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        # ROW 4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # CHECK BUTTON
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree Terms & Conditions",font=("times new roman",11,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        # SUBMIT BUTTON
        img=Image.open(r"F:\Face Recognition Project\images\Registernow.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=200)


        img1=Image.open(r"F:\Face Recognition Project\images\Loginnow.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=330,y=420,width=200)


# **********************Function Declaration***********************

    def register_data(self):
      if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
        messagebox.showerror("Error","All fields are required")
      elif self.var_pass.get()!=self.var_confpass.get():
        messagebox.showerror("Error","Password & Confirm Password must be same")    
      elif self.var_check.get()==0:
        messagebox.showerror("Error","Please agree our Terms & Conditions")
      else:
        conn=mysql.connector.connect(host="localhost",user="root",password="yash123",database="myData")
        my_cursor=conn.cursor()
        query=("select * from register where email=%s")
        value=(self.var_email.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        if row!=None:
              messagebox.showerror("Error","User already exist,please try with another email id")
        else:
          my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                 self.var_fname.get(),
                                                                                 self.var_lname.get(),
                                                                                 self.var_contact.get(),
                                                                                 self.var_email.get(),
                                                                                 self.var_securityQ.get(),
                                                                                 self.var_securityA.get(),
                                                                                 self.var_pass.get()
                                                                                  

                                                                                )) 
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Register Successfully")
                                                                                     











 









if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()

        