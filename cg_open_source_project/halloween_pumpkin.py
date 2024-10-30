import math
import cairo

# Set canvas size
WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)


def draw_sphere(context, center_x, center_y, radius):
    # Draw a 3D-looking orange sphere using radial gradient
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x - radius * 0.4, center_y - radius * 0.4, radius * 0.1,
                                    center_x, center_y, radius)

    # Adjust the colors to shades of orange with deeper contrast
    gradient.add_color_stop_rgb(0, 1, 0.8, 0.4)  # Bright orange highlight at the center
    gradient.add_color_stop_rgb(0.4, 1, 0.5, 0.1)  # Medium orange
    gradient.add_color_stop_rgb(0.75, 0.8, 0.3, 0)  # Darker orange
    gradient.add_color_stop_rgb(1, 0.4, 0.1, 0)  # Darkest orange at the edges

    context.set_source(gradient)
    context.fill()


def draw_eyes_nose_frown(context, center_x, center_y, radius):
    # Draw two circles for the eyes
    eye_radius = radius * 0.1
    eye_offset_x = radius * 0.3
    eye_offset_y = radius * 0.2

    # Left Eye
    context.arc(center_x - eye_offset_x, center_y - eye_offset_y, eye_radius, 0, 2 * math.pi)
    context.set_source_rgb(1, 1, 0)  # Yellow color for eyes
    context.fill()

    # Right Eye
    context.arc(center_x + eye_offset_x, center_y - eye_offset_y, eye_radius, 0, 2 * math.pi)
    context.set_source_rgb(1, 1, 0)  # Yellow color for eyes
    context.fill()

    # Draw a triangle for the nose
    nose_width = radius * 0.1
    nose_height = radius * 0.1
    context.move_to(center_x, center_y)  # Top point of the triangle
    context.line_to(center_x - nose_width, center_y + nose_height)  # Bottom left
    context.line_to(center_x + nose_width, center_y + nose_height)  # Bottom right
    context.close_path()
    context.set_source_rgb(1, 1, 0)  # Yellow color for the nose
    context.fill()

    # Draw a frown using a Bezier curve
    mouth_width = radius * 0.6
    mouth_height = radius * 0.2
    mouth_offset_y = radius * 0.4  # Below the nose

    context.move_to(center_x - mouth_width / 2, center_y + mouth_offset_y)  # Start of the mouth
    # Create a frown curve by adjusting control points
    context.curve_to(center_x - mouth_width / 3, center_y + mouth_offset_y + mouth_height,
                     center_x + mouth_width / 3, center_y + mouth_offset_y + mouth_height,
                     center_x + mouth_width / 2, center_y + mouth_offset_y)

    context.set_source_rgb(1, 1, 0)  # Yellow color for the frown
    context.set_line_width(5)
    context.stroke_preserve()  # Preserve the path so we can fill it
    context.fill()


def draw_longitudinal_lines(context, center_x, center_y, radius, num_lines=6):
    # Draw longitudinal lines from the north pole to the south pole of the sphere
    context.set_source_rgb(0.1, 0.1, 0.1)  # Dark gray lines
    context.set_line_width(2)

    for i in range(num_lines):
        angle = (i * 2 * math.pi) / num_lines  # Calculate angle between lines

        # Calculate points at the top and bottom of the sphere (north and south poles)
        for t in range(101):
            # t goes from 0 (north pole) to 1 (south pole)
            theta = math.pi * t / 100  # Theta is the angle from the north pole to the south pole
            x = center_x + radius * math.sin(theta) * math.cos(angle)
            y = center_y + radius * math.cos(theta)

            if t == 0:
                context.move_to(x, y)  # Start at the north pole
            else:
                context.line_to(x, y)  # Draw towards the south pole

        context.stroke()


# Background
context.set_source_rgb(0.2, 0.2, 0.2)  # Dark background
context.paint()

# Draw the orange sphere
draw_sphere(context, WIDTH // 2, HEIGHT // 2, 200)

# Draw the eyes, nose, and frown on the sphere
draw_eyes_nose_frown(context, WIDTH // 2, HEIGHT // 2, 200)

# Draw longitudinal lines around the sphere, originating from the north pole to the south pole
draw_longitudinal_lines(context, WIDTH // 2, HEIGHT // 2, 200, num_lines=8)

# Save the result as a PNG image with the same name
filename = "halloween_pumpkin.png"
surface.write_to_png(filename)

print(f"creative haloween pumpkin sphere created and saved as {filename}!")
