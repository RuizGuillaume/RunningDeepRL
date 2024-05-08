import pygame
import pymunk
import pymunk.pygame_util
from classes.stickman import Stickman

def run(window, width, height) -> None:
    #region Parameters of the run
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps

    space = pymunk.Space()
    space.gravity = (0.0, 981)

    total_camera_offset = 0
    #endregion

    #region Ground and background
    ground_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    ground_body.position = (0, GROUND_Y)
    ground_shape = pymunk.Poly.create_box(ground_body, (120000, 50))
    ground_shape.friction = 0.75
    space.add(ground_body, ground_shape)

    ground_img = pygame.image.load("content/imgs/Ground.jpg").convert_alpha()
    img_witdh, img_height = ground_img.get_size()
    new_height = height-(GROUND_Y-(0.52*img_height))
    new_width = int(img_witdh * (new_height / img_height))
    ground_img = pygame.transform.smoothscale(ground_img, (new_width, new_height))
    ground_position = pymunk.Vec2d(0, HEIGHT-ground_img.get_height())


    background_img = pygame.image.load("content/imgs/Background.jpg").convert_alpha()
    img_witdh, img_height = background_img.get_size()
    new_height = height-ground_img.get_height()
    new_width = int(img_witdh * (new_height / img_height))
    background_img = pygame.transform.smoothscale(background_img, (new_width, new_height))
    background_position = pymunk.Vec2d(0, 0)

    decoration = {"Ground_image" : ground_img,
                  "Background_image" : background_img,
                  "Ground_position": ground_position,
                  "Background_position" : background_position
                 }
    #endregion

    #region Stickman
    stickman = Stickman(width/5, GROUND_Y)
    stickman.draw(space)
    shadow = pygame.Surface((150, 40), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow, (0, 0, 0, 40), shadow.get_rect())
    shadow_infos = {"Surface" : shadow}
    #endregion

    #region Run loop management
    draw_options = pymunk.pygame_util.DrawOptions(window)
    pause = False
    follow_cam_mode = True
    while run:

        #region Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = not pause
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                follow_cam_mode = not follow_cam_mode
        #endregion

        #region Keys
        keys = pygame.key.get_pressed()
        pressZ = int(keys[pygame.K_z])        
        #endregion

        if pressZ :
            stickman.rotate_member_articulation(stickman.upper_right_leg, -4)
            stickman.rotate_member_articulation(stickman.upper_left_leg, -4)
            stickman.rotate_member_articulation(stickman.lower_right_leg, -4)
            stickman.rotate_member_articulation(stickman.lower_left_leg, -4)
            stickman.rotate_member_articulation(stickman.left_arm, -4)
            stickman.rotate_member_articulation(stickman.left_forearm, 4)
            stickman.rotate_member_articulation(stickman.right_arm, -4)
            stickman.rotate_member_articulation(stickman.right_forearm, 4)

        if not pause:
                
            #region Camera management
            if keys[pygame.K_LEFT]:
                follow_cam_mode = False
                total_camera_offset = move_camera(total_camera_offset, -80, stickman, decoration)                   
            elif keys[pygame.K_RIGHT]:
                follow_cam_mode = False
                total_camera_offset = move_camera(total_camera_offset, 80, stickman, decoration)
            elif follow_cam_mode:
                total_camera_offset = move_camera(total_camera_offset, stickman.bust.body.position[0]-(width/2), stickman, decoration)
            #endregion

            #region Text zone
            surfaces_text = []
            
            stickman.save_meters_traveled(total_camera_offset)
            meters = int(stickman.meters_traveled)
            text = f"Distance traveled : {meters} meter{'s' if meters >=2 else ''}"
            surfaces_text.append(font.render(text, True, 'white'))

            text = "[F] Camera follow mode"
            surfaces_text.append(font.render(text, True, 'white' if follow_cam_mode else 'red'))

            text = "[Left/Right arrow] Move camera"
            surfaces_text.append(font.render(text, True, 'white'))
            #endregion

            shadow_infos['Rect'] = (shadow.get_rect(center = (((stickman.bust.body.position[0]+stickman.upper_left_leg.body.position[0])/2), GROUND_Y-25)))

            draw(space, draw_options, window, stickman, decoration, surfaces_text, shadow_infos)

            space.step(dt)
            clock.tick(fps)
            #print(clock.get_fps())
    #endregion

    pygame.quit()


def draw(space, draw_options, window, stickman, decoration, surfaces_text, shadow_infos) -> None:
    '''
    Update and draw objects on the screen
    '''
    window.blit(decoration["Ground_image"], decoration["Ground_position"])
    window.blit(decoration["Background_image"], decoration["Background_position"])
    
    window.blit(shadow_infos['Surface'], shadow_infos['Rect'])
    
    stickman.print(window)

    for i, surface_text in enumerate(surfaces_text):
        window.blit(surface_text, (20, 20+(35*i)))

    #space.debug_draw(draw_options)

    pygame.display.update()


def move_camera(total_camera_offset: int, camera_offset: int, stickman: Stickman, decoration: dict) -> int:
    '''
    Move all visible objects (stickman and decorations) in the opposite direction of the offset to simulate a camera 
    '''

    if total_camera_offset+camera_offset <= 0 :
        camera_offset += total_camera_offset
    elif total_camera_offset+camera_offset >= 10000 :
        camera_offset += total_camera_offset
    else :
        total_camera_offset += camera_offset

        stickman.shift(-camera_offset)
        decoration["Ground_position"] -= (camera_offset, 0) 
        decoration["Background_position"] -= (camera_offset/5, 0)
   
    return total_camera_offset


if __name__ == '__main__':
    #region Parameters of the simulation
    pygame.init()
    pygame.display.set_caption("RunningDeepRL")
    monitorInfos = pygame.display.Info()
    WIDTH, HEIGHT = monitorInfos.current_w, monitorInfos.current_h
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    GROUND_Y = HEIGHT*0.94
    font = pygame.font.Font(None, 36)
    #endregion
    run(window, WIDTH, HEIGHT)
