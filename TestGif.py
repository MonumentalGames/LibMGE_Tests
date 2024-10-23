import MGE  # Import the LibMGE

MGE.init()  # Initialize the library

window = MGE.Window(resolution=(500, 500), flags=MGE.WindowFlag.Shown)  # Create window
window.frameRateLimit = 60  # Set frame rate limit

gif = MGE.Object2D((0, 0), 0, (500, 500))  # Create a 2D object
gif.material = MGE.Material(MGE.Texture(MGE.LoadImage("./image.gif")))  # Load the GIF and assign to object

gif_positions = [(0, 0), (250, 0), (250, 250), (0, 250)]  # Positions for smaller gif

scene = 0

while True:
    MGE.update()  # Update logic
    window.update()  # Update window

    window.title = f"LibMGE TestGif | FPS: {window.frameRate}"  # Display FPS

    if MGE.QuitEvent() or MGE.keyboard(MGE.KeyboardButton.F1):  # Exit if quit event or F1 key is pressed
        exit()

    if MGE.MouseButton():  # By default it checks if the left button was pressed
        scene = (scene + 1) % 5

    if scene < 4:
        gif.size = (500, 500)  # Set object size
        gif.location = (0, 0)  # Set object location
        gif.rotation = 90 * scene  # Set object rotation
        gif.drawObject(window)  # Draw GIF object on window
    else:
        gif.size = (250, 250)  # Set object size
        for i, pos in enumerate(gif_positions):
            if gif in window.drawnObjects:  # Checks if the object has already been drawn in the window
                window.drawnObjects.remove(gif)  # Remove object from the list of already drawn objects to force it to be drawn again
            gif.location = pos  # Set object location
            gif.rotation = 90 * i  # Set object rotation
            gif.drawObject(window)  # Draw GIF object on window
