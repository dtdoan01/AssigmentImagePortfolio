import os
import string

""" CODE TO ACCESS WORKING DIRECTORY """
try:
  #workingDir = string.replace(os.path.dirname(os.path.abspath(__file__)), "\Source", "")
  workingDir = os.path.dirname(os.path.abspath(__file__))
except:
  print "Please select the working directory"
  workingDir = pickAFolder()
  print workingDir
  
# Get Image by filename from SourceMedia directory.
def get_pic(fileName = ""): 
  try:
    path = workingDir + '\\SourceFiles\\' + fileName
    print path
    return makePicture(path)
  except:
    return makePicture(pickAFile())
   
# Save an image to the OutputMedia Directory
def saveOutput(img, fileName):
  repaint(img)
  writePictureTo(img, workingDir + "\\OutputFiles\\" + fileName)
  

""" BEGIN PROJECT CODE"""
def artify(pic):
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      p =  getPixel(pic, x, y)
      setRed(p, colorRange(getRed(p)))
      setGreen(p, colorRange(getGreen(p)))
      setBlue(p, colorRange(getBlue(p)))
  return pic
   
def colorRange(color):
  if color < 64:
    return 31
  if color < 128:	
    return 95
  if color < 192:
    return 159
  return 223


""" TEST CODE SECTION """
print "Testing Artify"
original = get_pic("Shrink.jpg")
artifyOtter = artify(original)
saveOutput(artifyOtter, "artify.jpg")



