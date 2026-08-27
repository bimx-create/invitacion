import sys

log = open('process.log', 'w')
log.write(f'Python: {sys.version}\n')
log.flush()

try:
    from PIL import Image

    log.write('PIL imported OK\n')
    log.flush()

    for filename in ['oso_nino_3d.jpg', 'oso_nina_3d.jpg']:
        log.write(f'Processing {filename}\n')
        log.flush()
        
        img = Image.open(filename).convert('RGBA')
        log.write(f'Opened image: {img.size}\n')
        log.flush()
        
        pixels = img.load()
        width, height = img.size
        
        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                # If pixel is near-white, make transparent
                if r > 230 and g > 230 and b > 230:
                    pixels[x, y] = (r, g, b, 0)
        
        output = filename.replace('.jpg', '_nobg.png')
        img.save(output, 'PNG')
        
        log.write(f'Saved {output} OK\n')
        log.flush()

    log.write('ALL DONE\n')
    
except Exception as e:
    import traceback
    log.write(f'ERROR: {e}\n')
    log.write(traceback.format_exc())

log.close()
