import pygame
import pymunk
from classes.member import Member, Bust

class Stickman:
    def __init__(self, x, y) -> None:
        
        self.meters_traveled :int = 0
        self.initial_x :int = x
        #region Members init
        radius = 5
        body_friction = 1
        max_force_arms = 1500000
        max_force_legs = 3000000

        #region Bust and head
        bust_body = pymunk.Body()
        bust_body.position = (x, y-200)
        bust_shape = pymunk.Segment(bust_body, (0, 0), (0, 100), radius+1)
        bust_shape.friction = body_friction
        bust_shape.mass = 26
        head_shape = pymunk.Circle(bust_body, 15, (0, 0))
        head_shape.friction = body_friction
        head_shape.mass = 4

        self.bust = Bust(bust_body, bust_shape, head_shape)
        #endregion

        #region Left arm
        # Arm
        left_arm_body = pymunk.Body()
        left_arm_body.position = bust_body.position+(0,15)
        left_arm_shape = pymunk.Segment(left_arm_body, (0, 0), (-35, 35), radius)
        left_arm_shape.friction = body_friction
        left_arm_shape.mass = 3
        left_arm_pin = pymunk.PivotJoint(bust_body, left_arm_body, left_arm_body.position) 
        left_arm_motor = pymunk.SimpleMotor(bust_body, left_arm_body, 0)

        self.left_arm = Member(left_arm_body, left_arm_shape, left_arm_pin, left_arm_motor, max_force_arms)

        # Forearm
        left_forearm_body = pymunk.Body()
        left_forearm_body.position = left_arm_body.position + left_arm_shape.b
        left_forearm_shape = pymunk.Segment(left_forearm_body, (0, 0), (-35, 35), radius)
        left_forearm_shape.friction = body_friction
        left_forearm_shape.mass = 3
        left_forearm_pin = pymunk.PivotJoint(left_arm_body, left_forearm_body, left_forearm_body.position) 
        left_forearm_motor = pymunk.SimpleMotor(left_arm_body, left_forearm_body, 0)

        self.left_forearm = Member(left_forearm_body, left_forearm_shape, left_forearm_pin, left_forearm_motor, max_force_arms)
        #endregion

        #region Right arm
        # Arm
        right_arm_body = pymunk.Body()
        right_arm_body.position = bust_body.position+(0,15)
        right_arm_shape = pymunk.Segment(right_arm_body, (0, 0), (35, 35), radius)
        right_arm_shape.friction = body_friction
        right_arm_shape.mass = 3
        right_arm_pin = pymunk.PivotJoint(bust_body, right_arm_body, right_arm_body.position) 
        right_arm_motor = pymunk.SimpleMotor(bust_body, right_arm_body, 0)

        self.right_arm = Member(right_arm_body, right_arm_shape, right_arm_pin, right_arm_motor, max_force_arms)

        # Forearm
        right_forearm_body = pymunk.Body()
        right_forearm_body.position = right_arm_body.position + right_arm_shape.b
        right_forearm_shape = pymunk.Segment(right_forearm_body, (0, 0), (35, 35), radius)
        right_forearm_shape.friction = body_friction
        right_forearm_shape.mass = 3
        right_forearm_pin = pymunk.PivotJoint(right_arm_body, right_forearm_body, right_forearm_body.position) 
        right_forearm_motor = pymunk.SimpleMotor(right_arm_body, right_forearm_body, 0)

        self.right_forearm = Member(right_forearm_body, right_forearm_shape, right_forearm_pin, right_forearm_motor, max_force_arms)
        #endregion

        #region Left leg
        # Upper
        upper_left_leg_body = pymunk.Body()
        upper_left_leg_body.position = bust_body.position + bust_shape.b
        upper_left_leg_shape = pymunk.Segment(upper_left_leg_body, (0, 0), (-35, 35), radius)
        upper_left_leg_shape.friction = body_friction
        upper_left_leg_shape.mass = 8
        upper_left_leg_pin = pymunk.PivotJoint(bust_body, upper_left_leg_body, upper_left_leg_body.position) 
        upper_left_leg_motor = pymunk.SimpleMotor(bust_body, upper_left_leg_body, 0)

        self.upper_left_leg = Member(upper_left_leg_body, upper_left_leg_shape, upper_left_leg_pin, upper_left_leg_motor, max_force_legs)

        # Lower
        lower_left_leg_body = pymunk.Body()
        lower_left_leg_body.position = upper_left_leg_body.position + upper_left_leg_shape.b
        lower_left_leg_shape = pymunk.Segment(lower_left_leg_body, (0, 0), (-35, 35), radius)
        lower_left_leg_shape.friction = body_friction
        lower_left_leg_shape.mass = 5
        lower_left_leg_pin = pymunk.PivotJoint(upper_left_leg_body, lower_left_leg_body, lower_left_leg_body.position) 
        lower_left_leg_motor = pymunk.SimpleMotor(upper_left_leg_body, lower_left_leg_body, 0)

        self.lower_left_leg = Member(lower_left_leg_body, lower_left_leg_shape, lower_left_leg_pin, lower_left_leg_motor, max_force_legs)
        #endregion
      
        #region Right leg
        # Upper
        upper_right_leg_body = pymunk.Body()
        upper_right_leg_body.position = bust_body.position + bust_shape.b
        upper_right_leg_shape = pymunk.Segment(upper_right_leg_body, (0, 0), (35, 35), radius)
        upper_right_leg_shape.friction = body_friction
        upper_right_leg_shape.mass = 8
        upper_right_leg_pin = pymunk.PivotJoint(bust_body, upper_right_leg_body, upper_right_leg_body.position) 
        upper_right_leg_motor = pymunk.SimpleMotor(bust_body, upper_right_leg_body, 0)

        self.upper_right_leg = Member(upper_right_leg_body, upper_right_leg_shape, upper_right_leg_pin, upper_right_leg_motor, max_force_legs)

        # Lower
        lower_right_leg_body = pymunk.Body()
        lower_right_leg_body.position = upper_right_leg_body.position + upper_right_leg_shape.b
        lower_right_leg_shape = pymunk.Segment(lower_right_leg_body, (0, 0), (35, 35), radius)
        lower_right_leg_shape.friction = body_friction
        lower_right_leg_shape.mass = 5
        lower_right_leg_pin = pymunk.PivotJoint(upper_right_leg_body, lower_right_leg_body, lower_right_leg_body.position) 
        lower_right_leg_motor = pymunk.SimpleMotor(upper_right_leg_body, lower_right_leg_body, 0)

        self.lower_right_leg = Member(lower_right_leg_body, lower_right_leg_shape, lower_right_leg_pin, lower_right_leg_motor, max_force_legs)
        #endregion

        #region Filter configuration to ignore collisions between stickman's body parts
        shape_filter = pymunk.ShapeFilter(group=1)
        self.bust.shape.filter = shape_filter
        self.bust.head_shape.filter = shape_filter
        self.left_arm.shape.filter = shape_filter
        self.left_forearm.shape.filter = shape_filter
        self.right_arm.shape.filter = shape_filter
        self.right_forearm.shape.filter = shape_filter
        self.upper_left_leg.shape.filter = shape_filter
        self.lower_left_leg.shape.filter = shape_filter
        self.upper_right_leg.shape.filter = shape_filter
        self.lower_right_leg.shape.filter = shape_filter
        #endregion
        #endregion
        


    def draw(self, space: pymunk.Space) -> None:

        space.add(self.bust.body, self.bust.shape, self.bust.head_shape,
                  self.left_arm.body, self.left_arm.shape, self.left_arm.pin, self.left_arm.motor,
                  self.left_forearm.body, self.left_forearm.shape, self.left_forearm.pin, self.left_forearm.motor,
                  self.right_arm.body, self.right_arm.shape, self.right_arm.pin, self.right_arm.motor,
                  self.right_forearm.body, self.right_forearm.shape, self.right_forearm.pin, self.right_forearm.motor,
                  self.upper_left_leg.body, self.upper_left_leg.shape, self.upper_left_leg.pin, self.upper_left_leg.motor,
                  self.lower_left_leg.body, self.lower_left_leg.shape, self.lower_left_leg.pin, self.lower_left_leg.motor,
                  self.upper_right_leg.body, self.upper_right_leg.shape, self.upper_right_leg.pin, self.upper_right_leg.motor,
                  self.lower_right_leg.body, self.lower_right_leg.shape, self.lower_right_leg.pin, self.lower_right_leg.motor
        )


    def print(self, window: pygame.Surface) -> None:

        self.bust.print(window)
        self.left_arm.print(window)
        self.left_forearm.print(window)
        self.right_arm.print(window)
        self.right_forearm.print(window)
        self.upper_left_leg.print(window)
        self.lower_left_leg.print(window)
        self.upper_right_leg.print(window)
        self.lower_right_leg.print(window)


    def rotate_member_articulation(self, member: Member, rate: int) -> None:

        if rate >= -2 and rate <= 2:
            member.motor.max_force = 0
        else:
            member.motor.max_force = member.original_max_force

        member.motor.rate = rate


    def save_meters_traveled(self, total_camera_offset) -> None:
        
        meters_traveled = round((self.bust.body.position[0] - self.initial_x + total_camera_offset)/100, 0)
        if meters_traveled > self.meters_traveled : self.meters_traveled = meters_traveled


    def shift(self, dx) -> None:

        self.bust.body.position += (dx, 0)
        self.left_arm.body.position += (dx, 0)
        self.left_forearm.body.position += (dx, 0)
        self.right_arm.body.position += (dx, 0)
        self.right_forearm.body.position += (dx, 0)
        self.upper_left_leg.body.position += (dx, 0)
        self.lower_left_leg.body.position += (dx, 0)
        self.upper_right_leg.body.position += (dx, 0)
        self.lower_right_leg.body.position += (dx, 0)

        