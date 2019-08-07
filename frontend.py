# coding=utf-8
from Tkinter import *
import backend
# AUN FALLA ESA MIERDA DE ELIMINAR


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    labe = Toplevel()
    labe
    for idx, row in enumerate(backend.search_row(selected_tuple[0])):
        Checkbutton(labe, text=row[1], variable=IntVar()
                    ).grid(row=1+idx, column=1)

    # list2.delete(0, END)
    # for row in backend.search_row(selected_tuple[0]):
    #     list2.insert(END, row[1])


# def get_selected_list_row(event):
#     global selected_list_tuple
#     index = list2.curselection()[0]
#     selected_list_tuple = list2.get(index)
#     e2.delete(0, END)
#     e2.insert(END, Checkbutton(window, text=selected_tuple[1]))

#     print(selected_list_tuple[0])


def view_command():
    list1.delete(0, END)

    for row in backend.view():
        list1.insert(END, row)


def insert_command():
    if title_text.get() != "":
        backend.insert(title_text.get())
    else:
        print('Nada Colocado')


def insert_list_command():
    if new_list.get() != "":
        backend.insert_row(
            new_list.get(), selected_tuple[0])
        # print(get_selected_list_row(selected_tuple[0]))
    else:
        print('Nada Colocado')


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


window = Tk()
window.title("Checker")
window.iconbitmap(
    r'C:\Users\pablo\Desktop\CheckDesktopApp\PythonV.2\Icono.ico')
l1 = Label(window, text="Categorias")
l1.grid(row=1, column=1)
l2 = Label(window, text="Listas")
l2.grid(row=1, column=3)


b0 = Button(window, text="Ver Todos", width=12, command=view_command)
b0.grid(row=0, column=4)
b = Button(window, text="Eliminar", width=12, command=delete_command)
b.grid(row=1, column=4)
b1 = Button(window, text="Añadir Lista", width=12, command=insert_list_command)
b1.grid(row=5, column=3)
b2 = Button(window, text="Añadir Categoria ", width=12, command=insert_command)
b2.grid(row=5, column=1)


title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=4, column=1)
new_list = StringVar()
e2 = Entry(window, textvariable=new_list)
e2.grid(row=4, column=3)

list1 = Listbox(window, height=6, width=36)
list1.grid(row=2, column=1)
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)


view_command()
# This will create a LabelFrame
# label_frame = Toplevel()
# label_frame.grid(row=2, column=3)

# list2 = Listbox(window, height=6, width=36)
# list2.grid(row=2, column=3)
# list2.bind('<<ListboxSelect>>', get_selected_list_row)
window.mainloop()
