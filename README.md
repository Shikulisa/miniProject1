# Mini Project - Sphere

## This Python script uses the cairo graphics library to create an image of a Halloween-inspired pumpkin sphere with eyes, nose, a frowning mouth, and longitudinal lines, resembling the look of a 3D globe.

### Draw the Pumpkin Sphere (draw_sphere function):

- A sphere is created using a radial gradient that shades from bright to dark orange, giving a 3D effect. 
- This function takes the center coordinates (center_x, center_y) and radius of the sphere.
- Different color stops in the radial gradient are applied to produce shading from bright orange at the center to darker orange at the edges.

### Add Eyes, Nose, and Mouth (draw_eyes_nose_frown function):

- Eyes: Two yellow circles are drawn for the eyes, positioned symmetrically on the pumpkin.
- Nose: A yellow triangle is drawn as the pumpkin's nose just below the eyes.
- Mouth (Frown): A curved frown is created using a Bezier curve for a Halloween expression, adding a whimsical touch.

### Add Longitudinal Lines (draw_longitudinal_lines function):

- Dark gray lines represent longitudinal arcs around the pumpkin, adding a globe-like appearance.
- These lines are drawn from the top to the bottom of the sphere (like meridians) at intervals around the circle.
