import cv2 as cv

video=cv.VideoCapture(0)
if video.isOpened(): 
    fps=video.get(cv.CAP_PROP_FPS)
    fourcc=cv.VideoWriter_fourcc(*'DIVX') 
    wait_msec=int(1/fps*1000)
    w = video.get(cv.CAP_PROP_FRAME_WIDTH)
    h = video.get(cv.CAP_PROP_FRAME_HEIGHT)
    size=(int(w), int(h))
    mode="preview"
    brightness=0
    brightness_step=1

    target=cv.VideoWriter('webcam.avi',fourcc,fps,size)
    while True:
        valid, frame=video.read()
        frame=frame+brightness
        
        cv.putText(frame,"Brightness: "+str(brightness),(10,20),cv.FONT_HERSHEY_COMPLEX,0.7,(0,0,200))      
        if(mode=="preview"):
            cv.imshow('video player', frame)
            if not valid:
                break
        elif(mode=="recoder"):
            
            frame=cv.circle(frame, (50,50), radius=20, color=(0,0,255), thickness=3)
            cv.imshow('video recording', frame)
            target.write(frame)
            if not valid:
                break
            

        key = cv.waitKey(wait_msec)
        if key ==27:
            break
        elif key==32:
            if mode=="recoder":
                mode="preview"
            elif mode=="preview":
                mode="recoder"
        elif key==ord('+') or key==ord('='):
            brightness+=brightness_step
        elif key==ord('-') or key==ord('_'):
            brightness-=brightness_step          

video.release()
target.release()          
cv.destroyAllWindows()