import tkinter

window = tkinter.Tk()
window.title("Mile to Km converter")
window.config(padx=20,pady=20)

km = 0
my_label = tkinter.Label(text="Miles", font=("Arial", 15))
my_label.grid(column=2, row=0)

mile_input= tkinter.Entry(width=8, font=("Arial", 15))
mile_input.grid(column=1, row=0)

my_label_2 = tkinter.Label(text=f"is equal to ", font=("Arial", 15))
my_label_2.grid(column=0, row=1)

my_label_3 = tkinter.Label(text=f"{km}",width=8, font=("Arial", 15))
my_label_3.grid(column=1,row=1)

my_label_4 = tkinter.Label(text="Km", font=("Arial", 15))
my_label_4.grid(column=2,row=1)

def button_clicked():
    my_label_3.config(text=f"{float(mile_input.get())*1.609:.2f}")

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()