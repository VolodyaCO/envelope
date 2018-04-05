from tkinter import *
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import pandas as pd
from functools import partial

class Envelope_Window:

    def __init__(self, master):

        # Define the window frame of the program:
        self.frame = Frame(master)
        master.title('Envelope program')
        self.frame.pack(fill=BOTH, expand=1)

        # Print instructions on how to open a file:
        self.instructions = Label(self.frame, text="The file must have two columns:\n 1. wavelengths       2. signal")
        self.instructions.grid(row=0, columnspan=2, sticky='N', padx=30)
        # Display a button that opens a system dialog that allows the selection of the data file:
        self.button_get_filename = Button(self.frame, text="Open", command=self.get_filename)
        self.button_get_filename.grid(row=1, column=0, sticky='N')
        # Start the value of the data file type (will be CSV or XLS/XLSX):
        self.file_type = None
        # Display an initially unactive button that plots the raw data:
        self.button_plot_raw = Button(self.frame, text='Plot data file', command=self.null_command)
        self.button_plot_raw.grid(row=1, column=1, sticky='N')
        # Define variables to store wavelengths and signal values:
        self.lambdas = None
        self.signal = None

    def get_filename(self):
        ftypes = [('Excel files', '*.xls*'), ('CSV files', '*.csv')]
        self.filename = filedialog.askopenfilename(filetypes=ftypes, title='Open data files')
        self.filename_selected = Label(self.frame, text='Your file is: ./{0}'.format(self.filename.split('/')[-1]))
        self.filename_selected.grid(row=2, sticky='N')
        self.file_type = self.filename.split('.')[-1]
        self.open_datafile(self.filename)

    def open_datafile(self, filename):
        if self.file_type.lower() == 'csv':
            df = pd.read_csv(filename)
        else:
            df = pd.read_excel(filename)
        self.lambdas = df[df.columns[0]].values
        self.signal = df[df.columns[1]].values
        # Activate button that plots the raw data:
        plot = partial(self.plot, xdata=[self.lambdas], ydata=[self.signal])
        self.button_plot_raw.configure(command = plot)

    def plot(self, xdata, ydata):
        """
        Arguments:
        xdata -> List containing N arrays. The i-th array has length M_i
        ydata -> same as xdata
        Function:
        Plot the data in a new window.
        """

        # Define a figure object:
        f = Figure(figsize=(5,5), dpi=100)
        # Define an axis object:
        a = f.add_subplot(111)
        # Plot the data on the axis object:
        for x, y in zip(xdata, ydata):
            a.plot(x, y)
        # Open a new window to display the plot:
        window = Toplevel(self.frame)
        canvas = FigureCanvasTkAgg(f, window)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        # Add the matplotlib toolbar to manipulate the plot online:
        toolbar = NavigationToolbar2TkAgg(canvas, window)
        toolbar.update()
        canvas._tkcanvas.pack(side=BOTTOM, fill=BOTH, expand=True)
    def null_command(self):
        pass

def main():
    root = Tk()
    ewindow = Envelope_Window(root)
    root.geometry("600x250+300+300")
    root.mainloop()
    try:
        root.destroy()
    except:
        pass

if __name__ == '__main__':
    main()