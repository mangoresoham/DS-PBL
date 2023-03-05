from datetime import date
import calendar
from queue import Queue
import qrcode
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#For 1st slot
data=''
data1=''
nq=Queue(maxsize=5)
pq=Queue(maxsize=5)
na=[]
ph=[]
na1=[]
ph1=[]
deln=[]
delp=[]
cna=[]
cph=[]

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
today = date.today()
d1 = today.strftime("%d/%m/%Y")

#function to get all details for admin
def details(l,k):
    Details={}
    Details["Name"]=[]
    Details["Phone"]=[]
    Details.update({"Name":l})
    Details.update({"Phone":k})
    print(Details)
    df=pd.DataFrame(Details)
    df.to_excel("{}st Slot.xlsx".format(choice3), index=False)
    print(df)

curr_date = date.today()
print(calendar.day_name[curr_date.weekday()],":",d1)
day=calendar.day_name[curr_date.weekday()]

if(day=="Monday"):
    print("1:Monday\n2:Tuesday\n3:Wednesday\n4:Thursday\n5:Friday\n6:Saturday\n7:Sunday")
elif(day=="Tuesday"):
    print("1:Tuesday\n2:Wednesday\n3:Thursday\n4:Friday\n5:Saturday\n6:Sunday\n7:Monday")
elif(day=="Wednesday"):
    print("1:Wednesday\n2:Thursday\n3:Friday\n4:Saturday\n5:Sunday\n6:Monday\n7:Tuesday")
elif(day=="Thursday"):
    print("1:Thursday\n2:Friday\n3:Saturday\n4:Sunday\n5:Monday\n6:Tuesday\n7:Wednesday")
elif(day=="Friday"):
    print("1:Friday\n2:Saturday\n3:Sunday\n4:Monday\n5:Tuesday\n6:Wednesday\n7:Thursday")
elif(day=="Saturday"):
    print("1:Saturday\n2:Sunday\n3:Monday\n4:Tuesday\n5:Wednesday\n6:Thursday\n7:Friday")
elif(day=="Sunday"):
    print("1:Sunday\n2:Monday\n3:Tuesday\n4:Wednesday\n5:Thursday\n6:Friday\n7:Saturday")

choice=input("Enter your required day:")
print("User choose {0}.".format(choice.capitalize()))

print("1:Book a new slot\n2:Cancel Booking\n3:Admin")
choice1=input("Enter the operation you want to perform:")

if(choice1=="1"):
    print("Darshan Timings are:")
    print("1:9:00am-11:00am\n2:3:00pm-5:00pm")
    choice2=input("Enter your choice:")

    if(choice2=="1"):
        # opening file for names
        file=open("name.txt","a")
        file.close()
        #opening file for phone nos.
        file=open("phone.txt","a")
        file.close()
        num=int(input("Enter the number of bookings to be done:"))
        # file updation for names
        file=open('name.txt', "r")
        name_content=file.readlines()
        for line in name_content:
            namef=line.strip()
            na.append(namef)
        #na.pop(0)
        #print(na)     
        # remove this later
        file.close()

        # file updation for phone numbers
        file=open('phone.txt', "r")
        phone_content=file.readlines()
        for line in phone_content:
            phonef=line.strip()
            ph.append(phonef)
        #ph.pop(0)
        #print(ph)    # remove this later
        file.close()
        if(len(na)+num>5):
            print("All slots are booked, there is no empty slot")
        else:   
            print("Enter details of the memebers:")
            #na.pop(0)
            #ph.pop(0)
            for i in range(num):
                name1=input("Enter your name:")
                phone1=int(input("Enter your phone number:"))
                

                na.append(name1)
                cna.append(name1)
                ph.append(phone1)
                cph.append(phone1)
                # updation of names file
                file=open("name.txt","a")
                file.write("\n{0}".format(name1))
                file.close()

                # updation of phone no. file
                file=open("phone.txt","a")
                file.write("\n{0}".format(str(phone1)))
                file.close()
            for i in range(len(cna)):
                data=data+"\n"+cna[i]
            for j in range(len(cph)):
                data1=data1+"\n"+str(cph[j])
            tfinal=data+"\t\t"+data1
            img = qrcode.make(tfinal)
            img.save('MyQRCode1.png')
            #print(cna)
            #print(cph)
            print("Your Booking has been confirmed from our side\nslot:- 9:00am-11:00am\nday:- {}\ndate:- {}".format(day,d1))

    elif(choice2=="2"):
        # opening file for names
        file=open("name2.txt","a")
        file.close()
        #opening file for phone nos.
        file=open("phone2.txt","a")
        file.close()
        num2=int(input("Enter the number of bookings to be done:"))
        # file updation for names
        file=open('name2.txt', "r")
        name_content2=file.readlines()
        for line in name_content2:
            namef2=line.strip()
            na2.append(namef2)
        #na.pop(0)
        #print(na)     # remove this later
        file.close()

        # file updation for phone numbers
        file=open('phone2.txt', "r")
        phone_content2=file.readlines()
        for line in phone_content2:
            phonef2=line.strip()
            ph2.append(phonef2)
        #ph.pop(0)
        #print(ph)    # remove this later
        file.close()
        if(len(na)+num2>5):
            print("All slots are booked, there is no empty slot")
        else:   
            print("Enter details of the memebers:")
            #na.pop(0)
            #ph.pop(0)
            for i in range(num2):
                name1_2=input("Enter your name:")
                phone1_2=int(input("Enter your phone number:"))
                

                na2.append(name1_2)
                cna2.append(name1_2)
                ph2.append(phone1_2)
                cph2.append(phone1_2)
                # updation of names file
                file=open("name2.txt","a")
                file.write("\n{0}".format(name1_2))
                file.close()

                # updation of phone no. file
                file=open("phone2.txt","a")
                file.write("\n{0}".format(str(phone1_2)))
                file.close()
            for i in range(len(cna2)):
                data2=data2+"\n"+cna2[i]
            for j in range(len(cph2)):
                data1_2=data1_2+"\n"+str(cph2[j])
            tfinal2=data2+"\t\t"+data1_2
            img2 = qrcode.make(tfinal2)
            img2.save('MyQRCode2.png')
            #print(cna)
            #print(cph)
            print("Your Booking has been confirmed from our side\nslot:- 9:00am-11:00am\nday:- {}\ndate:- {}".format(day,d1))

