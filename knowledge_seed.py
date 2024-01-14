from tkinter import *
import tkinter.messagebox as mb
import tkinter.filedialog as fi
import webbrowser
import os

root = Tk()
root.title("KNOWLEDGE SEED")
root.geometry("480x320")

input_field1 = Entry(width=10,textvariable=StringVar())
input_field1.place(x=60,y=20)

label1 = Label(text="word:")
label1.place(x=20,y=20)

input_field2 = Entry(width=10,textvariable=StringVar())
input_field2.place(x=60,y=50)

label2 = Label(text=" URL:")
label2.place(x=20,y=50)

knowledge_list = []
list_url = []

frame = Frame(master=None)
scrollbar = Scrollbar(master=frame,orient=VERTICAL)
listbox = Listbox(master=frame,listvariable=StringVar(value=knowledge_list), takefocus=True, justify=LEFT, yscrollcommand=scrollbar.set)

def show_selected(event):
    n = listbox.curselection()   #選択項目のindex取得
    try:
      webbrowser.open(list_url[n[0]])
    except:
      mb.showinfo("Error", "このURLのウェブサイトは存在しません")

listbox.bind(
    "<<ListboxSelect>>",
    show_selected,
    )

file = None

def saveFile(self):
  global file
  if file == None:
    file = fi.asksaveasfilename(
      initialdir=".",
      title="select ksファイル",
      initialfile= 'untitled.ks', 
      defaultextension=".ks",
      filetypes=[("ks files", "*.ks")])
    if file == "":
      file = None
      return "nosaved"
    else:
      f = open(file, "w", encoding="UTF-8",errors="ignore")
      for i in range(len(knowledge_list)):
        f.write(knowledge_list[i]+","+list_url[i]+"\n")
      f.close()
      root.title(os.path.basename(file))
  else:
    if type(file) != str:
      file = file.name
    file_path = os.path.dirname(file)
    f = open(file_path, "w", encoding="UTF-8", errors="ignore")
    for i in range(len(knowledge_list)):
      f.write(knowledge_list[i]+","+list_url[i]+"\n")
    f.close()
    

root.bind_all("<Control-KeyPress-s>", saveFile)

scrollbar.config(command=listbox.yview)
frame.pack(pady=20)
scrollbar.pack(side=RIGHT, fill="y")
listbox.pack()

def click_button():
  knowledge_list.append(input_field1.get())  
  list_url.append(input_field2.get())
  listbox.insert(END, input_field1.get())
  print(list_url)
  print(knowledge_list)

button1 = Button(text="実行", command = click_button)
button1.place(x=40, y=80)

root.mainloop()
