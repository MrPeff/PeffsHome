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

def GetSortKey(str):
    return str[30:35]


def main():
    reader = Reader('test_merge_1.txt')
    reader.ReadFile()
    file1 = reader.GetFileContent()
    reader = Reader('test_merge_2.txt')
    reader.ReadFile()
    file2 = reader.GetFileContent()
    print(file1)
    print(file2)
    file3 = file1 + file2
    str = file3.split('\n')
    PList = ['PM: ' + s for s in str]
    [print(i) for i in PList]
    NyLista = sorted(PList, key=GetSortKey)
    [print(i) for i in NyLista]



if __name__ == '__main__':
    main()
