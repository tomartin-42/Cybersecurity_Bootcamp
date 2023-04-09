import tkinter
from tkinter import ttk
from tkinter import font
import filemanager

class Win(filemanager.Reader):
    def __init__(self, args):
        super().__init__(args)
        self.root = tkinter.Tk()
        self.root.title("Aracnida")
        self.root.geometry("1000x1000")
        self.show_tree(super().get_info_list())
        self.root.mainloop()
        a = Iner_label()

    def show_tree(self, data_list):
        self.tree = ttk.Treeview(self.root, columns=('Label', 'Value'), show='headings')
        self.tree.configure(height=len(data_list[0]))
        self.tree.heading(0, text="Label") 
        self.tree.heading(1, text="Value") 
        self.tree.column("#2", width=2200)
        for e in data_list[0]:
            print(e, data_list[0][e])
            self.tree.insert('', 'end', values=(e, data_list[0][e]))
        self.tree.grid(row=1, column=2, columnspan=2)
        self.tree.bind('<Double-Button-1>', self.edit_value)

    def edit_value(self, event):
        # Obtenemos la fila seleccionada
        fila = self.tree.selection()[0]
        datos_fila = self.tree.item(fila)

        # Obtenemos el valor de la segunda columna
        valor = datos_fila['values'][1] 
        
        # Creamos una entrada para editar el valor
        entrada = tkinter.Entry(self.tree, width=500)
        entrada.insert(0, valor)
        entrada.pack()

        
        def actualizar():
            # Obtenemos el nuevo valor
            nuevo_valor = entrada.get()
            # Actualizamos el valor en la fila
            self.tree.item(fila, values=(datos_fila['values'][0], nuevo_valor))
            # Eliminamos la entrada
            entrada.destroy()
            # Eliminamos el botón actualizar
            boton.destroy()

        boton = tkinter.Button(self.tree, text='Actualizar', command=actualizar)
        boton.pack()


class Iner_label:
    def __init__(self):
        pass