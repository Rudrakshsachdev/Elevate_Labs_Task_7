import os
from PIL import Image

# === Configuration ===
input_folder = 'input_images'
output_folder = 'output_images'
new_size = (800, 800) # desired size for the images
output_format = 'PNG' # desired output format

os.makedirs(output_folder, exist_ok = True) # creating output folder if it doesn't exist

supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif'] # supported image formats

# processing images

for filename in os.listdir(input_folder):
    file_ext = os.path.splitext(filename)[1].lower() # get file extension
    if file_ext in supported_extensions:
        try:
            image_path = os.path.join(input_folder, filename)
            # Opening the image file            
            with Image.open(image_path) as img:

                # resizing the image
                resized_img = img.resize(new_size)
                # convert to the desired format if necessary
                if output_format.lower() == 'JPEG' and resized_img.mode != ('RGPA','p'):
                    resized_img = resized_img.convert('RGB')
                

                base_name = os.path.splitext(filename)[0] # getting the base name of the file
                output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}") # constructing the path for saving the resized image



                resized_img.save(output_path, format = output_format) # saving the resized image
                print(f"Resized and saved:{output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print('Image resizing completed...')

# === End of project ===