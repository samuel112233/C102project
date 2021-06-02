import random
import time
import dropbox
import cv2

startTime=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()

        imageName='img'+str(number)+'.png'
        cv2.imwrite(imageName,frame)
        startTime=time.time

        result=False
    return imageName
    print('Snapshot Taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload(imageName):
    accessToken='57rHcFQ-ge8AAAAAAAAAAd9cHrW_OySwFuj4Ss2Usd83LEPqauc0s_svjeCQHw_a'
    file=imageName
    fileFrom=file
    fileTo='/NewFolder1/'+imageName
    dbx=dropbox.Dropbox(accessToken)
    with open(fileFrom,'rb')as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print('File Uploaded')

def main():
    while(True):
            if((time.time()-startTime)>300):
                name=takeSnapshot()
                upload(name)

main()