from io import TextIOWrapper
import re
from typing import List

class Image:
    STYLE_EMBEDDED = 0
    STYLE_FLOATING = 1
    STYLE_SURROUNDED = 2

    def __init__(self) -> None:
        self.height = 0
        self.width = 0
        self.dx = 0
        self.dy = 0
        self.style = 0
        self.x, self.y = 0, 0
        self.text = False

    def setStyle(self, value):
        if value == 'surrounded':
            self.style = self.STYLE_SURROUNDED
        elif value == 'floating':
            self.style = self.STYLE_FLOATING
        elif value == 'embedded':
            self.style = self.STYLE_EMBEDDED


class Reader:
    def __init__(self, file_in: TextIOWrapper) -> None:
        self.file_in = file_in
        self.text = ''
        self.curParagraph = 0

        strs = []
        sb = []

        while True:
            cur = self.file_in.readline()
            if cur == '':
                break

            cur = cur.strip()
            
            if len(cur) == 0:
                strs.append("".join(sb))
                sb = []
            
            sb.append(' ')
            sb.append(cur)

        if len(sb) > 0:
            strs.append("".join(sb))

        self.text = []
        for i in range(len(strs)):
            self.text.append(list(strs[i]))


    def nextParagraph(self) -> List[Image]:
        if self.curParagraph == len(self.text):
            return None
        
        images = []
        strs = self.text[self.curParagraph]
        self.curParagraph += 1
        cur = 0
        
        while cur < len(strs):
            if strs[cur].isspace():
                cur += 1
                continue

            if strs[cur] == '(':
                from_ = cur + 1
                while strs[cur] != ')':
                    cur += 1
                to = cur
                cur += 1

                info = "".join(strs[from_:to])
                scan = re.split(r"[\s=]+", info)
                s = 1
                image = Image()
                while s < len(scan):
                    field = scan[s]
                    value = scan[s+1]
                    s += 2

                    if field == "layout":
                        image.setStyle(value)
                        continue
                    
                    if field == "dx":
                        image.dx = int(value)
                        continue
                    
                    if field == "dy":
                        image.dy = int(value)
                        continue
                    
                    if field == "width":
                        image.width = int(value)
                        continue
                    
                    if field == "height":
                        image.height = int(value)
                        continue
                
                images.append(image)
                continue
                

            size = 0
            while ((cur < len(strs)) and (strs[cur] != '(') and (not strs[cur].isspace())):
                cur += 1
                size += 1
            
            image = Image()
            image.text = True
            image.setStyle('embedded')
            image.width = size * c
            image.height = h
            images.append(image)
        
        return images


class Document:
    def __init__(self) -> None:
        self.startPosition = 0
    

    def addParagraph(self, images: List[Image]):
        curPosition = 0
        curHeightPos = self.startPosition
        curHeight = h

        needWhiteSpace = False

        for i in range(len(images)):
            curImage = images[i]

            if curImage.style == Image.STYLE_FLOATING:
                if i > 0 and images[i-1].style == Image.STYLE_FLOATING:
                    curImage.y = images[i-1].y + curImage.dy
                    curImage.x = images[i-1].x + images[i-1].width + curImage.dx
                    curImage.x = max(curImage.x, 0)
                    curImage.x = min(curImage.x, w - curImage.width)
                    continue
                
                curImage.y = curHeightPos + curImage.dy
                curImage.x = curPosition + curImage.dx
                curImage.x = max(curImage.x, 0)
                curImage.x= min(curImage.x, w - curImage.width)
                continue
        
            while True:
                newPos = w
                left = w
                widht = curImage.width
                if curImage.style == Image.STYLE_EMBEDDED and needWhiteSpace:
                    widht += c
                
                for j in range(i):
                    if (images[j].style == Image.STYLE_SURROUNDED and 
                        images[j].y + images[j].height > curHeightPos and
                        images[j].x >= curPosition):
                        if images[j].x < left:
                            left = images[j].x
                            newPos = images[j].x + images[j].width

                if curPosition + widht <= left:
                    break

                curPosition = newPos
                needWhiteSpace = False
                if curPosition == w:
                    curPosition = 0
                    curHeightPos += curHeight
                    curHeight = h
               
            if curImage.style == Image.STYLE_EMBEDDED and needWhiteSpace:
                curImage.x = curPosition + c
            else:
                curImage.x = curPosition
            
            curImage.y = curHeightPos
            needWhiteSpace = False
            if curImage.style == Image.STYLE_EMBEDDED:
                curHeight = max(curHeight, curImage.height)
                needWhiteSpace = True
            
            curPosition = curImage.x + curImage.width
            

        if len(images) > 0:
            self.startPosition = curHeightPos + curHeight
        else:
            self.startPosition = curHeightPos
        
        for n in range(len(images)):
            if images[n].style != Image.STYLE_SURROUNDED:
                continue
            self.startPosition = max(self.startPosition, images[n].y + images[n].height)





reader = open('input.txt', 'r', encoding='UTF-8')
out = open('output.txt', 'w', encoding='UTF-8')

w, h, c = map(int, reader.readline().split())
texts = []

inp = Reader(reader)
doc = Document()

while True:
    allImages = []

    cur = inp.nextParagraph()
    if cur == None:
        break
    
    for k in range(len(cur)):    
        allImages.append(cur[k])

    doc.addParagraph(cur)
    for i in range(len(allImages)):
        if not allImages[i].text:
            out.write(f"{allImages[i].x} {allImages[i].y}\n")
    
    
reader.close()
out.close()
