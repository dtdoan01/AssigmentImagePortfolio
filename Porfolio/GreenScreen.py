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
def chromakey(source, bg):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      p = getPixel(source, x, y)
      if (getRed(p) + getBlue(p) < getGreen(p)):
        setColor(p, getColor(getPixel(bg, x, y)))
  return source


""" TEST CODE SECTION """
print "Combining Corey and Paradise"
original3 = get_pic("corey.png")
bg2 = get_pic("micraft.jpg")
paradiseCorey = chromakey(original3, bg2)
saveOutput(paradiseCorey, "CoreyInMicraft.png")


