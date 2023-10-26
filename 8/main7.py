from recognizeimg import RecognizeImg
path = 'img/cat1.jpeg'
winName = 'Cat'
fileName = 'haarcascade_frontalcatface_extended.xml'
rec = RecognizeImg(path)
#rec.ShowImg(winName)
rec.GetCoordinates(fileName)
#print(rec.MultiScale)
#rec.HighLight()
#rec.ShowImg(winName)
newPath = 'img/glasses.png'
newPhotoPath = 'img/cat_with_glasses1.png'
rec.AddImage(newPath, newPhotoPath)