import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("La mia App Tkinter")
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.master, text="Benvenuti in Tkinter!")
        self.label.pack()
        
        self.button = tk.Button(self.master, text="Clicca qui!", command=self.on_click)
        self.button.pack()
        
    def on_click(self):
        self.label.config(text="Hai cliccato il pulsante!")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
