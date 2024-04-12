import pymysql
import tkinter as tk
import os
import random
import string

from datetime import date,datetime
from tkinter import ttk
from PIL import Image
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox, Entry, filedialog
import subprocess

def Prof():
    subprocess.run(["python", "prof.py"])

def classe():
    subprocess.run(["python", "classe.py"])

def cours():
    subprocess.run(["python", "cours.py"])

def remarque():
    subprocess.run(["python", "remarque.py"])

def Cahier_texte():
    subprocess.run(["python", "cahierdeTexte.py"])

def rp():
    subprocess.run(["python", "rp.py"])

def getCurrentDate():
    return f"{date.today().month}/{date.today().day}/{date.today().year}"

def generate_random_string(length=12):
    characters = string.ascii_lowercase
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def connection():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='enseignements_db'
    )
    return conn



def read():
    conn=connection()
    cursor=conn.cursor()
    cursor.connection.ping()
    sql=f"select idEtudiant,nom,prenom,mail,role,nomClasse from etudiant,classe where etudiant.idclasse = classe.idclasse"
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def renderTreeVIew(data):
    global treeFrame
    treeFrame=ttk.Frame(mainCanvas)
    treeFrame.place(x=270.0,y=130.0,width=760.0,height=535.0)

    global treeScroll
    treeScroll=ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right",fill="y")

    global treeview
    cols=("idEtudiant","nom","prenom","Email","role","nomClasse")
    treeview=ttk.Treeview(treeFrame,show="headings",style="mystyle.Treeview",yscrollcommand=treeScroll.set,columns=cols)
    treeview.heading("idEtudiant",text="idEtudiant",anchor="w")
    treeview.heading("nom",text="nom",anchor="w")
    treeview.heading("prenom",text="prenom",anchor="w")
    treeview.heading("Email",text="Email",anchor="w")
    treeview.heading("role",text="role",anchor="w")
    treeview.heading("nomClasse",text="nomClasse",anchor="w")
    

    treeview.column("idEtudiant",width=75)
    treeview.column("nom",width=90)
    treeview.column("prenom",width=108)
    treeview.column("Email",width=150)
    treeview.column("role",width=150)
    treeview.column("nomClasse",width=150)
    
    for data in treeview.get_children():
        treeview.delete(data)
    for array in data:
        treeview.insert('',tk.END,values=array[0:],iid=array[0])
        print(array)
    treeview.place(x=0,y=0,width=745.0,height=535.0)
    treeScroll.config(command=treeview.yview)

def closeWindow(window):
    window.destroy()
    if os.path.exists("./assets/uploaded/temp.png"):
        os.remove("./assets/uploaded/temp.png")

def addWindowAssets(str):
    return f"./assets/frame1/{str}"

def editWindowAssets(str):
    return f"./assets/frame1/{str}"

def viewWindowAssets(str):
    return f"./assets/frame1/{str}"

def mainWindowAssets(str):
    return f"./assets/frame0/{str}"

