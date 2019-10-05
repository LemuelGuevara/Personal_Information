from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD

class MyApp: #Widgets

     def __init__(self, master):
        frame = Frame(root, width=470, height=480, bg='#939393')
        frame.pack()

        self.Personal_Title = Label(frame, text="Personal Information", font=("Segoe UI", 16), bg='#939393')
        self.labels = Listbox(frame, width=15, font=("Segoe UI", 14), bg='#939393', bd=0, selectbackground='#939393', highlightthickness=0, relief='flat')

        for item in ['First Name', 'Last Name', 'Courses', 'Birthday', 'Skills']:
            self.labels.insert(END, item)
            self.labels.place(x=70, y=136)

            self.E1 = Entry(frame, font=("Segoe UI", 10), textvariable="")
            self.E2 = Entry(frame, font=("Segoe UI", 10), textvariable="")
            self.E3 = Entry(frame, font=("Segoe UI", 10), textvariable="")
            self.E4 = Entry(frame, font=("Segoe UI", 10), textvariable="")
            self.Clear = Button(frame, text="Clear", font=("Segoe UI", 10), relief='flat', command=self.clear)
            self.Submit = Button(frame, text="Submit", font=("Segoe UI", 10), relief='flat',command=self.submit)
            self.List = ttk.Combobox(frame, font=("Segoe UI", 10), values=["Computer Science", "Information Technology", "Computer Engineering"])

            self.Personal_Title.place(x=12, y=24)
            self.E1.place(x=180, y=139, width= 210, height= 21)
            self.E2.place(x=180, y=165, width= 210, height= 21)
            self.List.place(x=180, y=192, width= 210, height= 21)
            self.E3.place(x=180, y=218, width= 210, height= 21)
            self.E4.place(x=180, y=245, width= 210, height= 21)
            self.Clear.place(x=65, y=315, width=75, height=23)
            self.Submit.place(x=315, y=315, width=75, height=23)
        
     def clear(self):
         self.E1.delete(0, 'end')
         self.E2.delete(0, 'end')
         self.E3.delete(0, 'end')
         self.E4.delete(0, 'end')
         self.List.set('')

     def submit(self):
        if self.E1.get() == "":
           messagebox.showinfo("Personal Info", "Please fill up the form.")
        elif self.E2.get() == "":
            messagebox.showinfo("Personal Info", "Please fill up the form.")
        elif self.List.get() == "":
            messagebox.showinfo("Personal Info", "Please fill up the form.")
        elif self.E3.get() == "":
            messagebox.showinfo("Personal Info", "Please fill up the form.")
        elif self.E4.get() == "":
            messagebox.showinfo("Personal Info", "Please fill up the form.")
        else:
            messagebox.showinfo("Personal Info", "Your information hase been submitted\n Click OK to proceed.")         
            top = Toplevel(width=451, height=354, bg='#939393')
            self.Personal_information = Label(top, text="Personal Information", font=("Segoe UI", 14), bg='#939393')
            self.Personal_information.place(x=12, y=9)
            self.lb1 = Listbox(top, font=("Segoe UI", 14, BOLD), bg='#939393', bd=0, selectbackground='#939393', highlightthickness=0, relief='flat')
            self.lb2 = Listbox(top, font=("Segoe UI", 14), bg='#939393', bd=0, selectbackground='#939393', highlightthickness=0, relief='flat')
         
            fN = str(self.E1.get() + " " +  self.E2.get())
            cRS = str(self.List.get())
            bTD = str(self.E3.get())
            sKS = str(self.E4.get())

        for item in ["Name:", "Course:", "Birthday:", "Skills:"]:
            self.lb1.insert(END, item)
            self.lb1.place(x=12, y=78)

        for result in [fN, cRS, bTD, sKS]:
            self.lb2.insert(END, result)
            self.lb2.place(x=103, y=78, width=205)

            top.title("Personal Info")
            top.mainloop()
      
root = Tk()
root.title("Registration Form")
app = MyApp(root)
root.mainloop()
