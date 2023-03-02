import re
import copy
from tkinter import *
#_______________________________________________________________________________
class Reader:
    def __init__(self, FileName):
        self.FileName = FileName

    def ReadFile(self):
        fhd = open(self.FileName)
        self.FileContent = fhd.read()
        fhd.close()

    def PrintFile(self):
        print(self.FileContent)

    def GetFileContent(self):
        return self.FileContent
#_______________________________________________________________________________

reader = Reader('Lönekontot2021.csv')
reader.ReadFile()
reader.PrintFile()
str = reader.GetFileContent()
