import cv2

#configurable
source="adarsh.jpg"  #instead give your file path
destination="newImage.jpg" #destination folder name
scale_percent=50  #percent by which resizing

src=cv2.imread(source,cv2.IMREAD_UNCHANGED)
#cv2.imshow("title",src)


#calculating new dimensions
new_width=int(src.shape[1]*scale_percent/100)
new_height=int(src.shape[0]*scale_percent/100)
newdim=(new_width,new_height)

#resize
output=cv2.resize(src,newdim)

#showing
cv2.imwrite(destination,output)