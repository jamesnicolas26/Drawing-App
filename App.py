import tkinter as tk

def paint(event):
    """Draw on the canvas."""
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=3)

def create_drawing_app():
    """Create a simple drawing app GUI."""
    root = tk.Tk()
    root.title("Drawing App")

    global canvas
    canvas = tk.Canvas(root, width=500, height=500, bg="white")
    canvas.pack()

    canvas.bind("<B1-Motion>", paint)

    root.mainloop()

if __name__ == "__main__":
    create_drawing_app()
