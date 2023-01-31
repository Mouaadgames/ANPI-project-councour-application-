from genericpath import exists
from tkinter import *
from tkinter.messagebox import *
from time import sleep
from turtle import width
#---   Var   ---
Ncin     = 0
nom      = ""
prenom   = ""
age      = 0
decision = ""
pers = 0
studentNum = 0
activList = []
numofthearms = 0
inWin = False
win = Tk()
curentselection = 0
sellectedperson = []
editedNum        = StringVar()
editedName       = StringVar()
editedAge        = StringVar()
editedDecision   = StringVar()
editedLast       = StringVar()
decisionSelected = StringVar()
newNum        = StringVar()
newName       = StringVar()
newAge        = StringVar()
newDecision   = StringVar()
newLast       = StringVar()
#---   functions   ---

def findin(element):
    elm = element[::-1]
    t = ""
    for let in elm:
        if let == ";" or let == " " or let == "-":    
            break
        t += let
    t = t[::-1]
    t = t[:-1]
    return t

def saisir():
    global Ncin,nom,prenom,age,decision
    if Ncin != "" and nom != "" and prenom != "" and age != "" and decision != "":
        if exists("councour.txt"):
            _file = open("councour.txt","a+")
        else:
            _file = open("councour.txt","w+")
        _file.write(f"{Ncin};{nom};{prenom};{age};{decision}\n")
        _file.close()
    else:
        pass
    sAll()
    admis()
    attente()
    
def admis():
    if exists("councour.txt"):
        _cfile = open("councour.txt","r")
    else:
        return
    _afile = open("admis.txt","w+")
    count = _cfile.readlines()
    _cfile.close()
    for element in count:
        t = findin(element)
        if t == "Admis":
            _afile.write(f"{element[:-7]}\n")
    _afile.close()

def attente():
    if exists("admis.txt"):
        _afile = open("admis.txt","r")
    else:
        return
    _atfile = open("attente.txt","w")
    count = _afile.readlines()[::-1]
    i = len(count)
    for element in count:
        i -= 1
        t = findin(element)
        try:
            if int(t) >= 30:
                _atfile.write(f"{element[:(len(t)*-1)-2]}\n")
                supprimer(i)
        except:
            pass
    _atfile.close()



def statistiques(dec):
    if exists("councour.txt"):
        _cfile = open("councour.txt","r")
    else:
        return
    count = _cfile.readlines() 
    num = 0
    tot = len(count)
    try:
        if (dec == "Admis" or dec == "Refuse" or dec == "Ajourne"):
            for elemnt in count:
                t = findin(elemnt)
                if t == dec :
                    num += 1
            p = num/tot
            p*=100
        return p
    except:
        showerror("div/0","pas de candidats pour calculer")
        return 0
def supprimer(line):
    _afile = open("admis.txt","r")
    data = _afile.readlines()
    _afile.close()
    data.pop(line)
    _afile = open("admis.txt","w")
    _afile.writelines(data)
    _afile.close()
def deleat():
    global curentselection
    s = namesList.curselection()[::-1]
    if len(s) > 0:
        curentselection = s[0]
        global studentNum
        global activList
        namesList.delete(curentselection)
        activList.pop(curentselection)
        studentNum-=1
        _cfile = open("councour.txt","w")
        _cfile.writelines(activList)
        _cfile.close()
        admis()
        attente()
        noedit()
        delb["state"] = NORMAL
        modb["state"] = NORMAL
def mod():
    global activList
    global sellectedperson
    global curentselection
    sellectedperson = []
    s = namesList.curselection()
    if len(s) > 0:
        data = activList[s[0]]
        for _ in range(5):
            da = findin(data)
            data = data[:len(da)*-1-2] + "d" #just a random leter to pronevt cuting the suntence
            sellectedperson.append(da)
        curentselection = s[0]
        NCINfieald["state"] = NORMAL
        Namefieald["state"] = NORMAL
        Lastfieald["state"] = NORMAL
        Agefieald ["state"] = NORMAL
        savb["state"]       = NORMAL
        editedNum     .set(sellectedperson[4])
        editedName    .set(sellectedperson[2])
        editedAge     .set(sellectedperson[1])
        editedDecision.set(sellectedperson[0])
        editedLast    .set(sellectedperson[3])
    else:
        showerror("imposible","SVP selectioner un candidats")
