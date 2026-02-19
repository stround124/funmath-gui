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

def actionMainMenu(button):
    button.app.main_menu()

def onButtonClick(button):
    curr_menu = button.parent
    curr_menu.clear()
    match button.id:
        case 'exit':
            curr_menu.app.main_window.close()
        case _:
            lblCaption = toga.Label(button.text + f" | Ниво {curr_menu.app.level}")
            curr_menu.add(lblCaption)
            match button.id:
                case 'add':
                    lblQuestion = toga.Label(addition(curr_menu.app), margin=20)
                case 'sub':
                    lblQuestion = toga.Label(subtraction(curr_menu.app), margin=20)                   
                case 'mul':
                    lblQuestion = toga.Label(multiplication(curr_menu.app), margin=20)
                case 'div':
                    lblQuestion = toga.Label(division(curr_menu.app), margin=20)
                case _:
                    lblQuestion = toga.Label("Invalid operation", margin=20)
            curr_menu.add(lblQuestion)
            inAnswer = toga.TextInput(on_confirm=checkAnswer, margin=20)
            curr_menu.add(inAnswer)
            btnMM = toga.Button("Главно меню", on_press=actionMainMenu, margin=20)
            curr_menu.add(btnMM)

async def checkAnswer(widget):
    if float(widget.value) == float(widget.app.resTrue):
        await widget.app.main_window.dialog(
            toga.InfoDialog("Yay!", f"Браво!")
        )
    else:
        await widget.app.main_window.dialog(
            toga.InfoDialog("Hey!", f"Пак си помисли...")
        )
       
def addition(app):
    match app.level:
        case 1:
            j = 10
        case 2:
            j = 100
        case 3:
            j = 1000
    num1 = random.randint(1, j-1)
    num2 = random.randint(1, j-1)
    app.resTrue = num1 + num2
    return f"Пресметни {num1} + {num2}"

def subtraction(app):
    match app.level:
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
    app.resTrue = num1 - num2
    return f"Пресметни {num1} - {num2}"

def multiplication(app):
    match app.level:
        case 1:
            j = 10
        case 2:
            j = 100
        case 3: 
            j = 1000
    num1 = random.randint(1, j-1)
    num2 = random.randint(1, j-1)
    app.resTrue = num1 * num2
    return f"Пресметни {num1} x {num2}"

def division(app):
    match app.level:
        case 1:
            j = 10
        case 2:
            j = 100
        case 3:
            j = 1000

    num2 = random.randint(1, j-1)
    result = random.randint(1, j-1)
    num1 = num2 * result
    app.resTrue = result
    return f"Пресметни {num1} / {num2}"

def onLevelChange(widget):
    widget.app.level = int(widget.value)
    widget.app.widgets['lblLevel'].text = f"Ниво на трудност: {widget.app.level}"

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
        lblLevel = toga.Label(text=f"Ниво на трудност: {self.level}", id='lblLevel')
        sldLevel = toga.Slider(value=self.level, min=1, max=3, tick_count=3, on_change=onLevelChange, margin_bottom=20)
        btnAdd = toga.Button("Събиране", id="add", on_press=onButtonClick)
        btnSub = toga.Button("Изваждане", id="sub", on_press=onButtonClick)
        btnMul = toga.Button("Умножение", id="mul", on_press=onButtonClick)
        btnDiv = toga.Button("Деление", id="div", on_press=onButtonClick)
        btnExit = toga.Button("Изход", id="exit", on_press=onButtonClick, margin_top=20)
        curr_menu.add(lblLevel)
        curr_menu.add(sldLevel)
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
            toga.InfoDialog("Хмм!", "Ти защо цъкаш тук?")
        )
    
    async def on_exit(self):
        await self.main_window.dialog(
            toga.InfoDialog("ЕЕЕ!", "Ти сериозно ли си тръгваш? Ще ми липсваш!")
        )
        return True

def main():
    return FunMathGUI()
