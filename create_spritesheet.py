from PIL import Image
import os
import re

def numerical_sort(value):
    parts = re.split(r'(\d+)', value)
    return [int(text) if text.isdigit() else text for text in parts]

# Define the directory containing the images
image_dir = 'C:\\Users\\devib\\Desktop\\Brawlhalla Sprites\\Sentinel\\Cu-Sidhe-Skin\\Starlight Color\\Wallclimb'

# Define the size of each frame in the sprite sheet
frame_size = (500, 500)

# List all the image files in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith(('png', 'jpg', 'jpeg'))]

# Sort the images numerically
image_files.sort(key=numerical_sort)

# Calculate the size of the sprite sheet with one row
sprite_sheet_size = (frame_size[0] * len(image_files), frame_size[1])

# Create an empty image for the sprite sheet with one row
sprite_sheet = Image.new('RGBA', sprite_sheet_size)

# Load and place each image in the sprite sheet
for index, image_file in enumerate(image_files):
    img = Image.open(os.path.join(image_dir, image_file))
    img.thumbnail(frame_size, Image.LANCZOS)
    
    # Calculate position
    x = index * frame_size[0] + (frame_size[0] - img.width) // 2
    y = (frame_size[1] - img.height) // 2
    
    # Paste the image into the sprite sheet
    sprite_sheet.paste(img, (x, y))

# Save the final sprite sheet
sprite_sheet.save(os.path.join(image_dir, f'sprite_sheet_{len(image_files)}f.png'))
