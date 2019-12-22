import paramoops
from tkinter import *
from tkinter import messagebox
root=Tk()
root.config(bg="#29A887")
root.geometry("1100x1000")

#ADD CUSTOMER

def addcus():
    cus1=paramoops.customer()

    cus1.age = varAge.get().strip()
    cus1.name = varName.get().strip()
    cus1.mobile = varmbn.get().strip()
    cus1.data=varemid.get().strip()
    try:
        if (cus1.checkage() and cus1.checkname() and cus1.checkmobile())is True:
            if cus1.checkemail() is True:
                cus1.autoid()

                cus1.addcustomer()
                cus1.savetopickle()
                messagebox.showinfo("CMSPL", "CUSTOMER ADDED SUCCESSFULLY")
                varId.set(cus1.id)
                varAge.set(" ")
                varName.set(" ")
                varmbn.set(" ")
                varemid.set(" ")

            else:
                messagebox.showinfo("Error!", "Enter correct format like\t"
                                             "example@something.com")
        #else:

           # messagebox.showinfo("CMSPL", "PLEASE FILL ALL THE PARTICULARS OR ADD CORRECT DETAILS")


    except ValueError:
        messagebox.showinfo("CMSPL", "PLEASE FILL ALL THE PARTICULARS ")
#SEARCH CUSTOMER
cus1=paramoops.customer()
Options = [ "search by Mbno", "search by ID","search by email"]
param = StringVar()
param.set(Options[0])
def searchcus():

    set=OptionMenu(root, param,*Options)
    set.config(font=("Arial", 15), bg="white")
    set.grid(row=12,column=1)


    if param.get()==Options[0]:
      title="choice"
      text="Do you want to search it by Mbno?"
      reply=messagebox.askquestion(title,text)
      if reply == "yes":
          cus1.mobile=varmbn.get()


          while len(str(cus1.mobile))==0:

                  messagebox.showinfo("CMSPL","ENTER YOUR Mbno please")
                  break


          if len(cus1.mobile)!= 0:
                    cus1.searchcustomer()

                    varAge.set(cus1.age)
                    varName.set(cus1.name)
                    varId.set(cus1.id)
                    varemid.set(cus1.data)

                    if cus1.age != 0 and len(cus1.name) != 0 and len(cus1.id) != 0 and len(cus1.data) != 0:
                        messagebox.showinfo("CMSPL", "CUSTOMER FOUND")
                    else:
                        messagebox.showinfo("CMSPL", "Mbno NOT FOUND")

      else:
          messagebox.showinfo("CMSPL", "Select your choice")
    elif param.get()==Options[1]:
        title = "choice"
        text = "Do you want to search it by ID?"
        reply = messagebox.askquestion(title, text)
        if reply == "yes":
            cus1.id = varId.get()

            while len(cus1.id) == 0:
                messagebox.showinfo("CMSPL", "ENTER YOUR ID")
                break

            if len(cus1.id)!= 0:

                cus1.searchcustomer()

                varAge.set(cus1.age)
                varName.set(cus1.name)
                varmbn.set(cus1.mobile)
                varemid.set(cus1.data)

                if cus1.age != 0 and len(cus1.name) != 0 and cus1.mobile != 0 and len(cus1.data) != 0:
                    messagebox.showinfo("CMSPL", "CUSTOMER FOUND")


                else:
                    messagebox.showinfo("CMSPL", "ID  number NOT FOUND")
        else:
            messagebox.showinfo("CMSPL","select your choice")



    else:
        title = "choice"
        text = "Do you want to search it by email?"
        reply = messagebox.askquestion(title, text)
        if reply == "yes":
            cus1.data = varemid.get()

            while len(cus1.data) == 0:
                messagebox.showinfo("CMSPL", "ENTER YOUR Emailid")
                break

            if len(cus1.data) != 0:

                cus1.searchcustomer()

                varAge.set(cus1.age)
                varName.set(cus1.name)
                varmbn.set(cus1.mobile)
                varId.set(cus1.id)

                if cus1.age != 0 and len(cus1.name) != 0 and cus1.mobile != 0 and len(cus1.data) != 0:
                    messagebox.showinfo("CMSPL", "CUSTOMER FOUND")


                else:
                    messagebox.showinfo("CMSPL", "Email  ID NOT FOUND")





