import random
import bimpy

val = [random.randint(1, 1000)/random.randint(1, 100) for i in range(200)]


ctx = bimpy.Context()
ctx.init(800, 800, "Test")

while not ctx.should_close():
    ctx.new_frame()

    bimpy.set_next_window_pos(bimpy.Vec2(-5, -25), bimpy.Condition.Once)
    bimpy.set_next_window_size(bimpy.Vec2(810, 810), bimpy.Condition.Once)
    bimpy.begin("RPM")

    bimpy.plot_lines("", val, graph_size=bimpy.Vec2(690, 100))

    bimpy.end()

    ctx.render()
    val.reverse()
    val.append(random.randint(1, 1000)/random.randint(1, 100))
    val.pop(0)
    val.reverse()