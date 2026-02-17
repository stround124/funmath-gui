"""
Fun Math Application
"""

import asyncio
import random
import toga
from toga.style.pack import COLUMN, ROW
from toga.colors import WHITE, rgb
from toga.fonts import SANS_SERIF
from toga.constants import Baseline

global choice
choice = 0

def actionMainMenu(button):
    FunMathGUI.main_menu(button.app)

async def onButtonClick(button):
    curr_menu = button.parent
    curr_menu.clear()
    match button.id:
        case 'exit':
            lblCaption = toga.Label("Why, oh why are you leaving me?", margin=20)
            curr_menu.add(lblCaption)
            doExit = True
        case _:
            lblCaption = toga.Label(button.text)
            curr_menu.add(lblCaption)
            match button.id:
                case 'add':
                    lblQuestion = toga.Label(addition(FunMathGUI.level), margin=20)
                case 'sub':
                    lblQuestion = toga.Label(subtraction(FunMathGUI.level), margin=20)                   
                case 'mul':
                    lblQuestion = toga.Label(multiplication(FunMathGUI.level), margin=20)
                case 'div':
                    lblQuestion = toga.Label(division(FunMathGUI.level), margin=20)
                case _:
                    lblQuestion = toga.Label("Invalid operation", margin=20)
            curr_menu.add(lblQuestion)
            inAnswer = toga.TextInput(on_confirm=checkAnswer, margin = 20)
            curr_menu.add(inAnswer)
            btnMM = toga.Button("MainMenu", on_press=actionMainMenu)
            curr_menu.add(btnMM)
            doExit = False
    if doExit:
        await asyncio.sleep(5)
        exit(0)

async def checkAnswer(widget):
    if float(widget.value) == float(widget.app.resTrue):
        await widget.app.main_window.dialog(
            toga.InfoDialog("Yey!", f"Браво!")
        )
        match choice:
            case 1:
                addition(FunMathGUI.level)
            case 2:
                subtraction(FunMathGUI.level)
            case 3:
                multiplication(FunMathGUI.level)
            case 4:
                division(FunMathGUI.level)
    else:
        await widget.app.main_window.dialog(
            toga.InfoDialog("Hey!", f"Пак си помисли...")
        )
       
def addition(level):
    choice = 1
    match level:
        case 1:
            j = 10
        case 2:
            j = 100
        case 3:
            j = 1000
    num1 = random.randint(1, j-1)
    num2 = random.randint(1, j-1)
    FunMathGUI.resTrue = num1 + num2
    return f"Пресметни {num1} + {num2}"

def subtraction(level):
    choice = 2
    match level:
        case 1:
            j = 10
        case 2:
            j = 100
        case 3:
            j = 1000
    num1 = random.randint(1, j-1)
    num2 = random.randint(1, j-1)
    if num2 > num1:
        num1, num2 = num2, num1
    FunMathGUI.resTrue = num1 - num2
    return f"Пресметни {num1} - {num2}"
#     int j;
#     cout << u8"Изваждане. Ниво " << level << "\n";
#     switch (level) {
#     case 1:
#         j = 10;
#         break;
#     case 2:
#         j = 100;
#         break;
#     case 3:
#         j = 1000;
#         break;
#     }
#     int num1 = rand() % j;
#     int num2 = rand() % j;
#     if(num2>num1)
#     {
#         int temp=num1;
#         num1=num2;
#         num1=temp;
#     }
#     resTrue = num1;
    return f"" #f"Пресметни {num2+num1} - {num2}"

def multiplication(level):
    choice = 3
    match level:
        case 1:
            j = 10
        case 2:
            j = 100
        case 3: 
            j = 1000
    num1 = random.randint(1, j-1)
    num2 = random.randint(1, j-1)
    FunMathGUI.resTrue = num1 * num2
    return f"Пресметни {num1} x {num2}"
#     int j;
#     cout << u8"Умножение. Ниво " << level << "\n";
#     switch (level) {
#     case 1:
#         j = 10;
#         break;
#     case 2:
#         j = 100;
#         break;
#     case 3:
#         j = 1000;
#         break;
#     }
#     int num1 = rand() % j;
#     int num2 = rand() % j;
#     resTrue = num1*num2;

