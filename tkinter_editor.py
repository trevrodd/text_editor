import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font="Helvetica 16")
    text_edit.grid(row=0, column=1)


    window.mainloop()






main()