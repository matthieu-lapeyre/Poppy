'''
 Ddeplacemnt of the head Poppy to contact
 
 Author : H. Guermoule
'''
from __future__ import division

import pypot.primitive



class Sound_Detect_Motion(pypot.primitive.Primitive):
    '''
     primitive to make Poppy will return to contact
    '''
    def setup(self): 
        self.robot.compliant = False 
        self.robot.power_up() 

    def run(self):
		if (self.which_side == 'Left_Side'):
			self.robot.head_y.goal_position = 0
			self.robot.head_z.goal_position = 45
		elif (self.which_side == 'Right_Side') :
			self.robot.head_y.goal_position = 0
			self.robot.head_z.goal_position = -45
		elif (self.which_side == 'Center_Side') :
			self.robot.head_y.goal_position = 0
			self.robot.head_z.goal_position = 0
 
		
