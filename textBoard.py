from tkinter import *
import tkinter.messagebox,time,tkinter.filedialog,tkinter.scrolledtext
from cryptography import fernet
import speech_recognition as sr
# def button_listener():
#     print("one of the Button pressed")
count=0
textEditorYN=False
def counter(label):
    # count=0
    def start():
        global count
        count+=1
        label.config(text=str(count))
        label.after(1000,start)
    start()
# def restart():
#     global count
#     count=0
# root=Tk()
# # root.minsize(800,600)
# # root.maxsize(800,600)
# root.title('GUI')
# root.geometry("800x600")
# label_1=Label(master=root,text="My GUI: test 1",fg="green",bg='black')
# label_1.pack(fill=X)
# label_2=Label(master=root,text="This GUI is for testing pack method,frames and buttons",fg="blue",bg='grey')
# label_2.pack(fill=X)
# label_c=Label(root)
# label_c.pack()
# counter(label_c)
# frame_2=Frame(root,bg='blue',cursor='mouse')
# frame_2.pack(side=BOTTOM,pady=20)
# frame_1=Frame(root,bg='violet',cursor='spider',highlightbackground='blue',highlightcolor='black')
# frame_1.pack(side=BOTTOM,pady=20,padx=50)
# button_1=Button(frame_1,text='Button-1',bg='orange',command=button_listener,activeforeground='red')
# button_1.flash()
# button_2=Button(frame_1,text='Button-2',bg='yellow',command=button_listener,activebackground='blue')
# button_1.pack(side=LEFT,padx=50,pady=50)
# button_2.pack(side=LEFT,padx=50,pady=50)
# button_3=Button(frame_2,text='Button-3',bg='orange',command=restart,relief=RIDGE)
# button_4=Button(frame_2,text='Button-4',bg='yellow',command=label_c.destroy,relief=GROOVE)
# button_3.pack(side=LEFT,padx=50,pady=50)
# button_4.pack(side=LEFT,padx=50,pady=50)
# root.mainloop()

def showMail():
    s=entry_email.get()
    p=entry_pwd.get()
    if "@" in s:
        if '360'==p:
            label_welcome.configure(text="Welcome "+s[0:s.index('@')],bg='white',fg='green')
            entry_email.delete(0,last=100)
            entry_pwd.delete(0,last=100)
            if tkinter.messagebox.askokcancel(title='Tushar Gusain',message='Admin login continue?'):
                text_editor_title.config(text="My text: TUSHAR")
                packEditor()
                textEditorYN=True
            # root.destroy()

        else:
            label_welcome.configure(text="Wrong password! ", bg='black', fg='red')
    else:
        label_welcome.configure(text="Enter a valid Email id" )
# def showEmail(en):
#     s=en.get()
#     print(s)
# def back():
#     root.quit()

def click(event):
    if event.num==1:
        label_click.configure(text=f'Left click at ({event.x},{event.y})')
    if event.num==3:
        label_click.configure(text=f'Right click at ({event.x},{event.y})')
    print(event)
def keyboard(event):
    def pwdKey(event):
        label_key.configure(text=f'{event.char} pressed')
        print(event)
    frame.focus_set()
    entry_pwd.bind("<Key>",pwdKey)

def custom_quit():
    global packed
    if packed:
        ans = tkinter.messagebox.askquestion(title="Exit", message="Save the data before quiting?")
        if ans=='yes':
            print(ans)
            save_file()
        text_editor.forget()
        text_editor_title.forget()
        root.pack(fill=BOTH)
        status.config(text='Run')
        label_welcome.config(text='Logged out successfully',bg='violet')
        packed=False
    else:
        ans=tkinter.messagebox.showwarning(title="Are you sure you want to quit",message="Data may be lost!")
        if ans:
            print(ans)
            root_main.quit()
packed=False
def packEditor():
    root.forget()
    text_editor_title.pack(fill=X)
    text_editor.pack(fill=BOTH,expand='yes')
    status.config(text='Running.....')
    global packed
    packed=True

def about():
    print(tkinter.messagebox.showinfo(title="About",message="This is a text editor app made by Tushar Gusain"))

def open_file():
    if textEditorYN==False:packEditor()
    file=tkinter.filedialog.askopenfile(parent=text_editor,title='Select your file',mode='rb')
    if file!=None:
        content=file.read()
        text.insert("1.0",content)
        file.close()
def save_file():
    if packed:
        file=tkinter.filedialog.asksaveasfile(mode='w')
        if file!=None:
            data=text.get('1.0',END+'-1c')
            file.write(data)
    else:
        tkinter.messagebox.showerror(title='Save error',message='No file to save')
def get_dir():
    tkinter.filedialog.askdirectory()

