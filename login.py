# =========== This is a comment =======
from tkinter import *
import pymysql
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter.ttk import Combobox
##from ttkthemes import themed_tk as tk


Data = []#this is a list
count = 0
## ======== Database Connection =======

connection = pymysql.connect(host= 'localhost',user = 'root',passwd = '',database = 'dbuser')
cursor = connection.cursor()
a = "Select * from tbluser;"

cursor.execute(a)
rows = cursor.fetchall()
for i in rows:
    Data.append(i)

connection.close()


# ========= Python Code =========

# =========== Login Functions ==================
def showpassed():
    global count
    count += 1
    a = e2.get()
    if(count % 2 == 0):
        e2.config(show = "*")
        e2.config(font=('Seoge UI', 21,'bold'))
        e2.delete('0',END)
        e2.insert(0,a)

    if(count % 2 == 1):
        e2.config(show = "")
        e2.config(font=('Seoge UI', 13,'bold'))
        e2.delete('0',END)
        e2.insert(0,a)

   

    
def clickuser(event):
    e1.delete(0, "end")
    e1.config(fg = 'black')     
    return None

def clickpass(event):
    e2.config(show = '*')
    e2.delete(0, "end")
    e2.config(font=('Seoge UI', 21,'bold'))
    e2.config(width = 14,fg = 'black')
    return None

def menu():
    win1 =Tk()
    win1.geometry("350x350")
    win1.title("Facebook")
    userL = Label(win1, text = 'Login Successful', font=('Seoge UI', 20,'bold') ,bg  = '#357376',fg = '#E5DFDF')
    userL.place(x = 60,y = 30)
    win1.mainloop()
    
def Login():
    global e1,e2,win1,userL
    usern = userInput.get()
    passw = passInput.get()

    for i in range(len(Data)):  
        if(usern == Data[i][1]) and (passw == Data[i][2]):
            
            win1.destroy()
            userModule()
    else:
        userL = Label(win1, text = 'Invalid username or password', font=('Seoge UI', 12,'bold') ,bg  = '#2f5887',fg = 'red').place(x = 60,y = 85)

    
def exit():
    win1.destroy()

# ======= User Module Functions ======
def exit2():
    win3.destroy()
def searchtext(event):
    search.delete('0',END)
    search.config(fg = 'black')
    
def searchname():
    s = strSearch.get()
    for i in tree2.get_children():#delete all data
        tree2.delete(i)
    print('hello')
    for i in range(len(Data)):
        if(s == Data[i][1]):
            tree2.insert('',END,text = 'Direct1',values = (Data[i][0],Data[i][1],Data[i][2],Data[i][3],Data[i][4],Data[i][5]) )
            search.delete('0',END)
            search.insert('0','Search user')
             
            

    
def delete():

    connection = pymysql.connect(host= 'localhost',user = 'root',passwd = '',database = 'dbuser')
    cursor = connection.cursor()
    a = "Select * from tbluser;"

    cursor.execute(a)
    rows = cursor.fetchall()
    for i in rows:
        Data.append(i)

    curItem = tree2.focus()
    a = tree2.item(curItem)
    box = a.get('values')
    print(box)
    box2 =  list(box)
    print(box2[0])
    for i in range(len(Data)):
        if(Data[i][0] == box2[0]):
            print('naa ra')
            cursor.execute("Update tbluser set Status = '0' where UserID = %s;",Data[i][0])

    connection.commit()
    connection.close()
        

def view():
    Data = []
    connection = pymysql.connect(host= 'localhost',user = 'root',passwd = '',database = 'dbuser')
    cursor = connection.cursor()
    a = "Select * from tbluser;"

    cursor.execute(a)
    rows = cursor.fetchall()
    for i in rows:
        Data.append(i)

    connection.close()
    for i in tree2.get_children():#delete all data
        tree2.delete(i)
    
    for i in range(len(Data)):
        if(Data[i][7] != 0):
            tree2.insert('','end', text = 'Direct1',values = (Data[i][0],Data[i][1],Data[i][2],Data[i][3],Data[i][4],Data[i][5]), tags = ('odd',))

