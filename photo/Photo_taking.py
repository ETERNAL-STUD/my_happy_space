def my_camera():
    import cv2
    vid = cv2.VideoCapture(0)
    result,img = vid.read()
    cv2.imshow("Jason",img)
    cv2.imwrite("Jason.png", img)
    cv2.waitKey(0) 
    cv2.destroyWindow("geek")
take_input = input("Write 'photo' to take a picture: ").lower()
if take_input == "photo":
    my_camera()