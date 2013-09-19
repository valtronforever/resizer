import os, sys
import Image, ImageDraw, ImageFont, ImageEnhance

FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vera.ttf')


def add_watermark(img, text, angle=23, opacity=0.35):
    img = img.convert('RGB')
    watermark = Image.new('RGBA', img.size, (0,0,0,0))
    size = 2
    n_font = ImageFont.truetype(FONT, size)
    n_width, n_height = n_font.getsize(text)
    while n_width+n_height < watermark.size[0]:
        size += 2
        n_font = ImageFont.truetype(FONT, size)
        n_width, n_height = n_font.getsize(text)
    draw = ImageDraw.Draw(watermark, 'RGBA')
    draw.text(((watermark.size[0] - n_width) / 2,
              (watermark.size[1] - n_height) / 2),
              text, font=n_font)
    watermark = watermark.rotate(angle,Image.BICUBIC)
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    return Image.composite(watermark, img, watermark)


def resize(inDir, outDir, width, height, watermark):
    size = int(width), int(height)
    savedPath = os.getcwd()

    os.chdir(inDir)
    for dirpath, dnames, fnames in os.walk("."):

        # Create new dirs
        for dirname in dnames:
            if dirpath == '.':
                newDirFullName = os.path.join(outDir, dirname)
            else:
                newDirFullName = outDir + os.path.join(dirpath[1:], dirname)
            if not os.path.exists(newDirFullName): os.makedirs(newDirFullName)

        for f in fnames:
            if f.endswith((".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG",)):
                infile  = os.path.join(dirpath, f)
                outfile = outDir + infile[1:]
                try:
                    print("Resizing '%s'" % infile)
                    im = Image.open(infile)
                    im.thumbnail(size, Image.ANTIALIAS)

                    if watermark:
                        im = add_watermark(im, watermark)

                    im.save(outfile)
                except IOError as e:
                    print "Cannot create '%s', %s" % (outfile, e)
    os.chdir(savedPath)
