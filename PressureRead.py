import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def load_data(filepath):
    return pd.read_csv(filepath, sep='\t', header=None, names=['Time', 'Pressure', 'Cycle'])

def filter_by_cycle(df, cycle_number):
    return df[df['Cycle'] == cycle_number]

def update_plot(cycle_number, df, window, canvas, ax):
    df_cycle = filter_by_cycle(df, cycle_number)
    df_cycle['Time'] = df_cycle['Time'] / 1000
    ax.clear()
    ax.plot(df_cycle['Time'], df_cycle['Pressure'], label=f'Cycle {cycle_number}')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Pressure')
    ax.legend()
    canvas.draw()

def load_file(window):
    global df, canvas, ax
    filepath = filedialog.askopenfilename()
    if filepath:
        df = load_data(filepath)
        cycle_numbers = sorted(df['Cycle'].unique())

        # Initialize the plot with the first cycle
        update_plot(cycle_numbers[0], df, window, canvas, ax)

        # Dropdown to select cycle
        cycle_var = tk.IntVar(window)
        cycle_var.set(cycle_numbers[0])
        cycle_dropdown = ttk.Combobox(window, textvariable=cycle_var, values=cycle_numbers)
        cycle_dropdown.grid(row=0, column=1, padx=10)
        cycle_dropdown.bind("<<ComboboxSelected>>", lambda event: update_plot(cycle_var.get(), df, window, canvas, ax))

window = tk.Tk()
window.title("Cycle Data Analysis")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(row=1, column=0, columnspan=3)

toolbar_frame = tk.Frame(window)
toolbar_frame.grid(row=2, column=0, columnspan=3)
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.X)

load_btn = tk.Button(window, text="Load Data", command=lambda: load_file(window))
load_btn.grid(row=0, column=0)

window.mainloop()
