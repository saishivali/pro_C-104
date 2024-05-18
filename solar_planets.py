import cv2
img=cv2.imread("solar-system.jpg")

cv2.putText(img,
            "sun",
            (100,100),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255))

cv2.putText(img,
            "Mercury",
            (100,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,255))

cv2.putText(img,
            "venus",
            (190,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,255))

cv2.putText(img,
            "earth",
            (280,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,255))

cv2.putText(img,
            "mars",
            (390,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,255))

cv2.putText(img,
            "jupiter",
            (480,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,255))

cv2.putText(img,
            "saturn",
            (700,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,255))

cv2.putText(img,
            "uranus",
            (950,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,255))

cv2.putText(img,
            "Neptune",
            (1100,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,255))
cv2.imshow("output",img)
cv2.waitKey(0)
