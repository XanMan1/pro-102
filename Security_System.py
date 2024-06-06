import cv2
import time
import random
import dropbox

print(time.time())
print(random.randint(0,9))
start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    video_capture_object = cv2.VideoCapture(0)
    results = True
    while results:
        ret,frame = video_capture_object.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        results = False
    return img_name
    print("Snapshot taken!")
    video_capture_object.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
     access_token = 'sl.BybHTF_bBKKUreeSPCHWdsUd0mf1TwyHzERR6NXXHSt97eod9DP7NziZzxrZ761_auElDUGHJunuj5Xrp9lePCn6dq5spkENjqAQqxcz7ZHReM64rjMVr2VmX5tAWdUGDEcFxm2iim8X'
     file = img_name
     file_from = file
     file_to = "/newFolder1/"+(img_name)
     dbx = dropbox.Dropbox(access_token)
     with open(file_from,"rb") as f:
         dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
         print("file uploaded!")
     
def main():
    while True:
        if ((time.time()-start_time)>=300):
            name = take_snapshot()
            upload_file(name)
main()