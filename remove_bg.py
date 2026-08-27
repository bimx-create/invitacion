from rembg import remove
from PIL import Image

for filename in ['oso_nino_3d.jpg', 'oso_nina_3d.jpg']:
    input_path = filename
    output_path = filename.replace('.jpg', '_nobg.png')
    
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input_data = i.read()
            output_data = remove(input_data)
            o.write(output_data)
    print(f"Processed {filename}")
