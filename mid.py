import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

window.title("메모장")

window.geometry("600x400") 


current_file_path = None


def new_file():
    global current_file_path
    text_area.delete("1.0", "end")
    window.title("메모장")
    current_file_path = None


def open_file():
    global current_file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    
    text_area.delete("1.0", "end")
    with open(file_path, "r", encoding="utf-8") as file:
        text_area.insert("1.0", file.read())
    
    current_file_path = file_path
    window.title(f"메모장 - {file_path}")

def save_file():
    global current_file_path

    if current_file_path is None:
        save_as_file()
    else:
        with open(current_file_path, "w", encoding="utf-8") as file:
            content = text_area.get("1.0", "end-1c")
            file.write(content)
        window.title(f"메모장 - {current_file_path}")

def save_as_file():
    global current_file_path
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    
    with open(file_path, "w", encoding="utf-8") as file:
        content = text_area.get("1.0", "end-1c")
        file.write(content)
    
    current_file_path = file_path
    window.title(f"메모장 - {file_path}")

menu_bar = tk.Menu(window)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="새로 만들기", command=new_file)
file_menu.add_command(label="열기...", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_command(label="다른 이름으로 저장...", command=save_as_file)
file_menu.add_separator() 
file_menu.add_command(label="종료", command=window.quit) 
menu_bar.add_cascade(label="파일", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="실행 취소", command=lambda: text_area.edit_undo())
edit_menu.add_command(label="다시 실행", command=lambda: text_area.edit_redo())
edit_menu.add_separator()
edit_menu.add_command(label="잘라내기", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="복사", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="붙여넣기", command=lambda: text_area.event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="모두 선택", command=lambda: text_area.tag_add("sel", "1.0", "end"))
menu_bar.add_cascade(label="편집", menu=edit_menu)

window.config(menu=menu_bar)

text_area = tk.Text(window, wrap="word", undo=True)
text_area.pack(expand=True, fill='both', padx=5, pady=5)

window.mainloop()

