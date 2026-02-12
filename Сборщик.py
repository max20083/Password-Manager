from tkinter import *
from tkinter import ttk
def del_web():
    web = webs_combo.get()
    with open("webs.txt","r",encoding="utf-8") as f:
        content_webs = f.readline()
    f.close()
    with open("logs.txt","r",encoding="utf-8") as f1:
        content_logs = f1.readlines()
    f1.close()
    if web != "Выберите сайт":
        webs.remove(f"{web}")
        with open("webs.txt","w",encoding="utf-8") as f_w:
            cont_1 = content_webs.replace(f"{web},","")
            f_w.write(cont_1)
        file.close()
        try:
            for i in range(len(content_logs)):
                print(content_logs)
                cont = content_logs[i]
                cont = cont.split()
                if cont[0] == web:
                    del content_logs[i]
            with open("logs.txt","w",encoding="utf-8") as f1_w:
                for line in content_logs:
                    f1_w.write(line)
            f1_w.close()
            webs_combo.configure(values=webs)
            webs_combo.set("Выберите сайт")
            status_lbl.configure(text=f"{web} успешно удален")
        except:
            with open("logs.txt","w",encoding="utf-8") as f1_w:
                for line in content_logs:
                    f1_w.write(line)
            f1_w.close()
            webs_combo.configure(values=webs)
            webs_combo.set("Выберите сайт")
            status_lbl.configure(text=f"{web} успешно удален")
    else:
        status_lbl.configure(text="Выберите сайт")

def req_func():
    status_lbl.configure(text="Все аккаунты вынесены в отдельный txt файл!")
    with open("Логины и пароли.txt","w",encoding="utf-8") as file0:
        file0.write("----------------------------------------------------------")
        file0.close()
    with open("logs.txt","r",encoding="utf-8") as file1:
        while True:
            counter = 0
            content = (file1.readline()).split()
            logs = content[1:]
            web = content[0]
            if logs != "":
                with open("Логины и пароли.txt","a",encoding="utf-8") as file2:
                    file2.write(f"{web}\nЛогины и пароли для сайта - {web}:\n")
                    for log in logs:
                        counter += 1
                        cont = log.split(":")
                        login = cont[0]
                        password = cont[1]
                        file2.write(f"Логин - {login}, Пароль - {password}\n")
                        if counter == len(logs):
                            file2.write("----------------------------------------------------------")
                file2.close()
            if not content:
                break
            
                
    file1.close()

def create_acc(event):
    login=login_input_but.get()
    password=pass_input.get()
    web=webs_combo.get()
    with open("logs.txt","r+",encoding="utf-8") as f:
        lines=f.readlines()
        for i in range(len(lines)):
            web1 = lines[i].split()[0]
            if web != "Выберите сайт":
                if web == web1:
                    if login != "" and password != "" and " " not in login and " " not in password and ":" not in login and ":" not in password:
                        lines[i] = lines[i].rstrip("\n") + f" {login}:{password}\n"
                        status_lbl.configure(text="Данные добавлены")
                        f.seek(0)
                        f.writelines(lines)
                        login_input_but.delete("0",END)
                        pass_input.delete("0",END)
                    elif ":" in login or ":" in password:
                        status_lbl.configure(text="Поля не могут содержать символ ':' ")
                    else:
                        status_lbl.configure(text="Поля не должны оставаться пустыми или содержать пробелы ")
            else:
                status_lbl.configure(text="Выберите сайт")
        f.close()

def create_web():
    def add_web(event):
        web=(web_input_create.get()).rstrip()
        if web != "" and web not in webs and " " not in web and "," not in web:
            webs.append(web)
            with open("webs.txt","a",encoding="utf-8") as file:
                file.write(f"{web},")
                file.close()
                status_web.configure(text=f"""{web} - добавлен""")
            with open("logs.txt","a",encoding="utf-8") as file2:
                file2.write(f"{web}\n")
                file2.close()
            web_input_create.delete("0",END)
        elif "," in web:
            status_web.configure(text="Поле не могу содержать запятые")
        elif web in webs:
            status_web.configure(text="Такой сайт уже есть в базе")
        if "" == web or " " in web:
            status_web.configure(text="Сайт не может содержать пробелы " \
            "или быть пустым")
        webs_combo.configure(values=webs)
    web_root=Tk()
    web_root.title("Добавление веб-сайта")
    web_root.geometry("300x150")
    web_root.resizable(False,False)
    frame_input_web_create=Frame(web_root)
    frame_input_web_create.pack()
    web_input_create=Entry(frame_input_web_create,width=15)
    web_input_create.pack(pady=10)
    frame_web_create=Frame(web_root)
    frame_web_create.pack()
    web_create_but = Button(frame_web_create,text="Добавить сайт",width=15,command=add_web)
    web_create_but.pack(pady=15)
    frame_status_webroot = Frame(web_root)
    frame_status_webroot.pack()
    status_web = Label(frame_status_webroot,text="")
    status_web.pack(pady=10)
    web_root.bind("<Return>",add_web)
with open ("webs.txt","r",encoding="utf-8") as file:
    content_webs = file.read()
    file.close()
webs = content_webs.split(",")
del webs[-1]
root = Tk()
root.title("Сборщик паролей")
root.geometry("600x300")
root.resizable(False,False)
webs_combo_frame = Frame(root)
webs_combo_frame.pack()
webs_combo = ttk.Combobox(root,values=webs,state="readonly")
webs_combo.set("Выберите сайт")
webs_combo.pack(pady=(10))
frame_login_pass = Frame(root)
frame_login_pass.pack()
login_lbl = Label(frame_login_pass,text="Логин")
login_lbl.pack(side=LEFT,padx=0,pady=0)
login_input_but=Entry(frame_login_pass,width=20)
login_input_but.pack(side=LEFT,padx=10,pady=0)
pass_lbl=Label(frame_login_pass,text="Пароль")
pass_lbl.pack(side=LEFT,padx=10,pady=0)
pass_input=Entry(frame_login_pass,width=20)
pass_input.pack(side=LEFT,padx=0,pady=0)
frame_create_acc=Frame(root)
frame_create_acc.pack()
create_acc_but=Button(frame_create_acc,text="Добавить учетную запись",width=40,command=create_acc)
create_acc_but.pack(pady=20)
frame_create_web=Frame(root)
frame_create_web.pack()
create_web_but=Button(frame_create_web,text="Добавить сайт",width=20,command=create_web)
create_web_but.pack(side=LEFT, padx=0,pady=0)
del_web_but=Button(frame_create_web,text="Удалить сайт",width=20,command=del_web)
del_web_but.pack(side=LEFT,padx=10,pady=0)
frame_req=Frame(root)
frame_req.pack()
req_but=Button(frame_req,text="Запросить логины и пароли",width=25,command=req_func)
req_but.pack(pady=30)
frame_status=Frame(root)
frame_status.pack()
status_lbl=Label(frame_status,text="")
status_lbl.pack(pady=10)
root.bind("<Return>",create_acc)
root.mainloop()

