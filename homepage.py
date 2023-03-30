import tkinter as tk
 
class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
 
         
        ###MENU FRAME
        left_frame = tk.Frame(root, borderwidth=1, bg= "white", relief="solid", highlightthickness=2)
        left_frame.pack(side="left", expand=False, fill="y")
        container = tk.Frame(left_frame, borderwidth=1, bg= "white", relief="solid")
        container.pack(expand=True, fill="both", padx=5, pady=5)
        btn_1 = tk.Button(container, text="Home")
        btn_1.pack(padx=20, pady=20)
        btn_2 = tk.Button(container, text="Page One")
        btn_2.pack(padx=20,pady=20)
         
        ###TOP
        right_frame = tk.Frame(root, borderwidth=1, bg= "white", relief="solid", highlightthickness=2)
        right_frame.pack(side="right", expand=True, fill="both")
        top_box = tk.Frame(right_frame, borderwidth=1, bg= "white", relief="solid")
        top_box.pack(expand=True, fill="both", padx=10, pady=10)
        label_top = tk.Label(top_box, text="Title Logo", bg= "white")
        label_top.pack()
         
        ###BOTTOM
        bottom_box = tk.Frame(right_frame, borderwidth=1, bg= "white", relief="solid")
        bottom_box.pack(expand=True, fill="both", padx=10, pady=10)
 
         
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x650")
    MainApp(root).pack(side="top", fill="both", expand=True)
    root.mainloop()