def noedit():
    NCINfieald["state"] = DISABLED
    Namefieald["state"] = DISABLED
    Lastfieald["state"] = DISABLED
    Agefieald ["state"] = DISABLED
    savb["state"]       = DISABLED
    delb["state"] = DISABLED
    modb["state"] = DISABLED
    editedNum       .set("")
    editedName      .set("")
    editedAge       .set("")
    editedDecision  .set("")
    editedLast      .set("")
def add():
    global inWin
    if not(inWin):
        global addI
        global savI
        addWin = Toplevel()
        def move_app(e):
	        addWin.geometry(f'+{e.x_root}+{e.y_root}')
        def quitter():
            addWin.destroy()
            setit()
        def setit():
            global inWin
            inWin = False
        def reste():
            global Ncin,nom,prenom,age,decision
            Ncin,nom,prenom,age,decision="","","","",""
            newNum.set("")
            newLast.set("")
            newName.set("")
            newAge.set("")
            newDecision.set("")
        def addC():
            if newAge.get() != "" and newNum.get() != "" and newName.get() != ""  and   newDecision.get() != "" and newLast.get() != "":
                data = [newAge.get(),newNum.get(),newName.get(),newLast.get()]
                for element in data:
                    for leter in element:
                        if leter == " " or leter == "-" or leter == ";":
                            if leter == " ":
                                error = "[espace]"
                            else:
                                error = f"'{leter}'"
                            showerror("Erorr",f"Le nom ne doit pas contenir \nles caractères suivants : [espace] ,' - ' , ' ; ' \n l'erorr est dans '{element}' il contien {error}")
                            return
                global Ncin,nom,prenom,age,decision
                Ncin,nom,prenom,age,decision = newNum.get(),newLast.get(),newName.get(),newAge.get(),newDecision.get()
                saisir()
                reste()
                showinfo("Done","Le candidats est ajouter")
            else:
                showerror("Erorr","SVP remplissez toutes les cases")
        def savC():
            if newAge.get() != "" or newNum.get() != "" or newName.get() != ""  or  newAge.get() != ""  or   newDecision.get() != "" or newLast.get() != "":
                if askyesno("Abondoner","vous vouler abondoner ce candidat"):
                    quitter()
                    reste()
            else:
                quitter()
                reste()
        inWin = True
        addWin.geometry("500x300+50+50")
        addWin["bg"]= "#002A4F"
        title_bar = Frame(addWin, bg="darkgreen", relief="raised", bd=0,width=500,height = 30)
        title_bar.place(x=0,y=0)
        title_bar.bind("<B1-Motion>", move_app)
        title_label = Label(title_bar, text="  Ajouter un candidat", bg="darkgreen", fg="white")
        title_label.place(x = 10,y = 4)
        close_Btton = Button(title_bar,command=quitter, text="  X  ", bg="darkgreen", fg="white", relief="sunken", bd=0)
        close_Btton.place(x = 480,y = 4)
        addWin.attributes("-topmost", True)
        addWin.overrideredirect(True)

        editNCINLabel = Label(addWin,text="NCIN"  ,font=("Arial",12),bg="#002A4F",fg = "#FFF")
        editNameLabel = Label(addWin,text="Prenom",font=("Arial",12),bg="#002A4F",fg = "#FFF")
        editLastLabel = Label(addWin,text="Nom"   ,font=("Arial",12),bg="#002A4F",fg = "#FFF")
        editAgeLabel  = Label(addWin,text="Age"   ,font=("Arial",12),bg="#002A4F",fg = "#FFF")
        editNCINLabel.place(x=23,y = 0  + 40 )
        editNameLabel.place(x=23,y = 55 + 40 )
        editLastLabel.place(x=23,y = 110+ 40 )
        editAgeLabel .place(x=23,y = 165+ 40 )

        NCINfieald = Entry(addWin,textvariable=newNum ,font=("Arial",14),bg="#1A4266",width=18,fg = "#FFF")
        Namefieald = Entry(addWin,textvariable=newName,font=("Arial",14),bg="#1A4266",width=18,fg = "#FFF")
        Lastfieald = Entry(addWin,textvariable=newLast,font=("Arial",14),bg="#1A4266",width=18,fg = "#FFF")
        Agefieald  = Entry(addWin,textvariable=newAge,font=("Arial",14),bg="#1A4266",width=18,fg = "#FFF")
        NCINfieald.place(x=9,y = 0   +64)
        Namefieald.place(x=9,y = 55  +64)
        Lastfieald.place(x=9,y = 110 +64)
        Agefieald .place(x=9,y = 165 +64)
        editDecitionLabel = Label(addWin,text="Decision"   ,font=("Arial",14),bg="#002A4F",fg =  "#FFF")
        editDecitionLabel.place(x=310,y=40)
        Label      (addWin,width= 13,height= 6,bg="#5C96C9").place(x=300,y=70)
        Radiobutton(addWin,text="Admis"  ,font=("Arial",15),bg="#5C96C9",variable=newDecision,value="Admis"  ,fg = "#000",activeforeground="#FAA",activebackground="#808080").place(x=300,y=0 +70)
        Radiobutton(addWin,text="Refuse" ,font=("Arial",15),bg="#5C96C9",variable=newDecision,value="Refuse" ,fg = "#000",activeforeground="#FAA",activebackground="#808080").place(x=300,y=30+70)
        Radiobutton(addWin,text="Ajourne",font=("Arial",15),bg="#5C96C9",variable=newDecision,value="Ajourne",fg = "#000",activeforeground="#FAA",activebackground="#808080").place(x=300,y=60+70)

        addb = Button(addWin,width=186,height=48,image=addI,command=addC,borderwidth=0)
        addb.place(x=280,y=185)
        savb = Button(addWin,width=186,height=48,image=savI,command=savC,borderwidth=0)
        savb.place(x=280,y=240)
        addWin.mainloop()
    else:
        showerror("IMPOSIBLE","La fenetre a deja ete ouverte")
