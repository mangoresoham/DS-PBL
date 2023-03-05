from tkinter import *
import customtkinter
from tkcalendar import DateEntry
from tkinter.messagebox import showinfo
import pandas as pd
import qrcode
from pyqrcode import create
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import numpy as np
import matplotlib.pyplot as plt

#For slot 1
na=[]
ph=[]
na1=[]
ph1=[]
deln=[]
delp=[]
cna=[]
cph=[]
data=''
data1=''

#For 2nd slot
data2=''
data1_2=''
na2=[]
ph2=[]
cna2=[]
cph2=[]
deln2=[]
delp2=[]
na1_2=[]
ph1_2=[]

count=0

customtkinter.set_appearance_mode("dark")
root=customtkinter.CTk()
root.geometry("500x450")

#Qrcode
def qrcode_win(tf,r,d,s,t):
    root = customtkinter.CTkToplevel(r)
    root.title('Qr Code Generator')
    data = tf
    def gen_qr():
        global dta
        dta = data
        dta = create(dta)
        test = dta.xbm(scale=5)
        global xbm_image
        xbm_image = tkinter.BitmapImage(data=test, foreground="blue", background='yellow', )
        image_view.configure(image=xbm_image)

        #statement.config(text="this is a qr code for : " + data)
    #statement=tkinter.Label(root, text="Your has being confirmed from our side \n {} ".format(d.get_date(),s.get(),t.get())
    stat=customtkinter.CTkLabel(root, text="Your Booking has been confirmed for {}\nslot-{}\npeople-{}".format(d.get_date(),s.get(),t.get()), font=("Times New Roman",22))
    make_button = customtkinter.CTkButton(root, text=" Get QR", font=("Times New Roman",20), command=gen_qr)
    image_view = customtkinter.CTkLabel(root)
    #statement = tkinter.Label(root)
    stat.pack()
    make_button.pack()
    image_view.pack()
    #make_button.grid(row=2, column=0, columnspan=2)
    #image_view.grid(row=3, column=0, columnspan=2)
    #statement.grid(row=4, column=0, columnspan=2)

    #make_button.grid(row=2, column=0, columnspan=2)
    #image_view.grid(row=3, column=0, columnspan=2)
    #statement.grid(row=4, column=0, columnspan=2)

#Admin Window Login
def login_win():
    app=customtkinter.CTkToplevel(root)
    app.title("Login")
    app.geometry("350x200")
    app.config(bg="#242320")
    font1=('Arial',15, 'bold')

    global username
    username='hello'
    global password
    password='123'
    global trials
    trials=0
    def login():
        global username
        global password
        global trials
        written_username=username_entry.get()
        written_password=password_entry.get()
        if(written_username=='' or written_password==''):
            messagebox.showwarning (title="Error",message="Enter your username and password.")
        
        elif(written_username==username and written_password==password):
            choice_1(root)
        
        elif((written_username !=username or written_password!=password) and trials<3):
            messagebox.showerror(title="Error",message="You username or password is not correct.")
            trials=trials+1
            if(trials!=3):
                trials_label=customtkinter.CTkLabel(app, text=f'You have {3-trials} trials',font=("Times New Roman",20), text_color="#FFFFFF")
                trials_label.place(x=100, y=160)
            if(trials==3):
                login_button.destroy()
                locked_label=customtkinter.CTkLabel(app, text=f"Your Acc is locked.",font=("Times New Roman",20), text_color="#FFFFFF")
                locked_label.place(x=100, y=160)
            

    username_label=customtkinter.CTkLabel(app, text="Username:",font=("Times New Roman",20), text_color="#FFFFFF")
    username_label.place(x=2,y=25)
    password_label=customtkinter.CTkLabel(app,text="Password: ",font=("Times New Roman",20), text_color="#FFFFFF")
    password_label.place(x=2, y=75)

    username_entry=customtkinter.CTkEntry(app,fg_color="#FFFFFF",font=("Times New Roman",20),text_color="#000000", border_color="#FFFFFF",width=200, height=1)
    username_entry.place(x=130,y=25)
    password_entry=customtkinter.CTkEntry (app, show="*", fg_color="#FFFFFF", font=("Times New Roman",20), text_color="#000000", border_color="#FFFFFF",width=200, height=1)
    password_entry.place(x=130,y=75)
    login_button=customtkinter.CTkButton(app, command=login, text="Login",font=("Times New Roman",20), text_color="#FFFFFF",fg_color="#07b527", hover_color="#07b527", width=50)
    login_button.place(x=140, y=120)

