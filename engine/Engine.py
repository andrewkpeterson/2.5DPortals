from Renderer import *
from Environment1 import Environment1
from Environment2 import Environment2
from Environment3 import Environment3

SCREENWIDTH = 300
SCREENHEIGHT = 250

THETA_W = 45
THETA_H = 30

FAR = 1000
NEAR = .1


class Engine:

    def __init__(self):
        self.running = True
        self.screen = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pg.DOUBLEBUF | pg.RESIZABLE | pg.HWSURFACE)
        self.env = Environment3()
        self.camera = Camera(SCREENWIDTH, SCREENHEIGHT, THETA_W, THETA_H, NEAR, FAR, self.env.sectors[0], self.env, False)
        self.renderer = Renderer()

    def run(self):
        pg.init()
        pg.display.set_caption('2.5D Engine')
        clock = pg.time.Clock()
        while self.running:

            self.processInputs()
            self.camera.processEvents(pg.event.get())
            self.camera.update(self.env, False)
            self.renderer.renderFrame(self.screen, self.camera, self.env)
            pg.display.update()
            clock.tick()

    def processInputs(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
        self.camera.processEvents(events)


if __name__ == '__main__':
    engine = Engine()
    engine.run()
