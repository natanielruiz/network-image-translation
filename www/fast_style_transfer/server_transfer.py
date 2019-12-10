import evaluate
import os.path
import random

OUT_PATH = "/var/www/out_images/"
CPKT_DIR = "/var/www/checkpoints/"
NUM_STYLES = 6
CPKT_LIST = \
    [
    "la_muse.ckpt",
    "rain_princess.ckpt",
    "scream.ckpt",
    "udnie.ckpt",
    "wave.ckpt",
    "wreck.ckpt"
    ]
STYLE_PATHS = \
    [
        "/var/www/style_img/la_muse.jpg",
        "/var/www/style_img/rain_princess.jpg",
        "/var/www/style_img/scream.jpg",
        "/var/www/style_img/udnie.jpg",
        "/var/www/style_img/wave.jpg",
        "/var/www/style_img/wreck.jpg",
    ]

def stransfer_from_file(fpath):
    assert os.path.isfile(fpath)
    assert fpath.endswith(".jpg") or fpath.endswith(".png")

    fname = os.path.basename(fpath)
    out_path = os.path.join(OUT_PATH, fname)

    # picking random style
    style_id = random.randint(0, NUM_STYLES-1)
    cpkt_file = os.path.join(CPKT_DIR, CPKT_LIST[style_id] )
    style_imgpath = STYLE_PATHS[style_id]

    # running style transfer
    evaluate.ffwd_to_img(fpath, out_path, cpkt_file, device='/cpu:0')
    # return the path to the output image and the path to the style image
    return out_path, style_imgpath



