import tkinter as tkinter
import tkinter.font as tkFont

#width of the title
twidth = 5
#width of the buttons
bwidth = 5
#hight of the buttons
bhight = 3
#padding for the left and right
pad_x = 3
#padding for the top and bottom
pad_y = 0

class calculator():
    
    def __init__(self):
        #make a window
        self.window = tkinter.Tk()


        #font of the text
        self.f = tkFont.Font(family="Lucida Grande", size=20)
        
        #vars for the title box
        self.t = [tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar()]
        for i in range(10):
            self.t[i].set("")
        
        #useing titles as the screen make multiple titles as place on the screen
        self.title = [
        tkinter.Label(textvariable=self.t[0], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y), 
        tkinter.Label(textvariable=self.t[1], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y), 
        tkinter.Label(textvariable=self.t[2], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y),
        tkinter.Label(textvariable=self.t[3], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y),
        tkinter.Label(textvariable=self.t[4], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y),
        tkinter.Label(textvariable=self.t[5], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y),
        tkinter.Label(textvariable=self.t[6], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y),
        tkinter.Label(textvariable=self.t[7], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y),
        tkinter.Label(textvariable=self.t[8], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y),
        tkinter.Label(textvariable=self.t[9], font=self.f,foreground="white", background="black", width=twidth, height=bhight, padx=pad_x, pady= pad_y)
        ]

        #print titles
        self.c = 9
        for i in range(10):
            self.title[i].grid(row=0, column=self.c)
            self.c -= 1

        #button objects
        self.button0 = tkinter.Button(text="0", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.zero)
        self.button1 = tkinter.Button(text="1", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.one)
        self.button2 = tkinter.Button(text="2", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.two)
        self.button3 = tkinter.Button(text="3", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.three)
        self.button4 = tkinter.Button(text="4", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.four)
        self.button5 = tkinter.Button(text="5", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.five)
        self.button6 = tkinter.Button(text="6", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.six)
        self.button7 = tkinter.Button(text="7", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.seven)
        self.button8 = tkinter.Button(text="8", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.eight)
        self.button9 = tkinter.Button(text="9", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.nine)
        self.button_plus = tkinter.Button(text="+", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.plus)
        self.button_neg = tkinter.Button(text="-", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.minus)
        self.button_muti = tkinter.Button(text="*", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.muti)
        self.button_div = tkinter.Button(text="/", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.div)
        self.button_eq = tkinter.Button(text="=", font=self.f,width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.equals)
        self.button_clear = tkinter.Button(text="Clear", font=self.f, width=bwidth, height=bhight, bg="orange", fg="white", pady= pad_y, command=self.clear)
        
        #button Functions
        

        #print button
        self.button1.grid(row=1, column=0)
        self.button2.grid(row=1, column=1)
        self.button3.grid(row=1, column=2)
        self.button_neg.grid(row=1, column=3)

        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button_plus.grid(row=2, column=3)
        
        self.button7.grid(row=3, column=0)
        self.button8.grid(row=3, column=1)
        self.button9.grid(row=3, column=2)
        self.button_muti.grid(row=3, column=3)

        self.button_clear.grid(row=4, column=0)
        self.button0.grid(row=4, column=1)
        self.button_eq.grid(row=4, column=2)
        self.button_div.grid(row=4, column=3)
        
        #loop and listen for button press
        self.window.mainloop()
    
    #Functions for the Button Action
    def zero(self):
        self.screen("0")
    def one(self):
        self.screen("1")
    def two(self):
        self.screen("2")
    def three(self):
        self.screen("3")
    def four(self):
        self.screen("4")
    def five(self):
        self.screen("5")
    def six(self):
        self.screen("6")
    def seven(self):
        self.screen("7")
    def eight(self):
        self.screen("8")
    def nine(self):
        self.screen("9")
    def minus(self):
        self.screen("-")
    def plus(self):
        self.screen("+")
    def muti(self):
        self.screen("*")
    def div(self):
        self.screen("/")
    def equals(self):
        #set the strings to ints
        #see if you need to identify the operator or if the python will recongives it 
        #save the answer to the array
        #################################################################################
        #May/26/2020 
        #need to figure out how to tell if a StringVar is a digit as .isdigit is for String values
        #try converging the value in to a string useing .get() method
        #SOLVED

        operators = ["+", "-", "/", "*"]
        one = []
        two = []
        count = 0
        first = True
        operator = ""
        for i in range(9, -1, -1):
            if self.t[i].get().isdigit():
                if first:
                   one.insert(count, self.t[i].get())
                   count+=1
                else:
                    two.insert(count, self.t[i].get())
            elif self.t[i].get() in operators:
                count=+1
                first = False
                operator = self.t[i].get()
            else:
                count=+1
        
        # create new ints from the list 
        numOne = ""
        numTwo = ""
        for i in range(len(one)):
            numOne += one[i]
        for i in range(len(two)):
            numTwo += two[i]
        
        #compute the two numbers and output an answer
        #never executes. Skips this and give error that  var total is never assigned 
        Error = False
        if operator == "+":
            total = int(numOne) + int(numTwo)
        elif operator == "-":
            total = int(numOne) - int(numTwo)
        elif operator == "*":
            total = int(numOne) * int(numTwo)
        elif operator == "/":
            if int(numTwo) == 0:
                self.error()
                Error = True
            else:
                total = int(numOne) / int(numTwo)

        #print the answer
        if not Error:
            self.clear()
            answer = str(total)
            answer.split()
            for i in range(len(str(total))):
                self.screen(answer[i])

    #clears the screen
    def clear(self):
        for i in range(10):
            self.t[i].set("")
    
    #print an Error message
    def error(self):
        self.clear()
        self.t[0].set("r")
        self.t[1].set("o")
        self.t[2].set("r")
        self.t[3].set("r")
        self.t[4].set("E")
    
    #Screen Updater
    def screen(self, input):
        #clears the screen after an error
        if self.t[0].get() == "r":
            self.clear()
        #if to many numbers are filled display and error 
        if self.t[9].get():
            self.error()
        elif not self.t[0].get():
            #print("first")
            self.t[0].set(input)
        #this works on magic!! Its 3:40 fuck that took forever
        else:
            for i in range(9, -1, -1):
                if self.t[i].get():
                    self.t[i+1].set(self.t[i].get())
                if i == 0:
                    self.t[0].set(input)

app = calculator()
