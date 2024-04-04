import MGE

MGE.init()

window = MGE.Window()
internal_camera = MGE.Camera()

text_location = MGE.ObjectText((10, 10), 0, 15, "0x | 0y")
text_location._text_render_type = 1

color = MGE.Color((60, 60, 66))

speed = 10

while True:
    MGE.update()
    window.update(True)

    window.title = f"LibMGE Grid | FPS: {int(window.fps)}"

    if MGE.QuitEvent() or MGE.keyboard(MGE.KeyboardButton.F1):
        exit()

    if MGE.keyboard(MGE.KeyboardButton.KeyW):
        internal_camera.motionTimeStart(2)
    if MGE.keyboard(MGE.KeyboardButton.KeyW, True):
        internal_camera.motion(2, speed)

    if MGE.keyboard(MGE.KeyboardButton.KeyA):
        internal_camera.motionTimeStart(1)
    if MGE.keyboard(MGE.KeyboardButton.KeyA, True):
        internal_camera.motion(1, speed)

    if MGE.keyboard(MGE.KeyboardButton.KeyS):
        internal_camera.motionTimeStart(2)
    if MGE.keyboard(MGE.KeyboardButton.KeyS, True):
        internal_camera.motion(2, -speed)

    if MGE.keyboard(MGE.KeyboardButton.KeyD):
        internal_camera.motionTimeStart(1)
    if MGE.keyboard(MGE.KeyboardButton.KeyD, True):
        internal_camera.motion(1, -speed)

    window.clear(color=(40, 40, 40, 255))

    if "Line3996" not in window.draw_objects:
        window.draw_objects.append("Line3996")
        window_size, camera_location = window.logicalResolution, internal_camera.location

        for n in range(window_size[1] // 50 + 2):
            start = [(camera_location[0] * -1) + camera_location[0], (50 * int(camera_location[1] * -1 // 50) + 50 * n) + camera_location[1]]
            end = [start[0] + window_size[0], start[1]]
            window.drawLine(start, end, 1, color)

        for n in range(window_size[0] // 50 + 2):
            start = [(50 * int(camera_location[0] * -1 // 50) + 50 * n) + camera_location[0], (camera_location[1] * -1) + camera_location[1]]
            end = [start[0], start[1] + window_size[1]]
            window.drawLine(start, end, 1, color)

    text_location.text = f"{internal_camera.location[0] * -1}x | {internal_camera.location[1]}y"
    text_location.draw_object(window)
