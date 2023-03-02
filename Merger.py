import re
import copy
from tkinter import *

P_debug = 0
#_______________________________________________________________________________
class Reader:
    def __init__(self, FileName):
        self.FileName = FileName
    def ReadFile(self):
        try:
            fhd = open(self.FileName)
            self.FileContent = fhd.read()
        except IOError:
            print("Cannot open file: ", self.FileName)
            self.FileContent = ""
            exit(2)
        else:
            fhd.close()
    def PrintFile(self):
        print(self.FileContent)
    def GetFileContent(self):
        return self.FileContent
#_______________________________________________________________________________
class StringHandler:
    def __init__(self, Str):
        self.Str = Str
        self.Strings = self.Str.split('\n')
    def SetPrefix(self, Prefix):
        self.Strings = [Prefix + ': ' + s for s in self.Strings]
    def GetStrings(self):
        return self.Strings
#_______________________________________________________________________________
def GetSortKey(str):
    return str[7:32]
#_______________________________________________________________________________
def main():
    #___________________________________________________________________________
    # Read and check arguments
    NoOfArgs = len(sys.argv) - 1;
    if (NoOfArgs == 0) or (NoOfArgs %2 != 0):
        print("Usage: prefix1 file1 prefix2 file2 ...")
        exit(1)
    # Get prefixes and filenames from command line
    Prefixes = []
    CmdLine_PrefixIdx = range(1,len(sys.argv),2)
    for x in CmdLine_PrefixIdx:
        Prefixes.append(sys.argv[x][0:3])
    print("prefixes:", Prefixes)
    Filenames = []
    CmdLine_FileIdx = range(2,len(sys.argv),2)
    for x in CmdLine_FileIdx:
        Filenames.append(sys.argv[x])
    print("Filenames:", Filenames)
    #___________________________________________________________________________
    # Read all file contents and put in StringHandler array
    SH = []
    i = 0;
    for x in Filenames:
        reader = Reader(x)
        reader.ReadFile()
        sh = StringHandler(reader.GetFileContent())
        sh.SetPrefix(Prefixes[i])
        i += 1
        SH.append(sh)
    #___________________________________________________________________________
    # Put all strings in an array and do the sorting
    AllStrings = []
    for x in SH:
        AllStrings.extend(x.GetStrings())
    AllStringsSorted = sorted(AllStrings, key=GetSortKey)
    [print(i) for i in AllStringsSorted]
#_______________________________________________________________________________
if __name__ == '__main__':
    main()
#_______________________________________________________________________________
