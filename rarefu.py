# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import os

from utils.fenetre import Suivi, Suivi
from utils.fichier import choisitFichier, litFichier, parse

os.environ.__setitem__("RAREFU","DE")

lecteur = None
while lecteur == None:
    filename = choisitFichier()
    lecteur = litFichier(filename)

suivi = Suivi(lecteur)

for ipage in range(0, lecteur.getNumPages() - 1):
    if ipage % 10 == 0:
        suivi.maj(ipage + 1)
    parse(lecteur.getPage(ipage))
    print(ipage)



