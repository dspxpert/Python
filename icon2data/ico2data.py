with open("agilent.ico", "rb") as image:
    a = image.read()
data = (repr(a))
data = data[2:]  #trim out the b'
data = data[:-1]  #trim out the last '
dataList = data.split('\\x')  #split by hex unit
dataList = dataList[1:] #remove the blank  value at the beginning

totalLen = len(dataList)
i = 0
hexline = ''
lenCount = 0
groupCount = 0

fp = open('icon_template.py', 'w')
fp.write('import tkinter as tk\n')
fp.write('from tkinter import ttk\n')
fp.write('import tempfile\n\n')
fp.write('ICON = (')

for hex in dataList:
    if(lenCount == totalLen-1):
        hexline += '\\x' + hex
        #print('b\'' + hexline + '\'')
        fp.write('b\'' + hexline + '\'\n')
    if(i == 16):  #change number of grouping here       
        #print('b\'' + hexline + '\'')
        fp.write('b\'' + hexline + '\'\n')
        i=0
        hexline = ''
        groupCount += 1

    hexline += '\\x' + hex
    i+=1         
    lenCount += 1

fp.write(')\n\n')
fp.write('_, ICON_PATH = tempfile.mkstemp()\n')
fp.write("with open(ICON_PATH, 'wb') as icon_file:\n")
fp.write('    icon_file.write(ICON)\n\n')
fp.write('root = tk.Tk()\n')
fp.write('root.iconbitmap(default=ICON_PATH)\n\n')
fp.write('root.mainloop()\n')
fp.close()
