from tkinter import *
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import pandas as pd

class Envelope_Window:

    def __init__(self, master):
        self.frame = Frame(master)
        master.title('Envelope program')
        self.frame.pack(fill=BOTH, expand=1)

        self.instructions = Label(self.frame, text="The file must have two columns:\n 1. wavelengths       2. signal")
        self.instructions.grid(row=0, sticky='N', padx=30)
        self.button_get_filename = Button(self.frame, text="Open", command=self.get_filename)
        self.button_get_filename.grid(row=1, sticky='N')
        self.label_ask_headers = Label(self.frame, text="Does your file contain headers?\nOnly a row of headers is allowed")
        self.label_ask_headers.grid(row=0, column=1, columnspan=2)
        self.header = IntVar()
        self.yes_header = Radiobutton(self.frame, text='Yes', variable=self.header, value=1)
        self.yes_header.grid(row=1, column=1)
        self.no_header = Radiobutton(self.frame, text='No', variable=self.header, value=0)
        self.no_header.grid(row=1, column=2)



        # Test a plot:       
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, master)
        canvas.show()
        canvas.get_tk_widget().grid(row=3)

        toolbar = NavigationToolbar2TkAgg(canvas, master)
        toolbar.update()
        canvas._tkcanvas.pack(side=BOTTOM, fill=BOTH, expand=True)

    def get_filename(self):
        ftypes = [('Excel files', '*.xls*'), ('CSV files', '*.csv')]
        self.filename = filedialog.askopenfilename(filetypes=ftypes, title='Open data files')
        self.filename_selected = Label(self.frame, text='Your file is: {0}'.format(self.filename))
        self.filename_selected.grid(row=2, sticky='N')

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