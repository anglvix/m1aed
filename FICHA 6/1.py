from PIL import Image
import random
import os

def ImageArt(show=True, out_dir=None):
    img = Image.new('RGB', (400, 400))

    pixels = img.load()
    
    for x in range(400):
        for y in range(400):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pixels[x, y] = (r, g, b)

    # determine output directory relative to this script file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if out_dir is None:
        out_dir = os.path.join(base_dir, 'image')
    else:
        # if a relative path was provided, make it relative to script dir
        if not os.path.isabs(out_dir):
            out_dir = os.path.join(base_dir, out_dir)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    out_path = os.path.join(out_dir, 'imageArt.jpg')
    img.save(out_path)

    if show:
        try:
            img.show()
        except Exception:
            pass
    return out_path

if __name__ == "__main__":
    path = ImageArt()
    print(f'Random image saved to: {path}')
