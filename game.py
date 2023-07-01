import pygame
import debug
import defs.finals as finals

class Game(object):
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]
        self.desired_next_state = ""

    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self, next_state=""):
        if  next_state == "":
            next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        self.desired_next_state = self.state.desired_next_state
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state(self.desired_next_state)
            self.switch_music = True
        self.state.update(dt)

    def draw(self):
        self.state.draw()
        if debug.status:
            debug.display(int(self.clock.get_fps()))

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
