from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD

font_bold = ("Segoe UI", 14, BOLD)
font = ("Segoe UI", 14)
bg = '#939393'
rel = 'flat'

class MyApp: #Widgets

     def __init__(self, master):
        frame = Frame(root, width= 470, height= 480, bg= '#939393')
        frame.pack()

        self.Personal_Title = Label(frame, text="Personal Information", font=("Segoe UI", 14), bg='#939393')
        self.First_name = Label(frame, text=('First Name'),font=("Segoe UI", 10), bg= '#939393')
        self.Last_name = Label(frame, text="Last Name",font=("Segoe UI", 10), bg= '#939393')
        self.Courses = Label(frame, text="Courses",font=("Segoe UI", 10), bg= '#939393')
        self.Birthday = Label(frame, text="Birthday",font=("Segoe UI", 10), bg= '#939393')
        self.Skills = Label(frame, text="Skills",font=("Segoe UI", 10), bg= '#939393')
        self.E1 = Entry(frame, font=("Segoe UI", 10), textvariable="")
        self.E2 = Entry(frame, font=("Segoe UI", 10), textvariable="")
        self.E3 = Entry(frame, font=("Segoe UI", 10), textvariable="")
        self.E4 = Entry(frame, font=("Segoe UI", 10), textvariable="")
        self.Clear = Button(frame, text="Clear", font=("Segoe UI", 10), relief='flat', command=self.clear)
        self.Submit = Button(frame, text="Submit", font=("Segoe UI", 10), relief='flat',command=self.submit)
        self.List = ttk.Combobox(frame, values=["Computer Science", "Information Technology", "Computer Engineering"], font=("Segoe UI", 10))
        self.final_result = Label(frame, text="")

        self.Personal_Title.place(x=12, y=24)
        self.First_name.place(x=72, y=135)
        self.Last_name.place(x=74, y=164)
        self.Courses.place(x=90, y=195)
        self.Birthday.place(x=87, y=224)
        self.Skills.place(x=109, y=253)
        self.E1.place(x=152, y=137, width= 210, height= 23)
        self.E2.place(x=152, y=165, width= 210, height= 23)
        self.List.place(x=152, y=195, width= 210, height= 23)
        self.E3.place(x=152, y=224, width= 210, height= 23)
        self.E4.place(x=152, y=253, width= 210, height= 23)
        self.Clear.place(x=103, y=305, width=75, height=23)
        self.Submit.place(x=287, y=305, width=75, height=23)
        
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
         self.Personal_information = Label(top, text="Personal Information", font=font, bg=bg)
         self.Personal_information.place(x=12, y=9)
         self.lb1 = Listbox(top, font=font_bold, bg=bg, bd=0, selectbackground='#939393', highlightthickness=0, relief=rel)
         self.lb2 = Listbox(top, font=font, bg=bg, bd=0, selectbackground='#939393', highlightthickness=0, relief=rel )

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
