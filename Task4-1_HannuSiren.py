from flask import Flask
from flask import json
from flask import Response, request
import tensorflow as tf
from urllib.request import urlretrieve


import importlib.util
spec = importlib.util.spec_from_file_location("yolo", "D:/jyu/TIES4911 Deep-Learning for Cognitive Computing for devs/Task 4/YOLO_tensorflow-master/YOLO_tiny_tf.py")
yolo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(yolo)


app = Flask(__name__)
graph_path = 'D:/jyu/TIES4911 Deep-Learning for Cognitive Computing for devs/Task 3/output_graph_tiny.pb'
labels_path = 'D:/jyu/TIES4911 Deep-Learning for Cognitive Computing for devs/Task 3/output_labels_tiny.txt'
#@app.route('/yolo_classify', methods=['POST'])
@app.route('/yolo_classify', methods=['GET'])
def yolo_classify():
    #image_path = request.json['imageURL']
    image_path = 'https://upload.wikimedia.org/wikipedia/commons/e/e7/Leptotyphlops_carlae.jpg'
    output = {'result':[]}

    #with urllib.request.urlopen(image_path) as url: #python 3 support
        #image_data_original = url.read()
        #image_data = url.read()
    downloadedImg = 'test.jpg'
    result_txt = "result.txt"
    #urlretrieve(image_path, downloadedImg) 
    #yolo.YOLO_TF(['-fromfile', downloadedImg, '-tofile_txt', result_txt])
    yolo.YOLO_TF(['-fromfile', downloadedImg])
    #sleep(2)

    output_ = {}

    with open(result_txt) as f:
        output_ = {
        'result' : f.readlines()
        }

    output['result'].append(output_)
    js = json.dumps(output, sort_keys=True, indent=4)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://myWeb.com'
    return js

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
