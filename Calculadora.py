from tkinter import *  

#------------------------------------------------------------------------------------------------------------------------------------------V
# CONFIGURACION INICIAL DE LA VENTANA
ventana = Tk() 
ventana.title="Calculadora"
ventana.config(bg="#264040")
ventana.resizable(False, False)

#------------------------------------------------------------------------------------------------------------------------------------------V
# FUNCIONES
i=0
def click_boton(valor): # Para que los botones inserten su valor en la caja de entradas
    global i
    entrada.insert(i,valor)
    i +=1
    
def operacion():# Para que el "=" devuelva las operaciones resueltas
    try:
        ecuacion= entrada.get()  
        resultado=eval(ecuacion)
        entrada.delete(0, END)  
        entrada.insert(0, resultado)
    except Exception as error:
        entrada.delete(0, END)
        entrada.insert(0, "Error")
        print(f"Error: {error}")

def borrar_todo(): # Para el boton "C"
    entrada.delete(0, END)

def borrar_uno(): # Para el boton "Del"
    txt_actual= entrada.get()
    txt_nuevo=txt_actual[:-1]
    entrada.delete(0, END)
    entrada.insert(0, txt_nuevo)

#------------------------------------------------------------------------------------------------------------------------------------------V
# EFECTO HOVER
    
class Botton_Hovereado(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.BackGround = self["background"]
        self.bind("<Enter>", self.hover_activado)
        self.bind("<Leave>", self.hover_desactivado)
    
    def hover_activado(self, e):
        self["background"]="#999999"
    def hover_desactivado(self, e):
        self["background"]=self.BackGround

#------------------------------------------------------------------------------------------------------------------------------------------V
# BOTONES
        
    # Fila 0  --------------------------------------------------------------------------------------------------------------------------V
entrada= Entry(ventana,  font=("Calibri", 20), bg="#568f8f", borderwidth=0, width=16)
entrada.grid(row=0,column=0, columnspan=4, padx=0, pady=2, ipadx=1, ipady=3) 

    # Fila 1  --------------------------------------------------------------------------------------------------------------------------v
boton_clear = Botton_Hovereado(ventana, bg="#b3b3b3", text= "C", font="Calibri", width=6, height=2, command= lambda: borrar_todo())
boton_clear.grid(row=1 ,column=0)

boton_del = Botton_Hovereado(ventana, bg="#b3b3b3", text= "Del",font="Calibri", width=6, height=2, command= lambda: borrar_uno())
boton_del.grid(row= 1, column=1)

boton_elevar = Botton_Hovereado(ventana, bg="#b3b3b3", text= "^",font="Calibri", width=6, height=2, command= lambda: click_boton("**") )
boton_elevar.grid(row= 1,column= 2)

boton_divicion=Botton_Hovereado(ventana, bg="#b3b3b3", text="/", font="Calibri", width=6, height=2, command= lambda: click_boton("/"))
boton_divicion.grid(row=1,column=3)

    # Fila 2  --------------------------------------------------------------------------------------------------------------------------v
boton_7 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "7",font="Calibri", width=6, height=2, command= lambda: click_boton("7"))
boton_7.grid(row= 2,column= 0)

boton_8 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "8",font="Calibri", width=6, height=2, command= lambda: click_boton("8"))
boton_8.grid(row= 2,column= 1)

boton_9 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "9",font="Calibri", width=6, height=2, command= lambda: click_boton("9"))
boton_9.grid(row= 2,column= 2)

boton_multiplicar = Botton_Hovereado(ventana, bg="#b3b3b3", text= "X",font="Calibri", width=6, height=2, command= lambda: click_boton("*"))
boton_multiplicar.grid(row= 2,column= 3)

    # Fila 3  --------------------------------------------------------------------------------------------------------------------------v
boton_4 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "4",font="Calibri", width=6, height=2, command= lambda: click_boton("4"))
boton_4.grid(row= 3,column= 0)

boton_5 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "5",font="Calibri", width=6, height=2, command= lambda: click_boton("5"))
boton_5.grid(row= 3,column= 1)

boton_6 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "6",font="Calibri", width=6, height=2, command= lambda: click_boton("6"))
boton_6.grid(row= 3,column= 2)

boton_menos = Botton_Hovereado(ventana, bg="#b3b3b3", text= "-",font="Calibri", width=6, height=2, command= lambda: click_boton("-"))
boton_menos.grid(row= 3,column= 3)

    # Fila 4  --------------------------------------------------------------------------------------------------------------------------v
boton_1 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "1",font="Calibri", width=6, height=2, command= lambda: click_boton("1"))
boton_1.grid(row= 4,column= 0)

boton_2 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "2",font="Calibri", width=6, height=2, command= lambda: click_boton("2"))
boton_2.grid(row= 4,column= 1)

boton_3 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "3",font="Calibri", width=6, height=2, command= lambda: click_boton("3"))
boton_3.grid(row= 4,column= 2)

boton_mas = Botton_Hovereado(ventana, bg="#b3b3b3", text= "+",font="Calibri", width=6, height=2, command= lambda: click_boton("+"))
boton_mas.grid(row= 4,column= 3)

    # Fila 5  --------------------------------------------------------------------------------------------------------------------------v
boton_coma = Botton_Hovereado(ventana, bg="#b3b3b3", text= ",",font="Calibri", width=6, height=2, command= lambda: click_boton(","))
boton_coma.grid(row= 5,column= 0)

boton_0 = Botton_Hovereado(ventana, bg="#b3b3b3", text= "0",font="Calibri", width=6, height=2, command= lambda: click_boton("0"))
boton_0.grid(row= 5, column=1)

boton_raiz= Botton_Hovereado(ventana, bg="#b3b3b3", text= "√",font="Calibri", width=6, height=2, command= lambda: click_boton("√"))
boton_raiz.grid(row= 5,column= 2)

boton_porcentaje = Botton_Hovereado(ventana, bg="#b3b3b3", text= "%",font="Calibri", width=6, height=2, command= lambda: click_boton("%"))
boton_porcentaje.grid(row= 5,column= 3)

    # Fila 6  --------------------------------------------------------------------------------------------------------------------------v
boton_parentesis1 = Botton_Hovereado(ventana, bg="#b3b3b3", text="(", font="Calibri", width=6, height=2, command= lambda: click_boton("("))
boton_parentesis1.grid(row=6 ,column=0)

boton_parentesis2= Botton_Hovereado(ventana, bg="#b3b3b3", text=")", font="Calibri", width=6, height=2, command= lambda: click_boton(")"))
boton_parentesis2.grid(row=6 ,column=1)

boton_igual= Botton_Hovereado(ventana, bg="#b3b3b3", text="=",font="Calibri", width=13, height=2, command= lambda: operacion())
boton_igual.grid(row=6, column=2, columnspan=2)


#--------------------------------------------------------------------V
ventana.mainloop() 