#Admin Window Choosing the type of operation
def choice_1(r):
    root=customtkinter.CTkToplevel(r)
    customtkinter.set_appearance_mode("dark")
    root.geometry("500x450")
    customtkinter.set_appearance_mode("dark")
    stat=customtkinter.CTkLabel(master=root, text="Please select operation to be performed.", font=("Times New Roman",18))
    stat.pack()
    emp=customtkinter.CTkLabel(master=root, text=" ")
    emp.pack()
    combobox_var=customtkinter.StringVar()
    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)
    combobox=customtkinter.CTkComboBox(master=root, values=['See the record of Bookings', 'Compare the two slots'], command=combobox_callback, variable=combobox_var)
    combobox.pack()

    emp1=customtkinter.CTkLabel(master=root, text=" ")
    emp1.pack()
    next=customtkinter.CTkButton(master=root, text="Next", font=("Times New Roman",18), command=lambda: choice_1_2(root, combobox_var))
    next.pack()

#Admin Window to choose Slot
def choice_1_2(r,c):
    if(c.get()=='See the record of Bookings'):
        root=customtkinter.CTkToplevel(r)
        customtkinter.set_appearance_mode("dark")
        root.geometry("500x450")
        customtkinter.set_appearance_mode("dark")
        stat=customtkinter.CTkLabel(master=root, text="Please select required slot.", font=("Times New Roman",18))
        stat.pack()
        emp=customtkinter.CTkLabel(master=root, text=" ")
        emp.pack()
        combobox_var=customtkinter.StringVar()
        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)
        combobox=customtkinter.CTkComboBox(master=root, values=['9:00am to 11:00am','3:00pm to 5:00pm'], command=combobox_callback, variable=combobox_var)
        combobox.pack()

        emp1=customtkinter.CTkLabel(master=root, text=" ")
        emp1.pack()
        next=customtkinter.CTkButton(master=root, text="Next", font=("Times New Roman",18), command=lambda: data_extraction(root, combobox_var))
        next.pack()
    elif(c.get()=='Compare the two slots'):
        graph()

#Calling Excel
def cal_excel(r):
    # initalise the tkinter GUI
    root = tk.Toplevel(r)
    root.geometry("500x500") # set the root dimensions
    root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
    root.resizable(False, False) # makes the root window fixed in size.

    # Frame for TreeView
    frame1 = tk.LabelFrame(root, text="Excel Data")
    frame1.place(height=250, width=500)

    # Frame for open file dialog
    file_frame = tk.LabelFrame(root, text="Open File")
    file_frame.place(height=100, width=400, rely=0.65, relx=0)

    # Buttons
    button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
    button1.place(rely=0.65, relx=0.50)

    button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
    button2.place(rely=0.65, relx=0.30)

    # The file/file path text
    label_file = ttk.Label(file_frame, text="No File Selected")
    label_file.place(rely=0, relx=0)


    ## Treeview Widget
    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


    def File_dialog():
        """This Function will open the file explorer and assign the chosen file path to label_file"""
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
        label_file["text"] = filename
        return None


    def Load_excel_data():
        """If the file selected is valid this will load the file into the Treeview"""
        file_path = label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

        except ValueError:
            messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column) # let the column heading = column name

        df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None


    def clear_data():
        tv1.delete(*tv1.get_children())
        return None

