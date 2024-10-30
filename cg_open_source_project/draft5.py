import math
import cairo

# Image size
WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Function to draw a pumpkin-like sphere with shading, light, and longitudinal ridges
def draw_pumpkin(context, center_x, center_y, radius):
    # Base sphere (pumpkin body)
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    pumpkin_color = cairo.RadialGradient(center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.1,
                                         center_x, center_y, radius)
    pumpkin_color.add_color_stop_rgb(0, 1, 0.5, 0)  # Bright orange at the top
    pumpkin_color.add_color_stop_rgb(0.5, 1, 0.3, 0)  # Darker orange in the middle
    pumpkin_color.add_color_stop_rgb(1, 0.6, 0.2, 0)  # Deep orange at the bottom
    context.set_source(pumpkin_color)
    context.fill()

    # Create longitudinal ridges (from the top center)
    num_ridges = 12
    for i in range(num_ridges):
        angle = (i / num_ridges) * 2 * math.pi
        ridge_start_x = center_x + radius * 0.05 * math.cos(angle)  # Slight offset for the top center
        ridge_start_y = center_y - radius * 0.95  # Top of the pumpkin
        ridge_end_x = center_x + radius * math.cos(angle)
        ridge_end_y = center_y + radius * math.sin(angle)
        
        # Draw the ridge as a curved line (arc from top to bottom)
        context.move_to(ridge_start_x, ridge_start_y)
        context.curve_to(
            center_x + radius * 0.5 * math.cos(angle), center_y,
            center_x + radius * 0.5 * math.cos(angle), center_y,
            ridge_end_x, ridge_end_y
        )
        context.set_source_rgba(0, 0, 0, 0.3)  # Light shadow effect for the ridges
        context.set_line_width(2)
        context.stroke()

    # Add carved eyes and mouth
    # Eyes
    context.move_to(center_x - radius * 0.4, center_y - radius * 0.3)
    context.line_to(center_x - radius * 0.2, center_y - radius * 0.1)
    context.line_to(center_x - radius * 0.4, center_y - radius * 0.1)
    context.close_path()
    context.set_source_rgb(1, 1, 0.1)  # Glow from the inside
    context.fill()

    context.move_to(center_x + radius * 0.4, center_y - radius * 0.3)
    context.line_to(center_x + radius * 0.2, center_y - radius * 0.1)
    context.line_to(center_x + radius * 0.4, center_y - radius * 0.1)
    context.close_path()
    context.fill()

    # Mouth
    context.move_to(center_x - radius * 0.5, center_y + radius * 0.2)
    context.line_to(center_x + radius * 0.5, center_y + radius * 0.2)
    context.line_to(center_x + radius * 0.3, center_y + radius * 0.4)
    context.line_to(center_x - radius * 0.3, center_y + radius * 0.4)
    context.close_path()
    context.set_source_rgb(1, 1, 0.1)  # Glow for the mouth
    context.fill()

# Background (dark like nighttime)
context.set_source_rgb(0.1, 0.1, 0.1)
context.paint()

# Draw pumpkin in the center
draw_pumpkin(context, WIDTH // 2, HEIGHT // 2, 200)

# Save the image
surface.write_to_png("3d_pumpkin_longitudinal.png")

print("3D glowing pumpkin image with longitudinal ridges created!")
