import glob
import os, cv2

maskedCounter = 0
noMaskCounter = 0
undefCounter = 0

dir = os.path.dirname(__file__)
datasetDir = os.path.join(dir, 'data/kitti_dataset/train')

# getting all the label files from the label folder within the datasetDir
fileNames = glob.glob(datasetDir+'/labels/'+'*.txt')

print('Total of %s files found in the labels directory.' % (len(fileNames)))

for fileName in fileNames:
    name = fileName.split('/')[-1]
    name = name.split('.')[0]
    # read the image and the labels
    labelFilePath = datasetDir + '/labels/' + name + '.txt'
    labelFile = open(labelFilePath)
    lines = labelFile.readlines()

    # test_image_full_path = os.path.join(datasetDir, "images", name + '.jpg')
    # img = cv2.imread(test_image_full_path)

    for line in lines:
        comp = line.split()
        classLabel = comp[0]
        #extract the faces from the images and write them to a seperate file.
       
        if classLabel == 'No-Mask':
            noMaskCounter = noMaskCounter + 1
            color = (255, 0, 0)
        elif classLabel == 'Mask':
            maskedCounter = maskedCounter + 1
            color = (0, 255, 0)
        else:
            continue

        # 这里如果是浮点型，会出异常：ValueError: invalid literal for int() with base 10
        xmin = int(comp[4])
        xmax = int(comp[6])
        ymin = int(comp[5])
        ymax = int(comp[7])
        if xmax < xmin:
            print('label file(%s) x invalid: (%s, %s)' % (labelFilePath, xmin, xmax))
            (xmin, xmax) = (xmax, xmin)
        if ymax < ymin:
            print('label file(%s) y invalid: (%s, %s)' % (labelFilePath, ymin, ymax))
            (ymin, ymax) = (ymax, ymin)
        # bbox = [xmin, ymin, xmax, ymax]
        # cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, thickness=2)

    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    
print('Total "MASK" labels: %s\nTotal "No-Mask" labels: %s \nTotal undefined labels: %s' % (maskedCounter, noMaskCounter, undefCounter))