import tkinter as tk

window=tk.Tk()
window.title("Window Sample")
window.geometry('250x250')

greet=tk.Label(text='Hello',fg="black", bg='white')
button=tk.Button(text='Click Me', bg='black', fg='white')
entry=tk.Entry(fg="yellow", bg="blue", width=50)

greet.pack()
button.pack()
entry.pack()

frame=tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame.pack()
label=tk.Label(master=frame, text='Sample frame')
label.pack()

textbox=tk.Text(fg='green', bg='yellow')
textbox.pack()
window.mainloop()