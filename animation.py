import pyglet


window = pyglet.window.Window()
# self.sprites = [
#     Sprite(load("resources/char/0.png"), batch=self.batch),
#     Sprite(load("resources/char/1.png"), batch=self.batch),
#     Sprite(load("resources/char/2.png"), batch=self.batch),
#     Sprite(load("resources/char/3.png"), batch=self.batch),
# ]
animation = pyglet.image.load_animation(
    filename="running_hero.gif",
    file=open(
        "dinosaur.gif",
        "rb",
    ),
)
# bin = pyglet.image.atlas.TextureBin()
# animation.add_to_texture_bin(bin)
sprite = pyglet.sprite.Sprite(img=animation)


@window.event
def on_draw():
    print(animation.get_duration())
    window.clear()
    sprite.draw()


pyglet.app.run()
