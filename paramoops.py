# BLL
import pickle
from tkinter import messagebox
import re

class customer:
    listcus = []
    listp=[]


    def __init__(self):
        self.age = 0
        self.name= ""
        self.id = 0
        self.mobile = 0
        self.mobile1=0

        self.data=0


    def addcustomer(self):
        customer.listcus.append(self)

    def autoid(self):
        import random
        while (1):
            self.id = random.randint(1, 100000)
            self.id = str(self.id) + self.name[:2] + str(self.age)

            if customer.listcus.count(self.id) == 0:
                break

    def checkname(self):
        if len(self.name)!=0:
            for e in self.name:
                if (ord(e)>=65 and ord(e)<=90 or ord(e)>=97 and ord(e)<=122) or ord(e)==" ":
                    flag=0

                else:
                   flag=1
                    
                if flag==0:

                  return True
        else:
            messagebox.showinfo("CMSPL","Name in alphabets")

    def checkmobile(self):
        if len(self.mobile)!=0:


            if len(self.mobile)==10:
                self.mobile = int(self.mobile)
                return True
            else:
                messagebox.showinfo("Error!","ENTER 10 Digit mobile number")

        else:
            messagebox.showinfo("CMSPL", "ENTER 10 Digit mobile number")

    def checkmobile2(self):
        if len(self.mobile1)!=0:


            if len(self.mobile1)==10:
                self.mobile1 = int(self.mobile1)
                return True
            else:
                messagebox.showinfo("CMSPL","ENTER 10 Digit mobile number")

        else:
            messagebox.showinfo("CMSPL", "ENTER 10 Digit mobile number")


    def showcustomer(self):
        print(f"\tage:{self.age}"
              f"\tname:{self.name}"
              f"\tid:{self.id}"
              f"\tmobile:{self.mobile}")

    def searchcustomer(self):


         for e in customer.listcus:


            if e.mobile == int(self.mobile):
                self.name = e.name
                self.age = e.age
                self.id = e.id
                self.data=e.data
                return
            elif len(self.id)!=0:


                if e.id == self.id:
                    self.name = e.name
                    self.age = e.age
                    self.data = e.data
                    self.mobile=e.mobile
                    return

            elif len(self.data)!= 0:

                if e.data == self.data:
                    self.name = e.name
                    self.age = e.age
                    self.mobile = e.mobile
                    self.id = e.id
                    return
            else:
                pass

#AGE
    def modifycustomer(self):

        for e in customer.listcus:
            if e.mobile == self.mobile:

                if len(str(self.age))!=0:
                    self.id=e.id
                    self.mobile=e.mobile
                    self.data=e.data
                    self.name=e.name
                    e.age=self.age
                    return
            else:
                pass

    def modifycustomer1(self):

        for e in customer.listcus:
            if e.mobile == self.mobile:

                if len(str(self.age)) != 0:
                    self.id = e.id
                    self.mobile = e.mobile
                    self.data = e.data
                    e.name = self.name
                    self.age = e.age
                    return
            else:
                pass

    def modifycustomer2(self):

        for e in customer.listcus:
            if e.mobile == self.mobile:

                if len(str(self.mobile1)) != 0:
                    self.id = e.id
                    e.mobile = self.mobile1
                    self.data = e.data
                    self.name = e.name
                    self.age = e.age
                    return
            else:
                pass

    def modifycustomer3(self):

        for e in customer.listcus:
            if e.mobile == self.mobile:

                if len(self.data) != 0:
                    self.id = e.id
                    self.mobile = e.mobile
                    e.data = self.data
                    self.name = e.name
                    self.age = e.age
                    return
            else:
                pass
    def checkmobile1(self):
        for e in customer.listcus:
            if e.mobile==self.mobile:

                return True

            else:
                messagebox.showinfo("CMSPL","NO mobile no found")


    def checkemail(self):
        if len(self.data)!=0:
            self.p = "\w+@\w+[.]\w+"
            result = re.findall(self.p, self.data)
            print(result)
            for self.e in result:
                if self.e == self.data:

                    return True

        else:
            messagebox.showinfo("CMSPL","ENTER YOUR EMAILID")

    def checkage(self):
        if len(self.age)!=0:
            self.age=int(self.age)

            if self.age >= 12 and self.age <= 100 :
                return True



            else:
                messagebox.showinfo("CMSPL", "ENTER AGE BETWEEN 12 and 100")
        #else:
            #messagebox.showinfo("CMSPL","ENTER AGE BETWEEN 12 and 100" )

    def deletecustomer(self):
        if(len(customer.listcus)!=0):
            pass
        else:
            raise  ValueError("zero number of id in the data list")
        for e in customer.listcus:

                if e.id == self.id:
                   self.name1=e.name
                   self.mobile=e.mobile
                   self.data=e.data


                   customer.listcus.remove(e)
                   messagebox.showinfo("CMSPL","Data Deleted successfully")
                   break
                else:
                    raise ValueError("ID NOT FOUND")


    @staticmethod
    def func1(ob):
        return ob.age

    def savetopickle(self):
        f=open("C:/Users/pc/pycharmProjects/ParamProjects/game1.txt","wb")
        pickle.dump(customer.listcus,f)

        f.close()

    def loadfrompickle(self):
        f=open("C:/Users/pc/pycharmProjects/ParamProjects/game1.txt","rb")
        customer.listcus=pickle.load(f)
        f.close()
    @staticmethod
    def sortcustomer(l1,key=None):
        if key==None:
            for i in range(len(l1)-1):
                for j in range(i+1,len(l1)):
                    if l1[i]>l1[j]:
                        l1[i],l1[j]=l1[j],l1[i]
        else:
            for i in range(len(l1) - 1):
                for j in range(i + 1, len(l1)):
                    if key(l1[i])>key(l1[i]):
                        l1[i], l1[j] = l1[j], l1[i]








    def showall(self):
        for i in customer.listcus:

            # customer.listp.append(e)
            # print(type(e))
            # for i in customer.listp:
            #      self.data1[i]=i.id,i.age,i.name,i.mobile,i.data
            #
            #      print(self.data1[i])


                print(f"\tid:{i.id}"
                      f"\tage:{i.age}"
                      f"\tname:{i.name}"
                      f"\temail:{i.data}")