def showcus():

        cus1= paramoops.customer()


        root1=Tk()
        root1.config(bg="skyblue")
        label6 = Label(root1, text="CUSTOMER ID :", font=("", 14, "bold"), fg="black",)
        label6.grid(row=0, column=0, sticky=W, pady=14)
        label7=Label(root1,text="CUSTOMER Age",font=("times",14,"bold"),fg="black")
        label7.grid(row=0,column=1,padx=17)
        label8 = Label(root1, text="CUSTOMER NAME", font=("times", 14, "bold"), fg="black")
        label8.grid(row=0, column=2, padx=17)
        label9 = Label(root1, text="CUSTOMER mno", font=("times", 14, "bold"), fg="black")
        label9.grid(row=0, column=3, padx=17)
        label10 = Label(root1, text="CUSTOMER Email id", font=("times", 14, "bold"), fg="black")
        label10.grid(row=0, column=4, padx=17)


        for i in range(len(paramoops.customer.listcus)):
            cus1=paramoops.customer.listcus[i]



            label12 = Label(root1, text=cus1.id, font=("times", 14, "bold"), fg="black")

            label12.grid(row=i+1, column=0, padx=17)

            label13 =Label(root1, text=cus1.age, font=("times", 14, "bold"), fg="pink")
            label13.grid(row=i+1, column=1, padx=10)
            label14 = Label(root1, text=cus1.name, font=("times", 14, "bold"), fg="black")
            label14.grid(row=i+1, column=2, padx=17)

            label15 = Label(root1, text=cus1.mobile, font=("times", 14, "bold"), fg="black")
            label15.grid(row=i+1, column=3, padx=17)
            label15 = Label(root1, text=cus1.data, font=("times", 14, "bold"), fg="black")
            label15.grid(row=i+1, column=4, padx=17)

        root1.geometry("650x600")
        root1.mainloop()

        




def deletecus():
    try:


        cus1 = paramoops.customer()
        cus1.id = varId.get()
        cus1.deletecustomer()
        varmbn.set(cus1.mobile)
        varName.set(cus1.name1)
    except ValueError:
        messagebox.showinfo("CMSPL","Enter your ID")






Options1=["Modify Age","Modify Name","Modify mobile number","Modify Email"]
param1=StringVar()
param1.set(Options1[0])

