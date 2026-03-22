import ultimateraylib as rl
import player
def draw_space(player: player.Player):
    player.update()
    rl.clear_background(rl.BLACK)

    rl.begin_mode_3d(player.camera)
    rl.draw_grid(10, 1)
    rl.draw_cube(rl.Vector3(0,0,0), 1, 1, 1, rl.WHITE)
    rl.end_mode_3d()