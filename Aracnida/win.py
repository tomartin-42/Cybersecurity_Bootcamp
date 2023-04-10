import tkinter
from tkinter import ttk
from tkinter import font
import filemanager


class Main_Win(filemanager.Reader):
    def __init__(self, args):
        super().__init__(args)
        self.root = tkinter.Tk()
        self.root.title("Aracnida")
        self.root.geometry("1000x1300")
        boton_save = tkinter.Button(
            self.root, text='Actualizar')
        boton_quit = tkinter.Button(
            self.root, text='Salir', command=self.root.quit)
        Tree_Win(super().get_info_list(), self.root)
        boton_save.pack()
        boton_quit.pack()
        self.root.mainloop()


class Tree_Win():
    def __init__(self, data_list, frame):
        self.position = 0
        self.tree = ttk.Treeview(frame, columns=(
            'Label', 'Value'), show='headings')
        self.tree.configure(height=len(data_list[0]))
        self.tree.heading(0, text="Label")
        self.tree.heading(1, text="Value")
        self.tree.column("#2", width=800)
        for e in data_list[0]:
            print(e, data_list[self.position][e])
            self.tree.insert('', 'end', values=(e, data_list[self.position][e]))
        self.tree.grid(row=1, column=2, columnspan=2)
        self.tree.bind('<Double-Button-1>', self.edit_value)

    def edit_value(self):

        def actualizar():
            print("Actualizando")

        def cancle():
            print("Cancle")

        # Obtenemos la fila seleccionada
        row = self.tree.selection()[0]
        row_data = self.tree.item(row)

        # Obtenemos el valor de la segunda columna
        value = row_data['values'][1]

        # Creamos una entrada para editar el valor
        input = tkinter.Entry(self.tree, width=500)
        input.insert(0, value)
        boton1 = tkinter.Button(
            self.tree, text='Actualizar', command=actualizar)
        boton1 = tkinter.Button(
            self.tree, text='Cancel', command=cancle)
        input.pack()
        boton1.pack()
