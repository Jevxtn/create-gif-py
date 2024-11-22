from PIL import Image, ImageDraw, ImageFont
import imageio

# Initialize frames
frames = []

# Colors and Dimensions
bg_color = (0, 0, 0)
text_color = (255, 255, 255)
width, height = 500, 300

# Progress bar simulation
for i in range(1, 101, 5):
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Progress Bar
    bar_length = (width - 40) * (i / 100)
    draw.rectangle([20, height // 2 - 10, 20 + bar_length, height // 2 + 10], fill=(0, 255, 0))

    # Text: Motivational Words
    font = ImageFont.truetype("arial.ttf", 20)
    if i < 33:
        text = "Focus"
    elif i < 66:
        text = "Grow"
    else:
        text = "Achieve"
    draw.text((width // 2 - 40, height // 2 - 50), text, fill=text_color, font=font)

    # Add frame
    frames.append(img)

# Final Text Frame
final_frame = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(final_frame)
draw.text((width // 2 - 90, height // 2), "Empower Your Growth", fill=text_color, font=font)
frames.append(final_frame)

# Save as GIF
frames[0].save("motivational_goal.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
