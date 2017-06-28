# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Tkinter import Tk, Label
from ttk import Progressbar

class Suivi:
    def __init__(self, lecteur):
        self.root = Tk()
        self.max = lecteur.getNumPages()
        self.label = Label(self.root, text="Interprétation des pages")
        self.label.pack()
        self.progressbar = Progressbar(self.root, orient='horizontal', length=200, value=0)
        self.progressbar.pack()
        self.root.update()
    def maj(self, avancement):
        self.progressbar['value'] = avancement * 100 / self.max
        self.root.update()