#Registration Window
def registration_wid(r):
    root=customtkinter.CTkToplevel(r)
    customtkinter.set_appearance_mode("dark")
    root.geometry("500x500")
    root.title("Booking Form")

    label_tilte=customtkinter.CTkLabel(master=root, text="Booking Details", font=("Time New Roman",20))
    label_tilte.pack(fill=customtkinter.X, padx=5, pady=5)

    label_date=customtkinter.CTkLabel(master=root, text="Select Date", font=("Times New Roman",18))
    label_date.place(x=130,y=70)

    cal=DateEntry(root, selectmode="day", font=("Times New Roman",16))
    cal.place(x=450,y=110)

    label_st=customtkinter.CTkLabel(master=root,width=120, text="Please Select Time Slot", font=("Times New Roman",18))
    label_st.place(x=90, y=120)

    combobox_var=customtkinter.StringVar()
    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)
    combobox=customtkinter.CTkComboBox(master=root, values=['9:00am to 11:00am','3:00pm to 5:00pm'], command=combobox_callback, variable=combobox_var)
    combobox.place(x=290,y=120)

    label_people=customtkinter.CTkLabel(master=root, text="Enter the number of persons", font=("Times New Roman", 18))
    label_people.place(x=70, y=180)

    combobox_var_2=customtkinter.StringVar()
    def combobox_callback_2(choice):
        print("combobox dropdown clicked:", choice)
    combobox_2=customtkinter.CTkComboBox(master=root, values=['1','2','3','4','5'], command=combobox_callback_2, variable=combobox_var_2)
    combobox_2.place(x=290, y=180)

    def new_registration():
        """ handle the register event """
        if(int(combobox_var_2.get())>5):
            showinfo(
                title='Slot Full',
                message='All the slots are full, please try another slot'
            )
        else:
            reg_back(root,cal, combobox_var, combobox_var_2)

        #showinfo(
            #title='Registration Successfull',
            #message=f'Booking is done for  {cal.get_date()} {combobox_var.get()} for {combobox_var_2.get()} persons !'
        #)

    button_reg=customtkinter.CTkButton(master=root, text="Register", command=new_registration)
    button_reg.place(x=100, y=250)

    button_can=customtkinter.CTkButton(master=root, text="Cancel", command=root.destroy)
    button_can.place(x=250, y=250)


#Details Window for slot 1
def details_win(r,d,s,t):
    root=customtkinter.CTkToplevel(r)
    customtkinter.set_appearance_mode("dark")
    #root=customtkinter.CTk()
    root.geometry("500x500")

    myentries_na=[]
    myentries_ph=[]
    num1=int(t.get())

    lab_1=customtkinter.CTkLabel(master=root, text="Name", width=20, font=("Times New Roman", 25))
    lab_1.grid(row=0, column=0)

    lab_2=customtkinter.CTkLabel(master=root, text="Aadhaar",width=20,font=("Times New Roman", 25))
    lab_2.grid(row=0, column=1)

    for j in range(num1):
        entry_1=customtkinter.CTkEntry(master=root, font=("Times New Roman",30))
        entry_1.grid(row=j+1, column=0, padx=30, pady=40)
        myentries_na.append(entry_1)
        

        entry_2=customtkinter.CTkEntry(master=root, font=("Times New Roman",30))
        entry_2.grid(row=j+1, column=1, padx=30, pady=40)
        myentries_ph.append(entry_2)
            

    button_s=customtkinter.CTkButton(master=root, text="Submit", height=30, width=170, command=lambda: detail_back(myentries_na,myentries_ph, d, s, t))
    button_s.place(x=110, y=640)

