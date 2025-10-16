import tkinter as tk

window = tk.Tk()


window.title("메모장")

window.geometry("400x300")


label = tk.Label(window, text="메모장을 만들어봐요")
label.pack(pady=20) 

window.mainloop()
