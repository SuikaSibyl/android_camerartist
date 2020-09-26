#!/bin/bash
source ~/anaconda3/bin/activate tf21-gpu
cd ~/Desktop/fast-style-transfer
python evaluate.py --checkpoint ~/Desktop/fast-style-transfer/checkpoint --in-path ~/Desktop/Mask_RCNN/images --out-path ~/Desktop/Mask_RCNN/stylized
