try:
    import MGE.MGE_109 as MGE
except:
    import MGE

line = MGE.Object2D([100, 100], 0, [100, 1])
Material = MGE.Material(color=(60, 60, 66))
line.set_material(Material)
text_location = MGE.ObjectText((0, 0), 15, "0x | 0y", "verdana")

speed = 1

def logic_base():
    if MGE.Program.event.type == MGE.Program.pygame.QUIT:
        Program.loop = False

    MGE.Program.set_caption(f"Grid-MGE | FPS:{int(MGE.Program.get_fps())}")
    MGE.Program.update(False, False)

def logic():
    logic_base()

    if MGE.Keyboard.keyboard("w"):
        Program.internal_camera.set_location([Program.internal_camera.get_location()[0], Program.internal_camera.get_location()[1] + speed])

    if MGE.Keyboard.keyboard("a"):
        Program.internal_camera.set_location([Program.internal_camera.get_location()[0] + speed, Program.internal_camera.get_location()[1]])

    if MGE.Keyboard.keyboard("s"):
        Program.internal_camera.set_location([Program.internal_camera.get_location()[0], Program.internal_camera.get_location()[1] - speed])

    if MGE.Keyboard.keyboard("d"):
        Program.internal_camera.set_location([Program.internal_camera.get_location()[0] - speed, Program.internal_camera.get_location()[1]])

def draw():
    MGE.Program.screen.screen.fill((40, 40, 40))

    screen_size = MGE.Program.Temp.Resolution
    camera_location = Program.internal_camera.get_location()

    for n in range(int(screen_size[1] / 50) + 2):
        loc = [camera_location[0] * -1, 50 * int(camera_location[1] * -1 / 50) + 50 * n]
        if loc[1] < screen_size[1] + camera_location[1] * -1:
            line.set_localization(loc)
            line.set_size([screen_size[0], 1])
            line.draw_object(MGE.Program.screen, Program.internal_camera)

    for n in range(int(screen_size[0] / 50) + 2):
        loc = [50 * int(camera_location[0] * -1 / 50) + 50 * n, camera_location[1] * -1]
        if loc[0] < screen_size[0] + camera_location[0] * -1:
            line.set_localization(loc)
            line.set_size([1, screen_size[1]])
            line.draw_object(MGE.Program.screen, Program.internal_camera)

    text_location.set_text(f"Camera : {Program.internal_camera.get_location()[0] * -1}x | {Program.internal_camera.get_location()[1]}y")
    text_location.set_localization([0, 0])
    text_location.draw_object(MGE.Program.screen, True)

class Program:
    loop = False

    internal_camera = MGE.Camera()

    @staticmethod
    def start():
        try:
            MGE.Program.screen.set_size(1280, 720, "RESIZABLE")
            MGE.Program.set_clock(240)
            Program.android = True
        except:
            pass
        else:
            Program.loop = True
            Program.program_loop()

    @staticmethod
    def program_loop():
        while Program.loop:
            logic()
            if MGE.Program.event or MGE.keyboard("all"):
                draw()

Program.start()
