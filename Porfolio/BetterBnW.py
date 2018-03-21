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

def  betterBnW(pic):
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    avg = getRed(p)*0.299 + getGreen(p)*0.587 + getBlue(p)*0.114 
    setColor(p, makeColor(avg, avg, avg))   
  return pic
  

""" TEST CODE SECTION """
print "Testing negative"
original = get_pic("Mar.jpg")
betterBlackWhite = betterBnW(original)
saveOutput(betterBlackWhite, "betterBnW.jpg")



