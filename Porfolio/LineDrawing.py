import os
import string
# This function requires two paramaters, first is picture and second is threshold. 
# The function returns a new back and white picture that shows the line like hand drawing picture
# To show a best line drawing picture with Threshold value of 2 to 20
# The luminance of the current pixel calculate differ from the right of luminanace pixel and below luminance picxel 


try:
  workingDir = os.path.dirname(os.path.abspath(__file__))
except:
  print "Please select the working directory"
  workingDir = pickAFolder()
  print workingDir
  
def getImg(fileName):
  path = workingDir + '\\SourceFiles\\' + fileName
  print path
  return makePicture(path)
  
def saveOutput(img, fileName):
  writePictureTo(img, workingDir + "\\OutputFiles\\" + fileName + ".jpg")

def average(r, g, b):
  return (r + g + b) / 3

def DrawLine(pic, thredhold):
  w = getWidth(pic)
  h = getHeight(pic)
  target = makeEmptyPicture(w, h)
  for y in range(1, getHeight(pic) - 1):
    for x in range(1, getWidth(pic) - 1):
      currentPixel = getPixel(pic, x, y)
      rightPixel = getPixel(pic, x + 1, y)
      belowPixel = getPixel(pic, x, y + 1)
      
      currentLuminance = average(getRed(currentPixel), getGreen(currentPixel), getBlue(currentPixel))
      rightLuminance = average(getRed(rightPixel), getGreen(rightPixel), getBlue(rightPixel))
      belowLuminance = average(getRed(belowPixel), getGreen(belowPixel), getBlue(belowPixel))
      
      if abs(currentLuminance - rightLuminance) < thredhold and abs(currentLuminance - belowLuminance) < thredhold:
        setColor(getPixel(target, x, y), makeColor(255, 255, 255))   
      else:
        setColor(getPixel(target, x, y), makeColor(0, 0, 0))   
  return target

desertInBW = getImg("unnamed1.jpg")
drawlineInBW = DrawLine(desertInBW, 20)
saveOutput(drawlineInBW, "drawlineInBW")
repaint(drawlineInBW)

