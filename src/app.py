import tkinter as tk
from src.models.mandelbrot_model import MandelbrotModel


class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Mandelbrot Set")
        self.model = MandelbrotModel()
        self.canvas = tk.Canvas(
            root, width=self.model.width, height=self.model.height, bg="black"
        )
        self.canvas.pack()
        self.img = tk.PhotoImage(width=self.model.width, height=self.model.height)
        self.canvas.create_image((0, 0), image=self.img, anchor="nw")
        self.start_x = None
        self.start_y = None
        self.rect_id = None
        
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        
        self.canvas.bind("<Button-2>", self.on_right_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.root.bind("<Escape>", self.on_right_click)
        
        self.render()

    def render(self):
        image_data = self.model.generate_image_data()
        format_data = " ".join("{" + " ".join(row) + "}" for row in image_data)
        self.img.put(format_data)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect_id = self.canvas.create_rectangle(
            self.start_x,
            self.start_y,
            self.start_x,
            self.start_y,
            outline="white",
            width=2,
        )

    def on_move_press(self, event):
        cur_x, cur_y = event.x, event.y
        self.canvas.coords(
            self.rect_id, self.start_x, self.start_y, cur_x, cur_y
        )

    def on_button_release(self, event):
        end_x, end_y = event.x, event.y
        self.canvas.delete(self.rect_id)
        self.model.zoom(self.start_x, self.start_y, end_x, end_y)
        self.render()

    def on_right_click(self, event):
        self.model.reset_zoom()
        self.render()
