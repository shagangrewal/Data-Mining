import numpy as np
from PIL import Image, ImageDraw, ImageFont
from skimage import transform as tf
from matplotlib import pyplot as plt
from skimage.measure import regionprops, label
from sklearn.utils import check_random_state
from sklearn.preprocessing import OneHotEncoder
from skimage.transform import resize
from sklearn.cross_validation import train_test_split
from pybrain.datasets import SupervisedDataSet #using pybrain's data srt
from scipy.sparse.linalg import expm
 
def create_captcha(text, shear = 0, size = (100,24)):
    im = Image.new("L",size,"black") #using only black and white pixels for image
    draw = ImageDraw.Draw(im) 
    font = ImageFont.truetype("arial.ttf", 22) #deciding the type of font for text
    draw.text((2,2), text, fill=1, font=font) #specifying the text in the captcha
    image = np.array(im) #transforming image to array for ease of computation
    #shear transformation, changing the direction of the image
    affine_tf = tf.AffineTransform(shear=shear)
    image = tf.warp(image, affine_tf)
    return image / image.max() # division for the normalizing factor

def segment_image(image):
    labeled_image = label(image>0)
    subimage = [] # where we will place our each sub-image
    for region in regionprops(labeled_image): #regionprops- extracts info about regions
        x_start, y_start, x_end, y_end = region.bbox #extracting pixel points        
        subimage.append(image[x_start:x_end, y_start:y_end])
    if len(subimage)==0: #that is if there is only 1 character in captcha image
        return [image,]
    return subimage
    
image = create_captcha("GENE", shear = 0.5)
#plt.imshow(image, cmap = 'Greys')

subimages = []
subimages = segment_image(image)

#differenciating each individual character, in the base image itself
f, axes = plt.subplots(1, len(subimages), sharex=True, figsize=(10, 4), squeeze=False)
for i in range(len(subimages)):
    plt.imshow(subimages[i], cmap = 'Greys')
    #plt.show() # this code display each image in a new window

random_state = check_random_state(14)
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
shear_values = np.arange(0,0.5, 0.05)

def gen_sample(random_state = None):
    random_state = check_random_state(random_state)
    letter = random_state.choice(letters)
    shear = random_state.choice(shear_values)
    return create_captcha(letter, shear = shear , size = (20,20)), letters.index(letter)

image, target = gen_sample(random_state)
plt.imshow(image, cmap = 'Greys')
#plt.show()
print("The taget for the image is {}".format(target))

#creating the dataset for the problem, with size of 3000 data points
dataset, targets = zip(*(gen_sample(random_state) for i in range(3000)))
dataset = np.array(dataset, dtype= 'float')
targets = np.array(targets) # value of targets range from 0(a) to 25(z)

one_hot = OneHotEncoder()
y = one_hot.fit_transform(targets.reshape(targets.shape[0],1)) #creating row vector
y = y.todense() #for converting sparse matrix to dense numpy array

#transforming each image in the dataset to fit 20*20 pixel size
dataset = np.array([resize(segment_image(sample)[0],(20,20)) for sample in dataset])

#converting the three dimensional dataset to two-dimensional array
x = dataset.reshape((dataset.shape[0], dataset.shape[1]*dataset.shape[2]))

x_train, y_train, x_test, y_test = train_test_split(x,y, train_size = 0.9)

data = [x.shape[1],y.shape[1]]
#training = SupervisedDataSet(data)
#for i in range(x_train.shape[0]):
 #   training.addSample(x_train[i], y_train[i])









