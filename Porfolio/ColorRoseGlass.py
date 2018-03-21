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

def roseColoredGlasses(pic):
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p, r*0.9)
    setGreen(p, g*0.3)
    setBlue(p, b*0.6)
  return pic 


""" TEST CODE SECTION """
print "Testing roseColoredGlasses"
original = get_pic("grass.jpg")
rosePink = roseColoredGlasses(original)
saveOutput(rosePink, "GrassInPink.jpg")



