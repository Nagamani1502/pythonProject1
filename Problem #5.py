from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text = "Student Management System",bd = 10, relief =GROOVE,font=("times new roman",40,"bold"), bg = "yellow",fg = "red")
        title.pack(side = TOP, fill=X)


#====Manage Frame==========================
        Manage_Frame = Frame(self.root, bd = 4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=560)

        m_title = Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1,column=0, pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman", 14, "bold"))
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg="crimson", fg="white",
                        font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

#======= Button Frame =======================
        btn_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=30,y=605,width=420)

        Addbtn = Button(btn_Frame, text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10).grid(row=0, column=3, padx=10, pady=10)

        # ====Detail Frame==========================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_Search = Label(Detail_Frame, text="Search By", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame, width=10,font=("times new roman", 14, "bold"),state='readonly')
        combo_Search['values'] = ("Roll", "Name", "Contact")
        combo_Search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_Search=Entry(Manage_Frame,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Serach",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

#======= Table Frame ========================

        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        student_table = ttk.Treeview(Table_Frame,columns={"roll","name","email","gender","contact","dob","Address"}, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        """student_table.heading("roll", text="Roll No")
        student_table.heading("name", text="Name")
        student_table.heading("email", text="Email")
        student_table.heading("gender", text="Gender")
        student_table.heading("contact", text="Contact")
        student_table.heading("dob",text="D.O.B")
        student_table.heading("Address", text="Address")
        student_table['show']='headings'
        student_table.column("roll",width=0)
        student_table.column("name", width=1)
        student_table.column("email", width=2)
        student_table.column("gender", width=3)
        student_table.column("contact", width=4)
        student_table.column("dob", width=5)
        student_table.column("Address", width=6)
        student_table.pack(fill = BOTH,expand=1)"""


root = Tk()
ob = Student(root)
root.mainloop()

