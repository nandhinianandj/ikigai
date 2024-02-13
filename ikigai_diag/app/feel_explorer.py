# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : feel_explorer.py
#
#* Purpose :
#
#* Creation Date : 14-01-2023
#
#* Last Modified : Saturday 14 January 2023 01:09:45 PM
#
#* Created By : Yaay Nands
#_._._._._._._._._._._._._._._._._._._._._.#
import pysolr
import PyPDF2
import re
import os
import glob

PMOT_DIR = '/home/nands/Dropbox/Notes/personal/lwp_stuff/PMOTs'
print(files)
def read_pdf_files(file):
    reader = PyPDF2.PdfFileReader(open(files[0], "rb"))
    print(reader.numPages)
    for page in reader.pages:
        text = page.extractText()
        print(text)


def main():
    files = glob.glob(os.path.join(PMOT_DIR, '*.pdf'))
    texts = dict()
    for i,fil in enumerate(files):
        texts["PMOT"+ str(i)] = read_pdf_files(files)