def deleteStudent():
    try:
        deleteData = str(treeview.item(treeview.selection()[0])['values'][0])
    except:
        messagebox.showwarning("Info", "Please select a data row")
        return
    decision = messagebox.askquestion("Avertissement", "Voulez vous supprimez cette etudiant ?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM etudiant WHERE idEtudiant='{str(deleteData)}'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return
    print(deleteData)
    renderTreeVIew(read())

def editStudent():
    selectedStudData = [0,0,0,0,0,0]
    try:
        for i in range(0,6):
            selectedStudData[i] = str(treeview.item(treeview.selection()[0])['values'][i])
    except:
        messagebox.showwarning("Info", "Please select a data row")
        return
    print(selectedStudData)
    renderEditWindow(selectedStudData)

def viewStudent():
    selectedStudData = [0,0,0,0,0,0]
    try:
        for i in range(0,6):
            selectedStudData[i] = str(treeview.item(treeview.selection()[0])['values'][i])
    except:
        messagebox.showwarning("Info", "Please select a data row")
        return
    print(selectedStudData)
    renderViewWindow(selectedStudData)

def renderAddWindow():

    def addStudent():
        idclasse = int(addClasseId.get())
        role = str(addStudidEntry.get())
        nom = str(addFnameEntry.get())
        prenom = str(addLnameEntry.get())
        mail = str(addEmailEntry.get())
        if (idclasse == "" or idclasse == " ") or (nom == "" or nom == " ") or (prenom == "" or prenom == " ") or (mail == "" or mail == " "):
            messagebox.showinfo("Error", "Please fill up the blank entry",parent=addCanvas)
            return
        else:
            try:
                
                if os.path.exists("./assets/uploaded/temp.png"):
                    os.remove("./assets/uploaded/temp.png")
                conn=connection()
                cursor=conn.cursor()
                cursor.execute(f"INSERT INTO etudiant (nom,prenom,mail,role,idclasse) VALUES ('{nom}','{prenom}','{mail}','{role}',{idclasse}) ")
                conn.commit()
                conn.close()
            except:
                messagebox.showinfo("Error", "Stud ID already exist",parent=addCanvas)
                return
        closeWindow(addWindow)
        renderTreeVIew(read())

    

    

    print('render add window')
    addWindow = Tk()
    addWindow.title('Gestion des enseignements')
    addWindow.geometry("720x480")
    addWindow.configure(bg = "#FFFFFF")
    addCanvas = Canvas(addWindow,bg = "#FFFFFF",height = 480,width = 720,bd = 0,highlightthickness = 0,relief = "ridge")
    addCanvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(master=addWindow, file=addWindowAssets("image_1.png"))
    addCanvas.create_image(360.0, 264.0, image=image_image_1)
    image_image_2 = PhotoImage(master=addWindow, file=addWindowAssets("image_2.png"))
    addCanvas.create_image(360.0, 24.0, image=image_image_2)
    addCanvas.create_text(49.0, 10.0, anchor="nw", text="Ajouter Etudiant", fill="#FFFFFF", font=("Inter SemiBold", 24 * -1))
    image_image_3 = PhotoImage(master=addWindow, file=addWindowAssets("image_3.png"))
    addCanvas.create_image(28.0, 24.0, image=image_image_3)

    # stud id input

    image_image_5 = PhotoImage(master=addWindow, file=addWindowAssets("image_5.png"))
    addCanvas.create_image(456.0, 104.0, image=image_image_5)
    entry_image_2 = PhotoImage(master=addWindow, file=addWindowAssets("entry_2.png"))
    addCanvas.create_image(455.0, 109.5, image=entry_image_2)
    addStudidEntry = Entry(master=addWindow, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    addStudidEntry.place(x=325.0, y=98.0, width=260.0, height=21.0)
    addCanvas.create_text(325.0, 85.0, anchor="nw", text="Role", fill="#000000", font=("Inter", 11 * -1))




    # fname input
    image_image_4 = PhotoImage(master=addWindow, file=addWindowAssets("image_4.png"))
    addCanvas.create_image(457.0, 166.0, image=image_image_4)
    entry_image_1 = PhotoImage(master=addWindow, file=addWindowAssets("entry_1.png"))
    addCanvas.create_image(456.0, 171.5, image=entry_image_1)
    addClasseId = Entry(master=addWindow,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    addClasseId.place(x=35.0, y=160.0, width=260.0, height=21.0)
    addCanvas.create_text(35.0, 147.0, anchor="nw", text="idclasse", fill="#000000", font=("Inter", 11 * -1))



    image_image_4 = PhotoImage(master=addWindow, file=addWindowAssets("image_4.png"))
    addCanvas.create_image(457.0, 166.0, image=image_image_4)
    entry_image_1 = PhotoImage(master=addWindow, file=addWindowAssets("entry_1.png"))
    addCanvas.create_image(456.0, 171.5, image=entry_image_1)
    addFnameEntry = Entry(master=addWindow,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    addFnameEntry.place(x=326.0, y=160.0, width=260.0, height=21.0)
    addCanvas.create_text(326.0, 147.0, anchor="nw", text="nom", fill="#000000", font=("Inter", 11 * -1))

    # lname input
    image_image_6 = PhotoImage(master=addWindow, file=addWindowAssets("image_6.png"))
    addCanvas.create_image(457.0,230.0,image=image_image_6)
    entry_image_3 = PhotoImage(master=addWindow, file=addWindowAssets("entry_3.png"))
    addCanvas.create_image(456.0,235.5,image=entry_image_3)
    addLnameEntry = Entry(master=addWindow, bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    addLnameEntry.place(x=326.0,y=224.0,width=260.0,height=21.0)
    addCanvas.create_text(326.0,211.0,anchor="nw",text="prenom",fill="#000000",font=("Inter", 11 * -1))





    # Email
    image_image_7 = PhotoImage(master=addWindow, file=addWindowAssets("image_7.png"))
    addCanvas.create_image(166.0,294.0,image=image_image_7)
    entry_image_4 = PhotoImage(master=addWindow, file=addWindowAssets("entry_4.png"))
    addCanvas.create_image(165.0,299.5,image=entry_image_4)
    addEmailEntry = Entry(master=addWindow, bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    addEmailEntry.place(x=35.0,y=288.0,width=260.0,height=21.0)
    addCanvas.create_text(35.0,275.0,anchor="nw",text="mail",fill="#000000",font=("Inter", 11 * -1))
    

    

    
    

    # button_image_1 = PhotoImage(master=addWindow, file=addWindowAssets("button_1.png"))
    # clearImageBtn = Button(master=addWindow, image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
    # clearImageBtn.place(x=196.0, y=215.0, width=96.0, height=25.0)

    

    button_image_3 = PhotoImage(master=addWindow, file=addWindowAssets("button_3.png"))
    addSubmitBtn = Button(master=addWindow, image=button_image_3, borderwidth=0, highlightthickness=0, command=addStudent, relief="flat")
    addSubmitBtn.place(x=28.0, y=402.0, width=96.0, height=25.0)

    button_image_4 = PhotoImage(master=addWindow, file=addWindowAssets("button_4.png"))
    cancelBtn = Button(master=addWindow, image=button_image_4, borderwidth=0, highlightthickness=0, command=lambda: closeWindow(addWindow), relief="flat")
    cancelBtn.place(x=137.0, y=402.0, width=96.0, height=25.0)

    addWindow.resizable(False, False)
    addWindow.mainloop()

def renderEditWindow(selectedStudData):
    def editStudent():
        selectedStudid = selectedStudData[0]
        idEtudiant = str(editStudidEntry.get())
        nom = str(editFnameEntry.get())
        prenom = str(editLnameEntry.get())
        mail = str(editEmailEntry.get())
       
        # nom = str(addFnameEntry.get())
        # prenom = str(addLnameEntry.get())
        # mail = str(addEmailEntry.get())
        if (nom == "" or nom == " ") or (prenom == "" or prenom == " ")  or (email == "" or email == " "):
            messagebox.showinfo("Error", "Please fill up the blank entry",parent=editCanvas)
            return
        else:
            try:
                try:
                    global profile_img
                    profile_img = Image.open("./assets/uploaded/temp.png")
                    profile_img = profile_img.resize((145, 145), resample=Image.LANCZOS)
                    profile_img = profile_img.convert("RGB")
                    conn = connection()
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT * FROM etudiant WHERE idEtudiant='{idEtudiant}' ")
                    result = cursor.fetchone()
                    conn.commit()
                    conn.close()
                    if os.path.exists(f"./assets/uploaded/{result[1]}"):
                        os.remove(f"./assets/uploaded/{result[1]}")
                    conn = connection()
                    cursor = conn.cursor()
                    cursor.execute(f"UPDATE etudiant SET nom='{nom}',prenom='{prenom}',mail='{mail}' WHERE idEtudiant='{selectedStudid}' ")
                    conn.commit()
                    conn.close()
                except:
                    conn = connection()
                    cursor = conn.cursor()
                    cursor.execute(f"UPDATE etudiant SET nom='{nom}',prenom='{prenom}',mail='{mail}' WHERE idEtudiant='{selectedStudid}' ")
                    conn.commit()
                    conn.close()
                if os.path.exists("./assets/uploaded/temp.png"):
                    os.remove("./assets/uploaded/temp.png")
            except:
                messagebox.showinfo("Error", "Error occured",parent=editCanvas)
                return
        closeWindow(editWindow)
        renderTreeVIew(read())

    def setPreviewPic(filepath):
        global image
        try:
            image = PhotoImage(master=editWindow, file=filepath)
            editCanvas.create_image(112.0, 168.0, image=image)
        except Exception as e: 
            print(e)

    

    print('render edit window')
    idEtudiant=selectedStudData[0]
    nom=selectedStudData[1]
    prenom=selectedStudData[selectedStudData[2]]
    email=selectedStudData[3]
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM etudiant WHERE idEtudiant='{idEtudiant}' ")
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    editWindow = Tk()
    editWindow.title('Edit Window - Student Records Management System')
    editWindow.geometry("720x480")
    editWindow.configure(bg = "#FFFFFF")
    editCanvas = Canvas(editWindow,bg = "#FFFFFF",height = 480,width = 720,bd = 0,highlightthickness = 0,relief = "ridge")
    editCanvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(master=editWindow, file=editWindowAssets("image_1.png"))
    editCanvas.create_image(360.0, 264.0, image=image_image_1)
    image_image_2 = PhotoImage(master=editWindow, file=editWindowAssets("image_2.png"))
    editCanvas.create_image(360.0, 24.0, image=image_image_2)
    editCanvas.create_text(49.0, 10.0, anchor="nw", text="Edit Student", fill="#FFFFFF", font=("Inter SemiBold", 24 * -1))
    image_image_3 = PhotoImage(master=editWindow, file=editWindowAssets("image_3.png"))
    editCanvas.create_image(28.0, 24.0, image=image_image_3)

    # stud id input
    image_image_5 = PhotoImage(master=editWindow, file=editWindowAssets("image_5.png"))
    editCanvas.create_image(456.0, 104.0, image=image_image_5)
    entry_image_2 = PhotoImage(master=editWindow, file=editWindowAssets("entry_2.png"))
    editCanvas.create_image(455.0, 109.5, image=entry_image_2)
    editStudidEntry = Entry(master=editWindow, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    editStudidEntry.place(x=325.0, y=98.0, width=260.0, height=21.0)
    editCanvas.create_text(325.0, 85.0, anchor="nw", text="idEtudiant", fill="#000000", font=("Inter", 11 * -1))
    editStudidEntry.insert(0,idEtudiant)

    # fname input
    image_image_4 = PhotoImage(master=editWindow, file=editWindowAssets("image_4.png"))
    editCanvas.create_image(457.0, 166.0, image=image_image_4)
    entry_image_1 = PhotoImage(master=editWindow, file=editWindowAssets("entry_1.png"))
    editCanvas.create_image(456.0, 171.5, image=entry_image_1)
    editFnameEntry = Entry(master=editWindow,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    editFnameEntry.place(x=326.0, y=160.0, width=260.0, height=21.0)
    editCanvas.create_text(326.0, 147.0, anchor="nw", text="nom", fill="#000000", font=("Inter", 11 * -1))
    editFnameEntry.insert(0,nom)

    # lname input
    image_image_6 = PhotoImage(master=editWindow, file=editWindowAssets("image_6.png"))
    editCanvas.create_image(457.0,230.0,image=image_image_6)
    entry_image_3 = PhotoImage(master=editWindow, file=editWindowAssets("entry_3.png"))
    editCanvas.create_image(456.0,235.5,image=entry_image_3)
    editLnameEntry = Entry(master=editWindow, bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    editLnameEntry.place(x=326.0,y=224.0,width=260.0,height=21.0)
    editCanvas.create_text(326.0,211.0,anchor="nw",text="prenom",fill="#000000",font=("Inter", 11 * -1))
    editLnameEntry.insert(0,prenom)
    input
    # image_image_7 = PhotoImage(master=editWindow, file=editWindowAssets("image_7.png"))
    # editCanvas.create_image(166.0,294.0,image=image_image_7)
    # entry_image_4 = PhotoImage(master=editWindow, file=editWindowAssets("entry_4.png"))
    # editCanvas.create_image(165.0,299.5,image=entry_image_4)
    # editPhoneEntry = Entry(master=editWindow, bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    # editPhoneEntry.place(x=35.0,y=288.0,width=260.0,height=21.0)
    # editCanvas.create_text(35.0,275.0,anchor="nw",text="email",fill="#000000",font=("Inter", 11 * -1))
    # editPhoneEntry.inser

    # email input
    image_image_8 = PhotoImage(master=editWindow, file=editWindowAssets("image_8.png"))
    editCanvas.create_image(457.0,294.0,image=image_image_8)
    entry_image_5 = PhotoImage(master=editWindow, file=editWindowAssets("entry_5.png"))
    editCanvas.create_image(456.0,299.5,image=entry_image_5)
    editEmailEntry = Entry(master=editWindow, bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    editEmailEntry.place(x=326.0,y=288.0,width=260.0,height=21.0)
    editCanvas.create_text(326.0,275.0,anchor="nw",text="Email",fill="#000000",font=("Inter", 11 * -1))
    editEmailEntry.insert(0,email)
    
    # # editress input
    # image_image_9 = PhotoImage(master=editWindow, file=editWindowAssets("image_9.png"))
    # editCanvas.create_image(311.0, 358.0, image=image_image_9)
    # entry_image_6 = PhotoImage(master=editWindow, file=editWindowAssets("entry_6.png"))
    # editCanvas.create_image(310.5, 363.5, image=entry_image_6)
    # editAddressEntry = Entry(master=editWindow, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    # editAddressEntry.place(x=35.0, y=352.0, width=551.0, height=21.0)
    # editCanvas.create_text(35.0,339.0,anchor="nw",text="editress",fill="#000000",font=("Inter", 11 * -1))
    # editAddressEntry.insert(0,address)

    

    

    

    

    button_image_3 = PhotoImage(master=editWindow, file=editWindowAssets("button_3.png"))
    submitBtn = Button(master=editWindow, image=button_image_3, borderwidth=0, highlightthickness=0, command=editStudent, relief="flat")
    submitBtn.place(x=28.0, y=402.0, width=96.0, height=25.0)

    button_image_4 = PhotoImage(master=editWindow, file=editWindowAssets("button_4.png"))
    cancelBtn = Button(master=editWindow, image=button_image_4, borderwidth=0, highlightthickness=0, command=lambda: closeWindow(editWindow), relief="flat")
    cancelBtn.place(x=137.0, y=402.0, width=96.0, height=25.0)

    editWindow.resizable(False, False)
    editWindow.mainloop()


def renderViewWindow(selectedStudData):
    
    idEtudiant=selectedStudData[0]
    nom=selectedStudData[1]
    prenom=selectedStudData[selectedStudData[2]]
    mail=selectedStudData[3]

    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM etudiant WHERE idEtudiant='{idEtudiant}' ")
    result = cursor.fetchone()
    conn.commit()
    conn.close()

    print('render view window')
    viewWindow = Tk()
    viewWindow.title('View Window - Student Records Management System')
    viewWindow.geometry("720x480")
    viewWindow.configure(bg = "#FFFFFF")
    viewCanvas = Canvas(viewWindow,bg = "#FFFFFF",height = 480,width = 720,bd = 0,highlightthickness = 0,relief = "ridge")
    viewCanvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(master=viewWindow, file=viewWindowAssets("image_1.png"))
    viewCanvas.create_image(360.0, 264.0, image=image_image_1)
    image_image_2 = PhotoImage(master=viewWindow, file=viewWindowAssets("image_2.png"))
    viewCanvas.create_image(360.0, 24.0, image=image_image_2)
    viewCanvas.create_text(49.0, 10.0, anchor="nw", text="View Student", fill="#FFFFFF", font=("Inter SemiBold", 24 * -1))
    image_image_3 = PhotoImage(master=viewWindow, file=viewWindowAssets("image_3.png"))
    viewCanvas.create_image(28.0, 24.0, image=image_image_3)

    # stud id input
    image_image_5 = PhotoImage(master=viewWindow, file=viewWindowAssets("image_5.png"))
    viewCanvas.create_image(456.0, 104.0, image=image_image_5)
    entry_image_2 = PhotoImage(master=viewWindow, file=viewWindowAssets("entry_2.png"))
    viewCanvas.create_image(455.0, 109.5, image=entry_image_2)
    studidEntry = Entry(master=viewWindow, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    studidEntry.place(x=325.0, y=98.0, width=260.0, height=21.0)
    studidEntry.bind("<Key>", lambda e: "break")
    viewCanvas.create_text(325.0, 85.0, anchor="nw", text="idEtudiant", fill="#000000", font=("Inter", 11 * -1))
    studidEntry.insert(0,idEtudiant)

    # fname input
    image_image_4 = PhotoImage(master=viewWindow, file=viewWindowAssets("image_4.png"))
    viewCanvas.create_image(457.0, 166.0, image=image_image_4)
    entry_image_1 = PhotoImage(master=viewWindow, file=viewWindowAssets("entry_1.png"))
    viewCanvas.create_image(456.0, 171.5, image=entry_image_1)
    fnameEntry = Entry(master=viewWindow,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    fnameEntry.place(x=326.0, y=160.0, width=260.0, height=21.0)
    fnameEntry.bind("<Key>", lambda e: "break")
    viewCanvas.create_text(326.0, 147.0, anchor="nw", text="nom", fill="#000000", font=("Inter", 11 * -1))
    fnameEntry.insert(0,nom)

    # lname input
    image_image_6 = PhotoImage(master=viewWindow, file=viewWindowAssets("image_6.png"))
    viewCanvas.create_image(457.0,230.0,image=image_image_6)
    entry_image_3 = PhotoImage(master=viewWindow, file=viewWindowAssets("entry_3.png"))
    viewCanvas.create_image(456.0,235.5,image=entry_image_3)
    lnameEntry = Entry(master=viewWindow, bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    lnameEntry.place(x=326.0,y=224.0,width=260.0,height=21.0)
    lnameEntry.bind("<Key>", lambda e: "break")
    viewCanvas.create_text(326.0,211.0,anchor="nw",text="prenom",fill="#000000",font=("Inter", 11 * -1))
    lnameEntry.insert(0,prenom)
    input

    # email input
    image_image_8 = PhotoImage(master=viewWindow, file=viewWindowAssets("image_8.png"))
    viewCanvas.create_image(457.0,294.0,image=image_image_8)
    entry_image_5 = PhotoImage(master=viewWindow, file=viewWindowAssets("entry_5.png"))
    viewCanvas.create_image(456.0,299.5,image=entry_image_5)
    emailEntry = Entry(master=viewWindow, bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    emailEntry.place(x=326.0,y=288.0,width=260.0,height=21.0)
    emailEntry.bind("<Key>", lambda e: "break")
    viewCanvas.create_text(326.0,275.0,anchor="nw",text="Email",fill="#000000",font=("Inter", 11 * -1))
    emailEntry.insert(0,mail)
    
    # # address input
    # image_image_9 = PhotoImage(master=viewWindow, file=viewWindowAssets("image_9.png"))
    # viewCanvas.create_image(311.0, 358.0, image=image_image_9)
    # entry_image_6 = PhotoImage(master=viewWindow, file=viewWindowAssets("entry_6.png"))
    # viewCanvas.create_image(310.5, 363.5, image=entry_image_6)
    # addressEntry = Entry(master=viewWindow, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    # addressEntry.place(x=35.0, y=352.0, width=551.0, height=21.0)
    # addressEntry.bind("<Key>", lambda e: "break")
    # viewCanvas.create_text(35.0,339.0,anchor="nw",text="Address",fill="#000000",font=("Inter", 11 * -1))
    # addressEntry.insert(0,address)

    image_image_10 = PhotoImage(master=viewWindow, file=viewWindowAssets("image_10.png"))
    viewCanvas.create_image(166.0, 167.0, image=image_image_10)

    # process image before uploading
    # profile_img = Image.open("./assets/uploaded/images.jpeg")
    # desired_size = (145, 145)
    # profile_img = profile_img.resize(desired_size, resample=Image.LANCZOS)
    # profile_img = profile_img.convert("RGB")
    # temp_png_path = "./assets/uploaded/temp/image.png"
    # profile_img.save(temp_png_path, format="PNG")
    
    image_image_11 = PhotoImage(master=viewWindow, file=f"./assets/uploaded/{result[1]}")
    viewCanvas.create_image(168.0, 168.0, image=image_image_11)

    viewWindow.resizable(False, False)
    viewWindow.mainloop()






mainWindow = Tk()
mainWindow.title('Gestion des enseignements')
mainWindow.geometry("1080x720")
mainWindow.configure(bg = "#FFFFFF")
mainCanvas = Canvas(mainWindow,bg = "#FFFFFF",height = 720,width = 1080,bd = 0,highlightthickness = 0,relief = "ridge")
mainCanvas.place(x = 0, y = 0)

button1 = Button(mainWindow, text="Enseignant",command=Prof)
button1.place(x=300,y=75)
button2 = Button(mainWindow, text="Cahier de Texte",command=Cahier_texte)
button2.place(x=400,y=75)

button3 = Button(mainWindow, text="Remarques",command=remarque)
button3.place(x=500,y=75)

button4 = Button(mainWindow, text="Cours",command=cours)
button4.place(x=600,y=75)

button4 = Button(mainWindow, text="Classe",command=classe)
button4.place(x=700,y=75)

button5 = Button(mainWindow, text="rp",command=rp)
button5.place(x=750,y=75)


image_image_1 = PhotoImage(file=mainWindowAssets("image_1.png"))
image_1 = mainCanvas.create_image(645.0,397.0,image=image_image_1)
image_image_2 = PhotoImage(file=mainWindowAssets("image_2.png"))
image_2 = mainCanvas.create_image(648.0,398.0,image=image_image_2)
image_image_3 = PhotoImage(file=mainWindowAssets("image_3.png"))
image_3 = mainCanvas.create_image(540.0,37.0,image=image_image_3)
mainCanvas.create_text(73.0,15.0,anchor="nw",text="Gestion des Etudiants",fill="#FFFFFF",font=("Inter SemiBold", 36 * -1))
image_image_4 = PhotoImage(file=mainWindowAssets("image_4.png"))
image_4 = mainCanvas.create_image(38.0,36.0,image=image_image_4)
image_image_5 = PhotoImage(file=mainWindowAssets("image_5.png"))
image_5 = mainCanvas.create_image(105.0,397.0,image=image_image_5)

button_image_1 = PhotoImage(file=mainWindowAssets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=renderAddWindow,relief="flat")
button_1.place(x=28.0,y=105.0,width=148.0,height=57.0)

button_image_2 = PhotoImage(file=mainWindowAssets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=editStudent,relief="flat")
button_2.place(x=28.0,y=187.0,width=148.0,height=57.0)

button_image_3 = PhotoImage(file=mainWindowAssets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=deleteStudent,relief="flat")
button_3.place(x=28.0,y=269.0,width=148.0,height=57.0)

button_image_4 = PhotoImage(file=mainWindowAssets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=viewStudent,relief="flat")
button_4.place(x=28.0,y=351.0,width=148.0,height=57.0)



style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Inter SemiBold', 12),rowheight=30) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Inter SemiBold', 12,'bold'),background="black",foreground='black')
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

renderTreeVIew(read())

mainWindow.resizable(False, False)
mainWindow.mainloop()
















