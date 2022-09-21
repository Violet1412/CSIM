# CSIM
We provide the CSIM algorithm, including modified network and structure and trained weight files.
## Requirements for Windows, Linux and macOS
•	CMake   
•	Powershell    
•	CUDA >= 10.2:  
•	OpenCV >= 2.4:   
•	cuDNN >= 8.0.2   
•	GPU  
## Note
If you use build.ps1 script or the makefile (Linux only) you will find darknet in the root directory.  
If you use the deprecated Visual Studio solutions, you will find darknet in the directory \build\darknet\x64.  
If you customize build with CMake GUI, darknet executable will be installed in your preferred folder.  

## How to train (to detect your custom objects)
For training cfg/yolov4-custom.cfg download the pre-trained weights-file 
Create file yolo-obj.cfg and:  
change line batch   
change line subdivisions  
change line max_batches to (classes*2000, but not less than number of training images and not less than 6000), f.e. max_batches=6000 if you train for 3 classes)  
change line steps to 80% and 90% of max_batches, f.e. steps=4800,5400  
change line classes= to your number of objects in each of 3 [yolo]-layers:  
change [filters=255] to filters=(classes + 5)x3 in the 3 [convolutional] before each [yolo] layer, keep in mind that it only has to be the last [convolutional] before each of the [yolo] layers.  
Create file obj.names in the directory build\darknet\x64\data\, with objects names - each in new line  
Create file obj.data in the directory build\darknet\x64\data\, containing (where classes = number of objects):  
Put image-files (.jpg) of your objects in the directory build\darknet\x64\data\obj\  
You should label each object on images from your dataset. Use this visual GUI-software for marking bounded boxes of objects and generating annotation files  
Create file train.txt in directory build\darknet\x64\data\, with filenames of your images, each filename in new line, with path relative to darknet.exe, for example containing:  
Download pre-trained weights for the convolutional layers and put to the directory build\darknet\x64  

Start training by using the command line: darknet.exe detector train data/csim.data bdd.cfg csim_final.weights    
Note: If you changed width= or height= in your cfg-file, then new width and height must be divisible by 32.   
Note: After training use such command for detection: darknet.exe detector test data/bdd.data csim.cfg csim_final.weights    

## Dataset and trained weight file
We provide our dataset and trained weight file.
[BDD100k-selfmade](https://pan.baidu.com/s/10CbIF-zQ5X-h7bh_uGSOMg)Extraction code：dhyl
[Weight file](https://pan.baidu.com/s/1xl-1TIj3zKEoOxGCuaXWcA)Extraction code：86n8