elif(choice1=="2"):
    print("1:9:00am-11:00am\n2:3:00pm-5:00pm")
    choice4=input("Enter Your Required Slot:")
    if(choice4=="1"):
        name_del=input("Enter your name")
        phone_del=int(input("Enter phone number:"))

        file=open('phone.txt', "r")
        phone_content_del=file.readlines()
        for line in phone_content_del:
            phone_d=line.strip()
            delp.append(phone_d)
        delp.pop(0)

        file=open('name.txt', "r")
        name_content_del=file.readlines()
        for line in name_content_del:
            name_d=line.strip()
            deln.append(name_d)
        deln.pop(0)
        #print(deln)
        #print(delp)

        for i in deln:
            if(i==name_del):
                index_n=deln.index(i)
                print(index_n)
                deln.pop(index_n)
                #print(deln)

        for j in delp:
            if(int(j)==phone_del):
                index_p=delp.index(j)
                print(index_p)
                delp.pop(index_p)
                #print(delp)

        file_nd=open("name.txt","w")
        for i in range(len(deln)):
            file_nd.write("\n{0}".format(deln[i]))
        file_nd.close()

        file_pd=open("phone.txt","w")
        for i in range(len(deln)):
            file_pd.write("\n{0}".format(delp[i]))
        file_pd.close()

    elif(choice4=="2"):
        name_del2=input("Enter your name")
        phone_del2=int(input("Enter phone number:"))

        file=open('phone2.txt', "r")
        phone_content_del2=file.readlines()
        for line in phone_content_del2:
            phone_d2=line.strip()
            delp2.append(phone_d2)
        delp2.pop(0)

        file=open('name2.txt', "r")
        name_content_del2=file.readlines()
        for line in name_content_del2:
            name_d2=line.strip()
            deln2.append(name_d2)
        deln2.pop(0)
        #print(deln)
        #print(delp)

        for i in deln2:
            if(i==name_del2):
                index_n2=deln2.index(i)
                print(index_n2)
                deln2.pop(index_n2)
                #print(deln)

        for j in delp2:
            if(int(j)==phone_del2):
                index_p2=delp2.index(j)
                print(index_p2)
                delp2.pop(index_p2)
                #print(delp)

        file_nd=open("name2.txt","w")
        for i in range(len(deln2)):
            file_nd.write("\n{0}".format(deln2[i]))
        file_nd.close()

        file_pd=open("phone2.txt","w")
        for i in range(len(delp2)):
            file_pd.write("\n{0}".format(delp2[i]))
        file_pd.close()

elif(choice1=="3"):
    username=input("Enter your username:")
    password=input("Enter password:")

    if(username=="admin" and password=="admin@123"):
        print("Welcome Admin.")
        print("1:See the record of Bookings\n2:Compare the two slots")
        choice1_1=input("Enter the operation you want to perform:")
        if(choice1_1=="1"):
            print("1:9:00am-11:00am\n2:3:00pm-5:00pm")
            choice3=input("Enter the day, for which u want the data:")
            if(choice3=="1"):
                file=open('phone.txt', "r")
                phone_content_1=file.readlines()
                for line in phone_content_1:
                    phonef=line.strip()
                    ph1.append(phonef)
                ph1.pop(0)

                file=open('name.txt', "r")
                name_content_1=file.readlines()
                for line in name_content_1:
                    namef=line.strip()
                    na1.append(namef)
                na1.pop(0)
                details(na1,ph1)

            elif(choice3=="2"):
                file=open('phone2.txt', "r")
                phone_content_1_2=file.readlines()
                for line in phone_content_1_2:
                    phonef2=line.strip()
                    ph1_2.append(phonef2)
                ph1_2.pop(0)

                file=open('name2.txt', "r")
                name_content_1_2=file.readlines()
                for line in name_content_1_2:
                    namef2=line.strip()
                    na1_2.append(namef2)
                na1_2.pop(0)
                details(na1_2,ph1_2)
        
        elif(choice1_1=="2"):         
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