def converter(t):
    convert=Tk()
    convert.maxsize(width=300,height=300)
    label_from=Label(convert,text='Integer value:',fg='green')
    label_from.grid(row=0,column=0)
    entry_from=Entry(convert)
    entry_from.grid(row=0,column=1)
    entry_from.focus_set()
    def start():
        if t == 'b':
            num = bin(int(entry_from.get()))
            tt = "Binary"
        elif t == 'o':
            num = oct(int(entry_from.get()))
            tt = "Octal"
        elif t == 'h':
            num = hex(int(entry_from.get()))
            tt = "Hexadecimal"
        tkinter.messagebox.showinfo(title=tt + " value", message=num)
        convert.destroy()
    button_convert=Button(convert,text="convert",command=start)
    button_convert.grid(row=1,column=1,sticky='e')
    convert.mainloop()

def count_vc(vc):
    msg=text.get('1.0',END+'-1c')

    count = 0
    vowels = ('a', 'e', 'i', 'o', 'u')

    if vc == 0:
        for ch in msg:
            if ch in vowels:
                count = count + 1
        tkinter.messagebox.showinfo(title='vowels found', message=f'{count}')
    elif vc == 1:
        for ch in msg:
            if ch not in vowels:
                count = count + 1
        tkinter.messagebox.showinfo(title='consonants found', message=f'{count}')
    elif vc==2:
        for ch in msg:
            count = count + 1
        tkinter.messagebox.showinfo(title='vowels found', message=f'{count}')


key=None
def crypt(ed):
    global key
    data = text.get('1.0', END + '-1c')
    crypt_gui=Tk()
    enc_dec=Label(crypt_gui,text='key')
    enc_dec.grid(row=0,column=0)
    key_entry=Entry(crypt_gui)
    key_entry.grid(row=0,column=1)
    dns_label=Label(crypt_gui)
    dns_label.grid(row=1,column=0)
    enc_dec_button=Button(crypt_gui)
    enc_dec_button.grid(row=1,column=1)

    if ed==0:
        def enc_key():
            enc_data = fernet.Fernet(key).encrypt(data.encode())
            text.delete('1.0', END + '-1c')
            text.insert("1.0", enc_data)
            crypt_gui.destroy()
        key=fernet.Fernet.generate_key()
        key_entry.insert(0,key)
        dns_label.config(text="plz do not share",bg='orange')
        enc_dec_button.config(text='encrypt',command=enc_key)

    else:
        def dec_key():
            key_entry.focus_set()
            dKey = key_entry.get().encode()
            #print(dKey)
            #print(key)
            if dKey==key:
                dec_data = fernet.Fernet(dKey).decrypt(data.encode())
                text.delete('1.0', END + '-1c')
                text.insert("1.0", dec_data)
            else:
                tkinter.messagebox.showwarning(title='Mismatch',message='keys do not match')
            crypt_gui.destroy()

        key_entry.config(show="*")
        dns_label.config(text="plz enter the key", bg='green')
        enc_dec_button.config(text='decrypt',command=dec_key)
    crypt_gui.mainloop()

def speech_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # print("Speak something: ")
        audio = r.listen(source)
    stt=r.recognize_google(audio)
    if stt=='dot':
        text.insert(END + '-1c','. ')
    elif stt=='comma':
        text.insert(END + '-1c', ', ')
    else:
        text.insert(END+'-1c',stt+' ')

root_main=Tk()
root_main.title('GUI')
root_main.minsize(width=400,height=400)
menu=Menu(root_main)
root_main.config(menu=menu)

#File
menu_file=Menu(menu,activebackground='red',bd=4,cursor='spider')
menu.add_cascade(label='File',menu=menu_file)
menu_file.add_command(label='New',command=packEditor)
menu_file.add_command(label='Open',command=open_file)
menu_file.add_command(label='Save',command=save_file)
menu_file.add_cascade(label='Settings')
menu_file.add_command(label='Exit',command=custom_quit)

#Edit
menu_edit=Menu(menu,activebackground='green',bd=4)
menu.add_cascade(label='Edit',menu=menu_edit)
menu_edit.add_cascade(label='Cut')
menu_edit.add_cascade(label='Copy')
menu_edit.add_cascade(label='Paste')
menu_edit.add_cascade(label='Delete')
#Edit.Count
menu_find=Menu(menu_edit,activebackground='#012901')
menu_edit.add_cascade(label='Count',menu=menu_find)
menu_find.add_command(label='Vowels',command=lambda :count_vc(0))
menu_find.add_command(label='Consonants',command=lambda :count_vc(1))
menu_find.add_command(label='Characters',command=lambda :count_vc(2))

#View
menu_view=Menu(menu,activebackground='blue',bd=4)
menu.add_cascade(label='View',menu=menu_view)
menu_view.add_cascade(label='Recent files')
menu_view.add_command(label='Directory',command=get_dir)
menu_view.add_cascade(label='Navigationbar')
# menu_view.add_cascade(label='Editor')
#View.Crypt
menu_crypt=Menu(menu_view,activebackground='cyan')
menu_view.add_cascade(label='Crypt',menu=menu_crypt)
menu_crypt.add_command(label='Encrypt',command=lambda :crypt(0))
menu_crypt.add_command(label='Decrypt',command=lambda :crypt(1))

