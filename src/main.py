import sys, random
import pygame
import pymunk
import pymunk.pygame_util
from classes.stickman import Stickman
import math

#region Parameters of the simulation
pygame.init()
pygame.display.set_caption("RunningDeepRL")
WIDTH, HEIGHT = 1800, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
#random.seed(1)
#endregion

def run(window, width, height) -> None:
    #region Paramaters of the run
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps 

    space = pymunk.Space()
    space.gravity = (0.0, 981)
    #endregion

    #region Ground
    ground_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    ground_body.position = (width/2, height-100)
    ground_shape = pymunk.Poly.create_box(ground_body, (width, 200))
    ground_shape.friction = 0.75
    space.add(ground_body, ground_shape)
    #endregion

    #region Stickman
    stickman = Stickman(height)
    stickman.draw(space)
    stickman.rotate_member_articulation(stickman.lower_left_leg_motor, 4)
    stickman.rotate_member_articulation(stickman.lower_right_leg_motor, 3.7)
    stickman.rotate_member_articulation(stickman.upper_left_leg_motor, 4.2)
    stickman.rotate_member_articulation(stickman.upper_right_leg_motor, 4.1)
    stickman.rotate_member_articulation(stickman.left_arm_motor, 3.9)
    stickman.rotate_member_articulation(stickman.right_arm_motor, 4.15)
    stickman.rotate_member_articulation(stickman.left_forearm_motor, 4.05)
    stickman.rotate_member_articulation(stickman.right_forearm_motor, 3.85)
    #endregion

    #region Run loop management
    draw_options = pymunk.pygame_util.DrawOptions(window)
    translation = pymunk.Transform()
    pause = False
    while run:
        #region Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = not pause
        #endregion

        #region Keys
        keys = pygame.key.get_pressed()
        left = int(keys[pygame.K_LEFT])
        right = int(keys[pygame.K_RIGHT])
        #endregion

        #region Camera management
        translate_speed = 10
        translation = translation.translated(
           translate_speed * left - translate_speed * right,
            0,
        )

        draw_options.transform = (
                    pymunk.Transform.translation(300, 300)
                    @ translation
                    @ pymunk.Transform.translation(-300, -300)
                )
        #endregion

        draw(space, window, draw_options)

        if not pause:
            space.step(dt)
            pygame.display.flip()
            clock.tick(fps)
    #endregion

    pygame.quit() 


def draw(space, window, draw_options) -> None:
    '''
    Update and draw objects on the screen
    '''
    window.fill('white')
    space.debug_draw(draw_options)
    pygame.display.update()

if __name__ == '__main__':
    run(window, WIDTH, HEIGHT)
