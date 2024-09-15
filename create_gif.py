import os
import argparse
from PIL import Image

def create_gif_from_folder(folder_path, output_path, fps=10, loop=0, output_file_name="output.gif", reverse=0,):
    # Get a list of all files in the folder
    file_names = os.listdir(folder_path)

    # Filter out files to only include images (e.g., jpg, png, jpeg files)
    image_files = [f for f in file_names if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Sort the files to maintain order
    image_files.sort()

    # Create the list of image paths
    image_paths = [os.path.join(folder_path, f) for f in image_files]

    # Open images and convert them to 'RGBA' mode
    images = [Image.open(image_path).convert('RGBA') for image_path in image_paths]

    # Calculate duration per frame in milliseconds
    duration = int(1000 / fps)

    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Create a background image to paste frames onto
    base_image = Image.new('RGBA', images[0].size)

    # Create frames with transparency
    frames = []
    for img in images:
        frame = base_image.copy()
        frame.paste(img, (0, 0), img)
        frames.append(frame)

    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)
    
    if reverse == 1:
        frames.reverse()
    
    output_file = os.path.join(output_path, output_file_name)
    frames[0].save(
        output_file, save_all=True, append_images=frames[1:], duration=duration, loop=loop, disposal=2, optimize=False
    )

def create_gif_from_strip(strip_path, output_path, fps=10, loop=0, frame_width=None, output_file_name="output.gif", reverse=False,):
    # Open the image strip and convert to 'RGBA' mode
    strip = Image.open(strip_path).convert('RGBA')

    # If frame_width is not provided, assume each frame is square
    if not frame_width:
        frame_width = strip.height

    # Calculate the number of frames
    num_frames = strip.width // frame_width

    # Extract each frame
    frames = []
    for i in range(num_frames):
        frame = strip.crop((i * frame_width, 0, (i + 1) * frame_width, strip.height))
        frame_rgba = frame.convert('RGBA')
        frames.append(frame_rgba)

    # Calculate duration per frame in milliseconds
    duration = int(1000 / fps)

    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)
    
    if reverse == 1:
        frames.reverse()
    
    output_file = os.path.join(output_path, output_file_name)
    frames[0].save(
        output_file, save_all=True, append_images=frames[1:], duration=duration, loop=loop, disposal=2, optimize=False
    )

if __name__ == "__main__":
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_output_dir = os.path.join(script_dir, "outputs")

    # Setup argument parser
    parser = argparse.ArgumentParser(description='Create a GIF from a folder of images or an image strip.')
    parser.add_argument('input_path', type=str, help='Path to the folder containing images or the image strip.')
    parser.add_argument('output_path', type=str, nargs='?', default=default_output_dir, help='Directory to save the output GIF (default: outputs folder in script directory).')
    parser.add_argument('--fps', type=int, default=10, help='Frames per second for the GIF (default: 10).')
    parser.add_argument('--loop', type=int, default=0, help='Number of times to loop the GIF (default: 0 for infinite loop).')
    parser.add_argument('--strip', action='store_true', help='Indicate if the input is an image strip.')
    parser.add_argument('--frame_width', type=int, help='Width of each frame in the image strip (optional, if not provided assumes square frames).')
    parser.add_argument('--output_file_name', type=str, default="output.gif", help='Optional output file name for the GIF.')
    parser.add_argument('--reverse', type=int, default=0, help='Optional, saves the gif images backwards if set to 1 (default: 0)')

    # Parse arguments
    args = parser.parse_args()

    # Create GIF with provided arguments
    if args.strip:
        # Check if input_path is a file
        if not os.path.isfile(args.input_path):
            print(f"Error: {args.input_path} is not a file.")
        else:
            create_gif_from_strip(args.input_path, args.output_path, args.fps, args.loop, args.frame_width, args.output_file_name, args.reverse)
    else:
        # Check if input_path is a directory
        if not os.path.isdir(args.input_path):
            print(f"Error: {args.input_path} is not a directory.")
        else:
            create_gif_from_folder(args.input_path, args.output_path, args.fps, args.loop, args.output_file_name, args.reverse)
