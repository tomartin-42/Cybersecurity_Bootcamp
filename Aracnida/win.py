import tkinter
from tkinter import ttk
import filemanager
import subprocess

class Main_Win(filemanager.Reader):
    def __init__(self, args):
        super().__init__(args)
        self.list = super().get_info_list()
        self.position = 0
        self.root = tkinter.Tk()
        self.root.title("Aracnida")
        self.root.geometry("1000x1300")

        if len(self.list) == 0:
            print("No hay archivos")
            exit(1)
        button_container = tkinter.Frame(self.root)
        boton_quit = tkinter.Button(
            button_container, text='Salir', command=self.root.quit)
        boton_prev = tkinter.Button(
            button_container, text='<', command=self._prev)
        boton_next = tkinter.Button(
            button_container, text='>', command=self._next)
        boton_quit.pack(side='left', padx=10, pady=10)
        boton_prev.pack(side='left', padx=10, pady=10)
        boton_next.pack(side='left', padx=10, pady=10)
        button_container.pack(side='top', fill='x')

        self.tree = Tree_Win(self.list, self.root, self.position)

        self.root.mainloop()

    def _next(self):
        if self.position + 1 < len(self.list):
            self.position += 1
            self.tree.update_tree(self.list, self.position)
    
    def _prev(self):
        if self.position - 1 >= 0:
            self.position -= 1
            self.tree.update_tree(self.list, self.position)


class Tree_Win():
    def __init__(self, data_list, frame, position):
        self.data_list = data_list
        self.position = position
        self.tree = ttk.Treeview(frame, columns=(
            'Label', 'Value'), show='headings')
        self.tree.configure(height=len(data_list[0]))
        self.tree.heading(0, text="Label")
        self.tree.heading(1, text="Value")
        self.tree.column("#2", width=800)
        for e in data_list[position]:
            self.tree.insert('', 'end', values=(e, data_list[position][e]))
        self.tree.pack(side='top', fill='both', expand=True)
        self.tree.bind('<Double-Button-1>', self.edit_value)

    def edit_value(self, event):

        def actualizar():
            cmd = ["exiftool", '-' + row_data['values'][0] + '=' + input.get(), self.data_list[self.position]['SourceFile']] 
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.data_list[self.position][row_data['values'][0]] = input.get()
            top.destroy()
            self.update_tree(self.data_list, self.position)
            print("Actualizando")

        def cancle():
            top.destroy()
        
        # Obtenemos la fila seleccionada
        row = self.tree.selection()[0]
        row_data = self.tree.item(row)

        # Obtenemos el valor de la segunda columna
        value = row_data['values'][1]

        # Creamos una nueva ventana para mostrar el Entry
        top = tkinter.Toplevel(self.tree.winfo_toplevel())
        top.geometry("800x100")

        # Creamos una entrada para editar el valor
        input = tkinter.Entry(top, width=50)
        input.insert(0, value)

        boton1 = tkinter.Button(
            top, text='Actualizar', command=actualizar)
        boton2 = tkinter.Button(
            top, text='Cancel', command=cancle)
        input.pack(side='left', padx=10, pady=10)
        boton1.pack(side='left', padx=10, pady=10)
        boton2.pack(side='left', padx=10, pady=10)

    def update_tree(self, data_list, position):
        self.tree.delete(*self.tree.get_children())
        for e in data_list[position]:
            self.tree.insert('', 'end', values=(e, data_list[position][e]))
