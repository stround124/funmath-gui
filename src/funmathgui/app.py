"""
Fun Math Application
"""
import asyncio
import toga
from toga.style.pack import COLUMN, ROW

def actionMainMenu(button):
    FunMathGUI.mainmenu(button.app)

def actionAddition(button):
    curr_menu = toga.Box()
    lbl = toga.Label("Addition")
    btnMM = toga.Button("MainMenu", on_press=actionMainMenu)
    curr_menu.add(lbl)
    curr_menu.add(btnMM)
    button.app.main_window.content = curr_menu

def actionSubtraction(button):
    curr_menu = toga.Box()
    lbl = toga.Label("Subtraction")
    btnMM = toga.Button("MainMenu", on_press=actionMainMenu)
    curr_menu.add(lbl)
    curr_menu.add(btnMM)
    button.app.main_window.content = curr_menu

def actionMultiplication(button):
    curr_menu = toga.Box()
    lbl = toga.Label("Multiplication")
    btnMM = toga.Button("MainMenu", on_press=actionMainMenu)
    curr_menu.add(lbl)
    curr_menu.add(btnMM)
    button.app.main_window.content = curr_menu

def actionDivision(button):
    curr_menu = toga.Box()
    lbl = toga.Label("Division")
    btnMM = toga.Button("MainMenu", on_press=actionMainMenu)
    curr_menu.add(lbl)
    curr_menu.add(btnMM)
    button.app.main_window.content = curr_menu

async def actionExit(button):
    curr_menu = toga.Box()
    lbl = toga.Label("Why, oh why are you leaving me?")
    curr_menu.add(lbl)
    button.app.main_window.content = curr_menu
    await asyncio.sleep(5)
    exit(0)

class FunMathGUI(toga.App):
    def startup(self):
        print("Hello!")
        self.main_window = toga.Window(title=self.formal_name)

        self.mainmenu()

        self.main_window.show()
    
    def mainmenu(self):
        curr_menu = toga.Box()
        btnAdd = toga.Button("Add", on_press=actionAddition)
        btnSub = toga.Button("Sub", on_press=actionSubtraction)
        btnMul = toga.Button("Mul", on_press=actionMultiplication)
        btnDiv = toga.Button("Div", on_press=actionDivision)
        btnExit = toga.Button("Exit", on_press=actionExit) 
        curr_menu.add(btnAdd)
        curr_menu.add(btnSub)
        curr_menu.add(btnMul)
        curr_menu.add(btnDiv)
        curr_menu.add(btnExit)
        self.main_window.content = curr_menu

def main():
    return FunMathGUI()