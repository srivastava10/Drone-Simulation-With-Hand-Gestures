# Drone Simulation Using Ursina Engine

from ursina import *
from ursina.shaders import lit_with_shadows_shader
app = Ursina()
window.title = 'Drone Simulation'
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True


player = Entity(model='drone-obj/drone.obj',color=color.white,scale=1,shaders=lit_with_shadows_shader)

#For the model above, you can use any other drone model.


e=EditorCamera()


pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True)
plane = Entity(model='plane', scale=1000)

def update():
	player.x += held_keys['d'] * 0.1
	player.x -= held_keys['a'] * 0.1
	
	player.y += held_keys['w'] * 2
	player.y -= held_keys['s'] * 2
	
	player.z += held_keys['j'] * 0.4
	player.z -= held_keys['k'] * 0.4
	
	
	
app.run()