def modifycus():
    cus1=paramoops.customer()
    try:

        cus1.mobile=int(varmbn.get().strip())


        if cus1.checkmobile1() is True:
            messagebox.showinfo("CORRECT","Mobile number found")


            if len(str(cus1.mobile))!=0:
                set = OptionMenu(root, param1, *Options1)
                set.config(font=("Arial", 15),bg="white")
                set.grid(row=12,column=0)


                if param1.get() == Options1[0]:
                    title = "choice"
                    text = "Want to modify Age?"
                    reply = messagebox.askquestion(title, text)
                    if reply == "yes":
                        cus1.age=varAge.get()

                        while len((str(cus1.age)))== 0:
                            messagebox.showinfo("CMSPL", "ENTER YOUR Updated Age")
                            break

                        if len(str(cus1.age))!=0:
                            cus1.modifycustomer()

                            varAge.set(cus1.age)
                            varName.set(cus1.name)
                            varId.set(cus1.id)
                            varemid.set(cus1.data)
                            varmbn.set(cus1.mobile)




                            if cus1.age != 0 and len(cus1.name) != 0 and len(cus1.id) != 0 and len(cus1.data) != 0:
                                messagebox.showinfo("CMSPL", "CUSTOMER'S Data Updated Successfully")


                            else:
                                messagebox.showinfo("CMSPL", "Customer particulars cannot be Updated")
                    else:
                        messagebox.showinfo("CMSPL","Select Your choice")


                elif param1.get()==Options1[1]:
                    title="choice"
                    text="Want to modify Name?"
                    reply=messagebox.askquestion(title,text)
                    if reply=="yes":
                        cus1.name=varName.get().strip()

                        while len(cus1.name)==0:
                            messagebox.showinfo("CMSPL","Enter your updated Name")
                            break
                        if len(cus1.name)!=0:
                            cus1.modifycustomer1()

                            varName.set(cus1.name)
                            varmbn.set(cus1.mobile)
                            varAge.set(cus1.age)
                            varId.set(cus1.id)
                            varemid.set(cus1.data)

                            if cus1.age != 0 and len(cus1.name) != 0 and len(cus1.id) != 0 and len(cus1.data) != 0:
                                messagebox.showinfo("CMSPL", "CUSTOMER'S Data Updated Successfully")


                            else:
                                messagebox.showinfo("CMSPL", "Customer particulars cannot be Updated")
                elif param1.get()==Options1[2]:
                    title="choice"
                    text="Want to modify Mbno"
                    reply=messagebox.askquestion(title,text)
                    if reply=="yes":
                        cus1.mobile1=varmbn.get().strip()

                        if cus1.checkmobile2() is True:
                            cus1.modifycustomer2()

                            varName.set(cus1.name)
                            varmbn.set(cus1.mobile1)
                            varAge.set(cus1.age)
                            varId.set(cus1.id)
                            varemid.set(cus1.data)

                            if cus1.age != 0 and len(cus1.name) != 0 and len(cus1.id) != 0 and len(cus1.data) != 0:
                                messagebox.showinfo("CMSPL", "CUSTOMER'S Data Updated Successfully")


                            else:
                                messagebox.showinfo("CMSPL", "Customer particulars cannot be Updated")

                else:

                    param1.get()==Options1[3]
                    title = "choice"
                    text = "Want to modify Email?"
                    reply = messagebox.askquestion(title, text)
                    if reply == "yes":
                        cus1.data = varemid.get().strip()

                        while len(cus1.data) == 0:
                            messagebox.showinfo("CMSPL", "Enter your updated Email")
                            break
                        if len(cus1.data) != 0:
                            cus1.modifycustomer3()

                            varName.set(cus1.name)
                            varmbn.set(cus1.mobile)
                            varAge.set(cus1.age)
                            varId.set(cus1.id)
                            varemid.set(cus1.data)

                            if cus1.age != 0 and len(cus1.name) != 0 and len(cus1.id) != 0 and len(cus1.data) != 0:
                                messagebox.showinfo("CMSPL", "CUSTOMER'S Data Updated Successfully")


                            else:
                                messagebox.showinfo("CMSPL", "Customer particulars cannot be Updated")

    except ValueError:
        messagebox.showinfo("CMSPL","Enter Mbno")





    # else:
    #     messagebox.showinfo("CMSPL","Enter your Mbn")


def reset():
    varId.set("")
    varmbn.set("")
    varAge.set("")
    varName.set(" ")
    varemid.set(" ")

def func1(e):
    btn1["bg"]="#b43757"

def func2(e):
    btn1["bg"]="#00A86B"

def func3(e):
    btn2["bg"]="#b43757"

def func4(e):
    btn2["bg"]="#00A86B"

def func5(e):
    btn3["bg"]="#b43757"

def func6(e):
    btn3["bg"]="#00A86B"

def func7(e):
    btn4["bg"]="#b43757"

def func8(e):
    btn4["bg"]="#00A86B"

def func9(e):
    btn5["bg"]="#b43757"

def func10(e):
    btn5["bg"]="#00A86B"

def func11(e):
    btn6["bg"]="white"

def func12(e):
    btn6["bg"]="white"



