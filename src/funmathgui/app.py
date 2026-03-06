"""
Fun Math Application
"""
import asyncio
import fractions
import random
import toga
from toga.style.pack import COLUMN, ROW, CENTER
from toga.colors import WHITE, rgb
from toga.fonts import SANS_SERIF
from toga.constants import Baseline

def actionMainMenu(button):
    button.app.main_menu()

def onButtonClick(button):
    curr_menu = button.parent
    curr_menu.clear()
    match button.id:
        case 'btnExit':
            curr_menu.app.main_window.close()
        case _:
            lblCaption = toga.Label(button.text + f" | Ниво {curr_menu.app.level}")
            curr_menu.app.doRetry = 3
            match button.id:
                case 'btnAdd':
                    curr_menu.app.answer_img = toga.Image(curr_menu.app.paths.app / "resources/addition.jpg")
                    lblQuestion = toga.Label(askAddition(curr_menu.app), margin=20)
                case 'btnSub':
                    curr_menu.app.answer_img = toga.Image(curr_menu.app.paths.app / "resources/subtraction.jpg")
                    lblQuestion = toga.Label(askSubtraction(curr_menu.app), margin=20)                   
                case 'btnMul':
                    curr_menu.app.answer_img = toga.Image(curr_menu.app.paths.app / "resources/multiplication.jpg")
                    lblQuestion = toga.Label(askMultiplication(curr_menu.app), margin=20)
                case 'btnDiv':
                    curr_menu.app.answer_img = toga.Image(curr_menu.app.paths.app / "resources/division.jpg")
                    lblQuestion = toga.Label(askDivision(curr_menu.app), margin=20)
                case 'btnFrac':
                    curr_menu.app.answer_img = toga.Image(curr_menu.app.paths.app / "resources/fractions.jpg")
                    lblQuestion = toga.Label(askFractions(curr_menu.app), margin=20)
                case 'btnX':
                    curr_menu.app.answer_img = toga.Image(curr_menu.app.paths.app / "resources/findx.jpg")
                    lblQuestion = toga.Label(askX(curr_menu.app), margin=20)
                case _:
                    lblQuestion = toga.Label("Invalid operation", margin=20)
            curr_menu.app.answer_imgview.image = curr_menu.app.answer_img
            curr_menu.add(curr_menu.app.answer_imgview)
            curr_menu.add(lblCaption)
            curr_menu.add(lblQuestion)
            inAnswer = toga.TextInput(on_confirm=checkAnswer, margin=20)
            curr_menu.add(inAnswer)
            btnMM = toga.Button("Главно меню", on_press=actionMainMenu, margin=20)
            curr_menu.add(btnMM)
            inAnswer.focus()

async def checkAnswer(widget):
    try:
        user_input = widget.value.strip()

        if "/" in user_input:
            user_value = float(fractions.Fraction(user_input))
        else:
            user_value = float(user_input)

        if abs(user_value - float(widget.app.resTrue)) < 0.01:
            widget.app.answer_img = toga.Image(widget.app.paths.app / "resources/horray.gif")        
            widget.app.answer_imgview.image = widget.app.answer_img
            await widget.app.main_window.dialog(
                toga.InfoDialog("Йее!", "Браво!")
            )
            widget.app.doRetry = 0
            actionMainMenu(widget)
            return

    except:
        await widget.app.main_window.dialog(
            toga.InfoDialog("Грешка", "Моля въведи число или дроб")
        )
        return

    match widget.app.doRetry:
        case 3: sMsg = "Пробвай се отново!"
        case 2: sMsg = "Още два пъти и може да уцелиш!"
        case 1: sMsg = "Давам ти последен шанс!"
        case 0: sMsg = "Затваряй компютъра и си отваряй учебника!"
    
    widget.app.answer_img = toga.Image(widget.app.paths.app / "resources/einstein-math.png")
    widget.app.answer_imgview.image = widget.app.answer_img

    await widget.app.main_window.dialog(
        toga.InfoDialog("Не!", sMsg)
    )

    if widget.app.doRetry > 0:
        widget.app.doRetry -= 1
    else:
        actionMainMenu(widget)
        
def askAddition(app):
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

def askSubtraction(app):
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

