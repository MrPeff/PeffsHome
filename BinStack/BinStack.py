import re

f = open("map3.txt", "r")
IdxFileText = f.read()
p1 = re.compile(r'EYECATCH\s*?(.*?)endprotecteddata', re.DOTALL)
p2 = re.compile(r'([0-9,A-F,a-f]{8})\s(.*)')
IdxFuncsText = p1.findall(IdxFileText)
text = IdxFuncsText[0]

IdxListAddrAndFunc = p2.findall(text)

FuncAddr = [0 for i in range(0,len(IdxListAddrAndFunc))]
FuncName = [0 for i in range(0,len(IdxListAddrAndFunc))]
i = 0
for i, tuple in enumerate(IdxListAddrAndFunc):
    #print(tuple)
    FuncAddr[i] = int(tuple[0], 16)
    FuncName[i] = tuple[1]
    i = i + 1

#print(*MapList, sep = "\n")
#raise SystemExit(0) 

f = open("stack3.txt", "r")
Stack_text = f.read()
Stack_text = Stack_text.replace(u'\xa0', u'') #remove "No-Break Space"
Stack_text = Stack_text.replace(u',', '.')    #change , to .
f.close()

p = re.compile(r'[0-9,A-F]{8}|\b[0-9,A-F]{8}\b[0-9,A-F]{8}\b[0-9,A-F]{8}\b[0-9,A-F]{8}.*?')
StackDumpLine = p.findall(Stack_text)
#print(StackDumpLine)

StackDumpLine_len = len(StackDumpLine)
NoOfStackEntries = 4 * (StackDumpLine_len//5)
StackAddr = [0 for i in range(0,NoOfStackEntries)]
StackData = [0 for i in range(0,NoOfStackEntries)]

j = 0
for i in range(0,StackDumpLine_len,5):
  StackAddr[j]   =  int(StackDumpLine[i], 16)
  StackAddr[j+1] = StackAddr[j]+4
  StackAddr[j+2] = StackAddr[j]+8
  StackAddr[j+3] = StackAddr[j]+12
  StackData[j]   = int(StackDumpLine[i+1], 16)
  StackData[j+1] = int(StackDumpLine[i+2], 16)
  StackData[j+2] = int(StackDumpLine[i+3], 16)
  StackData[j+3] = int(StackDumpLine[i+4], 16)
  j = j + 4

#print(StackAddr)
#print(StackData)

print("Searching")

for i in range(0, len(StackData)-1):
  found = 0
  if i%4 == 0:
    print("\n{0:>10X} {1:>10X} {1:>10X} {1:>10X} {1:>10X} "\
      .format(StackAddr[i], StackData[i], StackData[i+1], StackData[i+2], StackData[i+3]), end='')
  for j in range(0, len(FuncAddr)-5):
    if (FuncAddr[j] <= StackData[i]) and (StackData[i] < FuncAddr[j+1]):
      found = 1
      print("{0:<30}".format(FuncName[j]), end='')
      break
  if found == 0:
    print("{0:<30}".format(" "), end='')
      
      
  






#______________________________________________________________________________
# Extract the transactions into tuples and compute the sum
# text -> Transactions List of Tuples:(text,  belopp)
#p = re.compile(r'.*?\t(.*?)\t(.*?)\t.*?')
#Transactions = p.findall(ek_text)
#print(Transactions)