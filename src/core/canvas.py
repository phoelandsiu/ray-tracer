class Canvas:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # Initialize canvas with black pixels
        self.canvas = [[(0,0,0) for _ in range(width)] for _ in range(height)]

    def write_pixel(self, x: int, y: int, color: tuple):
        """Sets the color of a pixel at (x,y) on the canvas to the specified color."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.canvas[y][x] = color
        else:
            raise ValueError("Pixel coordinates out of bounds")

    def draw(self):
        """Prints text-based representation of the canvas."""
        for row in self.canvas:
            print(" ".join(f"{pixel}" for pixel in row))

    def scale_and_clamp(self, value: float) -> int:
        """Scales and clams the value to the range [0, 255]."""
        # scaled = int(value * 255)
        if isinstance(value, float):
            value = round(value * 255)
        return max(0, min(255, int(value)))
    
    def scale_and_clamp_color(self, color: tuple) -> tuple:
        """Scales and clamps the color tuple to the range [0, 255]."""
        return tuple(self.scale_and_clamp(c) for c in color)
    
    def pixel_to_ppm(self):
        """Converts pixel data to PPM string."""
        lines = []
        for row in self.canvas:
            line_values = []
            for pixel in row:
                scaled = self.scale_and_clamp_color(pixel)
                line_values.extend(str(c) for c in scaled)
            lines.append(" ".join(line_values))
        return "\n".join(lines)

    def canvas_to_ppm(self):
        """Converts the canvas to PPM format."""
        header = f"P3\n{self.width} {self.height}\n255"
        body = self.pixel_to_ppm()
        return header + "\n" + body + "\n"