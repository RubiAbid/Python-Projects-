'''Implement an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. 
We then create an eraser rectangle which, when dragged around the canvas, sets all of the 
rectangles it is in contact with to white.'''


import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    # Get the current position of the eraser
    x1, y1, x2, y2 = canvas.coords(eraser)
    
    # Find all items overlapping with the eraser
    overlapping_items = canvas.find_overlapping(x1, y1, x2, y2)
    
    # Change the color of overlapping items to white
    for item in overlapping_items:
        if item != eraser:
            canvas.itemconfig(item, fill='white')

def on_mouse_move(event):
    # Move the eraser to follow the mouse cursor
    x = event.x
    y = event.y
    canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    erase_objects(canvas, eraser)

# Create the main window
root = tk.Tk()
root.title("Canvas Eraser")

# Create the canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Create a grid of blue rectangles (cells)
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue', outline='purple')

# Create the eraser rectangle
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink', outline='black')

# Bind mouse movement to the on_mouse_move function
canvas.bind('<Motion>', on_mouse_move)

# Start the Tkinter event loop
root.mainloop()
