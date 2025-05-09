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
        value = round(value * 255)
        return max(0, min(255, int(value)))
    
    def scale_and_clamp_color(self, color: tuple) -> tuple:
        """Scales and clamps the color tuple to the range [0, 255]."""
        return tuple(self.scale_and_clamp(c) for c in color)
    
    def pixel_to_ppm(self):
        """Converts pixel data to PPM string."""
        lines = []
        for row in self.canvas:
            current_line = ""
            for pixel in row:
                scaled = self.scale_and_clamp_color(pixel)
                for component in scaled:
                    value_str = str(component)
                    # Check if adding this value would exceed 70 characters
                    if len(current_line) + len(value_str) + (1 if current_line else 0) > 70:
                        lines.append(current_line) # Append current line as is
                        current_line = value_str # Start a new line with the current value
                    else: 
                        current_line += (" " if current_line else "") + value_str # Add space if not the first value
            if current_line: # Append remaining values in the current line
                lines.append(current_line)
        return "\n".join(lines)

    def canvas_to_ppm(self):
        """Converts the canvas to PPM format."""
        header = f"P3\n{self.width} {self.height}\n255"
        body = self.pixel_to_ppm()
        return header + "\n" + body + "\n"