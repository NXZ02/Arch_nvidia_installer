#################################
from tkinter import *
from PIL import Image, ImageTk # import lib 
import os
import tkinter.messagebox
from customtkinter import *
################################

# config 
root = CTk()
# size windows
root.geometry("600x500")

# title
root.title("Nvidia Installler")

#  not resize windows
root.resizable(width=False, height=False)

################## # Funtion exit gui

def Cilck_exit():
	root.destroy()

####################
############### Backgournd image

img  = Image.open("n2.png") 
# resize img to 600x500
resize_image = img.resize((1000, 500))
#  ....
photo=ImageTk.PhotoImage(resize_image)
# show img in programe
lab=Label(image=photo) .pack()  # center 

############################
def install_pass():
    tkinter.messagebox.showinfo("Message","Install Finish reboot you computer ")
############################

logo_img = Image.open("logo.png")
resize_logo = logo_img.resize((50, 50))  # Adjust size as needed
logo_photo = ImageTk.PhotoImage(resize_logo)
logo_label = Label(root, image=logo_photo)
logo_label.place(x=520, y=10)  # Adjust position as needed


#######################################################
#button_img = Image.open("next1.png")
#resize_button_img = button_img.resize((150, 45))
#button_photo = ImageTk.PhotoImage(resize_button_img)
###########################3#########################


########################################### create frame gui
frame = Frame(root, bd=2, relief="groove")
frame.place(x=80, y=100)
############################################

Head = Label(root,text="NVIDIA Graphics Driver",fg="green",font=("Helvetica", 12)) .place(x=5,y=5)
lowHead = Label(root,text="Version Arch Linux",fg="green",font=("Helvetica", 12)) .place(x=5,y=30)

TextFrame = Label(frame, text=" NVIDIA Graphics Driver", fg="green", font=("Helvetica", 12))
TextFrame.pack(padx=30,pady=40)

TextFrame1 = Label(frame, text="            ", fg="green", font=("Helvetica", 12))
TextFrame1.pack(padx=30,pady=100)

#create_button = Button(root,text="HELLO") .place(x=90,y=60)
#create_button = Button(root, image=button_photo) .place(x=400,y=400)
#create_exit = Button(root,text="EXIT",command=Cilck_exit) .place(x=300,y=425)

def Check():
    tkinter.messagebox.askquestion("Message","Confirm Yes/No")

def INSTALL(): # funtion choice nvidia driver 
    r = int(text.get())
    r2 = int(text2.get())
    r3  = int(text3.get()) 
    r4 = int(text4.get())
    r5 = int(text5.get())
    SUM = r + r2 + r3 + r4 + r5
    if SUM != 1:
        tkinter.messagebox.showerror("Message ERROR","Please select only 1 option.")
    elif r == 1:
        Check()
        root.destroy()
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-340xx-dkms nvidia-340xx-utils lib32-nvidia-340xx-utils nvidia-settings --noconfirm")
        install_pass()
    elif r2 == 2:
        Check()
        root.destroy()
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-390xx-dkms nvidia-390xx-utils lib32-nvidia-390xx-utils nvidia-settings --noconfirm")
        install_pass()
    elif r3 == 3:
        Check()
        root.destroy()
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-470xx-dkms nvidia-470xx-utils lib32-nvidia-470xx-utils nvidia-settings --noconfirm")
        install_pass()
    elif r4 == 4:
        Check()
        root.destroy()
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-525xx-dkms nvidia-525xx-utils lib32-nvidia-525xx-utils nvidia-settings --noconfirm")
        install_pass()
    elif r5 == 5:
        Check()
        root.destroy()
        os.system("sudo pacman -S base-devel linux-headers git nano --needed --noconfirm")
        os.system("yay -S nvidia-535xx-dkms nvidia-535xx-utils lib32-nvidia-535xx-utils nvidia-settings --noconfirm")
        install_pass()


    

text = IntVar()
text2 = IntVar()
text3 = IntVar()
text4 = IntVar()
text5 = IntVar()

xin = 90 # x = 90


############################################ NXZ02 ###############################################
 #                                  
 #                                * NVIDIA GRAPHICS DRIVER   * 
 #
##################################################################################################
CTkCheckBox(master=root, text="340xx",fg_color="green",corner_radius=36, onvalue=1,offvalue=0,variable=text) .place(relx=0.3, rely=0.4 ,anchor="center")
CTkCheckBox(master=root, text="390xx",fg_color="green",corner_radius=36, onvalue=1,offvalue=0,variable=text2) .place(relx=0.3, rely=0.5 ,anchor="center")
CTkCheckBox(master=root, text="470xx",fg_color="green",corner_radius=36, onvalue=1,offvalue=0,variable=text3) .place(relx=0.3, rely=0.6 ,anchor="center")
CTkCheckBox(master=root, text="525xx",fg_color="green",corner_radius=36, onvalue=1,offvalue=0,variable=text4) .place(relx=0.3, rely=0.7 ,anchor="center")
CTkCheckBox(master=root, text="535xx",fg_color="green",corner_radius=36, onvalue=1,offvalue=0,variable=text5) .place(relx=0.3, rely=0.8 ,anchor="center")
CTkButton(master=root, text="Install",border_color="black",fg_color="green",border_width=2, hover_color="black",command=INSTALL) .place(x=450,y= 400)
##################################################################################################

##########################################   END #################################################




root.mainloop()
