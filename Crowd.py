import cv2   # Importing the openCV library
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')   # We load the cascade for the face.
 
image = cv2.imread(r"E:\Downloads\crowd.jpg")  # Importing the image in which we will do the process
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converting the image into gray so that haarcascading can be done

faces = face_cascade.detectMultiScale(grayImage,1.001,1) # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
 
print(type(faces))
 
if len(faces) == 0: # We apply if else condition to detect the number of faces
    print("No faces found")
 
else:
    print(faces)
    print(faces.shape)
    print("Number of faces detected: " + str(faces.shape[0]))
 
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1) # We paint a rectangle around the face.
 
cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)# We print our result of number of faces detected in the image
 
cv2.imshow('Image with faces',image)# We print the result in the kernal
cv2.waitKey(0)
cv2.destroyAllWindows()# We destroy all the windows inside which the images were displayed.
