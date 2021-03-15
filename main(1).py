# ---------------------------|importing libs|-------------------------------#
import time
import os
import colorama
from colorama import Fore as F 
from colorama import init
import pyfiglet 
import sys
#---------------------------|starting|---------------------------------------#
a="""    _    ____ ____ ___ ___      _    ____ _____   _____ ___   ___  _     ____
   / \  / ___/ ___|_ _|_ _|    / \  |  _ \_   _| |_   _/ _ \ / _ \| |   / ___|
  / _ \| |  | |    | | | |    / _ \ | |_) || |     | || | | | | | | |   \___ |
 / ___ \ |__| |___ | | | |   / ___ \|  _ < | |     | || |_| | |_| | |___ ___) |
/_/   \_\____\____|___|___| /_/   \_\_| \_\|_|     |_| \___/ \___/|_____|____/ """

def banner():
    os.system("cls"or"clear")
    print("\n \t starting ..... \t \n")
    time.sleep(3)
    print(F.GREEN+a)
    print("\n")
    out_put()
#-----------------------|function for out put and fonts|--------------------------#
def out_put():
    user_input_text=input(F.RED+"[ + ]  please enter your text here : " )
    user_input_font=input(" [ + ] ok please enter font name  here : ")
    print(F.WHITE+"ok please let us to make it ,it will save on screen in the one txt file and will show here !")
    time.sleep(6)
    #--------------condithion for standard font--------------#
    if user_input_font == "standard ":
        resualt=pyfiglet.figlet_format(user_input_text)
        print(f" your text will be this : \n \n \n{resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #--------------------condition for slant font-----------#
    if user_input_font == "slant":
        resualt=pyfiglet.figlet_format(user_input_text,font="slant")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for 3-d font -------------------#
    if user_input_font == "3-d":
        resualt=pyfiglet.figlet_format(user_input_text,font="3-d")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for 3x5 font -------------------#
    if user_input_font == "3x5":
        resualt=pyfiglet.figlet_format(user_input_text,font="3x5")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for 5lineoblique  font -------------------#
    if user_input_font == "5lineoblique":
        resualt=pyfiglet.figlet_format(user_input_text,font="5lineoblique")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for alphabet  font -------------------#
    if user_input_font == "alphabet":
        resualt=pyfiglet.figlet_format(user_input_text,font="alphabet")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for doh  font -------------------#
    if user_input_font == "doh":
        resualt=pyfiglet.figlet_format(user_input_text,font="doh")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for isometric   font -------------------#
    if user_input_font == "isometric":
        resualt=pyfiglet.figlet_format(user_input_text,font="isometric1")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for letters   font -------------------#
    if user_input_font == "letters":
        resualt=pyfiglet.figlet_format(user_input_text,font="letters")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for alligator   font -------------------#
    if user_input_font == "alligator":
        resualt=pyfiglet.figlet_format(user_input_text,font="alligator")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for dotmatrix   font -------------------#
    if user_input_font == "dotmatrix":
        resualt=pyfiglet.figlet_format(user_input_text,font="dotmatrix")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for bubble   font -------------------#
    if user_input_font == "bubble":
        resualt=pyfiglet.figlet_format(user_input_text,font="bubble")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for bulbhead   font -------------------#
    if user_input_font == "bulbhead":
        resualt=pyfiglet.figlet_format(user_input_text,font="bulbhead")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
    #-----------------------------condition for digital   font -------------------#
    if user_input_font == "digital":
        resualt=pyfiglet.figlet_format(user_input_text,font="digital")
        print(f" your text will be this : \n \n \n {resualt}")
        with open("your_text.txt",mode="a") as file:
            file.write(resualt)
        os.system("start your_text.txt")
#-------------------------------------|preveiwe function|-----------------------------#
def pre_veiw():
    os.system("cls")
    time.sleep(3)
    print("ok please whait 3 secound \n we want to write all fonts in one text ,file will be save  on screen !")
    time.sleep(3)
    preview_text="alone"
    with open("./TEXT.txt",mode="a") as file :
        
        file.write("ok this is all of fonts we can made it for you \n \n ")
        file.write("this font name is : standard \n ")
        file.write(pyfiglet.figlet_format(preview_text))
        file.write("\n \n \n")
        file.write("this font name is : slant \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="slant"))
        file.write("\n \n \n")
        file.write("this font name is : 3-d \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="3-d"))
        file.write("\n \n \n")
        file.write("this font name is : 3x5 \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="3x5"))
        file.write("\n \n \n")
        file.write("this font name is : 5lineoblique \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="5lineoblique"))
        file.write("\n \n \n")
        file.write("this font name is : alphabet \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="alphabet"))
        file.write("\n \n \n")
        file.write("this font name is : doh \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="doh"))
        file.write("\n \n \n")
        file.write("this font name is : isometric \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="isometric1"))
        file.write("\n \n \n")
        file.write("this font name is : letters \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="letters"))
        file.write("\n \n \n")
        file.write("this font name is : alligator \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="alligator"))
        file.write("\n \n \n")
        file.write("this font name is : dotmatrix \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="dotmatrix"))
        file.write("\n \n \n")
        file.write("this font name is : bubble \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="bubble"))
        file.write("\n \n \n")
        file.write("this font name is : bulbhead \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="bulbhead"))
        file.write("\n \n \n")
        file.write("this font name is : digital \n ")
        file.write(pyfiglet.figlet_format(preview_text,font="digital"))
    user_start_text=input(" Do you want to start it ?(y/n)")
    if user_start_text == "y":
        os.system("start TEXT.txt ")
    if user_start_text == "n":
        print('ok returning you to the main menue.......')
        time.sleep(5)
#------------------------------------------|help function|----------------------------------------#
def show_help():
    time.sleep(2)
    os.system("cls"or "clear")
    time.sleep(0.2)
    print(F.GREEN+a)
    print(F.LIGHTRED_EX+"ok let me think how can i explane  it for you ,wait 3 secound ")
    time.sleep(3)
    print(F.LIGHTRED_EX+"for knowing the fonts name you must restart tool and enter -w")
    time.sleep(3)
    print(F.LIGHTRED_EX+" for using fonts go to the TEXT.txt and copy the name of font and enterd at the secound entry !")
#----------------------------------|loop for free working tool until user want|----------------------#
while True:
    
    User_start_veiw_help_command= input(F.CYAN+"for start input -s for preweiv enter -w and for help how to use enter --h:")
    if os.name == "nt":
        init()
    if os.name == "posix":
        pass
    if User_start_veiw_help_command == "-w":
        pre_veiw()
    if User_start_veiw_help_command == "-s":
        banner()
    if User_start_veiw_help_command == "--h":
        show_help()
    
    
            
#--------------------------------------------GOOD luck ----------------------------------------------#

