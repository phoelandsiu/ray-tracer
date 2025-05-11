from canvas import *
from tuples import *

start = Point(0, 1, 0)
velocity = Vector(1, 1.8, 0)
velocity = velocity.normalize().multiply(11.25)
proj = Projectile(start, velocity)
gravity = Vector(0, -0.1, 0)
wind = Vector(-0.01, 0, 0)
env = Environment(gravity, wind)

canvas = Canvas(900,550)
color = (1, 0, 0) # Red color

while proj.position.y > 0:
    x = int(proj.position.x)
    # Flip y to match canvas coordinates
    y = canvas.height - int(proj.position.y)
    if 0 <= x < canvas.width and 0 <= y < canvas.height:
        canvas.write_pixel(x, y, color)
    proj = proj.tick(env, proj)

with open("projectile.ppm", "w") as f:
    f.write(canvas.canvas_to_ppm())