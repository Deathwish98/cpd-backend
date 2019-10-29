import cv2 
import os 
import sys

def get_filename_without_extension(file_path):
    file_basename = os.path.basename(file_path)
    filename_without_extension = file_path.split('.')[0]
    return filename_without_extension

def main(in_vid, in_thumb):

    # Read the video from specified path 
    cam = cv2.VideoCapture(in_vid) 
    
    try: 
        thumb_dir = os.path.join(os.getcwd(), './assets/thumbnails')
        thumb_dir = os.path.abspath(thumb_dir)
        # creating a folder named data 
        # if not os.path.exists('data'): 
        #     os.makedirs('data') 
      
    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of data') 
      
    ret,frame = cam.read()
         
    name = os.path.join(thumb_dir, get_filename_without_extension(in_thumb))
    name = name + '.jpg'
    cv2.imwrite(name, frame)
      
    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows()

    print((get_filename_without_extension(in_thumb) + '.jpg').strip())
    sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python {} video.ext".format(__name__))
    else:
        main(sys.argv[1], sys.argv[2])