def sAll():       
    global activList
    global numofthearms
    try:
        _cfile = open("councour.txt","r")   
    except:
        _cfile = open("councour.txt","w+")           
    activList = _cfile.readlines()    
    numofthearms = 5
    _cfile.close()      
    titel["text"] = "Tous"
    noedit()
    delb["state"] = NORMAL
    modb["state"] = NORMAL
    updateList()

def sAdm():      
    global activList
    global numofthearms
    _afile = open("admis.txt","r")           
    activList = _afile.readlines()    
    numofthearms = 4
    _afile.close()         
    titel["text"] = "Admis"
    noedit()
    updateList()
         
def sAtt():        
    global activList
    global numofthearms
    _atfile = open("attente.txt","r")           
    activList = _atfile.readlines()   
    numofthearms = 3
    _atfile.close()    
    titel["text"] = "Attente"
    noedit()
    updateList()         



def saveEdit():
    global curentselection
    _cfile = open("councour.txt","r")
    data = _cfile.readlines()
    _cfile.close()
    data[curentselection] = f"{editedNum.get()};{editedLast.get()};{editedName.get()};{editedAge.get()};{editedDecision.get()}\n"
    _cfile = open("councour.txt","w")
    _cfile.writelines(data)
    _cfile.close()
    sAll()
    admis()
    attente()


def stat():
   global decisionSelected
   if decisionSelected.get() == "Selectioner":
        showerror("Imposible", "Selectiner une decision")
   else:
        updatepersenteg(int(statistiques(decisionSelected.get())))
   # call the statistique function with the selected paramiter 

def updateList():
    global activList
    global numofthearms 
    global studentNum
    for _ in range(studentNum):
        namesList.delete(0)
    studentNum = 0
    for i,student in enumerate(activList):
        final = ""
        counter = 0
        for leter in student:
            if leter != ";" and counter != numofthearms:
                final += leter
            elif counter == 1:
                final += " "
                counter += 1
            else:
                final += "-"
                counter += 1
        namesList.insert(i,final)
        studentNum += 1

def updatepersenteg(per):
    per = per *3.6
    global presentegbar
    staCan.delete(presentegbar)
    xx = 230
    yy = 22
    size = 160
    fooset = 28
    coord = xx, yy, xx + size, yy + size
    presentegbar = staCan.create_arc(coord, start=90, extent=-1*per, fill="#FF0",outline="")
    staCan.create_oval(coord,fill="",outline="#F00",width= 5)
    staCan.create_oval(xx+fooset, yy+fooset, xx + size-fooset, yy + size-fooset,fill="#3d3d3d",outline="#F00",width= 5)
    staCan.create_text(xx+(size/2), yy +(size/2),font=("Arial",15),text=f"{int(per/3.6)}%",fill="#FFF")
