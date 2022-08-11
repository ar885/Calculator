from tkinter import *
import math
from pygame import mixer
import speech_recognition
mixer.init()

class Calculator:
    def __init__(self):
        root = Tk()
        root.title('Team Outcomes')
        root.config(bg='white')
        root.geometry('680x486+100+100')

        logoImage = PhotoImage(file='logo.png')
        logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
        logoLabel.grid(row=0, column=0)

        self.entryField = Entry(root, font=('arial', 20, 'bold'),
                        bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
        self.entryField.grid(row=0, column=0, columnspan=8)

        micImage = PhotoImage(file='microphone.png')
        micButton = Button(root, image=micImage, bd=0, bg='dodgerblue3',
                        activebackground='dodgerblue3', command=self.audio)
        micButton.grid(row=0, column=7)

        button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                            "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                            "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                            "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                            "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
        rowvalue = 1
        columnvalue = 0
        for i in button_text_list:

            button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white',
                            font=('arial', 18, 'bold'), activebackground='dodgerblue3', command=lambda button=i: self.click(button))
            button.grid(row=rowvalue, column=columnvalue, pady=1)
            columnvalue += 1
            if columnvalue > 7:
                rowvalue += 1
                columnvalue = 0

        root.mainloop()

    def click(self,value):
        ex = self.entryField.get()  # 789 ex[0:len(ex)-1]
        answer = ''

        try:

            if value == 'C':
                ex = ex[0:len(ex) - 1]  # 78
                self.entryField.delete(0, END)
                self.entryField.insert(0, ex)
                return

            elif value == 'CE':
                self.entryField.delete(0, END)

            elif value == '√':
                answer = math.sqrt(eval(ex))

            elif value == 'π':
                answer = math.pi

            elif value == 'cosθ':
                answer = math.cos(math.radians(eval(ex)))

            elif value == 'tanθ':
                answer = math.tan(math.radians(eval(ex)))

            elif value == 'sinθ':
                answer = math.sin(math.radians(eval(ex)))

            elif value == '2π':
                answer = 2 * math.pi

            elif value == 'cosh':
                answer = math.cosh(eval(ex))

            elif value == 'tanh':
                answer = math.tanh(eval(ex))

            elif value == 'sinh':
                answer = math.sinh(eval(ex))

            elif value == chr(8731):
                answer = eval(ex) ** (1 / 3)

            elif value == 'x\u02b8':  # 7**2
                self.entryField.insert(END, '**')
                return

            elif value == 'x\u00B3':
                answer = eval(ex) ** 3

            elif value == 'x\u00B2':
                answer = eval(ex) ** 2

            elif value == 'ln':
                answer = math.log2(eval(ex))

            elif value == 'deg':
                answer = math.degrees(eval(ex))

            elif value == "rad":
                answer = math.radians(eval(ex))

            elif value == 'e':
                answer = math.e

            elif value == 'log₁₀':
                answer = math.log10(eval(ex))

            elif value == 'x!':
                answer = math.factorial(ex)

            elif value == chr(247):  # 7/2=3.5
                self.entryField.insert(END, "/")
                return

            elif value == '=':
                answer = eval(ex)

            else:
                self.entryField.insert(END, value)
                return

            self.entryField.delete(0, END)
            self.entryField.insert(0, answer)

        except SyntaxError:
            pass


    def add(self,a, b):
        return a+b


    def sub(self,a, b):
        return a-b


    def mul(self,a, b):
        return a * b


    def div(self,a, b):
        return a / b


    def mod(self,a, b):
        return a % b


    def lcm(self,a, b):
        l = math.lcm(a, b)
        return l


    def hcf(self,a, b):
        h = math.gcd(a, b)
        return h



    def findNumbers(self,t):
        l = []
        for num in t:
            try:
                l.append(int(num))
            except ValueError:
                pass
        return l


    def audio(self):
        self.operations = {
                'ADD': self.add,
                'ADDITION': self.add,
                'SUM': self.add, 
                'PLUS': self.add,
                'SUBTRACTION': self.sub,
                'DIFFERENCE': self.sub,
                'MINUS': self.sub,
                'SUBTRACT': self.sub,
                'PRODUCT': self.mul, 
                'MULTIPLICATION': self.mul,
                'MULTIPLY': self.mul,
                'DIVISION': self.div, 
                'DIV': self.div,
                'DIVIDE': self.div,
                'LCM': self.lcm,
                'HCF': self.hcf,
                'MOD': self.mod, 
                'REMAINDER': self.mod,
                'MODULUS': self.mod
                }
        mixer.music.load('music1.mp3')
        mixer.music.play()
        sr = speech_recognition.Recognizer()
        with speech_recognition.Microphone()as m:
            try:
                sr.adjust_for_ambient_noise(m, duration=0.2)
                voice = sr.listen(m)
                text = sr.recognize_google(voice)

                mixer.music.load('music2.mp3')
                mixer.music.play()
                text_list = text.split(' ')
                for word in text_list:
                    if word.upper() in self.operations.keys():
                        l = self.findNumbers(text_list)
                        print(l)
                        result = self.operations[word.upper()](
                            l[0], l[1])  # mul(5.0,6.0)
                        self.entryField.delete(0, END)
                        self.entryField.insert(END, result)

                    else:
                        pass

            except:
                pass



clac = Calculator()