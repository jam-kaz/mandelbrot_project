class MandelbrotModel:

    def __init__(self, width=800, height=600, max_iter=50):
        self.width = width
        self.height = height
        self.max_iter = max_iter
        self.xmin, self.xmax = -2.0, 2.0
        self.ymin, self.ymax = -1.5, 1.5

    def reset_zoom(self):
        self.xmin, self.xmax = -2.0, 2.0
        self.ymin, self.ymax = -1.5, 1.5

    def generate_image_data(self):
        data = []
        for y in range(self.height):
            row = []
            cy = self.ymin + (y / self.height) * (self.ymax - self.ymin)
            for x in range(self.width):
                cx = self.xmin + (x / self.width) * (self.xmax - self.xmin)
                zx, zy = 0.0, 0.0
                iteration = 0
                while zx * zx + zy * zy <= 4.0 and iteration < self.max_iter:
                    xtemp = zx * zx - zy * zy + cx
                    zy = 2.0 * zx * zy + cy
                    zx = xtemp
                    iteration += 1
                if iteration == self.max_iter:
                    row.append("#000000")
                else:
                    intensity = int((iteration / self.max_iter) * 255)
                    row.append(f"#{intensity:02x}0000")
            data.append(row)
        return data

    def zoom(self, start_x, start_y, end_x, end_y):
        x1 = max(0, min(start_x, self.width))
        x2 = max(0, min(end_x, self.width))
        y1 = max(0, min(start_y, self.height))
        y2 = max(0, min(end_y, self.height))
        real_start_x, real_end_x = min(x1, x2), max(x1, x2)
        real_start_y, real_end_y = min(y1, y2), max(y1, y2)
        if (real_end_x - real_start_x) < 5 or (real_end_y - real_start_y) < 5:
            return
        new_xmin = self.xmin + (real_start_x / self.width) * (self.xmax - self.xmin)
        new_xmax = self.xmin + (real_end_x / self.width) * (self.xmax - self.xmin)
        new_ymin = self.ymin + (real_start_y / self.height) * (self.ymax - self.ymin)
        new_ymax = self.ymin + (real_end_y / self.height) * (self.ymax - self.ymin)
        self.xmin, self.xmax = new_xmin, new_xmax
        self.ymin, self.ymax = new_ymin, new_ymax
