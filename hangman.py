from tkinter import *
import random
from PIL import ImageTk,Image
from tkinter import messagebox
W=Tk()
W.title("H A N G M A N")
W.geometry("490x490")#size of window as (length X breadth) in units of number of pixels
W.resizable(0,0)
L1=Label(W,text="Press start button to play").grid(row=5,column=1)
z=Image.open("guess the word1.jpg")
new=z.resize((350,250))
image1=ImageTk.PhotoImage(new)
label1=Label(image=image1)
label1.image=image1
Label(text="HANGMAN").place(x=150,y=10)
label1.grid(row=0,column=0,columnspan=4)
f=1 # variable that indicates level
a = [0, 1, 2] #will be used to access elements of the lists of clues and words
clues = ["A VEHICLE THAT HAS FOUR WHEELS", "WHAT SOUND DOES A CAT MAKE ??", "NAME OF A METAL"]#list of clues
words = ["car", "meow", "iron"]# list of words
#clue in list(clues) corresponds to word in list(words) if both have the same index in their respective lists
V1=StringVar()# creating 6 string variables to be displayed as text in label widgets
V2=StringVar()
V3=StringVar()
V4=StringVar()
V5=StringVar()
V6=StringVar()
V1.set("Incorrect guesses remaining: 5")
V2.set("Level: 1")

def F1():# function that will be called as a command to button B1
    # This function creates and alligns required label widgets and also initiates level 1 of the game
    L2=Label(W, text="GOOD LUCK !!!").grid(row=6, column=1)
    global b
    global f
    global c
    global e
    global E1
    c=random.choice(a)
    V2.set("LEVEL "+str(f))
    V3.set("Hint: "+clues[int(c)])
    V4.set("Word has "+str(len(words[int(c)]))+" letters")
    e = "_"*len(words[int(c)]) # creates string with same number of "_"s as the number of letters in the word to be guessed
    V6.set("  ".join(e)) #to print e with gap between elements to help user to identify position of guessed letter
    B2=Button(W, text="Submit", command =F2)
    B2.grid(row=10, column=2)
    E1=Entry(W, width=5)
    E1.grid(row=10, column=1)
    L7=Label(W, text="Enter letter to guess: ").grid(row=10, column=0)
    L3=Label(W, textvariable=V1).grid(row=12, column=1)
    L4=Label(W,textvariable=V2).grid(row=7, column=1)
    L5=Label(W, textvariable=V3).grid(row=8, column=1)
    L6=Label(W, textvariable=V4).grid(row=9, column=1)

L8=Label(W, textvariable=V5).grid(row=13, column=1)
L9=Label(W, textvariable=V6).grid(row=11, column=1)
B1=Button(W, text="START!",command=F1).grid(row=1, column=1) # Start button
b=5 #number of incorrect guesses 
def F2():# the function that will be called as a command to button B2(submit button)
    global b
    global f
    global c
    global e
    if b > 0 :# to allow execution only if incorrect guesses aren't exhausted
                if len(a)!=0 : # to proceed only if there is at least one word left to be guesses
                        V2.set("LEVEL "+str(f))
                        V3.set("Hint: "+clues[int(c)])
                        V4.set("Word has "+str(len(words[int(c)]))+" letters")
                        if e.count("_")>1 : # will be executed if there is more than one letter left to be guessed in the word
                                        if len(E1.get().lower())==1 :
                                                if E1.get().lower() in words[c] :# will be executed in case the guess is correct
                                                        V5.set("Well Done !")
                                                        e = e[ : words[c].index(E1.get().lower())] + E1.get().lower() + e[words[c].index(E1.get().lower()) + 1 :]# reconstituting the string e by revealing the guessed letter
                                                        V6.set("  ".join(e))
                                                        V1.set("Incorrect guesses remaining: "+str(b))
                                                        E1.delete(0,"end")# deletes entry at position 0
                                                else :   # if the guess is wrong     
                                                        V5.set("better luck next time !")
                                                        b-= 1 # to reduce incorrect guesses remaining
                                                        V1.set("Incorrect guesses remaining: "+str(b))
                                                        V6.set("  ".join(e))
                                                        E1.delete(0,"end")
       
                                        elif len(E1.get())>1: # if user has entered more than one character
                                                messagebox.showerror(title="error", message="Please enter One letter at a time only")
                                                V6.set("  ".join(e))
                                                E1.delete(0,"end")
                                        elif len(E1.get())==0:# if user has clicked submit button without entering any character
                                                messagebox.showerror(title="error", message="Entry field is empty")
                        elif e.count("_")==1: # will be executed when there is only one letter in the word left to be guessed
                            # same as the block of statements inside the above if statement except for the text set to variable V5
                                        if len(E1.get())==1 :
                                                if E1.get().lower() in words[c] :
                                                        e = e[ : words[c].index(E1.get().lower())] + E1.get().lower() + e[words[c].index(E1.get().lower()) + 1 :]
                                                        V5.set("Congrats!, The word is "+e)
                                                        V6.set("  ".join(e))
                                                        V1.set("Incorrect guesses remaining: "+str(b))
                                                        E1.delete(0,"end")
                                                else :       
                                                        V5.set("better luck next time !")
                                                        b-= 1
                                                        V1.set("Incorrect guesses remaining: "+str(b))
                                                        V6.set("  ".join(e))
                                                        E1.delete(0,"end")
                                                      
                                        elif len(E1.get())>1:
                                                messagebox.showerror(title="Error", message="Please enter One letter at a time only")
                                                V6.set("  ".join(e))
                                                E1.delete(0,"end")
                                        elif len(E1.get())==0:
                                                messagebox.showerror(title="Error", message="Entry field is empty")
                                                
                        
                        else : # in case all the letters of the word are guessed
                                        V5.set("")
                                        a.remove(c)
                                        if len(a)!=0:
                                            f+=1 #to increse level by 1 if previous word is guessed correctly
                                            c=random.choice(a)
                                            V2.set("LEVEL "+str(f))
                                            V3.set("Hint: "+clues[int(c)])
                                            V4.set("Word has "+str(len(words[int(c)]))+" letters")
                                            e = "_"*len(words[int(c)])
                                            V6.set("  ".join(e))
                                        E1.delete(0,"end")
                else:# if all words have been guessed
                        messagebox.showinfo(title="", message="CONGRATS!!!, GAME COMPLETED!!!")
                        V3.set("")
                        V4.set("")
                        V5.set("")
                        W.destroy()
    elif b==0: #to end game if all the guesses have been exhausted
        messagebox.showwarning(title="", message="Sorry, choices exhausted! GAME OVER!!!")
        W.destroy()

W.mainloop()