def addEntry():
    connection = pymysql.connect(host= 'localhost',user = 'root',passwd = '',database = 'dbuser')
    cursor = connection.cursor()
    
    
    if(cmbtype.get() == 'Admin'):
        a = 1;
    if(cmbtype.get() == 'Employee'):
        a = 2;
        
    
    b = fname.get()
    c = lname.get()
    d = contact.get()
    e = uname.get()
    f = passwd.get()
    data2 = [uname.get(), passwd.get(),fname.get(), lname.get(), contact.get(), a]
    cursor.execute("INSERT INTO tbluser(Username, Password, fname, lname, Contact, UserTypeID,Status) values(%s,%s,%s,%s,%s,%s,%s)", (e,f,b,c,d,a,1))
    connection.commit()
    connection.close()
    win3.destroy()
    
def fnameE(event):
    fname1.delete('0',END)
def lnameE(event):
    lname1.delete('0',END)
def contactE(event):
    contact1.delete('0',END)
def unameE(event):
    uname1.delete('0',END)
def passE(event):
    passwd1.delete('0',END)
# =========== Users Modules ===========================
def AddUser():
    global cmbtype, fname, lname, contact, uname, passwd,win3
    global cmbuser, fname1, lname1, contact1, uname1, passwd1
    
    win3 = Toplevel(win2)
    win3.geometry("400x600")
    win3.title("Add user")
    win3.config(bg = '#2f5887')

    # ==== Add user logo ===
    imgadduser = ImageTk.PhotoImage(Image.open('add2.png'))
    Label(win3,image = imgadduser,bg = '#2f5887').place(x = 25, y = 30)
    Label(win3, text = 'Add User', font=('Seoge UI', 20,'bold') ,bg  = '#2f5887',fg = '#E5DFDF').place(x = 130,y = 65)

    # ==== User type ===
    style = ttk.Style()

    style.map('TCombobox', fieldbackground=[('readonly','#6497b1')])
    style.map('TCombobox', selectbackground=[('readonly', '#6497b1')])
    style.map('TCombobox', selectforeground=[('readonly', 'white')])
    
    en1 = Frame(win3,height = 47,width =280,bg = '#6497b1').place(x = 45,y = 150)
    utype = ['Admin','Employee']
    cmbtype= StringVar()
    cmbuser = ttk.Combobox(win3,style = 'TCombobox',textvariable = cmbtype, font = ('Segoe ui',15,'bold'),values = utype,width = 20,height =5)
    cmbuser.place(x = 60,y = 160,height =  30)
    cmbuser.set('User type')
    cmbuser['state'] = 'readonly'
    
    # ==== fname ===
    en2 = Frame(win3,height = 47,width =280,bg = '#6497b1').place(x = 45,y = 210)
    fname = StringVar()
    fname1 = Entry(win3,textvariable = fname,width =21,font=('Seoge UI', 16,'bold'),bg = '#6497b1',fg = 'white',borderwidth = 0)
    fname1.insert('0','Firstname')
    fname1.place(x = 60, y = 220)
    fname1.bind("<Button-1>",fnameE)

    # ==== Lastname ===
    en3 = Frame(win3,height = 47,width =280,bg = '#6497b1').place(x = 45,y = 270)
    lname = StringVar()
    lname1 = Entry(win3,textvariable = lname,width =21,font=('Seoge UI', 16,'bold'),bg = '#6497b1',fg = 'white',borderwidth = 0)
    lname1.insert('0','Lastname')
    lname1.place(x = 60, y = 280)
    lname1.bind("<Button-1>",lnameE)

    # ==== Contact ===
    en1 = Frame(win3,height = 47,width =280,bg = '#6497b1').place(x = 45,y = 330)
    contact = StringVar()
    contact1 = Entry(win3,textvariable = contact,width =21,font=('Seoge UI', 16,'bold'),bg = '#6497b1',fg = 'white',borderwidth = 0)
    contact1.insert('0','Contact')
    contact1.place(x = 60, y = 340)
    contact1.bind("<Button-1>",contactE)

    # ==== user ===
    en1 = Frame(win3,height = 47,width =280,bg = '#6497b1').place(x = 45,y = 390)
    uname = StringVar()
    uname1 = Entry(win3,textvariable = uname,width =21,font=('Seoge UI', 16,'bold'),bg = '#6497b1',fg = 'white',borderwidth = 0)
    uname1.insert('0','Username')
    uname1.place(x = 60, y = 400)
    uname1.bind("<Button-1>",unameE)

    # ==== pass ===
    en1 = Frame(win3,height = 47,width =280,bg = '#6497b1').place(x = 45,y = 450)
    passwd = StringVar()
    passwd1 = Entry(win3,textvariable = passwd,width =21,font=('Seoge UI', 16,'bold'),bg = '#6497b1',fg = 'white',borderwidth = 0)
    passwd1.insert('0','Password')
    passwd1.place(x = 60, y = 460)
    passwd1.bind("<Button-1>",passE)

    # == button ===
    btnadd = Button(win3,text = 'Add',font=('Seoge UI', 12,'bold'),bg = '#f39422',fg= 'white', command = addEntry, width = 13, height = 2,borderwidth = 0).place(x = 45,y = 520)
    btnadd = Button(win3,text = 'Cancel',font=('Seoge UI', 12,'bold'),bg = '#f39422',fg= 'white', command = exit2, width = 13,height = 2,borderwidth = 0).place(x = 195,y = 520)
    
    
    win3.resizable(False,False)
    win3.mainloop()
    

