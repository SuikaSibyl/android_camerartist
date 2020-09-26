import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt

from multiprocessing import Process

# Root directory of the project
ROOT_DIR = os.path.abspath("../")
# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")
# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")
# Download COCO trained weights from Releases if needed
# if not os.path.exists(COCO_MODEL_PATH):
#     utils.download_trained_weights(COCO_MODEL_PATH)

# Directory of images to run detection on
IMAGE_DIR = os.path.join(ROOT_DIR, "images")

from datetime import datetime
import time
# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))  # To find local version
import coco
# ## Configurations
#
# We'll be using a model trained on the MS-COCO dataset. The configurations of this model are in the ```CocoConfig``` class in ```coco.py```.
#
# For inferencing, modify the configurations a bit to fit the task. To do so, sub-class the ```CocoConfig``` class and override the attributes you need to change.

class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


import time  # 引入time模块
# COCO Class names
# Index of the class in the list is its ID. For example, to get ID of
# the teddy bear class, use: class_names.index('teddy bear')
class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']

# Deynamic use GPU
import tensorflow as tf
import keras

config1 = tf.ConfigProto()
config1.gpu_options.allow_growth = True

# ## Create Model and Load Trained Weights
config2 = InferenceConfig()
config2.display()

def myProcess1():
    recorder = open("./record_mode0.csv", "a")
    start = time.clock()

    keras.backend.tensorflow_backend.set_session(tf.Session(config=config1))
    # Create model object in inference mode.
    model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config2)
    # Load weights trained on MS-COCO
    model.load_weights(COCO_MODEL_PATH, by_name=True)

    elapsed = time.clock()
    recorder.write(str(elapsed - start))
    start = elapsed
    recorder.write(",")

    # Run detection
    results = model.detect([image], verbose=1)
    print("Process going")
    IMAGE_DIR

    elapsed = time.clock()
    recorder.write(str(elapsed - start))
    start = elapsed
    recorder.write(",")

    stylized = skimage.io.imread("../stylized/send.jpg")

    # Visualize results
    print(type(results[0]))
    r = results[0]
    result_image = visualize.display_instances(image, stylized, r['rois'], r['masks'], r['class_ids'],
                                class_names, r['scores'])

    elapsed = time.clock()
    recorder.write(str(elapsed - start))
    start = elapsed
    recorder.write(",")

    from PIL import Image
    im = Image.fromarray(result_image)
    im.save("out.jpeg")

    elapsed = time.clock()
    recorder.write(str(elapsed - start))
    print(elapsed - start)
    recorder.write(",\r\n")
    recorder.close()

def myProcess2():
    recorder = open("./record_mode1.csv", "a")
    start = time.clock()

    keras.backend.tensorflow_backend.set_session(tf.Session(config=config1))
    # Create model object in inference mode.
    model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config2)
    # Load weights trained on MS-COCO
    model.load_weights(COCO_MODEL_PATH, by_name=True)

    elapsed = time.clock()
    recorder.write(str(elapsed - start))
    start = elapsed
    recorder.write(",")

    # Run detection
    results = model.detect([image], verbose=1)
    print("Process going")
    IMAGE_DIR

    elapsed = time.clock()
    recorder.write(str(elapsed - start))
    start = elapsed
    recorder.write(",")

    # Visualize results
    print(type(results[0]))
    r = results[0]
    result_image = visualize.fadebackground(image, r['rois'], r['masks'], r['class_ids'],
                                               class_names, r['scores'])

    elapsed = time.clock()
    recorder.write(str(elapsed - start))
    start = elapsed
    recorder.write(",")

    from PIL import Image
    im = Image.fromarray(result_image)
    im.save("out.jpeg")

    elapsed = time.clock()
    recorder.write(str(elapsed - start))
    print(elapsed - start)
    recorder.write(",\r\n")
    recorder.close()


if __name__== '__main__':
    ## Run Object Detection
    import gc
    import socket

    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 固定端口号
    tcp_socket.bind(("", 8999))
    # 将主动套接字转为被动套接字
    tcp_socket.listen(1)

    while True:
        print("======== 等待连接 ========")
        # 利用accept获取分套接字以及客户端的地址
        client_socket, client_addr = tcp_socket.accept()

        for index in range(0, len(client_addr), 2):
            print("Ip:" + client_addr[index] + "已连接")

        try:
            # length = int.from_bytes(client_socket.recv(1024), 'big')
            # print(length)

            fo = open("../images/send.jpg", "wb")

            recorder = open("./record.csv", "a")
            start = time.clock()

            rec_4byte = client_socket.recv(4)
            rec_type = rec_4byte[0]
            print("Process mode: ", rec_type)

            print("======== 开始接收文件 ========");
            while True:
                rec_bytes = client_socket.recv(1024)
                if len(rec_bytes) == 0:
                    break
                fo.write(rec_bytes)
            fo.close()
            print("======== 文件接收成功 ========");

            elapsed = time.clock()
            recorder.write(str(elapsed-start))
            recorder.write(",")
            start = elapsed
            recorder.close()

            import os
            os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

            if rec_type == 0:
                recorder = open("./record_mode0.csv", "a")
                start = time.time()

                cmd = "./demo.sh"
                # os.system(cmd)
                data = os.popen(cmd)
                print
                data.read()

                # Load a random image from the images folder
                file_names = next(os.walk(IMAGE_DIR))[2]
                image = skimage.io.imread(os.path.join(IMAGE_DIR, random.choice(file_names)))

                # RECORD TIME
                elapsed = time.time()
                recorder.write(str(elapsed - start))
                recorder.write(",")
                start = elapsed
                recorder.close()

                p = Process(target=myProcess1)
                p.start()
                p.join()

            elif rec_type == 1:
                # Load a random image from the images folder
                file_names = next(os.walk(IMAGE_DIR))[2]
                image = skimage.io.imread(os.path.join(IMAGE_DIR, random.choice(file_names)))

                p = Process(target=myProcess2)
                p.start()
                p.join()

            recorder = open("./record.csv", "a")
            start = time.clock()

            fout = open("./out.jpeg", "rb+")

            print("======== 开始回传结果 ========");
            while True:
                data = fout.read(1024)
                if not data:
                    break
                client_socket.send(data)

            client_socket.close()
            print("======== 结束连接 ========");

            elapsed = time.clock()
            recorder.write(str(elapsed-start))
            recorder.write(",\r\n")
            start = elapsed
            recorder.close()

        except IOError:
            print("没有该文件")