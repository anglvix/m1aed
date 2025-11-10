from PIL import Image
import os

def imageGradiente(show=True, out_dir=None):
    width, height = 250, 250

    img = Image.new('RGB', (width, height))
    pixels = img.load()

    for x in range(width):
        t = x / (width - 1)
        r = int(round(255 * t))
        g = 0
        b = int(round(255 * (1 - t)))
        for y in range(height):
            pixels[x, y] = (r, g, b)

    # determine output directory relative to this script file if not absolute
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if out_dir is None:
        out_dir = os.path.join(base_dir, 'image')
    else:
        if not os.path.isabs(out_dir):
            out_dir = os.path.join(base_dir, out_dir)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    out_path = os.path.join(out_dir, 'imageGradiente.jpg')
    img.save(out_path)

    if show:
        try:
            img.show()
        except Exception:
            pass

    return out_path


if __name__ == '__main__':
    path = imageGradiente()
    print(f'Gradient image saved to: {path}')
