import ultimateraylib as rl
import player
def draw_space(player: player.Player, e:rl.Model, r:rl.Texture2D):
    player.update()
    rl.clear_background(rl.BLACK)

    rl.begin_mode_3d(player.camera)
    rl.draw_grid(50, 1)
    #rl.draw_cube(rl.Vector3(0,0,0), 1, 1, 1, rl.WHITE)
    
    e.materials[0].maps[rl.MATERIAL_MAP_ALBEDO[0]].texture = r # pyright: ignore[reportIndexIssue]
    rl.draw_model(e, rl.Vector3(0,0,0), 1, rl.WHITE)
    rl.end_mode_3d()