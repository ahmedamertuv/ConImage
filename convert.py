import os
import sys
from PIL import Image


def convert_to_webp(input_folder, output_folder, width):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)
        if os.path.isfile(filepath):
            try:
                img = Image.open(filepath)
                # Resize image while maintaining aspect ratio
                w_percent = width / float(img.size[0])
                h_size = int((float(img.size[1]) * float(w_percent)))
                img = img.resize((width, h_size))

                # Save as WebP format
                output_path = os.path.join(
                    output_folder, os.path.splitext(filename)[0] + ".webp"
                )
                img.save(output_path, "WEBP")
                print(f"Converted {filename} to WebP")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python convert.py <input_folder> <output_folder> <width>")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        width = int(sys.argv[3])
        convert_to_webp(input_folder, output_folder, width)
