# The Homemake St. Patrick's date card is using the green screen techniques to paint the background images
# The green screen techniques is backdropped and replaced all pixels with more interesting backgound. 
# Because the St Patrick's is green, the placing email is using the different color than green. In this case is using red for the
# original image to be add on.

import os
import string

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
             
def identifyColor(pixel):
    threshhold = 150
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    if abs(r - b) < 25 and abs(g - b) > threshhold and abs(g - r) > threshhold:
      return "green"
    elif abs(g - b) < 25 and abs(r - b) > threshhold and abs(r - g) > threshhold:
      return "red"
    else:
      return "blue"
           
def colorPaste(source, target, targetX, targetY, colorToIgnore):
  sY = 0  
  for tY in range(targetY, getHeight(source) + targetY): # Write source to target
    sX = 0
    if tY < 0 or tY >= getHeight(target):
      sY +=1
      continue
    for tX in range(targetX, getWidth(source)  + targetX):
      if tX < 0 or tX >= getWidth(target):
        sX += 1
        continue
      pixel = getPixel(source, sX, sY)
      if colorToIgnore != identifyColor(pixel):
        setColor(getPixel(target, tX, tY), getColor(pixel))
      sX +=1
    sY +=1    
  return target
  
def makeCard():
  color = "red"
  base = getImg("BaseImg.jpg")
  sprite = getImg("patrick.jpg")
  base = colorPaste(sprite, base, 900, 400, color)
  sprite = getImg("hat.jpg")
  base = colorPaste(sprite, base, 1040, 317, color)
  return base
      
""" TEST CODE """

# Make St. Patrick's Day Card
card = makeCard()
saveOutput(card, "stPatricksDayCard.jpg")
repaint(card)
  