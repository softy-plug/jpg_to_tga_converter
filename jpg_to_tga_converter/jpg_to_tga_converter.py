import os
from PIL import Image

def convert_image(input_path, output_path):
    with Image.open(input_path) as im:
        im.save(output_path, 'tga', optimize=True, quality=100)

def main():
    print("Welcome to JPG to TGA Converter!")
    while True:
        jpg_folder = input("Enter the path to the folder containing JPG images: ")
        if os.path.exists(jpg_folder):
            break
        else:
            print("The folder does not exist.")
    while True:
        tga_folder = input("Enter the path to the folder where TGA images will be saved: ")
        if os.path.exists(tga_folder):
            break
        else:
            print("The folder does not exist.")
    # Create the TGA folder if it doesn't exist yet
    if not os.path.exists(tga_folder):
        os.makedirs(tga_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            output_path = os.path.join(tga_folder, os.path.splitext(filename)[0] + '.tga')
            convert_image(input_path, output_path)
    print("All images converted successfully!")

if __name__ == "__main__":
    main()

# softy_plug