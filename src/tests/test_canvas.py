import sys
import os
import pytest

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from core.canvas import Canvas

@pytest.fixture
def setup_canvas():
    """Fixture to set up a canvas for testing."""
    width = 10
    height = 20
    canvas = Canvas(width, height)
    return canvas

def test_canvas_initialization(setup_canvas):
    """Test the initialization of the canvas."""
    canvas = setup_canvas
    assert canvas.width == 10
    assert canvas.height == 20
    assert len(canvas.canvas) == 20
    assert len(canvas.canvas[0]) == 10
    assert all(pixel == (0,0,0) for row in canvas.canvas for pixel in row)

def test_write_pixel(setup_canvas):
    """Test setting a pixel color on canvas."""
    canvas = setup_canvas
    canvas.write_pixel(5, 10, (255, 0, 0))
    assert canvas.canvas[10][5] == (255, 0, 0)
    canvas.write_pixel(9, 15, (0, 255, 0))
    assert canvas.canvas[15][9] == (0, 255, 0)

def test_canvas_to_ppm(setup_canvas):
    """Test the conversion of canvas to PPM format."""
    canvas = Canvas(5, 3)
    canvas.write_pixel(0, 0, (1.5, 0, 0))
    canvas.write_pixel(2, 1, (0, 0.5, 0))
    canvas.write_pixel(4, 2, (-0.5, 0, 1))

    ppm_output = canvas.canvas_to_ppm()
    expected_header = f"P3\n{canvas.width} {canvas.height}\n255\n"
    assert ppm_output.startswith(expected_header)

    expected_body = "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n"
    expected_body += "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n"
    expected_body += "0 0 0 0 0 0 0 0 0 0 0 0 0 0 1\n"
    # expected_body += "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n" * (20 - 3)

    print("PPM Output:")
    print(ppm_output)
    assert ppm_output[len(expected_header):].startswith(expected_body)