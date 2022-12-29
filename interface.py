from tkinter import *
from math import *
from buttons_operations import input_filter, returning

op = []


def displayed(num: str):
    """
    Fonction qui modifie l'affichage à l'écran
    :param num: ce qui sera affiché (sélectionné parmi les boutons)
    :return:
    """
    output_text = ""

    if num != '=':
        op.append(num)

    if num == 'C':
        op.clear()

    for i in range(len(op)):
        output_text += op[i]
    output.config(text=output_text)

    if num == '=':
        if str(returning()[0]).endswith('.0'):
            print(returning()[0], 'is an integer')
            output.config(text=int(returning()[0]))
            to_add = int(returning()[0])
        else:
            output.config(text=returning()[0])
            to_add = returning()[0]
        op.clear()
        op.append(str(to_add))

        input_filter(str(returning()[0]))

        returning().pop(0)


# Création de l'interface

calc = Tk()

calc.title("Calculatrice")

calc.minsize(230, 210)
calc.maxsize(230, 210)

output = Label(calc, text="", width=25, height=3, borderwidth=3, bg="white")
output.grid(row=0, column=0, columnspan=4)

# Création des boutons

bouton0 = Button(calc, text="0", command=lambda: [displayed('0'), input_filter('0')])
# bouton0.pack(side=BOTTOM, pady=5)
bouton0.grid(row=5, column=0, columnspan=2, ipadx=30)
bouton1 = Button(calc, text="1", command=lambda: [displayed('1'), input_filter('1')])
# bouton1.pack(side=LEFT, pady=5)
bouton1.grid(row=4, column=0)
bouton2 = Button(calc, text="2", command=lambda: [displayed('2'), input_filter('2')])
# bouton2.pack(side=BOTTOM, pady=5)
bouton2.grid(row=4, column=1)
bouton3 = Button(calc, text="3", command=lambda: [displayed('3'), input_filter('3')])
# bouton3.pack(side=RIGHT, pady=5)
bouton3.grid(row=4, column=2)
bouton4 = Button(calc, text="4", command=lambda: [displayed('4'), input_filter('4')])
# bouton4.pack(side=LEFT, pady=5)
bouton4.grid(row=3, column=0)
bouton5 = Button(calc, text="5", command=lambda: [displayed('5'), input_filter('5')])
# bouton5.pack()
bouton5.grid(row=3, column=1)
bouton6 = Button(calc, text="6", command=lambda: [displayed('6'), input_filter('6')])
# bouton6.pack(side=RIGHT, pady=5)
bouton6.grid(row=3, column=2)
bouton7 = Button(calc, text="7", command=lambda: [displayed('7'), input_filter('7')])
# bouton7.pack(side=LEFT, pady=5)
bouton7.grid(row=2, column=0)
bouton8 = Button(calc, text="8", command=lambda: [displayed('8'), input_filter('8')])
# bouton8.pack()
bouton8.grid(row=2, column=1)
bouton9 = Button(calc, text="9", command=lambda: [displayed('9'), input_filter('9')])
# bouton9.pack(side=RIGHT, pady=5)
bouton9.grid(row=2, column=2)
bouton_point = Button(calc, text=".", command=lambda: [displayed('.'), input_filter('.')])
# bouton_point.pack(side=BOTTOM, pady=5)
bouton_point.grid(row=5, column=2)

bouton_plus = Button(calc, text="+", command=lambda: [displayed('+'), input_filter('+')])
# bouton_plus.pack()
bouton_plus.grid(row=4, column=3)
bouton_moins = Button(calc, text="-", command=lambda: [displayed('-'), input_filter('-')])
# bouton_moins.pack()
bouton_moins.grid(row=3, column=3)
bouton_fois = Button(calc, text="*", command=lambda: [displayed('*'), input_filter('*')])
# bouton_fois.pack()
bouton_fois.grid(row=2, column=3)
bouton_divise = Button(calc, text="/", command=lambda: [displayed('/'), input_filter('/')])
# bouton_divise.pack()
bouton_divise.grid(row=1, column=3)
bouton_egal = Button(calc, text="=", command=lambda: [input_filter('='), returning(), displayed('=')])
# bouton_egal.pack()
bouton_egal.grid(row=5, column=3)
bouton_puissance = Button(calc, text="^", command=lambda: [displayed('^'), input_filter('^')])
# bouton_puissance.pack()
bouton_puissance.grid(row=1, column=2)

boutonC = Button(calc, text='C', command=lambda: [displayed('C'), input_filter('C')])
# boutonC.place(x=250, y=60)
boutonC.grid(row=1, column=0, columnspan=2, ipadx=30)

calc.mainloop()
