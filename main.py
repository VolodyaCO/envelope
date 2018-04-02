from tkinter import *
from tkinter import filedialog

class Envelope_Window:

    def __init__(self, master):
        self.frame = Frame(master)
        master.title('Envelope program')
        self.frame.pack(fill=BOTH, expand=1)

        self.instructions = Label(self.frame, text="The file must have two columns:\n 1. wavelengths\n 2. signal\nEach column must have a text header")
        self.instructions.grid(row=0, sticky='W')
        self.button_time = Button(self.frame, text="Open", command=self.open_file)
        self.button_time.grid(row=1, sticky='N')

    def open_file(self):
        ftypes = [('Excel files', '*.xls*'), ('CSV files', '*.csv'), ('All files', '*')]
        dlg = filedialog.askopenfilename(filetypes=ftypes, title='Open data files')

def main():
    root = Tk()
    ewindow = Envelope_Window(root)
    root.geometry("300x250+300+300")
    root.mainloop()
    try:
        root.destroy()
    except:
        pass

if __name__ == '__main__':
    main()