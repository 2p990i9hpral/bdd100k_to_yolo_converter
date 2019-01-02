# Dependency
* tqdm
* cv2
  
  
# How to use
download bdd100k file(Images, Labels) from http://bdd-data.berkeley.edu/index.html

make directory structure and move files
```
* bdd100k_to_yolo_converter
  - 100k  
    + test  
       * img  
    + train  
       * img  
    + val  
       * img      
  - labels  
    + bdd100k_labels_images_train.json  
    + bdd100k_labels_images_val.json
  - bdd100k2yolo.py  
```

run "bdd100k2yolo.py" file

