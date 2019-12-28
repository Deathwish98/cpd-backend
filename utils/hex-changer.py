import cv2
import numpy as np
import time
import sys
import math
import os

OUTPUT = []

def get_filename_without_extension(file_path):
    file_basename = os.path.basename(file_path)
    filename_without_extension = file_path.split('.')[0]
    return filename_without_extension


def main(in_vid_path, in_blind_type_arr):
    global OUTPUT
    for in_blind_type in in_blind_type_arr:
        cap = cv2.VideoCapture(in_vid_path)
        in_vid_name = get_filename_without_extension(in_vid_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        # paste path here inside quotes

    ##    case = input('Enter Your Choice')
        
        case = in_blind_type
        edited_vid = f'{in_vid_name}-{case}.mp4'
        OUTPUT.append(edited_vid)
        
    ##    name = case + str(date) + '.mp4'

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(edited_vid, 0x00000021, fps, (640,480))
        # out = cv2.VideoWriter(edited_vid, 0x7634706d, fps, (640,480))



        #change the case value
        #1 Protan Color Blindness
        #2 Deutan Color Blindness
        #3 Tritan Color Blindness

        while True:
            res, frame = cap.read()
            if (not res):
                break
            img = frame.copy()
            img = cv2.resize(img, (640,480))
            
            # Color Ranges in RGB
            
            #1 Red
            lower_red = np.array([245,150,122])
            lower_red1 = np.array([240,118,104])
            lower_red2 = np.array([223,140,112])
            lower_red3 = np.array([230,108,128])
            lower_red4 = np.array([195,82,82])
            lower_red5 = np.array([210,10,50])
            lower_red6 = np.array([168,24,24])
            lower_red7 = np.array([245,0,0])
            lower_red8 = np.array([129,0,0])
            lower_red9 = np.array([118,0,0])
            lower_red10 = np.array([245,89,71])
            lower_red11 = np.array([245,59,0])
            lower_red12 = np.array([209,102,147])
            upper_red = np.array([255,160,123])
            upper_red1 = np.array([250,128,115])
            upper_red2 = np.array([233,150,123])
            upper_red3 = np.array([240,128,129])
            upper_red4 = np.array([205,92,93])
            upper_red5 = np.array([220,20,61])
            upper_red6 = np.array([178,34,35])
            upper_red7 = np.array([255,0,1])
            upper_red8 = np.array([139,0,1])
            upper_red9 = np.array([128,0,1])
            upper_red10 = np.array([255,99,72])
            upper_red11 = np.array([255,69,1])
            upper_red12 = np.array([219,112,148])
            
            #2 Blue 
            lower_blue = np.array([230,238,245])
            lower_blue1 = np.array([220,220,240])
            lower_blue2 = np.array([166,214,220])
            lower_blue3 = np.array([163,206,220])
            lower_blue4 = np.array([125,196,225])
            lower_blue5 = np.array([0,181,245])
            lower_blue6 = np.array([166,186,212])
            lower_blue7 = np.array([20,134,245])
            lower_blue8 = np.array([90,139,227])
            lower_blue9 = np.array([60,120,170])
            lower_blue10 = np.array([85,148,150])
            lower_blue11 = np.array([113,94,228])
            lower_blue12 = np.array([96,80,195])
            lower_blue13 = np.array([62,51,129])
            lower_blue14 = np.array([55,95,215])
            lower_blue15 = np.array([0,0,245])
            lower_blue16 = np.array([0,0,195])
            lower_blue17 = np.array([0,0,129])
            lower_blue18 = np.array([0,0,118])
            lower_blue19 = np.array([15,15,102])
            lower_blue20 = np.array([128,33,216])
            lower_blue21 = np.array([65,0,120])
            lower_blue22 = np.array([125,196,240])
            upper_blue = np.array([241,248,255])
            upper_blue1 = np.array([230,230,251])
            upper_blue2 = np.array([176,224,231])
            upper_blue3 = np.array([173,216,231])
            upper_blue4 = np.array([135,206,236])
            upper_blue5 = np.array([1,191,255])
            upper_blue6 = np.array([176,196,223])
            upper_blue7 = np.array([31,144,255])
            upper_blue8 = np.array([101,149,237])
            upper_blue9 = np.array([70,130,181])
            upper_blue10 = np.array([95,158,161])
            upper_blue11 = np.array([123,104,239])
            upper_blue12 = np.array([106,90,206])
            upper_blue13 = np.array([72,61,140])
            upper_blue14 = np.array([65,105,226])
            upper_blue15 = np.array([0,1,255])
            upper_blue16 = np.array([1,0,205])
            upper_blue17 = np.array([0,1,139])
            upper_blue18 = np.array([1,0,128])
            upper_blue19 = np.array([26,25,112])
            upper_blue20 = np.array([138,44,226])
            upper_blue21 = np.array([75,0,131])
            upper_blue22 = np.array([135,207,250])

            #3 Green
            lower_green = np.array([114,242,0])
            lower_green1 = np.array([117,245,0])
            lower_green2 = np.array([40,195,40])
            lower_green3 = np.array([0,245,0])
            lower_green4 = np.array([24,129,24])
            lower_green5 = np.array([0,118,0])
            lower_green6 = np.array([0,90,0])
            lower_green7 = np.array([163,245,37])
            lower_green8 = np.array([144,195,40])
            lower_green9 = np.array([0,245,117])
            lower_green10 = np.array([0,240,144])
            lower_green11 = np.array([134,228,134])
            lower_green12 = np.array([142,241,142])
            lower_green13 = np.array([133,178,133])
            lower_green14 = np.array([50,169,103])
            lower_green15 = np.array([22,168,160])
            lower_green16 = np.array([36,129,77])
            lower_green17 = np.array([118,118,0])
            lower_green18 = np.array([75,97,37])
            lower_green19 = np.array([97,132,25])
            upper_green = np.array([124,252,1])
            upper_green1 = np.array([127,255,1])
            upper_green2 = np.array([50,205,51])
            upper_green3 = np.array([0,255,1])
            upper_green4 = np.array([34,139,35])
            upper_green5 = np.array([0,128,1])
            upper_green6 = np.array([0,100,1])
            upper_green7 = np.array([173,255,48])
            upper_green8 = np.array([154,205,51])
            upper_green9 = np.array([0,255,128])
            upper_green10 = np.array([0,250,155])
            upper_green11 = np.array([144,238,145])
            upper_green12 = np.array([152,251,153])
            upper_green13 = np.array([143,188,144])
            upper_green14 = np.array([60,179,112])
            upper_green15 = np.array([32,178,171])
            upper_green16 = np.array([46,139,88])
            upper_green17 = np.array([128,128,1])
            upper_green18 = np.array([85,107,48])
            upper_green19 = np.array([107,142,36])
            
            #Case Check
            #Don't change any value
            
            if case == 'Protan':
                
                img[np.where(cv2.inRange(img,lower_red,upper_red))] = [255,160,123]
                img[np.where(cv2.inRange(img,lower_green,upper_green))] = [124,242,0]
                img[np.where(cv2.inRange(img,lower_red1,upper_red1))] = [255,128,128]
                img[np.where(cv2.inRange(img,lower_green1,upper_green1))] = [127,245,0]
                img[np.where(cv2.inRange(img,lower_red2,upper_red2))] = [243,150,123]
                img[np.where(cv2.inRange(img,lower_green2,upper_green2))] = [50,195,51]
                img[np.where(cv2.inRange(img,lower_red3,upper_red3))] = [250,128,129]
                img[np.where(cv2.inRange(img,lower_green3,upper_green3))] = [0,245,0]
                img[np.where(cv2.inRange(img,lower_red4,upper_red4))] = [215,92,93]
                img[np.where(cv2.inRange(img,lower_green4,upper_green4))] = [34,129,35]
                img[np.where(cv2.inRange(img,lower_red5,upper_red5))] = [230,20,61]
                img[np.where(cv2.inRange(img,lower_green5,upper_green5))] = [0,118,1]
                img[np.where(cv2.inRange(img,lower_red6,upper_red6))] = [188,34,34]
                img[np.where(cv2.inRange(img,lower_green6,upper_green6))] = [0,90,0]
                img[np.where(cv2.inRange(img,lower_red7,upper_red7))] = [255,0,0]
                img[np.where(cv2.inRange(img,lower_green7,upper_green7))] = [173,245,48]
                img[np.where(cv2.inRange(img,lower_red8,upper_red8))] = [149,0,1]
                img[np.where(cv2.inRange(img,lower_green8,upper_green8))] = [154,195,51]
                img[np.where(cv2.inRange(img,lower_red9,upper_red9))] = [138,0,1]
                img[np.where(cv2.inRange(img,lower_green9,upper_green9))] = [0,245,128]
                img[np.where(cv2.inRange(img,lower_red10,upper_red10))] = [255,99,72]
                img[np.where(cv2.inRange(img,lower_green10,upper_green10))] = [0,240,155]
                img[np.where(cv2.inRange(img,lower_red11,upper_red11))] = [255,69,0]
                img[np.where(cv2.inRange(img,lower_green11,upper_green11))] = [144,228,145]
                img[np.where(cv2.inRange(img,lower_red12,upper_red12))] = [229,112,147]
                img[np.where(cv2.inRange(img,lower_green12,upper_green12))] = [152,241,153]
                img[np.where(cv2.inRange(img,lower_green13,upper_green13))] = [143,178,144]
                img[np.where(cv2.inRange(img,lower_green14,upper_green14))] = [60,169,112]
                img[np.where(cv2.inRange(img,lower_green15,upper_green15))] = [32,168,171]
                img[np.where(cv2.inRange(img,lower_green16,upper_green16))] = [46,129,88]
                img[np.where(cv2.inRange(img,lower_green17,upper_green17))] = [128,118,0]
                img[np.where(cv2.inRange(img,lower_green18,upper_green18))] = [85,97,48]
                img[np.where(cv2.inRange(img,lower_green19,upper_green19))] = [107,142,36]
                #img is the current frame of the video 
                #return whatever you want from here after processing is done
               
                
            elif case == 'Deutan':
                
                
                img[np.where(cv2.inRange(img,lower_red,upper_red))] = [255,150,123]
                img[np.where(cv2.inRange(img,lower_green,upper_green))] = [124,255,0]
                img[np.where(cv2.inRange(img,lower_red1,upper_red1))] = [250,118,115]
                img[np.where(cv2.inRange(img,lower_green1,upper_green1))] = [127,255,0]
                img[np.where(cv2.inRange(img,lower_red2,upper_red2))] = [233,140,123]
                img[np.where(cv2.inRange(img,lower_green2,upper_green2))] = [50,215,51]
                img[np.where(cv2.inRange(img,lower_red3,upper_red3))] = [240,118,129]
                img[np.where(cv2.inRange(img,lower_green3,upper_green3))] = [0,255,0]
                img[np.where(cv2.inRange(img,lower_red4,upper_red4))] = [205,82,93]
                img[np.where(cv2.inRange(img,lower_green4,upper_green4))] = [34,149,35]
                img[np.where(cv2.inRange(img,lower_red5,upper_red5))] = [220,10,61]
                img[np.where(cv2.inRange(img,lower_green5,upper_green5))] = [0,138,0]
                img[np.where(cv2.inRange(img,lower_red6,upper_red6))] = [178,24,35]
                img[np.where(cv2.inRange(img,lower_green6,upper_green6))] = [0,110,0]
                img[np.where(cv2.inRange(img,lower_red7,upper_red7))] = [255,0,0]
                img[np.where(cv2.inRange(img,lower_green7,upper_green7))] = [173,255,48]
                img[np.where(cv2.inRange(img,lower_red8,upper_red8))] = [139,0,0]
                img[np.where(cv2.inRange(img,lower_green8,upper_green8))] = [154,215,51]
                img[np.where(cv2.inRange(img,lower_red9,upper_red9))] = [128,0,0]
                img[np.where(cv2.inRange(img,lower_green9,upper_green9))] = [0,255,128]
                img[np.where(cv2.inRange(img,lower_red10,upper_red10))] = [255,89,72]
                img[np.where(cv2.inRange(img,lower_green10,upper_green10))] = [0,255,155]
                img[np.where(cv2.inRange(img,lower_red11,upper_red11))] = [255,59,0]
                img[np.where(cv2.inRange(img,lower_green11,upper_green11))] = [144,248,145]
                img[np.where(cv2.inRange(img,lower_red12,upper_red12))] = [219,102,148]
                img[np.where(cv2.inRange(img,lower_green12,upper_green12))] = [152,255,153]
                img[np.where(cv2.inRange(img,lower_green13,upper_green13))] = [143,198,144]
                img[np.where(cv2.inRange(img,lower_green14,upper_green14))] = [60,189,112]
                img[np.where(cv2.inRange(img,lower_green15,upper_green15))] = [32,188,171]
                img[np.where(cv2.inRange(img,lower_green16,upper_green16))] = [46,149,88]
                img[np.where(cv2.inRange(img,lower_green17,upper_green17))] = [128,138,0]
                img[np.where(cv2.inRange(img,lower_green18,upper_green18))] = [85,117,48]
                img[np.where(cv2.inRange(img,lower_green19,upper_green19))] = [107,162,36]
                #img is the current frame of the video 
                #return whatever you want from here after processing is done
              
                
            elif case == 'Tritan':
                img[np.where(cv2.inRange(img,lower_blue,upper_blue))] = [231,238,255]
                img[np.where(cv2.inRange(img,lower_blue1,upper_blue1))] = [220,220,255]
                img[np.where(cv2.inRange(img,lower_blue2,upper_blue2))] = [166,214,241]
                img[np.where(cv2.inRange(img,lower_blue3,upper_blue3))] = [163,206,241]
                img[np.where(cv2.inRange(img,lower_blue4,upper_blue4))] = [125,196,246]
                img[np.where(cv2.inRange(img,lower_blue5,upper_blue5))] = [0,181,255]
                img[np.where(cv2.inRange(img,lower_blue6,upper_blue6))] = [166,186,233]
                img[np.where(cv2.inRange(img,lower_blue7,upper_blue7))] = [21,134,255]
                img[np.where(cv2.inRange(img,lower_blue8,upper_blue8))] = [91,139,237]
                img[np.where(cv2.inRange(img,lower_blue9,upper_blue9))] = [60,120,191]
                img[np.where(cv2.inRange(img,lower_blue10,upper_blue10))] = [85,148,171]
                img[np.where(cv2.inRange(img,lower_blue11,upper_blue11))] = [113,94,229]
                img[np.where(cv2.inRange(img,lower_blue12,upper_blue12))] = [96,80,216]
                img[np.where(cv2.inRange(img,lower_blue13,upper_blue13))] = [62,51,150]
                img[np.where(cv2.inRange(img,lower_blue14,upper_blue14))] = [55,95,236]
                img[np.where(cv2.inRange(img,lower_blue15,upper_blue15))] = [0,0,255]
                img[np.where(cv2.inRange(img,lower_blue16,upper_blue16))] = [0,0,215]
                img[np.where(cv2.inRange(img,lower_blue17,upper_blue17))] = [0,0,149]
                img[np.where(cv2.inRange(img,lower_blue18,upper_blue18))] = [0,0,138]
                img[np.where(cv2.inRange(img,lower_blue19,upper_blue19))] = [16,15,122]
                img[np.where(cv2.inRange(img,lower_blue20,upper_blue20))] = [128,34,236]
                img[np.where(cv2.inRange(img,lower_blue21,upper_blue21))] = [65,0,141]
                img[np.where(cv2.inRange(img,lower_blue22,upper_blue22))] = [125,197,255]
                #img is the current frame of the video 
                #return whatever you want from here after processing is done
               
        ##    cv2.imshow('img', img)    
            out.write(img) 
            # return here if you want but make sure framerate is same as original
            # esc key to get out of loop
            k=cv2.waitKey(5) & 0xFF
            if k==27:
                break

        cap.release()
        out.release()

        cv2.destroyAllWindows()

    OUTPUT = ','.join(OUTPUT)
    print(OUTPUT)
    sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python {} video.ext blind_type".format(__name__))
    else:
        arr = sys.argv[2].split(',')
        main(sys.argv[1], arr)
