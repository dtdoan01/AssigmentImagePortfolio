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
def Shrink(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  newPic = makeEmptyPicture(w / 2, h / 2)
  for x in range (0, getWidth(pic), 2):
    for y in range (0, getHeight(pic), 2):
      setColor(getPixel(newPic,x/2,y/2), getColor(getPixel(pic,x,y)))
    
  return newPic

""" TEST CODE SECTION """
print "Testing Shrink"
original = get_pic("otter.jpg")
shrinkOtter = Shrink(original)
saveOutput(shrinkOtter, "Shrink.jpg")



