import os, sys
import Image

def resize(inDir, outDir, width, height):
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
            if f.endswith(".jpg"):
                infile  = os.path.join(dirpath, f)
                outfile = outDir + infile[1:]
                try:
                    print("Resizing '%s'" % infile)
                    im = Image.open(infile)
                    im.thumbnail(size, Image.ANTIALIAS)
                    im.save(outfile)
                except IOError:
                    print "Cannot create '%s'" % outfile
    os.chdir(savedPath)