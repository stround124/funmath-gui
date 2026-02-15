"""
Fun Math Application
"""
import asyncio
import toga
from toga.style.pack import COLUMN, ROW
from toga.colors import WHITE, rgb
from toga.fonts import SANS_SERIF
from toga.constants import Baseline

def actionMainMenu(button):
    FunMathGUI.main_menu(button.app)

async def onButtonClick(button):
    curr_menu = button.parent
    curr_menu.clear()
    match button.id:
        case 'exit':
            lblCaption = toga.Label("Why, oh why are you leaving me?")
            doExit = True
        case _:
            lblCaption = toga.Label(button.text)
            btnMM = toga.Button("MainMenu", on_press=actionMainMenu)
            curr_menu.add(btnMM)
            doExit = False
    curr_menu.add(lblCaption)
    if doExit:
        await asyncio.sleep(5)
        exit(0)

class FunMathGUI(toga.App):
    def startup(self):
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