# %%
from pyglet.app import run
from pyglet.window import Window
from pyglet.text import Label
from pyglet.resource import image

# %%
WINDOW = Window()  # fullscreen=True
FONT_SIZE = 24
BACKGROUND = image("resources/background.jpg")
GREET_LBL = Label(
    text="Вітаю на прокачку)",
    font_name="Roboto",
    font_size=FONT_SIZE,
    bold=True,
    x=WINDOW.width // 2,
    y=WINDOW.height - FONT_SIZE // 2,  # // 2 - FONT_SIZE,
    anchor_x="center",
    anchor_y="center",
)


# %%
@WINDOW.event
def on_draw():
    WINDOW.clear()
    BACKGROUND.blit(0, 0, width=WINDOW.width - 1, height=WINDOW.height - 1)
    GREET_LBL.draw()


# %%
run()
