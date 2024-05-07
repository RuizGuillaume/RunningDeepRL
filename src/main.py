import os, sys, random
import pygame
import pymunk
import pymunk.pygame_util
from classes.stickman import Stickman
import math

#region Parameters of the simulation
pygame.init()
pygame.display.set_caption("RunningDeepRL")
monitorInfos = pygame.display.Info()
WIDTH, HEIGHT = monitorInfos.current_w, monitorInfos.current_h
window = pygame.display.set_mode((WIDTH, HEIGHT))
GROUND_Y = HEIGHT*0.92

#random.seed(1)
#endregion

def run(window, width, height) -> None:
    #region Parameters of the run
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps

    space = pymunk.Space()
    space.gravity = (0.0, 981)
    #endregion


    #region Ground
    ground_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    ground_body.position = (0, GROUND_Y)
    ground_shape = pymunk.Poly.create_box(ground_body, (12000, 50))
    ground_shape.friction = 0.75
    ground_shape_back = pymunk.Poly.create_box(ground_body, (1, 3000))
    ground_shape_back.friction = 0.75
    space.add(ground_body, ground_shape, ground_shape_back)

    background_img = pygame.image.load("content/imgs/Background.jpg").convert_alpha()
    multiplier_for_fullscreen = height/background_img.get_height()
    background_img = pygame.transform.scale(background_img, (background_img.get_width()*multiplier_for_fullscreen, background_img.get_height()*multiplier_for_fullscreen))  
    #endregion

    #region Stickman
    stickman = Stickman(width/5, GROUND_Y)
    stickman.draw(space)
    shadow = pygame.Surface((width, height), pygame.SRCALPHA)
    #endregion

    #region Score text
 
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
        pressZ = int(keys[pygame.K_z])        
        #endregion

        if pressZ :
            stickman.rotate_member_articulation(stickman.upper_right_leg, -4)
            stickman.rotate_member_articulation(stickman.upper_left_leg, 4)
            stickman.rotate_member_articulation(stickman.lower_right_leg, 4)
            stickman.rotate_member_articulation(stickman.lower_left_leg, 4)
            stickman.rotate_member_articulation(stickman.left_arm, -4)
            stickman.rotate_member_articulation(stickman.left_forearm, 4)
            stickman.rotate_member_articulation(stickman.right_arm, 4)
            stickman.rotate_member_articulation(stickman.right_forearm, 4)


        #region Camera management
        # if keys[pygame.K_LEFT]:
        #     camera_speed = -3
        #     for shape in space.shapes:
        #         if isinstance(shape.body, pymunk.Body):
        #             shape.body.position -= (camera_speed, 0)
                    
        # elif keys[pygame.K_RIGHT]:
        #     camera_speed = 3
        #     for shape in space.shapes:
        #         if isinstance(shape.body, pymunk.Body):
        #             shape.body.position -= (camera_speed, 0)

        # else:
        #     center_x = width/2
        #     for shape in space.shapes:
        #         if isinstance(shape.body, pymunk.Body):
        #             body_x = shape.body.position[0]
        #             shape.body.position += (center_x - body_x , 0)


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
        #print(clock.get_fps())
        draw(space, window, draw_options, stickman, background_img, shadow)

        if not pause:
            space.step(dt)
            clock.tick(fps)
    #endregion

    pygame.quit() 


def draw(space, window, draw_options, stickman, background_img, shadow) -> None:
    '''
    Update and draw objects on the screen
    '''
    window.fill('white')
    window.blit(background_img, (0, 0))


    #space.debug_draw(draw_options)

    stickman.print(window)
    
    window.blit(shadow, (0,0))
    shadow.fill((0,0,0,0))
    pygame.draw.ellipse(shadow, (0, 0, 0, 80), (((stickman.bust.body.position[0]+stickman.upper_left_leg.body.position[0])/2)-60, GROUND_Y-35, 120, 30))
    print(stickman.bust.body.position)
    pygame.display.update()


if __name__ == '__main__':
    run(window, WIDTH, HEIGHT)
