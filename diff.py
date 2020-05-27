import difflib
import wasabi
from colorama import init 
from termcolor import colored 
import shutil
import tkinter as tk
from tkinter import filedialog

init() 
center_point = shutil.get_terminal_size().columns   #screen center point
root = tk.Tk()
root.withdraw()
count =0;

print("SELECT FIRST FILE");
file_path = filedialog.askopenfilename()
file1 = open(file_path, 'r')

print("SELECT SECOND FILE");

file_path = filedialog.askopenfilename()
file2 = open(file_path, 'r')

diff = difflib.context_diff(file1.readlines(), file2.readlines())
delta = ''.join(diff)
# print (delta)

print('###########################################################################')

delta = "".join(str(x) for x in delta)
fname = ""
delta = delta.split("***************");
for line in delta:
    if ("*** ") in line:
        fname = "FILE 1 -> "+ file1.name +"\n Line: ";
        var = line.replace("*** ", colored(fname, 'green') )

    if ("--- ") in var:
        fname = "FILE 2 -> "+ file2.name +"\n Line: ";
        var = var.replace("--- ", colored(fname, 'green') )

    if ("! ") in var:
        var = var.replace("! ", colored("! ", 'green', 'on_red') )

    if ("- ") in var:
        var = var.replace("- ", colored("- ", 'red') )
    count =count+1;
    print(colored('---------------------------------------------------------------------------------------------------------'.center(center_point), 'red')) 
    print(colored("NEW Change found".center(center_point),'red'))
    print(colored('---------------------------------------------------------------------------------------------------------'.center(center_point), 'red')) 
    print(var)



print(colored('Hello, World!', 'green', 'on_red')) 

