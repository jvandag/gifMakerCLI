# gifMakerCLI
A simple CLI for creating gifs from an image strip or directory of images. Fixes discoloration or improper background removal which is a common occurrence in similar free software.

# Example use:
**bash commands:**
```bash
python create_gif.py path/to/your/directory --fps 12 --loop 0 --frame_width 64 --output_file_name "Runing12fps.gif"
#Creates gif from multiple image files

python create_gif.py path/to/your/strip.png output.gif --fps 15 --loop 3 --strip --frame_width 100
# Creates gif from image strip
    
# fps default: 10 fps
#loop default: 0 (loops forever)
```


