import pygame
import pymunk

class Bust:

    def __init__(self, body: pymunk.Body, shape: pymunk.Segment, head_shape: pymunk.Circle) -> None:
        
        self.body = body
        self.shape = shape
        self.head_shape = head_shape

    def print(self, window):
        
        point1 = self.body.position + self.shape.a.rotated(self.body.angle)
        point2 = self.body.position + self.shape.b.rotated(self.body.angle)
        pygame.draw.line(window, 'black', point1, point2, int(self.shape.radius+4)) # Bust
        pygame.draw.circle(window, 'black', self.body.position, self.head_shape.radius) # Head
        pygame.draw.circle(window, 'black', point2, self.shape.radius-2) # Round bottom of the bust


        

class Member:

    def __init__(self, body: pymunk.Body, shape: pymunk.Segment, pin: pymunk.PivotJoint, motor: pymunk.SimpleMotor, original_max_force: int) -> None:
        
        self.body = body
        self.shape = shape
        self.pin = pin
        self.motor = motor
        self.original_max_force = original_max_force


    def print(self, window):
        
        point1 = self.body.position + self.shape.a.rotated(self.body.angle)
        point2 = self.body.position + self.shape.b.rotated(self.body.angle)
        pygame.draw.line(window, 'black', point1, point2, int(self.shape.radius+4)) # Member
        pygame.draw.circle(window, 'black', point2, self.shape.radius-1) # Round end of the member