#View.Window_size
menu_window=Menu(menu_view,activebackground='indigo',bd=4)
menu_view.add_cascade(label='Window size',menu=menu_window)
menu_window.add_command(label='600x400',command=lambda :root_main.geometry('600x400'))
menu_window.add_command(label='800x600',command=lambda :root_main.geometry('800x600'))
menu_window.add_command(label='1200x800',command=lambda :root_main.geometry('1200x800'))
menu_window.add_command(label='1200x960',command=lambda :root_main.geometry('1200x960'))
menu_window.add_command(label='1400x960',command=lambda :root_main.geometry('1400x960'))

#converter
menu_convert=Menu(menu,activebackground='magenta',bd=4)
menu.add_cascade(label='Converter',menu=menu_convert)
menu_convert.add_command(label='Binary',command=lambda :converter('b'))
menu_convert.add_command(label='Octal',command=lambda :converter('o'))
menu_convert.add_command(label='Hexadecimal',command=lambda :converter('h'))

#SpeechToText
menu.add_command(label='SpeechToText',command=speech_text)


#Help
menu_help=Menu(menu,activebackground='yellow',bd=4,activeforeground='black')
menu.add_cascade(label='Help',menu=menu_help)
menu_help.add_cascade(label='Find action')
menu_help.add_cascade(label='?Help')
menu_help.add_command(label='Tip of the day',command=lambda :tkinter.messagebox.showinfo(title='Tip of the day',message='Stay hungry,stay foolish'))
menu_help.add_cascade(label='Contact support')
menu_help.add_command(label="About",command=about)
title=Label(root_main,text="Test GUI",bg="black",fg="green")
title.pack(fill=X)
sub_title=Label(root_main,text="This GUI is made by TUSHAR GUSAIN",bg="BLUE",fg="orange")
sub_title.pack(fill=X)

label_counter=Label(root_main,text="0",fg="red")
label_counter.pack(fill=X)
counter(label_counter)



#Login page
root=Frame(root_main)
root.pack(fill=BOTH)
# label_1=Label(master=root,text="My GUI: test 1",fg="green",bg='black')
# label_1.grid(row=0)
# label_2=Label(master=root,text="This GUI is for testing grid method",fg="blue",bg='grey')
# label_2.grid(row=1)
label_email=Label(root,text='Email')
label_email.grid(row=1,column=0,sticky='e')
label_pwd=Label(root,text='Password')
label_pwd.grid(row=2,column=0,sticky='e')
e=StringVar()
entry_email=Entry(root,bd=4,cursor='shuttle',fg='green',textvariable=e)
entry_email.bind("<Button-1>",lambda event:entry_email.delete(0,last=100))
entry_email.grid(row=1,column=1)
e.set("your email id")
# s=v.get()
# s=entry_email.get()
entry_email.focus_set()
# showMail()
p=StringVar()
entry_pwd=Entry(root,bd=0,cursor='cross',bg='red',relief=FLAT,show='♫',textvariable=p)
# entry_pwd.bind("<Key>",keyboard)
entry_pwd.bind("<Button-1>",lambda event:entry_pwd.delete(0,last=100))
p.set("password")
entry_pwd.grid(row=2,column=1)
entry_pwd.focus_set()
checkbox=Checkbutton(root,text='remember me')
checkbox.grid(row=3,column=1,sticky='e')
button_login=Button(root,text="Login",command=showMail)
button_login.grid(row=4,column=1)
button_back=Button(root,text="Back",command=root.quit)
button_back.grid(row=4,column=1,sticky='e')
label_welcome=Label(root,text='No user found!',bg='red')
label_welcome.grid(row=5,column=1)
frame=Frame(root,width=400,height=400,bg='red')
frame.grid(row=6,column=1)
label_click=Label(frame,bg='blue',text='Click me to know your click')
label_click.pack(fill=X)
label_click.bind("<Button-1>",click)
label_click.bind("<Button-3>",click)
label_key=Label(frame,bg='orange',text='know the character pressed')
label_key.bind("<Button-1>",keyboard)
label_key.pack(fill=X)


#Text Editor page
text_editor_title=Label(root_main,text="My text: GUEST")
text_editor=Frame(root_main)
text=tkinter.scrolledtext.ScrolledText(text_editor,width=20,height=40,bg='gray',relief=SUNKEN,fg='blue',bd=10,cursor='pirate')
text.pack(fill=BOTH)

#statusBar
status=Label(root_main,text="Run",bg="yellow",relief=SUNKEN)
status.pack(fill=X,side=BOTTOM)


root_main.mainloop()


# d={4:'four',1:'one',2:'two',3:'three'}
# print(d)
# import json
# print(json.dumps(d,indent=0,sort_keys=True))