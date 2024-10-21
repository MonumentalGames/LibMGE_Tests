import MGE  # Import the LibMGE

MGE.init()  # Initialize the library

window = MGE.Window(resolution=(500, 500), flags=MGE.WindowFlag.Shown)  # Create window
window.frameRateLimit = 60  # Set frame rate limit

gif = MGE.Object2D((0, 0), 0, (500, 500))
gif.material = MGE.Material(MGE.Texture(MGE.LoadImage("./image.gif")))

gif_positions = [(0, 0), (250, 0), (250, 250), (0, 250)]  # Positions for smaller gif

scene = 0

while True:
    MGE.update()  # Update logic
    window.update()  # Update window

    window.title = f"LibMGE TestGif | FPS: {window.frameRate}"  # Display FPS

    if MGE.QuitEvent() or MGE.keyboard(MGE.KeyboardButton.F1):  # Exit if quit event or F1 key is pressed
        exit()

    if MGE.MouseButton():
        scene = (scene + 1) % 5

    if scene < 4:
        gif.size = (500, 500)
        gif.location = (0, 0)
        gif.rotation = 90 * scene
        gif.drawObject(window)
    else:
        gif.size = (250, 250)
        for i, pos in enumerate(gif_positions):
            if gif in window.drawnObjects:
                window.drawnObjects.remove(gif)
            gif.location = pos
            gif.rotation = 90 * i
            gif.drawObject(window)
