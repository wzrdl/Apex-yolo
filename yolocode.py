import os
import xml.etree.ElementTree as ET


def change_one_xml(xml_path, xml_dw, update_content):
    # 打开xml文档
    doc = ET.parse(xml_path)
    root = doc.getroot()
    # 查找修改路劲
    sub1 = root.find(xml_dw)
    # 修改标签内容
    sub1.text = update_content
    # 保存修改
    doc.write(xml_path)


image_path=r'C:\\Users\wzrdl\Desktop\\yolo\\apexdataset\\JPEGImages'
image_filename=os.listdir(image_path)
print(image_filename)
annotation_path=r'C:\\Users\wzrdl\Desktop\\yolo\\apexdataset\\annotations'
annotation_filename=os.listdir(annotation_path)
print(annotation_filename)
count=0

for file in annotation_filename:
    # 欲修改文件
    xml_path = os.path.join(annotation_path ,file)

    # 修改文件中的xpath定位
    xml_dw = './/folder'

    # 想要修改成什么内容
    update_content = 'JPEGImages'
    change_one_xml(xml_path, xml_dw, update_content)
    splitext = os.path.splitext(file)

#python tools/infer.py -c configs/ppyolo/ppyolov2_r50vd_dcn_voc.yml --infer_img=../1.png -o weights=output/ppyolov2_r50vd_dcn_voc/model_final.pdparams


#paddlex --split_dataset --format VOC --dataset_dir smoke --val_value 0.2 --test_value 0.1

#python tools/train.py -c configs/ppyolo/ppyolov2_r50vd_dcn_voc.yml --eval --use_vdl=True --vdl_log_dir="./output"


#python tools/infer.py -c configs/ppyolo/ppyolov2_r50vd_dcn_voc.yml -o weights=output/ppyolov2_r50vd_dcn_voc/model_final.pdparams --infer_dir=../test

#python tools/eval.py -c configs/ppyolo/ppyolov2_r50vd_dcn_voc.yml  -o use_gpu=true