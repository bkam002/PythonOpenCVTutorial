import cv2 

def main():

    imgpath = "/Users/brandonkam/Documents/Python/OpenCVDatasets/Images/4.1.01.tiff"  
    img = cv2.imread(imgpath,0)
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
