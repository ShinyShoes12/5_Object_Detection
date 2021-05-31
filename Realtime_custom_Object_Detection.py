## 1. Check out : GPU

GPU상태 확인
1. Driver version : 사용하고 있는 GPU_Driver version

2. CUDA Version : 사용하고 있는 드라이버의 추천 CUDA version (사용하고 있는 CUDA version x)

3. GPU/Fan : 0-7까지는 GPU number 이며, N/A가 표기 된 곳은 Fan이 장착 되어있는 GPU 사용시 사용 %로 표기, tesla계열의 GPU에는 fan이 없다.

4. Name : GPU model

   persistence-m : 파워지속성 모드 (default 는 off 이다.) on으로 변경시 파워제한을 걸 수 있다.

   Temp : GPU온도, 일정 온도가 지나면 성능 저하 및 GPU drop이 발생

   Perf : Performance mode P0 ~ P12 까지 있으며, 숫자가 작을수록 많은 high-performance 상태이다.

   Pwr:usage/cap : GPU의 usage 현재 전력 사용량과 cap 최대용량

5. Bus-id : 서버 제조사의 메인보드마다 가지고 있는 PCI slot에 부여된 Bus-id, Bus-id를 참고하여 사용하는 GPU number와 메인보드의 PCI 슬롯을 매칭 시켜 확인 할 수 있다.

   Disp.A : RTX나 Quadro 계열의 GPU에서 사용, 모니터를 연결한 출력 포트의 GPU는 on 상태로 변경

   Memory-Usage : 현재 사용하는 GPU 메모리 / 총 GPU 메모리

6. Voltaile GPU-Util : GPU의 총 사용량

   Uncorr. ECC : ECC count가 생기면 숫자 0이 계속 증가하며, default 값은 ECC ON 상태이다.
	- ECC ON 상태에서 count가 계속 발생하면 시스템 Hang이 발생하므로, Off 시켜놓고 작업하는 곳이 많다.
	  (nvidia-smi -e 0)

   Compute M : 현재 사용중인 compute Mode
	- 0 : default
	- 1 : exclusive_thread
	- 2 : prohibited
	- 3 : exclusive_process

7. Processes : GPU가 작업을 시작하면 No running processes found 에 PID process ID등 현재 사용중인 내용들이 표기



## 2. Mount Google Drive

Google Drive와 연동



## 3. Unzip picture_data

Google Drive에 yolo_custom_model_Training 폴더 생성

yolo_custom_model_Training 폴더 안에 custom_data.zip 업로드 후 unzip 한다.



## 4. Get AlexeyAB/darknet

darknet : C언어로 작성된 물체 인식 오픈소스 신경망

AlexeyAB의 github로 부터 yolo_custom_model_Training/darknet에 git clone 한다.

darknet으로 이동후 Makefile의 값을 수정한 후 compile 한다.

	- OPENCV, GPU, CUDNN, CUDNN_HALF, LIBSO 활성화

%cd ..
!darknet/darknet

위의 코드를 실행 했을 때 usage: darknet/darknet <function> 와 같은 결과가 출력되어야 한다.



## 5. Create Train&Test dataset

train.txt, test.txt, labelled_data.data 생성을 위해 github에서 training_yolo_custom_object_detection_files를 다운

creating-train-and-test-txt-files.py 와 creating-files-data-and-name.py 파일을 custom_data 로 이동 후 경로 및 확장자명을 변경한다.

train.txt, test.txt, labelled_data.data 파일 생성



## 6. Setting diretory & values

custom_weight 폴더 생성

Google에서 yolov4.conv.137파일 다운

yolov4.conv.137파일을 custom_weight 폴더 밑으로 이동

yolov4.cfg 파일을 yolov4_custom.cfg 파일로 복사 후 안의 내용들을 수정
	- maxbatch = classes * 2000
	- filters = (5 + classes) * 3

backup 폴더 생성



## 7. Train the model

모델 훈련



## 8. Check performance

imShow 함수 생성 후 모델 훈련 후 만들어진 chart.png 파일 확인

5번에서 생성한 test.txt, train.txt, labelled_data.data의 경로 수정 (경로를 수정하지 않고 8.1 Check mAP 단계가 잘 실행 된다면 수행하지 않아도 된다.)

darknet 의 권한 부여 후 mAP 확인



## 9. Test custom Object Detection

yolov4_custom.cfg 파일의 batch와 subdivisions 을 1로 변경

## 9.1 Run detector on an image
드라이브에 있는 사진을 이용하여 Obj Detection

!./darknet detector test /content/drive/MyDrive/yolo_custom_model_Training/custom_data/labelled_data.data /content/drive/MyDrive/yolo_custom_model_Training/darknet/cfg/yolov4_custom.cfg /content/drive/MyDrive/yolo_custom_model_Training/backup/yolov4_custom_10000.weights /content/drive/MyDrive/yolo_custom_model_Training/custom_data/1.jpg -thresh 0.3

이미지의 이름(1.jpg)을 변경해서 원하는 이미지를 detection 할 수 있다.

 ## 9.2 Run detector on a webcam image 

webcam을 이용하여 capture 한 이미즈를 detection 

## 9.3 Run detector on a video

드라이브에 있는 동영상을 이용하여 Obj Detection

## 9.4 Run detector on a live webcam

webcam을 이용하여 real time Obj Detection


