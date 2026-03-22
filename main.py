import ultimateraylib as rl

import space
import player

me = player.Player()
cursor = False

e = rl.load_model("assets/models/planet.glb")

def main():
    global cursor
    rl.set_config_flags(rl.FLAG_WINDOW_RESIZABLE)
    rl.init_window(title="Minecraft 2")
    rl.set_target_fps(60)
    rl.init_audio_device()
    rl.disable_cursor()

    while not rl.window_should_close():
        if rl.is_key_pressed(rl.KEY_M):
            if cursor:
                rl.disable_cursor()
            else:
                rl.enable_cursor()
            cursor = not cursor

        rl.begin_drawing()
        space.draw_space(me)
        rl.end_drawing()
    rl.close_audio_device()
    rl.close_window()

if __name__ == "__main__":
    main()