def userModule():
    global tree2,win2,search,strSearch
    win2 = Tk()
    win2.geometry("900x600")
    win2.title("user menu")
    win2.config(bg = '#6497b1')

## ==== Treeview styles ====
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview",background = '#b3cde0', fieldbackground="#b3cde0", foreground= "black")
    style.theme_use('clam')
    tree2 = ttk.Treeview(win2,selectmode='browse',style = 'Treeview')
    
## === scrollbar ===
    vsb = ttk.Scrollbar(win2, orient="vertical", command=tree2.yview)
    vsb.place(x=813, y=301, height = 228)
    tree2.configure(yscrollcommand=vsb.set)

    
# ==== Window Header ==
    userLogo = ImageTk.PhotoImage(Image.open('UserIcon.png'))
    Label(win2,image = userLogo,bg = '#6497b1').place(x = 20,y = 20)
    Label(win2, text = 'User Management', font=('Seoge UI', 34,'bold') ,bg  = '#6497b1',fg = '#E5DFDF').place(x = 170,y = 75)
    
    #buttons
    btnadd = Button(win2,text = 'Add User',font=('Seoge UI', 12,'bold'),bg = '#f39422',fg= 'white', command = AddUser, width = 10, height = 2,borderwidth = 0).place(x = 40,y = 205)
    btnview = Button(win2,text = 'View',font=('Seoge UI', 12,'bold'),bg = '#f39422',fg= 'white', command = view, width = 10, height = 2,borderwidth = 0).place(x = 150,y = 205)
    btndel = Button(win2,text = 'Delete',font=('Seoge UI', 12,'bold'),bg = '#f39422',fg= 'white', command = delete, width = 10, height = 2,borderwidth = 0).place(x = 260,y = 205)

    #search bar
    en1 = Frame(height = 47,width =240,bg = '#b3cde0').place(x = 490,y = 205)
    strSearch = StringVar()
    search = Entry(win2,textvariable = strSearch,width =15,font=('Seoge UI', 16,'bold'),bg = '#b3cde0',fg = 'white',borderwidth = 0)

    search.insert('0','Search Customer')
    search.place(x = 500, y = 215)
    search.bind("<Button-1>",searchtext)
    btndel = Button(win2,text = 'Search',font=('Seoge UI', 12,'bold'),bg = '#f39422',fg= 'white', command = searchname, width = 10, height = 2,borderwidth = 0).place(x = 725,y = 205)

    #table
    tree2['column'] = ('1','2','3','4','5','6')
    tree2['show'] = 'headings'
    tree2.column('1', width = 70,anchor = 'c')
    tree2.column('2', width = 160,anchor = 'c')
    tree2.column('3', width = 160,anchor = 'c')
    tree2.column('4', width = 160,anchor = 'c')
    tree2.column('5', width = 100,anchor = 'c')
    tree2.column('6', width = 120,anchor = 'c')
    tree2.tag_configure('odd', background='red')


    
    tree2.heading('1',text = 'UserID')
    tree2.heading('2',text = 'First Name')
    tree2.heading('3',text = 'Last Name')
    tree2.heading('4',text = 'Email')
    tree2.heading('5',text = 'Gender')
    tree2.heading('6',text = 'Contact')

    
    for i in range(len(Data)):
        
        if (Data[i][7] == 1):
            tree2.insert('','end', text = 'Direct1',values = (Data[i][0],Data[i][1],Data[i][2],Data[i][3],Data[i][4],Data[i][5]))

    tree2.tag_configure('odd', background='#E8E8E8')
    tree2.place(x = 40,y = 300)
    win2.resizable(False,False)
    win2.mainloop()