#Details Window for slot 2
def details_win2(r,d,s,t):
    root=customtkinter.CTkToplevel(r)
    customtkinter.set_appearance_mode("dark")
    #root=customtkinter.CTk()
    root.geometry("500x500")

    myentries_na=[]
    myentries_ph=[]
    num1=int(t.get())

    lab_1=customtkinter.CTkLabel(master=root, text="Name", width=20, font=("Times New Roman", 25))
    lab_1.grid(row=0, column=0)

    lab_2=customtkinter.CTkLabel(master=root, text="Aadhaar",width=20,font=("Times New Roman", 25))
    lab_2.grid(row=0, column=1)
        

    for j in range(num1):
        entry_1=customtkinter.CTkEntry(master=root, font=("Times New Roman",30))
        entry_1.grid(row=j+1, column=0, padx=30, pady=40)
        myentries_na.append(entry_1)
        

        entry_2=customtkinter.CTkEntry(master=root, font=("Times New Roman",30))
        entry_2.grid(row=j+1, column=1, padx=30, pady=40)
        myentries_ph.append(entry_2)
            

    button_s=customtkinter.CTkButton(master=root, text="Submit", height=30, width=170, command=lambda: detail_back2(myentries_na,myentries_ph, d, s, t))
    button_s.place(x=110, y=640)



#cancelation Window
def cancel_Inm(r):
    root=customtkinter.CTkToplevel(r)
    root.geometry("500x500")
    customtkinter.set_appearance_mode("dark")
    stat=customtkinter.CTkLabel(master=root, text="Please select your booked slot", font=("Times New Roman",18))
    stat.pack()
    emp=customtkinter.CTkLabel(master=root, text=" ")
    emp.pack()
    combobox_var=customtkinter.StringVar()
    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)
    combobox=customtkinter.CTkComboBox(master=root, values=['9:00am to 11:00am','3:00pm to 5:00pm'], command=combobox_callback, variable=combobox_var)
    combobox.pack()

    emp1=customtkinter.CTkLabel(master=root, text=" ")
    emp1.pack()
    next=customtkinter.CTkButton(master=root, text="Next", font=("Times New Roman",18), command=lambda: cancel_In(root, combobox_var))
    next.pack()
def cancel_In(r, s):
    base1=customtkinter.CTkToplevel(r)
    base1.geometry("500x500")
    customtkinter.set_appearance_mode("dark")
    root=customtkinter.CTk()
    root.geometry("500x500")

    lab_1=customtkinter.CTkLabel(master=base1, text="Name", width=20, font=("Times New Roman", 20))
    lab_1.place(x=150,y=130)

    entry_1=customtkinter.CTkEntry(master=base1)
    entry_1.place(x=220, y=130)

    lab_2=customtkinter.CTkLabel(master=base1, text="Aadhaar",width=20,font=("Times New Roman", 20))  
    lab_2.place(x=150,y=200)  
    
    entry_2=customtkinter.CTkEntry(master=base1)
    entry_2.place(x=220,y=200)

    button_s=customtkinter.CTkButton(master=base1, text="Submit", command=lambda: cancel_bk(entry_1,entry_2,s))
    button_s.place(relx=0.5, rely=0.55, anchor=CENTER)

#Creating a lable
myLable=customtkinter.CTkLabel(master=root, text="Welcome To\nDarshan Booking System\n", font=("Verdana",25), text_color="#FFBF00")
myLable.pack()
#creating buttons for options 
button_1=customtkinter.CTkButton(master=root, height=40, width=190, text="   Book a slot   ",fg_color="#81BC00", hover_color="#557B00",command=lambda: registration_wid(root))
button_1.pack(pady=20, padx=20)

button_2=customtkinter.CTkButton(master=root, height=40, width=190, text="Cancel a Booking", hover_color="#9D2B22", fg_color="#DD0000", command=lambda: cancel_Inm(root))
button_2.pack(padx=20, pady=20)

button_3=customtkinter.CTkButton(master=root, height=40, width=190, text="Admin", command=login_win)
button_3.pack(pady=20, padx=40)
#button_1.pack(side=TOP)
#button_2.pack(side=TOP)
#button_3.pack(side=TOP)


#--------------------------------------------------------------------

