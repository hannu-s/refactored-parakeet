darkflow

pip install --upgrade cython
python3 setup.py build_ext --inplace
pip install opencv-python

lataa painot https://pjreddie.com/darknet/yolo/ - tiny yolo 

korvaa cfg/tiny-ylo.cfg tiedosto uudella versiolla
virhe: expect 44948596 bytes, found 44948600 
    darkflow/utils/loader.py rivi 121 => self.offset = 20 (normi arvo 16)


python flow --model cfg/tiny-yolo.cfg --load bin/tiny-yolo.weights
python flow --model cfg/yolo-new.cfg
python flow --model cfg/yolo-new.cfg --load bin/tiny-yolo.weights

python flow --imgdir sample_img/ --model cfg/tiny-yolo.cfg --load bin/tiny-yolo.weights --gpu 1.0


    python flow --imgdir sample_img/ --model cfg/tiny-yolo.cfg --load bin/tiny-yolo.weights --json




YOLO_tensorflow

lataa painot https://drive.google.com/file/d/0B2JbaJSrWLpza0FtQlc3ejhMTTA/view

korjaa printit python3 tyyliin



python YOLO_(small or tiny)_tf.py -fromfile (input image filename)
python YOLO_tiny_tf.py -fromfile "D:\jyu\TIES4911 Deep-Learning for Cognitive Computing for devs\Task 4\YOLO_tensorflow-master\test\person.jpg"
python YOLO_tiny_tf.py -fromfile "D:\jyu\TIES4911 Deep-Learning for Cognitive Computing for devs\Task 4\YOLO_tensorflow-master\test\person.jpg" -tofile_txt "test.txt"