# ============= Login Screen =====================
def main():

    global e1,e2,userInput,passInput,win1
    win1 =Tk()
    win1.geometry("350x350")
    win1.title("Login menu")
    win1.config(bg = '#2f5887')

    image1 = ImageTk.PhotoImage(Image.open('2.png'))#logo
    
    Frame(height = 80,width =350,bg = '#1e436d').place(x=0,y = 0)
    userInput = StringVar()
    Label(image = image1,bg = '#1e436d').place(x = 60, y= 15)#logo
    userL = Label(win1, text = ' Admin Login', font=('Seoge UI', 20,'bold') ,bg  = '#1e436d',fg = '#E5DFDF').place(x = 120,y = 25)

    #=== user entry ====
    en1 = Frame(height = 45,width =250,bg = '#b3cde0').place(x = 60,y = 110)
    e1 = Entry(en1,textvariable = userInput,width =25,font=('Seoge UI', 13,'bold'),bg = '#b3cde0',fg = 'white',borderwidth = 0)#dde6ef

    e1.insert(0,'  Username')
    e1.place(x = 70, y = 115,height = 40)
    e1.bind("<Button-1>",clickuser)


    # === pass entry ====
    en2 = Frame(height = 45,width =250,bg = '#6497b1').place(x = 60,y = 170)
    passInput = StringVar()
    e2 = Entry(win1,textvariable = passInput,width = 25,font=('Seoge UI', 13,'bold'),bg = '#6497b1',fg = 'white',borderwidth = 0)
    e2.insert(0,'  Password')
    e2.place(x = 70, y = 172,height = 40)  
    e2.bind("<Button-1>",clickpass)

    # === show password ===
    showpass = ImageTk.PhotoImage(Image.open('hidepass.png'))#showpass
    btn1 = Button(win1,image = showpass, bg = '#6497b1', command = showpassed, width = 30, height = 30,borderwidth = 0).place(x = 262,y = 175)

    # ==== save cancel =====
    btn1 = Button(win1,text = 'Login',font=('Seoge UI', 12,'bold'),bg = '#f39422',fg= 'white', command = Login, width = 11, height = 2,borderwidth = 0).place(x = 60,y = 250)

    btn2 = Button(win1,text = 'Exit',font=('Seoge UI', 12,'bold'),bg = '#00909e',fg= 'white', command = exit, width = 11, height = 2,borderwidth = 0).place(x = 195,y = 250)

    win1.mainloop()

main()# this is the main execution

