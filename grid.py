import tkinter as tk
window=tk.Tk()

for i in range(3):
  for j in range(3):
    frame = tk.Frame(
      master=window, #frame is a container 
      relief=tk.RAISED, #widgets
      borderwidth=1
    )
    frame.grid(row=i, column=j, padx=5, pady=5)
    label=tk.Label(master=frame, text=f"Row{i}\nColumn{j}")
    label.pack()
    
window.mainloop()