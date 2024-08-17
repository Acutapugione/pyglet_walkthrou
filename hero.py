from direction import Direction
from dummie import Dummie
from pyglet.sprite import Sprite
from pyglet.image import load
from pyglet.graphics import Batch


class Hero(Dummie):
    def __init__(
        self,
        # resource,
        x: int = 0,
        y: int = 0,
        jump_acceleration: float = 50,
        move_acceleration: float = 50,
    ) -> None:
        # self.resource = resource
        self.ctr = 0
        self.batch = Batch()

        self.sprites = [
            Sprite(load(f"resources/char/right/{x}.png"), batch=self.batch)
            for x in range(0, 11)
        ]
        super().__init__(
            x,
            y,
            jump_acceleration,
            move_acceleration,
        )

    def update(self, dt) -> None:
        upd_res = super().update(dt)

        self.__apply_pos()
        return upd_res

    def __apply_pos(self):
        for sprite in self.sprites:
            sprite.x, sprite.y = (
                self.pos.x,
                self.pos.y,
            )

    def move(self, direction: Direction):
        if direction == Direction.LEFT:
            self.sprites = [
                Sprite(load(f"resources/char/left/{x}.png"), batch=self.batch)
                for x in range(0, 11)
            ]
        else:
            self.sprites = [
                Sprite(load(f"resources/char/right/{x}.png"), batch=self.batch)
                for x in range(0, 11)
            ]
        return super().move(direction)

    def draw(self):
        if self.is_move or self.is_jump:
            self.ctr += 1
            if self.ctr > len(self.sprites) - 1:
                self.ctr = 0
        return self.sprites[self.ctr].draw()
        # return self.batch.draw()

    # def draw(self):
    #     self.sprite = Sprite(img=self.resource, x=self.pos.x, y=self.pos.y)
    #     self.sprite.draw()