#Panda Backend
def details(l,k,c):
    Details={}
    Details["Name"]=[]
    Details["Aadhaar"]=[]
    Details.update({"Name":l})
    Details.update({"Aadhaar":k})
    print(Details)
    if(c.get()=='9:00am to 11:00am'):
        df=pd.DataFrame(Details)
        df.to_excel("1st Slot.xlsx", index=False)
        print(df)
    elif(c.get()=='3:00pm to 5:00pm'):
        df=pd.DataFrame(Details)
        df.to_excel("2nd Slot.xlsx", index=False)
        print(df)
    

#Registration Backend
def reg_back(r,d,s,t):
    if(s.get()=='9:00am to 11:00am'):
        # opening file for names
        file=open("name.txt","a")
        file.close()
        #opening file for aadhaar nos.
        file=open("aadhaar.txt","a")
        file.close()
        num=int(t.get())
        
        # file updation for names
        file=open('name.txt', "r")
        name_content=file.readlines()
        for line in name_content:
            namef=line.strip()
            na.append(namef)
        #na.pop(0)
        #print(na)     # remove this later
        file.close()

        # file updation for aadhaar numbers
        file=open('aadhaar.txt', "r")
        aadhaar_content=file.readlines()
        for line in aadhaar_content:
            aadhaarf=line.strip()
            ph.append(aadhaarf)
        #ph.pop(0)
        #print(ph)    # remove this later
        file.close()
        print(len(na)+num)
        if(len(na)+num>6):
            showinfo(
            title='Slot Full',
            message='All the slots are full, please try another slot'
        )

        else:
            details_win(r,d,s,t)
    elif(s.get()=='3:00pm to 5:00pm'):
        # opening file for names
        file=open("name2.txt","a")
        file.close()
        #opening file for aadhaar nos.
        file=open("aadhaar2.txt","a")
        file.close()
        num2=int(t.get())
        
        # file updation for names
        file=open('name2.txt', "r")
        name_content2=file.readlines()
        for line in name_content2:
            namef2=line.strip()
            na2.append(namef2)
        #na.pop(0)
        #print(na)     # remove this later
        file.close()

        # file updation for aadhaar numbers
        file=open('aadhaar2.txt', "r")
        aadhaar_content2=file.readlines()
        for line in aadhaar_content2:
            aadhaarf2=line.strip()
            ph2.append(aadhaarf2)
        #ph.pop(0)
        #print(ph)    # remove this later
        file.close()
        print(len(na2)+num2)
        if(len(na2)+num2>6):
            showinfo(
            title='Slot Full',
            message='All the slots are full, please try another slot'
        )

        else:
            details_win2(r,d,s,t)

