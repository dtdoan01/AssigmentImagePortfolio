import os
import string

""" CODE TO ACCESS WORKING DIRECTORY """
try:
  workingDir = os.path.dirname(os.path.abspath(__file__))
except:
  print "Please select the working directory"
  workingDir = pickAFolder()
  print workingDir
  
# Get Image by filename from SourceMedia directory.
def get_pic(fileName = ""): 
  try:
    path = workingDir + '\\SourceFiles\\' + fileName
    return makePicture(path)
  except:
    return makePicture(pickAFile())
   
# Save an image to the OutputMedia Directory
def saveOutput(img, fileName):
  repaint(img)
  writePictureTo(img, workingDir + "\\OutputFiles\\" + fileName)
  

""" BEGIN PROJECT CODE"""

def makeNegative(img):
  pixels = getPixels(img)
  for p in pixels:
    r = 255 - getRed(p)
    g = 255 - getGreen(p)
    b = 255 - getBlue(p)
    setColor(p, makeColor(r, g, b))
  return img


def HorizontalFlipUp(pic):
  h = getHeight(pic)
  for x in range(0, getWidth(pic)):
    for y in range(getHeight(pic)-1, getHeight(pic) / 2, -1):
      p = getPixel(pic, x, y)
      c = getColor(p)
      pb = getPixel(pic, x, h - y) 
      setColor(pb, c)
  return pic



""" TEST CODE SECTION """
print "Testing negative"
original = get_pic("Mar.jpg")
negative = makeNegative(original)
saveOutput(negative, "negative.jpg")



