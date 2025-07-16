#!/usr/bin/python3
from tkinter import *
import pyopenms as oms

class Decomposer:
    def __init__(self):
        self.master = Tk()
        self.master.title("Mass Decomposer")
        self.mass = 0
        self.tol = 0
        self.namelist = ['Mass (m/z)', 'Tolerance (m/z)']
        self.entry_boxes = []
        for x, name in enumerate(self.namelist):
            labels = Label(self.master, text=name)
            labels.grid(column=x, row=0)
            entry_box = Entry(self.master)
            entry_box.grid(column=x, row=1, pady = 2, padx=2)    
            self.entry_boxes.append(entry_box)
        self.output = Text(self.master,
                           height=10,
                           width=30)
        self.output.grid(row=2, column=0, columnspan=2, pady=4, padx=5)
        scroll = Scrollbar(self.master, orient='vertical', command=self.output.yview)
        scroll.grid(row=0, column=1, sticky='ns')
        self.output['yscrollcommand'] = scroll.set
        scroll.grid(row=2, column=2, sticky=N+S+W)
        ok_button = Button(self.master, text = "OK", command=self.calculate, width=10)
        ok_button.grid(row = 4, column = 0, rowspan=2, pady = 4, padx=5)
        self.warnlabel = Label(self.master, text=(""))
        self.warnlabel.grid(row = 4, column = 1, sticky = W)
        self.master.bind('<Return>', self.calculate)
        
        self.master.mainloop()
        
    def calculate(self, *args):
        self.output.delete('1.0', END)
        self.warnlabel.configure(text="")
        try:
            self.mass = float(self.entry_boxes[0].get()) 
            self.tol = float(self.entry_boxes[1].get())
        except ValueError:
            self.warnlabel.configure(text="Please enter values!")
            return None
        
        md_alg = oms.MassDecompositionAlgorithm()
        param = md_alg.getParameters()
        param.setValue("tolerance", self.tol)
        param.setValue("residue_set", b"Natural20")
        md_alg.setParameters(param)
        decomps = []
        md_alg.getDecompositions(decomps, self.mass)
        if decomps:
            for d in decomps:
                self.output.insert(END, d.toExpandedString() + '\n')
                pass
        else:
            self.output.insert(END, "No AA found")
        
if __name__ == "__main__":            
    calc = Decomposer()