#Cancellation Backend
def cancel_bk(e1,e2,s):
    if(s.get()=="9:00am to 11:00am"):
        name_del=e1.get()
        aadhaar_del=str(e2.get())
        if(name_del=='' or aadhaar_del==''):
            messagebox.showerror(title="Error", message="Please enter the specified data")
        else:
            file=open('aadhaar.txt', "r")
            aadhaar_content_del=file.readlines()
            for line in aadhaar_content_del:
                aadhaar_d=line.strip()
                delp.append(aadhaar_d)
            delp.pop(0)

            file=open('name.txt', "r")
            name_content_del=file.readlines()
            for line in name_content_del:
                name_d=line.strip()
                deln.append(name_d)
            deln.pop(0)
            print(deln)
            print(delp)

            for j in delp:
                if(str(j)==aadhaar_del):
                    global index_p
                    index_p=delp.index(j)
                    print(index_p)
                    #delp.pop(index_p)
                    #print(delp)
            
            for i in deln:
                if(i==name_del):
                    global index_n
                    index_n=deln.index(i)
                    print(index_n)
                    #deln.pop(index_n)
                    #print(deln)
            p=index_p
            if(index_n==p):
                    deln.pop(index_n)
                    delp.pop(index_p)
                    print(delp)
                    print(deln)

                    file_nd=open("name.txt","w")
                    for i in range(len(deln)):
                        file_nd.write("\n{0}".format(deln[i]))
                    file_nd.close()

                    file_pd=open("aadhaar.txt","w")
                    for i in range(len(deln)):
                        file_pd.write("\n{0}".format(delp[i]))
                    file_pd.close()
                    showinfo(
                        title='Cancelled Successfully',
                        message='Your Booking has been cancelled successfully'
                    )
            else:
                messagebox.showerror(title="Error",message="You have entered incorrect data! Please try again.")

    elif(s.get()=="3:00pm to 5:00pm"):
        name_del2=e1.get()
        aadhaar_del2=str(e2.get())
        if(name_del2=='' or aadhaar_del2==''):
            messagebox.showerror(title="Error", message="Please enter specified data")
        else:
            file=open('aadhaar2.txt', "r")
            aadhaar_content_del2=file.readlines()
            for line in aadhaar_content_del2:
                aadhaar_d2=line.strip()
                delp2.append(aadhaar_d2)
            delp2.pop(0)

            file=open('name2.txt', "r")
            name_content_del2=file.readlines()
            for line in name_content_del2:
                name_d2=line.strip()
                deln2.append(name_d2)
            deln2.pop(0)
            print(deln2)
            print(delp2)

            for j in delp2:
                if(str(j)==aadhaar_del2):
                    global index_p2
                    index_p2=delp2.index(j)
                    print(index_p2)
                    #delp2.pop(index_p2)
                    #print(delp2)
            
            for i in deln2:
                if(str(i)==name_del2):
                    global index_n2
                    index_n2=deln2.index(i)
                    print(index_n2)
                    #deln2.pop(index_n2)
                    #print(deln2)
            if(index_n2==index_p2):
                deln2.pop(index_n2)
                delp2.pop(index_p2)
                print(delp2)
                print(deln2)
                
                file_nd=open("name2.txt","w")
                for i in range(len(deln2)):
                    file_nd.write("\n{0}".format(deln2[i]))
                file_nd.close()

                file_pd=open("aadhaar2.txt","w")
                for i in range(len(delp2)):
                    file_pd.write("\n{0}".format(delp2[i]))
                file_pd.close()
                showinfo(
                    title='Cancelled Successfully',
                    message='Your Booking has been cancelled successfully'
                )
            else:
                messagebox.showerror(title="Error",message="You have entered incorrect data! Please try again.")

#Details Backend for slot 1
def detail_back(e1,e2,d,s,t):    
    data=''
    data1=''
    val1=recheck(e2)
    if(val1>0):
        messagebox.showerror(title="Error",message="You have entered incorrect data! Please try again.")
    else:
        for i in e1:
            na.append(str(i.get()))
            #index_n=na.index('\n')
            #print(index_n)
            cna.append(str(i.get()))      
        #na.pop(1)
        #cna.pop(1)
        print(na)
        print(cna)

        for j in e2:
            ph.append(str(j.get()))
            cph.append(str(j.get()))
        
        #ph.pop(1)
        #cph.pop(1)
        print(ph)
        print(cph)

        #na.append(name1)
        #cna.append(name1)
        #ph.append(aadhaar1)
        #cph.append(aadhaar1)

        # updation of names file
        file_nd=open("name.txt","a")
        for i in range(len(cna)):
            file_nd.write("\n{0}".format(cna[i]))
        file_nd.close()

        # updation of aadhaar no. file
        file_pd=open("aadhaar.txt","a")
        for i in range(len(cph)):
            file_pd.write("\n{0}".format(cph[i]))
        file_pd.close()

        for i in range(len(cna)):
            data=data+"\n"+cna[i]
        for j in range(len(cph)):
            data1=data1+"\n"+str(cph[j])
        tfinal="Name:"+data+"\n----------------\n"+"Aadhaar No.:"+data1
        qrcode_win(tfinal,root,d,s,t)
        img = qrcode.make(tfinal)
        img.save('MyQRCode1.png')

        showinfo(
        title='Registration Successfull',
        message=f'Booking is done for  {d.get_date()} {s.get()} for {t.get()} persons !'
        )

