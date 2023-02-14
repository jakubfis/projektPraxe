import tkinter as tk
from tkinter import ttk
from tkinter import *
import re
from pytube import YouTube
import os
from PIL import Image
from tkinter import filedialog as fd
from tkinter import messagebox

def help():
    #root.withdraw()
    help = tk.Tk()
    T = tk.Text(help, height=30, width=45)
    T.pack()
    help.eval('tk::PlaceWindow . center')
    help.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, help))
    quote = """HELP
---------------------------------------------
Open Calculator
Jedná se o jednoduchou kalkulačku.
---------------------------------------------
Download YT video
Stačí vložit link na vybrané video. Po
stlačení tlačítka "save" se video stáhne
ale pokud je link neplatný/špatný, nic
se nestane.
---------------------------------------------
Convertor
Convertor převádí JPG do PNG a PGN do JPEG
Po vybrání stačí najít soubor, který chceme
převést a dáme otevřít. Potom se soubor
převede a stačí si ho pojmenovat a vybrat
kam se uloží.
---------------------------------------------"""
    T.insert(tk.END, quote)
    tk.mainloop()
def open_calculator():
    root.withdraw()
    class Calculator:
        def __init__(self, master):
            self.master = master            
            master.title("Python Calculator")
            self.screen = Text(master, state='disabled', width=30, height=3,background="yellow", foreground="blue")
            self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
            self.screen.configure(state='normal')
            self.equation = ''            
            b1 =  self.createButton(7)
            b2 = self.createButton(8)
            b3 = self.createButton(9)
            b4 = self.createButton(u"\u232B",None)
            b5 = self.createButton(4)
            b6 = self.createButton(5)
            b7 = self.createButton(6)
            b8 = self.createButton(u"\u00F7")
            b9 = self.createButton(1)
            b10 = self.createButton(2)
            b11 = self.createButton(3)
            b12 = self.createButton('*')
            b13 = self.createButton('.')
            b14 = self.createButton(0)
            b15 = self.createButton('+')
            b16 = self.createButton('-')
            b17 = self.createButton('=',None,34)
            buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]
            count = 0            
            for row in range(1,5):
                for column in range(4):
                    buttons[count].grid(row=row,column=column)
                    count += 1            
                    buttons[16].grid(row=5,column=0,columnspan=4)
        def createButton(self,val,write=True,width=7,):
            return Button(self.master, text=val,command = lambda: self.click(val,write), width=width)
        def click(self,text,write):
            if write == None:
                if text == '=' and self.equation: 
                    self.equation= re.sub(u"\u00F7", '/', self.equation)
                    answer = str(eval(self.equation))
                    self.clear_screen()
                    self.insert_screen(answer,newline=True)
                elif text == u"\u232B":
                    self.clear_screen()
            else:
                self.insert_screen(text)
        def clear_screen(self):
            self.equation = ''            
            self.screen.configure(state='normal')
            self.screen.delete('1.0', END)
        def insert_screen(self, value,newline=False):
            self.screen.configure(state='normal')
            self.screen.insert(END,value)
            self.equation += str(value)
            self.screen.configure(state ='disabled')
    cal = Tk()
    cal.eval('tk::PlaceWindow . center')
    cal.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, cal))
    my_gui = Calculator(cal)
    cal.mainloop()
def on_closing(root, cal):
    root.deiconify()
    cal.destroy()
def youtubed():
    root.withdraw()
    def save_text():
        global text_content   
        text_content = text_widget.get("1.0", "end-1c")
        link = text_content
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            messagebox.showerror('Python Error', 'Error: This is an Error Message!')
        messagebox.showinfo('Downloader', 'Download successful')
        ytd.destroy()
        root.destroy()
    ytd = tk.Tk()
    ytd.title("Entry youtube link")
    ytd.eval('tk::PlaceWindow . center')
    text_widget = tk.Text(ytd, height=5, width=45)
    text_widget.pack()
    save_button = tk.Button(ytd, text="Save", command=save_text)
    save_button.pack()
    text_content = ""    
    ytd.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, ytd))
    ytd.mainloop()
def convertor():
    root.withdraw()    
    con = Tk()
    con.title("Convertor")
    con.eval('tk::PlaceWindow . center')
    def jpg_to_png():
        global im1        
        import_filename = fd.askopenfilename()
        if import_filename.endswith(".jpg"):
            im1 = Image.open(import_filename)
            export_filename = fd.asksaveasfilename(defaultextension=".png")
            im1.save(export_filename)
            messagebox.showinfo("success ", "your Image converted to Png")
        else:
            Label_2 = Label(con, text="Error!", width=20,
                            fg="red", font=("bold", 15))
            Label_2.place(x=80, y=280)
            messagebox.showerror("Fail!!", "Something Went Wrong...")
    def png_to_jpg():
        global im1        
        import_filename = fd.askopenfilename()
        if import_filename.endswith(".png"):
            im1 = Image.open(import_filename)
            export_filename = fd.asksaveasfilename(defaultextension=".jpg")
            im1.save(export_filename)
            messagebox.showinfo("success ", "your Image converted to jpg ")
        else:
            Label_2 = Label(con, text="Error!", width=20,
                            fg="red", font=("bold", 15))
            Label_2.place(x=80, y=280)
            messagebox.showerror("Fail!!", "Something Went Wrong...")
    button1 = Button(con, text="JPG_to_PNG", width=20, height=2, bg="green",
                    fg="white", font=("helvetica", 12, "bold"), command=jpg_to_png)
    button1.place(x=120, y=120)
    button2 = Button(con, text="PNG_to_JPEG", width=20, height=2, bg="green",
                    fg="white", font=("helvetica", 12, "bold"), command=png_to_jpg)
    button2.place(x=120, y=220)
    con.geometry("500x500+400+200")
    con.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, con))
    con.mainloop()
root = tk.Tk()
root.geometry('360x240')
root.eval('tk::PlaceWindow . center')
root.title("Main Menu")
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open Calculator", command=open_calculator)
file_menu.add_command(label="Download YT video", command=youtubed)
file_menu.add_command(label="Convertor", command=convertor)
file_menu.add_command(label="Help", command=help)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)
open_calc_button = ttk.Button(root, text="Open Calculator", command=open_calculator,)
open_calc_button.pack(pady = 5)
youtube_button = ttk.Button(root, text="Download YT video", command=youtubed)
youtube_button.pack(pady = 5)
convertor_button = ttk.Button(root, text="Convertor", command=convertor)
convertor_button.pack(pady = 5)
exit_button = ttk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady = 20)
root.mainloop()