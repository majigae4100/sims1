import cv2
from PIL import Image

class RecognizeImg:
    def __init__(self, path:str):
        self.Path:str = path
        self.Image = cv2.imread(self.Path)
        self.MultiScale  = list()
    def ShowImg(self, winName:str):
        cv2.imshow(winName, self.Image)
        cv2.waitKey()

    def GetCoordinates(self, fileName:str):
        cascade = cv2.CascadeClassifier(fileName)
        self.MultiScale = cascade.detectMultiScale(self.Image)

    def HighLight(self):
        for (x, y, width, height) in self.MultiScale:
            cv2.rectangle(self.Image, (x, y), (x+width, y+height), (0, 0, 255), 3)

    def AddImage(self, path:str, newPhotoPath:str):
        try:
            fLayout = Image.open(self.Path)
            sLayout = Image.open(path)
            fLayoutConvert = fLayout.convert('RGBA')
            sLayoutConvert = sLayout.convert('RGBA')
            for (x, y, width, height) in self.MultiScale:
                sLayoutConvert = sLayoutConvert.resize((width, int(height/3)))
                fLayoutConvert.paste(sLayoutConvert, (x, int(y + height/4)))
                fLayoutConvert.save(newPhotoPath)
                self.Image = cv2.imread(newPhotoPath)
                self.ShowImg('AddImage Cat')
        except Exception as ex:
            print(ex)