#PL
if __name__=="__main__":
    while (1):
        try:
            choice = int(input('''enter your choice
            1-add customer
            2-searchcustomer
            3-modifycustomer
            4-delete customer
            5-showallcustomer
            7-save to pickle
            8-load from pickle
            9-sortcustomer'''))
            if choice == 1:
                while(1):
                    try:
                        cus = customer()
                        cus.checkage()
                        cus.checkname()

                        cus.checkmobile()
                        cus.autoid()
                        cus.addcustomer()
                        cus.showcustomer()
                    except Exception:
                        print("wrong ")
                    finally:
                        ch=input("do you want to y or n")
                        if ch=="n" or ch=="N":
                            break

            elif choice == 2:
                try:
                    cus = customer()
                    cus.id = input("enter your id")
                    cus.searchcustomer()

                except Exception as err:
                    print("error!",err)

            elif choice == 3:
                while (1):
                    cus = customer()
                    cus.id = input("enter your id:")
                    choice1 = int(input('''enter your choice between
                            1-name
                            2-age
                            3-mobile'''))

                    if choice1 == 1:
                        cus.checkname()
                        for e in customer.listcus:
                            if e.id==cus.id:
                                cus.age=e.age
                                cus.mobile=e.mobile
                        cus.modifycustomer()

                        break
                    elif choice1 == 2:
                        print("enter your updated age:")
                        cus.checkage()
                        for e in customer.listcus:
                            if e.id==cus.id:
                                cus.name=e.name
                                cus.mobile=e.mobile
                        cus.modifycustomer()
                        break

                    elif choice1 == 3:
                        print("enter your updated mobile number")
                        cus.checkmobile()
                        for e in customer.listcus:
                            if e.id == cus.id:
                                cus.name = e.name
                                cus.age = e.age
                        cus.modifycustomer()

                        break
                    elif choice1 == 4:
                        break
                    else:
                        print("enter correct choice")

                cus.showcustomer()
            elif choice == 4:
                try:
                    cus=customer()
                    cus.id = input("enter your id:")
                    cus.deletecustomer()
                except Exception as err:
                    print("error!",err)
                finally:
                    ch=input("do you want to continue y or n")
                    if ch=="n" or ch=="N":
                        pass


            elif choice == 5:

                showall()
            elif choice == 6:
                break
            elif choice==7:
                customer.savetopickle()
            elif choice==8:
                customer.loadfrompickle()
            elif choice==9:

                customer.sortcustomer(customer.listcus,key=customer.func1)
        except ValueError:
            print("enter correct choice")



