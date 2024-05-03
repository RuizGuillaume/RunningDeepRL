import pymunk

class Stickman:
    def __init__(self, height) -> None:
        
        #region Members init

        body_friction = 1
        max_force_arms = 1000000
        max_force_legs = 2000000

        #region Bust and head
        bust_body = pymunk.Body()
        bust_body.position = (300, height-400)
        bust_shape = pymunk.Segment(bust_body, (0, 0), (0, 100), 6)
        bust_shape.friction = body_friction
        bust_shape.mass = 26
        head_shape = pymunk.Circle(bust_body, 15, (0, -15))
        head_shape.friction = body_friction
        head_shape.mass = 4
        self.bust_body = bust_body
        self.bust_shape = bust_shape
        self.head_shape = head_shape
        #endregion

        #region Left arm
        # Arm
        left_arm_body = pymunk.Body()
        left_arm_body.position = bust_body.position
        left_arm_shape = pymunk.Segment(left_arm_body, (0, 0), (-35, 35), 5.0)
        left_arm_shape.friction = body_friction
        left_arm_shape.mass = 3
        left_arm_pin = pymunk.PivotJoint(bust_body, left_arm_body, left_arm_body.position) 
        left_arm_motor = pymunk.SimpleMotor(bust_body, left_arm_body, 0)
        left_arm_motor.max_force = max_force_arms
        self.left_arm_body = left_arm_body
        self.left_arm_shape = left_arm_shape
        self.left_arm_pin = left_arm_pin
        self.left_arm_motor = left_arm_motor

        # Forearm
        left_forearm_body = pymunk.Body()
        left_forearm_body.position = left_arm_body.position + left_arm_shape.b
        left_forearm_shape = pymunk.Segment(left_forearm_body, (0, 0), (-35, 35), 5.0)
        left_forearm_shape.friction = body_friction
        left_forearm_shape.mass = 3
        left_forearm_pin = pymunk.PivotJoint(left_arm_body, left_forearm_body, left_forearm_body.position) 
        left_forearm_motor = pymunk.SimpleMotor(left_arm_body, left_forearm_body, 0)
        left_forearm_motor.max_force = max_force_arms
        self.left_forearm_body = left_forearm_body
        self.left_forearm_shape = left_forearm_shape
        self.left_forearm_pin = left_forearm_pin
        self.left_forearm_motor = left_forearm_motor
        #endregion

        #region Right arm
        # Arm
        right_arm_body = pymunk.Body()
        right_arm_body.position = bust_body.position
        right_arm_shape = pymunk.Segment(right_arm_body, (0, 0), (35, 35), 5.0)
        right_arm_shape.friction = body_friction
        right_arm_shape.mass = 3
        right_arm_pin = pymunk.PivotJoint(bust_body, right_arm_body, right_arm_body.position) 
        right_arm_motor = pymunk.SimpleMotor(bust_body, right_arm_body, 0)
        right_arm_motor.max_force = max_force_arms
        self.right_arm_body = right_arm_body
        self.right_arm_shape = right_arm_shape
        self.right_arm_pin = right_arm_pin
        self.right_arm_motor = right_arm_motor

        # Forearm
        right_forearm_body = pymunk.Body()
        right_forearm_body.position = right_arm_body.position + right_arm_shape.b
        right_forearm_shape = pymunk.Segment(right_forearm_body, (0, 0), (35, 35), 5.0)
        right_forearm_shape.friction = body_friction
        right_forearm_shape.mass = 3
        right_forearm_pin = pymunk.PivotJoint(right_arm_body, right_forearm_body, right_forearm_body.position) 
        right_forearm_motor = pymunk.SimpleMotor(right_arm_body, right_forearm_body, 0)
        right_forearm_motor.max_force = max_force_arms
        self.right_forearm_body = right_forearm_body
        self.right_forearm_shape = right_forearm_shape
        self.right_forearm_pin = right_forearm_pin
        self.right_forearm_motor = right_forearm_motor
        #endregion

        #region Left leg
        # Upper
        upper_left_leg_body = pymunk.Body()
        upper_left_leg_body.position = bust_body.position + bust_shape.b
        upper_left_leg_shape = pymunk.Segment(upper_left_leg_body, (0, 0), (-35, 35), 5.0)
        upper_left_leg_shape.friction = body_friction
        upper_left_leg_shape.mass = 8
        upper_left_leg_pin = pymunk.PivotJoint(bust_body, upper_left_leg_body, upper_left_leg_body.position) 
        upper_left_leg_motor = pymunk.SimpleMotor(bust_body, upper_left_leg_body, 0)
        upper_left_leg_motor.max_force = max_force_legs
        self.upper_left_leg_body = upper_left_leg_body
        self.upper_left_leg_shape = upper_left_leg_shape
        self.upper_left_leg_pin = upper_left_leg_pin
        self.upper_left_leg_motor = upper_left_leg_motor

        # Lower
        lower_left_leg_body = pymunk.Body()
        lower_left_leg_body.position = upper_left_leg_body.position + upper_left_leg_shape.b
        lower_left_leg_shape = pymunk.Segment(lower_left_leg_body, (0, 0), (-35, 35), 5.0)
        lower_left_leg_shape.friction = body_friction
        lower_left_leg_shape.mass = 5
        lower_left_leg_pin = pymunk.PivotJoint(upper_left_leg_body, lower_left_leg_body, lower_left_leg_body.position) 
        lower_left_leg_motor = pymunk.SimpleMotor(upper_left_leg_body, lower_left_leg_body, 0)
        lower_left_leg_motor.max_force = max_force_legs
        self.lower_left_leg_body = lower_left_leg_body
        self.lower_left_leg_shape = lower_left_leg_shape
        self.lower_left_leg_pin = lower_left_leg_pin
        self.lower_left_leg_motor = lower_left_leg_motor
        #endregion
      
        #region Right leg
        # Upper
        upper_right_leg_body = pymunk.Body()
        upper_right_leg_body.position = bust_body.position + bust_shape.b
        upper_right_leg_shape = pymunk.Segment(upper_right_leg_body, (0, 0), (35, 35), 5.0)
        upper_right_leg_shape.friction = body_friction
        upper_right_leg_shape.mass = 8
        upper_right_leg_pin = pymunk.PivotJoint(bust_body, upper_right_leg_body, upper_right_leg_body.position) 
        upper_right_leg_motor = pymunk.SimpleMotor(bust_body, upper_right_leg_body, 0)
        upper_right_leg_motor.max_force = max_force_legs
        self.upper_right_leg_body = upper_right_leg_body
        self.upper_right_leg_shape = upper_right_leg_shape
        self.upper_right_leg_pin = upper_right_leg_pin
        self.upper_right_leg_motor = upper_right_leg_motor

        # Lower
        lower_right_leg_body = pymunk.Body()
        lower_right_leg_body.position = upper_right_leg_body.position + upper_right_leg_shape.b
        lower_right_leg_shape = pymunk.Segment(lower_right_leg_body, (0, 0), (35, 35), 5.0)
        lower_right_leg_shape.friction = body_friction
        lower_right_leg_shape.mass = 5
        lower_right_leg_pin = pymunk.PivotJoint(upper_right_leg_body, lower_right_leg_body, lower_right_leg_body.position) 
        lower_right_leg_motor = pymunk.SimpleMotor(upper_right_leg_body, lower_right_leg_body, 0)
        lower_right_leg_motor.max_force = max_force_legs
        self.lower_right_leg_body = lower_right_leg_body
        self.lower_right_leg_shape = lower_right_leg_shape
        self.lower_right_leg_pin = lower_right_leg_pin
        self.lower_right_leg_motor = lower_right_leg_motor
        #endregion

        #region Filter configuration to ignore collisions between stickman's body parts
        shape_filter = pymunk.ShapeFilter(group=1)
        self.bust_shape.filter = shape_filter
        self.head_shape.filter = shape_filter
        self.left_arm_shape.filter = shape_filter
        self.left_forearm_shape.filter = shape_filter
        self.right_arm_shape.filter = shape_filter
        self.right_forearm_shape.filter = shape_filter
        self.upper_left_leg_shape.filter = shape_filter
        self.lower_left_leg_shape.filter = shape_filter
        self.upper_right_leg_shape.filter = shape_filter
        self.lower_right_leg_shape.filter = shape_filter
        #endregion
        #endregion

    def draw(self, space: pymunk.Space) -> None:

        space.add(self.bust_body, self.bust_shape, self.head_shape,
                  self.left_arm_body, self.left_arm_shape, self.left_arm_pin, self.left_arm_motor,
                  self.left_forearm_body, self.left_forearm_shape, self.left_forearm_pin, self.left_forearm_motor,
                  self.right_arm_body, self.right_arm_shape, self.right_arm_pin, self.right_arm_motor,
                  self.right_forearm_body, self.right_forearm_shape, self.right_forearm_pin, self.right_forearm_motor,
                  self.upper_left_leg_body, self.upper_left_leg_shape, self.upper_left_leg_pin, self.upper_left_leg_motor,
                  self.lower_left_leg_body, self.lower_left_leg_shape, self.lower_left_leg_pin, self.lower_left_leg_motor,
                  self.upper_right_leg_body, self.upper_right_leg_shape, self.upper_right_leg_pin, self.upper_right_leg_motor,
                  self.lower_right_leg_body, self.lower_right_leg_shape, self.lower_right_leg_pin, self.lower_right_leg_motor
        )

    def rotate_member_articulation(self, member: pymunk.SimpleMotor, rate: int) -> None:
        member.rate = rate