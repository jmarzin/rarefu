# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from Tkinter import Tk
from tkFileDialog import askopenfilename

import PyPDF2
import os

from appJar import gui


def choisitFichier():
    if os.environ.__getitem__("RAREFU") == "DEV":
        return "LISTES_juin_2017.pdf"
    root = Tk()
    root.withdraw()
    root.update()
    resultat = askopenfilename(filetypes=[("fichiers pdf", "*.pdf")], title="Sélctionnez le fichier à traiter")
    root.update()
    if resultat == '':
        sys.exit(0)
    else:
        return resultat

def litFichier(filename):
    pdf_file = PyPDF2.PdfFileReader(filename)
    page0 = pdf_file.getPage(0)
    if "RAREFU20" in page0.extractText():
        return pdf_file
    else:
        app = gui()
        app.infoBox("Erreur","Le fichier choisit n'est pas un fichier RAREFU.")
        return None
def parse(page):
    texte = page.extractText()
    pass