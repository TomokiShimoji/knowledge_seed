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
listbox = Listbox(master=frame,listvariable=StringVar(value=knowledge_list), takefocus=True, justify=LEFT, yscrollcommand=scrollbar.set, selectmode=MULTIPLE)

def show_selected(event):
    n = listbox.curselection()   #選択項目のindex取得
    for i in n:
      try:
        webbrowser.open(list_url[i])
      except:
        mb.showinfo("Error", "このURLのウェブサイトは存在しません")

listbox.bind(
    "<Double-Button-1>",
    show_selected,
    )

file = None

def saveFile():
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
      file = None
  else:
    if type(file) != str:
      file = file.name
    file_path = os.path.dirname(file)
    f = open(file_path, "w", encoding="UTF-8", errors="ignore")
    for i in range(len(knowledge_list)):
      f.write(knowledge_list[i]+","+list_url[i]+"\n")
    file = None
    f.close()
    
def openFile():
  global knowledge_list, list_url
  file = fi.askopenfilename(
    initialdir=".",
    title="select ksファイル", 
    defaultextension=".ks",
    filetypes=[("ks files", "*.ks")])
  if file == "":
    file = None
    return "noopened"
  else:
    f = open(file, "r", encoding="UTF-8",errors="ignore")
    knowledge_list = []
    list_url = []
    listbox.delete(0, END)
    for i in f.readlines():
      knowledge_list.append(i.split(",")[0])
      list_url.append(i.split(",")[1])
      listbox.insert(END, i.split(",")[0])
    f.close()
    print(knowledge_list)
    print(list_url)
    file = None


scrollbar.config(command=listbox.yview)
frame.pack(pady=20)
scrollbar.pack(side=RIGHT, fill="y")
listbox.pack()

def click_button():
  knowledge_list.append(input_field1.get())  
  list_url.append(input_field2.get())
  listbox.insert(END, input_field1.get())
  print(knowledge_list)
  print(list_url)

button1 = Button(text="実行", command = click_button)
button1.place(x=60, y=80)

button2 = Button(text="保存", command = saveFile)
button2.pack()

button3 = Button(text="ファイルを開く", command = openFile)
button3.pack()

def deleteword():
  n = listbox.curselection()   #選択項目のindex取得
  if not n:
    print("選択されていません")
    return
  adjustment = 0
  for i in n:
    listbox.delete(i- adjustment)
    knowledge_list.pop(i-adjustment)
    list_url.pop(i-adjustment)
    adjustment += 1
  print(knowledge_list)
  print(list_url)

button4 = Button(text="削除", command = deleteword)
button4.place(x=60, y=110)

def on_window_click(event):
  x, y = event.x, event.y
  if not (0 <= x < listbox.winfo_width() and 0 <= y < listbox.winfo_height()):
    # Listbox以外の領域をクリックした場合、選択を解除する
    listbox.selection_clear(0, END)

root.bind("<Button-1>", on_window_click)

root.mainloop()