#Details Backend for slot 2
def detail_back2(e1,e2,d,s,t):    
    data2=''
    data1_2=''
    val1=recheck(e2)
    if(val1>0):
        messagebox.showerror(title="Error",message="You have entered incorrect data! Please try again.")
    else:
        for i in e1:
            na2.append(str(i.get()))
            #index_n=na.index('\n')
            #print(index_n)
            cna2.append(str(i.get()))

        #na2.pop(1)
        #cna2.pop(1)
        print(na2)
        print(cna2)

        for j in e2:
            ph2.append(str(j.get()))
            cph2.append(str(j.get()))
        #ph2.pop(1)
        #cph2.pop(1)
        print(ph2)
        print(cph2)

        #na.append(name1)
        #cna.append(name1)
        #ph.append(aadhaar1)
        #cph.append(aadhaar1)

        # updation of names file
        file_nd=open("name2.txt","a")
        for i in range(len(cna2)):
            file_nd.write("\n{0}".format(cna2[i]))
        file_nd.close()

        # updation of aadhaar no. file
        file_pd=open("aadhaar2.txt","a")
        for i in range(len(cph2)):
            file_pd.write("\n{0}".format(cph2[i]))
        file_pd.close()

        for i in range(len(cna2)):
            data2=data2+"\n"+cna2[i]
        for j in range(len(cph2)):
            data1_2=data1_2+"\n"+str(cph2[j])
        tfinal2="Name:"+data2+"\n-----------------------\n"+"Aadhaar No.:"+data1_2
        qrcode_win(tfinal2,root,d,s,t)
        img2 = qrcode.make(tfinal2)
        img2.save('MyQRCode2.png')

        showinfo(
        title='Registration Successfull',
        message=f'Booking is done for  {d.get_date()} {s.get()} for {t.get()} persons !'
        )

#Admin Backend
def data_extraction(r,c):
    if(c.get()=='9:00am to 11:00am'):
        file=open('aadhaar.txt', "r")
        aadhaar_content_1=file.readlines()
        for line in aadhaar_content_1:
            aadhaarf=line.strip()
            ph1.append(aadhaarf)
        ph1.pop(0)

        file=open('name.txt', "r")
        name_content_1=file.readlines()
        for line in name_content_1:
            namef=line.strip()
            na1.append(namef)
        na1.pop(0)
        details(na1,ph1,c)
        cal_excel(r)

    elif(c.get()=='3:00pm to 5:00pm'):
        file=open('aadhaar2.txt', "r")
        aadhaar_content_1_2=file.readlines()
        for line in aadhaar_content_1_2:
            aadhaarf2=line.strip()
            ph1_2.append(aadhaarf2)
        ph1_2.pop(0)

        file=open('name2.txt', "r")
        name_content_1_2=file.readlines()
        for line in name_content_1_2:
            namef2=line.strip()
            na1_2.append(namef2)
        na1_2.pop(0)
        details(na1_2,ph1_2,c)
        cal_excel(r)

#Getting Graphs
def graph():
    file=open('name.txt', "r")
    name_content_1=file.readlines()
    for line in name_content_1:
        namef=line.strip()
        na1.append(namef)
    na1.pop(0)
    
    file=open('name2.txt', "r")
    name_content_1_2=file.readlines()
    for line in name_content_1_2:
        namef2=line.strip()
        na1_2.append(namef2)
    na1_2.pop(0)

    total1=len(na1)
    total2=len(na1_2)

    raw={}
    raw["9:00am-11:00am"]=[]
    raw["3:00pm-5:00pm"]=[]
    raw.update({"9:00am-11:00am":total1})
    raw.update({"3:00pm-5:00pm":total2})
    print(raw)

    Slots=list(raw.keys())
    Bookings=list(raw.values())
    fig=plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(Slots, Bookings, color ='maroon', width = 0.2)
    plt.show()

#Rechecking the adhar number
def recheck(e2):
    count=0
    for j in e2:
        val=str(j.get())
        if(len(val)!=4 or not val.isdigit()):
            count=count+1
    return count

root.mainloop()