def howCreat():
    showinfo("Creer Par !?","Mouaad ELbarrik \n Age: 15 \n Je vous remercie pour vos efforts")
def Help():
    showinfo("Aide !","Le programme est facile à utiliser et tout s'explique lui meme \n pour plus d'aiformation Lisez le fichier README.txt pour en savoir plus ")
###def bttna(frame,posx,posy,Width,Height,img,nbcolor,sbcolor,cmd):
###    def on_enter(e):
###        thebutton["background"] = nbcolor
###    def on_exit(e):
###        thebutton["background"] = sbcolor
###    thebutton = Button(frame,width=Width,height=Height,image=img,command=cmd,bg=nbcolor)
###    thebutton.bind("<Enter>",on_enter)
###    thebutton.bind("<Leave>",on_exit)
###    thebutton.place(x=posx,y=posy)

#---   GUI   ---
try:
    delI = PhotoImage(file='./images/del.png')
    modI = PhotoImage(file='./images/mod.png')
    addI = PhotoImage(file='./images/add.png')
    staI = PhotoImage(file='./images/sta.png')
    savI = PhotoImage(file='./images/sav.png')
    sAdI = PhotoImage(file='./images/sAd.png')
    sAtI = PhotoImage(file='./images/sAt.png')
    sAlI = PhotoImage(file='./images/sAl.png')
    #---   Frames   ---
    mainFrame = Frame(win,bg="#808080",width=350,height=590,borderwidth=4,relief="ridge")
    mainFrame.place(x = 5,y = 5)
    editFrame = Frame(win,bg="#3d3d3d",width=435,height=590,borderwidth=4,relief="ridge")
    editFrame.place(x = 360,y = 5)
    #---   commpenets   ---
    #--  Frame1  --
    titel = Label(mainFrame,text = "Tous",font=("Arial",25),bg="#808080",fg="#FFF")
    titel.place(relx=.4,rely=.02)
    
    namesList = Listbox(mainFrame,font=("Arial",15),fg = "#FFF",selectmode=SINGLE,width=29,height=18,bg="#606060")
    namesList.place(x= 7, y = 65) 
    
    delb = Button(mainFrame,width=153,height=40,image=delI,command=deleat,borderwidth=0)
    delb.place(x=5,y=530)
    
    modb = Button(mainFrame,width=153,height=40,image=modI,command=mod,borderwidth=0)
    modb.place(x=180,y=530)
    #--  Frame2  --
    staCan = Canvas(editFrame,width=405,height=200,bg = "#3d3d3d")
    staCan.place(x = 5,y = 150)
    
    addb = Button(editFrame,width=186,height=48,image=addI,command=add,borderwidth=0)
    addb.place(x=225,y=15)
    
    stab = Button(editFrame,width=186,height=48,image=staI,command=stat,borderwidth=0)
    stab.place(x=15,y=160)
    
    sAdb = Button(editFrame,width=186,height=48,image=sAdI,command=sAdm,highlightthickness=0)
    sAdb.place(x=10,y=80)
    
    sAtb = Button(editFrame,width=186,height=48,image=sAtI,command=sAtt,borderwidth=0)
    sAtb.place(x=225,y=80)
    
    sAlb = Button(editFrame,width=186,height=48,image=sAlI,command=sAll,borderwidth=0)
    sAlb.place(x=10,y=15)
    
    ###dropDeci = OptionMenu(editFrame,decitionSelected,"Admis","Refuse","Attent",bg="#3d3d3d")
    ###dropDeci.place(x=25,y=230)
    Radiobutton(editFrame,text="Admis"  ,font=("Arial",15),bg="#969696",variable=decisionSelected,value="Admis" ,fg = "#1C2500",activeforeground="#FAA",activebackground="#808080").place(x=25,y=230)
    Radiobutton(editFrame,text="Refuse" ,font=("Arial",15),bg="#969696",variable=decisionSelected,value="Refuse",fg = "#1C2500",activeforeground="#FAA",activebackground="#808080").place(x=25,y=260)
    Radiobutton(editFrame,text="Ajourne",font=("Arial",15),bg="#969696",variable=decisionSelected,value="Ajourne",fg = "#1C2500",activeforeground="#FAA",activebackground="#808080").place(x=25,y=290)
    
    staCan.create_rectangle(20,78,117,150,fill="#969696",outline="")
    
    presentegbar = staCan.create_arc(0,0,0,0, start=90, extent=-1*0, fill="red",outline="")
    updatepersenteg(0)
    
    editNCINLabel = Label(editFrame,text="NCIN"  ,font=("Arial",12),bg="#3d3d3d",fg = "#FFF")
    editNameLabel = Label(editFrame,text="Prenom",font=("Arial",12),bg="#3d3d3d",fg = "#FFF")
    editLastLabel = Label(editFrame,text="Nom"   ,font=("Arial",12),bg="#3d3d3d",fg = "#FFF")
    editAgeLabel  = Label(editFrame,text="Age"   ,font=("Arial",12),bg="#3d3d3d",fg =  "#FFF")
    editNCINLabel.place(x=23,y = 0   + 357)
    editNameLabel.place(x=23,y = 55  + 357)
    editLastLabel.place(x=23,y = 110 + 357)
    editAgeLabel .place(x=23,y = 165 + 357)
    
    NCINfieald = Entry(editFrame,textvariable=editedNum ,font=("Arial",14),bg="#969696",width=18,fg = "#FFF")
    Namefieald = Entry(editFrame,textvariable=editedName,font=("Arial",14),bg="#969696",width=18,fg = "#FFF")
    Lastfieald = Entry(editFrame,textvariable=editedLast,font=("Arial",14),bg="#969696",width=18,fg = "#FFF")
    Agefieald = Entry(editFrame ,textvariable=editedAge ,font=("Arial",14),bg="#969696" ,width=18,fg = "#FFF")
    NCINfieald.place(x=9,y = 0   + 379 )
    Namefieald.place(x=9,y = 55  + 379 )
    Lastfieald.place(x=9,y = 110 + 379 )
    Agefieald .place(x=9,y = 165 + 379 )
    
    editDecitionLabel = Label(editFrame,text="Decision"   ,font=("Arial",14),bg="#3d3d3d",fg =  "#FFF")
    editDecitionLabel.place(x = 270,y = 370)
    Label(editFrame,width= 13,height= 6,bg="#969696").place(x=260,y=410)
    Radiobutton(editFrame,text="Admis"  ,font=("Arial",15),bg="#969696",variable=editedDecision,value="Admis" ,fg = "#1C2500",activeforeground="#FAA",activebackground="#808080").place(x=260,y=0 +410)
    Radiobutton(editFrame,text="Refuse" ,font=("Arial",15),bg="#969696",variable=editedDecision,value="Refuse",fg = "#1C2500",activeforeground="#FAA",activebackground="#808080").place(x=260,y=30+410)
    Radiobutton(editFrame,text="Ajourne",font=("Arial",15),bg="#969696",variable=editedDecision,value="Ajourne",fg = "#1C2500",activeforeground="#FAA",activebackground="#808080").place(x=260,y=60+410)
    
    
    savb = Button(editFrame,width=186,height=48,image=savI,command=saveEdit,borderwidth=0)
    savb.place(x=230,y=520)
    
    menubar = Menu(win)
    
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Voir Qui", command=howCreat)
    menubar.add_cascade(label="creer Par", menu=menu1)
    
    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Aide", command=Help)
    menubar.add_cascade(label="Aide", menu=menu2)
    
    #---   start   ---
    win.geometry("800x600")
    win.maxsize(800,600)
    win.minsize(800,600)
    win["bg"] = "#020202"
    win.title("Project de fin de Formation")
    win.iconbitmap("./images/Icon.ico")
    sAll()
    decisionSelected.set("Selectioner")
    editedDecision.set("Selectioner")
    NCINfieald["state"] = DISABLED
    Namefieald["state"] = DISABLED
    Lastfieald["state"] = DISABLED
    Agefieald ["state"] = DISABLED
    savb["state"]= DISABLED
    win["menu"]=menubar
    showinfo("inforamtion","Lisez le fichier README.txt pour en savoir plus sur le programme et cliquez sur 'cree par' dans la bar en haut pour voir qui l'a créé")
    #---   test place   ---
    """
    Ncin     = 123123
    nom      = "Elbarrik"
    prenom   = "Mouaad"
    age      = 15
    decision = "Admis"
    """
    admis()
    attente()
except Exception as e: 
    showerror("partie manquante",f"Il manque des fichiers qui doivent être inclus\n dans le même fichier avec le programme\n{e}")
    #on exit programes
    input
win.mainloop()

