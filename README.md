## About

This is an Android Application, on which you can stylize your photo taken to various style. For example, you can change the background to 'the Great Wave' or simply grayscale.

To finish this application, I use three great repository:

1. [Mask RCNN](https://github.com/matterport/Mask_RCNN)
2. [fast-style-transfer](https://github.com/lengstrom/fast-style-transfer)
3. [Camera2Basic](https://github.com/googlearchive/android-Camera2Basic)

Also, if you want to run server on your computer, Mask RCNN & fast-style-transfer are needed.

## To use the Application:

1. Install Anaconda, virtual environment is needed, as different version of tensorflow will be used.

2. Download Mask RCNN, with the coco pretrained model, using Anaconda!

   Make sure you can run Mask RCNN first.

3. Download faster-style-transfer. There is no pretrained model, so you need to train it first.

   Also, use Anaconda. Make sure you can run Faster-style-transfer.

4. Open 'android-CamerArtist' project in './client' folder, using Android Studio
   1. open src/main/java/com/example/android/Tcp/Client.java;
   2. change the SERVER_IP to your IP, where you run the server;
   3. build the project, and run it on your mobile device.

5. Open './server' folder, put 'server.py' & 'demo.sh' in your 'Mask_RCNN/samples' folder.

   You need to change some information in demo.sh

   	1. source + the path to Anaconda virtual environment for faster-style-transfer
    	2. cd + the path to fast-style-transfer directory
    	3. python evalueate.py --checkpoint {path to checkpoint} --in-path {path to Mask_RCNN/images} --out-path {path to Desktop/Mask_RCNN/stylized (This directory is create by yourself)}

   Then run server.py, server will be started.

6. Now you can run your Application on mobile.