def division(level):
    choice = 4
    match level:
        case 1:
            j = 10
        case 2:
            j = 100
        case 3:
            j = 100

    num2 = random.randint(1, j-1)
    result = random.randint(1, j-1)
    num1 = num2 * result
    FunMathGUI.resTrue = result
    return f"Пресметни {num1} / {num2}"

#     // num1/num2=res => num1=res*num2  
#     int j=0,k=0;
#     double d=0;
#     cout << u8"Деление. Ниво " << level << "\n";
#     switch (level) {
#     case 1: # xx/y=z; =1..9; z=1..9
#         j = 9;
#         k = 9;
#         d = 1;
#         break;
#     case 2: # xxx/yy=z; y=1..99; z=1..9
#         j = 99;
#         k = 9;
#         d = 1;
#         break;
#     case 3: # xxxx/yy=z.zz
#         j = 99;
#         k = 1000;
#         d = 0.01;
#         break;
#     }
#     int num2 = (rand() % (j - 1)) + 1; #не може да се дели на 0, затова num2 е от 1 до j
#     resTrue = (rand() % k) * d;
    return f"" #f"Пресметни {resTrue*num2} / {num2}"

class FunMathGUI(toga.App):
    resTrue = 0
    level = 1

    def startup(self):
        random.seed()

        self.canvas_logo = toga.Canvas(
            flex=1,
            on_resize=self.on_resize,
            on_press=self.on_press,            
        )
        self.main_view = toga.Box(direction=COLUMN, margin=50)

        self.draw_logo()
        self.main_menu()

        container_left = toga.ScrollContainer(horizontal=False)
        container_right = toga.ScrollContainer(horizontal=False)
        container_left.content = self.canvas_logo
        container_right.content = self.main_view

        split_main = toga.SplitContainer()
        split_main.content = [(container_left, 1), (container_right, 2)]

        self.main_window = toga.Window(title=self.formal_name)
        self.main_window.content = split_main
        self.main_window.show()
    
    def main_menu(self):
        curr_menu = self.main_view
        curr_menu.clear()
        btnAdd = toga.Button("Addition", id="add", on_press=onButtonClick)
        btnSub = toga.Button("Subtraction", id="sub", on_press=onButtonClick)
        btnMul = toga.Button("Multiplication", id="mul", on_press=onButtonClick)
        btnDiv = toga.Button("Division", id="div", on_press=onButtonClick)
        btnExit = toga.Button("Exit", id="exit", on_press=onButtonClick) 
        curr_menu.add(btnAdd)
        curr_menu.add(btnSub)
        curr_menu.add(btnMul)
        curr_menu.add(btnDiv)
        curr_menu.add(btnExit)

    def draw_logo(self):
        font = toga.Font(family=SANS_SERIF, size=20)
        self.text_width, text_height = self.canvas_logo.measure_text("Fun Math GUI", font)

        x = (150 - self.text_width) // 2
        y = 175

        with self.canvas_logo.Stroke(color="CYAN", line_width=4.0) as rect_stroker:
            self.text_border = rect_stroker.rect(
                x - 5,
                y - 5,
                self.text_width + 10,
                text_height + 10,
            )
        with self.canvas_logo.Fill(color="LIGHTGREEN") as text_filler:
            self.text = text_filler.write_text("Fun Math GUI", x, y, font, Baseline.TOP)

    def on_resize(self, widget, width, height, **kwargs):
        # On resize, center the text horizontally on the canvas. on_resize will be
        # called when the canvas is initially created, when the drawing objects won't
        # exist yet. Only attempt to reposition the text if there's context objects on
        # the canvas.
        if widget.context:
            left_pad = (width - self.text_width) // 2
            self.text.x = left_pad
            self.text_border.x = left_pad - 5
            widget.redraw()

    async def on_press(self, widget, x, y, **kwargs):
        await self.main_window.dialog(
            toga.InfoDialog("Hey!", f"You've got no business here:({x}, {y})")
        )


def main():
    return FunMathGUI()
