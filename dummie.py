from pyglet.sprite import Sprite, SpriteGroup
from pyglet.image import load
from pyglet.graphics import Batch

from time import time
from direction import Direction
from position import Position


class Dummie:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        jump_acceleration: float = 50.0,
        move_acceleration: float = 50.0,
    ) -> None:
        self.batch = Batch()
        self.ctr = 0
        self.is_jump = False
        self.is_move = False
        # self.sprites = [
        #     Sprite(load("resources/char/0.png"), batch=self.batch),
        #     Sprite(load("resources/char/1.png"), batch=self.batch),
        #     Sprite(load("resources/char/2.png"), batch=self.batch),
        #     Sprite(load("resources/char/3.png"), batch=self.batch),
        # ]
        self.jump_time = 3
        self.move_time = 3
        self.pos = Position(
            x=x,
            y=y,
        )
        self.falling_direction = Direction.NONE
        self.direction = Direction.NONE
        self.jump_acceleration = jump_acceleration
        self.move_acceleration = move_acceleration

    def move(self, direction: Direction):
        if not self.is_jump:
            self.is_move = True
            self.direction = direction
            self.move_start = time()

    def jump(self):
        if not self.is_jump:
            self.is_jump = True
            self.jump_start = time()

    def update(
        self,
        dt,
    ) -> None:
        print(f"{self.pos=}")
        if self.is_move:
            if time() - self.move_start > self.move_time:

                if not self.is_jump:
                    self.direction = Direction.NONE
                    self.is_move = False

            match self.direction:
                case Direction.LEFT:  # "left"
                    self.pos.x -= dt * self.move_acceleration
                case Direction.RIGHT:  # "right":
                    self.pos.x += dt * self.move_acceleration
                case Direction.NONE:
                    ...
                case _:
                    ...
        if self.is_jump:
            if time() - self.jump_start > self.jump_time:
                self.pos.y -= dt * self.jump_acceleration
            else:
                self.pos.y += dt * self.jump_acceleration
        if self.pos.y < 10 and self.is_jump:
            self.is_jump = False

    #     self.__apply_pos()

    # def __apply_pos(self):
    #     for sprite in self.sprites:
    #         sprite.x, sprite.y = (
    #             self.pos.x,
    #             self.pos.y,
    #         )

    # def draw(self):
    #     self.ctr += 1
    #     if self.ctr > len(self.sprites) - 1:
    #         self.ctr = 0
    #     return self.sprites[self.ctr].draw()
    #     # return self.batch.draw()
