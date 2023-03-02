
import re

FileNameStack = r'D:\Dev\Problem3\Bug 47095 PM866 IP\SU LOG 20170205\BinStack.txt'
FileNameIdx   = r'D:\Dev\Problem3\Bug 47095 PM866 IP\SU LOG 20170205\559f035294.idx'
f_Stack = open(FileNameStack, "r")
f_Idx   = open(FileNameIdx,   "r")
text_Stack = f_Stack.read()
text_Idx   = f_Idx.read()

Lines = re.split('\|', text_Stack)
print(Lines)