label5=Label(root,text="Customer Management System",font=("",25,"bold","underline"),bg="#b43757")
label5.grid(row=0,column=1,padx=12,pady=2)



#ID
label1=Label(root,text="CUSTOMER ID :",font=("",14,"bold"),bg="#C7EA46",width=18)
label1.grid(row=2,column=0,sticky=W,pady=14)
varId=StringVar()
entry1=Entry(root,font=16,textvariable=varId)
entry1.grid(row=2,column=1,sticky=W)

#AGE
label2=Label(root,text="ENTER CUSTOMER AGE :",font=("",14,"bold"),bg="#C7EA46",pady=8)
label2.grid(row=3,column=0,sticky=W,pady=14)
varAge=StringVar()
entry2=Entry(root,font=16,textvariable=varAge)
entry2.grid(row=3,column=1,sticky=W)


#CUSTOMER NAME
label3=Label(root,text="ENTER CUSTOMER NAME :",font=("",14,"bold"),bg="#C7EA46")
label3.grid(row=4,column=0,sticky=W,pady=14)
varName=StringVar()
entry3=Entry(root,font=16,textvariable=varName)
entry3.grid(row=4,column=1,sticky=W)

#CUSTOMER MOBILENUMBER
label4=Label(root,text="ENTER CUSTOMER Mno :",font=("",14,"bold"),bg="#C7EA46")
label4.grid(row=6,column=0,sticky=W,pady=14)
varmbn=StringVar()
entry4=Entry(root,font=16,textvariable=varmbn)
entry4.grid(row=6,column=1,sticky=W)


#CUSTOMER EMAILID
label5=Label(root,text="ENTER CUSTOMER EMAILID:",font=("",14,"bold"),bg="#C7EA46")
label5.grid(row=8,column=0,sticky=W,pady=14)
varemid=StringVar()
entry5=Entry(root,font=16,textvariable=varemid)
entry5.grid(row=8,column=1,sticky=W,padx=4)


#BUTTONS
btn1=Button(root,text="ADD CUSTOMER",bg="#00A86B",font=("",12,"bold"),command=addcus)
btn1.grid(row=16,column=1,pady=30)
btn1.bind("<Enter>",func1)
btn1.bind("<Leave>",func2)

btn2=Button(root,text="SEARCH CUSTOMER",bg="#00A86B",font=("",12,"bold"),command=searchcus)
btn2.grid(row=10,column=1,pady=30)
btn2.bind("<Enter>",func3)
btn2.bind("<Leave>",func4)


btn3=Button(root,text="SHOW CUSTOMER",bg="#00A86B",font=("",12,"bold"),command=showcus)
btn3.grid(row=10,column=5,padx=20)
btn3.bind("<Enter>",func5)
btn3.bind("<Leave>",func6)


btn4=Button(root,text="Delete customer's Record",bg="#00A86B",font=("",13,"bold"),command=deletecus)
btn4.grid(row=16,column=0,pady=20)
btn4.bind("<Enter>",func7)
btn4.bind("<Leave>",func8)

btn5=Button(root,text="Modify customer's Record",bg="#00A86B",font=("",12,"bold"),command=modifycus)
btn5.grid(row=10,column=0,pady=20,padx=24)
btn5.bind("<Enter>",func9)
btn5.bind("<Leave>",func10)


btn6=Button(root,text="RESET",bg="red",font=("",16,"bold"),command=reset)
btn6.grid(row=2,column=10)
btn6.bind("<Enter>",func11)
btn6.bind("<Leave>",func12)

#
# menubar=Menu(root)
# filemenu=Menu(menubar,font=("times",65,"bold"))
# menubar.add_cascade(label="MODIFY ",menu=filemenu,font=("times",65,"bold"))
# filemenu.add_command(label='Name',command=func1,font=("times",12,"bold"))
# filemenu.add_command(label='Age',command=func1,font=("times",12,"bold"))
# filemenu.add_command(label='Mno',command=func1,font=("times",12,"bold"))


root.mainloop()