def askMultiplication(app):
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
    return f"Пресметни {num1} * {num2}"

def askDivision(app):
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

def askFractions(app):
    match app.level:
        case 1:
            j = 10
        case 2:
            j = 100
        case 3:
            j = 1000
    num1 = random.randint(1, j-1)
    num2 = random.randint(1, j-1)
    num3 = random.randint(1, j-1)
    num4 = random.randint(1, j-1)
    app.resTrue = (num1/num2) + (num3/num4)
    return f"Пресметни {num1}/{num2} + {num3}/{num4}"

def askX(app):
    match app.level:
        case 1:
            j = 10
        case 2:
            j = 100
        case 3:
            j = 1000
    num1 = random.randint(1, j-1)
    num2 = random.randint(1, j-1)
    rand = random.randint(1, 4) 
    
    match random.randint(1,4):
        case 1:
            app.resTrue = num2 - num1
            return f"Пресметни x + {num1} = {num2}"
        case 2:
            app.resTrue = num2 + num1
            return f"Пресметни x - {num1} = {num2}"
        case 3:
            app.resTrue = num2 / num1
            return f"Пресметни x * {num1} = {num2}"
        case 4:
            app.resTrue = num1 * num2
            return f"Пресметни x / {num1} = {num2}"

def onLevelChange(widget):
    widget.app.level = int(widget.value)
    widget.app.widgets['lblLevel'].text = f"Ниво на трудност: {widget.app.level}"

class FunMathGUI(toga.App):
    resTrue = 0
    doRetry = 0
    level = 1

    def startup(self):
        random.seed()
        self.answer_img = toga.Image(self.paths.app / "resources/main_menu.jpg")
        self.answer_imgview = toga.ImageView(self.answer_img, height = 240, flex = 1, margin = 10)
        self.main_view = toga.Box(direction=COLUMN, alignment=CENTER, margin=50)

        self.main_menu()


        self.main_window = toga.Window(title=self.formal_name)
        self.main_window.content = self.main_view
        self.main_window.show()

    
    def main_menu(self):
        curr_menu = self.main_view
        curr_menu.clear()
        lblLevel = toga.Label(text=f"Ниво на трудност: {self.level}", id='lblLevel')
        sldLevel = toga.Slider(value=self.level, min=1, max=3, tick_count=3, on_change=onLevelChange, margin=5, margin_bottom=20)
        btnAdd   = toga.Button("Събиране", id="btnAdd", on_press=onButtonClick, margin=5)
        btnSub   = toga.Button("Изваждане", id="btnSub", on_press=onButtonClick, margin=5)
        btnMul   = toga.Button("Умножение", id="btnMul", on_press=onButtonClick, margin=5)
        btnDiv   = toga.Button("Деление", id="btnDiv", on_press=onButtonClick, margin=5)
        btnDrobi = toga.Button("Дроби", id="btnFrac", on_press=onButtonClick, margin=5, margin_top=20)
        btnX     = toga.Button("Задачи с X", id="btnX", on_press=onButtonClick, margin=5)
        btnExit  = toga.Button("Изход", id="btnExit", on_press=onButtonClick, margin=5, margin_top=20)
        self.answer_img = toga.Image(self.paths.app / "resources/main_menu.jpg")        
        self.answer_imgview.image = self.answer_img
        curr_menu.add(self.answer_imgview)
        curr_menu.add(lblLevel)
        curr_menu.add(sldLevel)
        curr_menu.add(btnAdd)
        curr_menu.add(btnSub)
        curr_menu.add(btnMul)
        curr_menu.add(btnDiv)
        curr_menu.add(btnDrobi)
        curr_menu.add(btnX)
        curr_menu.add(btnExit)
        btnAdd.focus()

    
    async def on_exit(self):
        self.main_view.clear()
        self.answer_img = toga.Image(self.paths.app / "resources/sad.jpg")        
        self.answer_imgview.image = self.answer_img
        self.main_view.add(self.answer_imgview)
        lblBye = toga.Label(text="Не трябваше да натискаш този бутон :(", margin=20)
        self.main_view.add(lblBye)
        await asyncio.sleep(3)
        return True

def main():
    return FunMathGUI()
