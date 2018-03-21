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
def changeCat(picture, newColor):
  ltgray = makeColor(152, 32, 5)
  aqua = makeColor(34, 25, 16)
  for x in range(1, 240):
    for y in range(0 , 480):
      px = getPixel(picture, x, y)
      color = getColor(px)
      if distance(color, red) < 50.0:
        setColor(px, newColor)
      if distance(color, ltgray) < 80.0:
        setColor(px, aqua)
  return picture
  
  
""" TEST CODE SECTION """
print "Testing Red-eyes"
getSourcePic = get_pic("RedeyesCat02.jpg")
Redeyes = changeCat(getSourcePic, black)
saveOutput(Redeyes, "Red-eyes.jpg")

  