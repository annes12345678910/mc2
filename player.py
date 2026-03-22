import ultimateraylib as rl

class Player:
    def __init__(self) -> None:
        self.camera = rl.make_camera(
            rl.Vector3(0,1,0),
            rl.Vector3(1,0,0),
            rl.Vector3(0,1,0),
            60,
            rl.CAMERA_PERSPECTIVE
        )
    
    def update(self):
        rl.update_camera(self.camera, rl.CAMERA_FREE)