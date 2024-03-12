import cv2
import mediapipe as mp
import numpy as np
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import os
import subprocess
import json  # For working with OpenPose JSON output

# Define angle and score functions
def angle(v1, v2):
    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return np.arccos(cos_theta) * 180 / np.pi

def score(angles):
    return np.mean(angles) / 180



# Initialize pose model and video capture
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
cap = cv2.VideoCapture(0)

# Function to get user details
def get_user_details():
    root = tk.Tk()
    root.withdraw()

    # Create a custom dialog box for user details
    dialog = tk.Toplevel(root)
    dialog.title("User Details")

    # Set dialog box size
    dialog_width = 400
    dialog_height = 300
    dialog.geometry(f"{dialog_width}x{dialog_height}")

    # Function to center the dialog box on the screen
    def center_window():
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()
        x = (screen_width - dialog_width) // 2
        y = (screen_height - dialog_height) // 2
        dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    # Center the dialog box on the screen
    center_window()

    # Create a frame to hold the input fields
    frame = tk.Frame(dialog)
    frame.pack(pady=20)

    # Entry fields for first name, last name, and age
    tk.Label(frame, text="First Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
    tk.Label(frame, text="Last Name:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
    tk.Label(frame, text="Age:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)

    first_name_entry = tk.Entry(frame, font=("Arial", 12))
    last_name_entry = tk.Entry(frame, font=("Arial", 12))
    age_entry = tk.Entry(frame, font=("Arial", 12))

    first_name_entry.grid(row=0, column=1, padx=10, pady=5)
    last_name_entry.grid(row=1, column=1, padx=10, pady=5)
    age_entry.grid(row=2, column=1, padx=10, pady=5)

    # Function to get user input and destroy dialog box
    def get_input():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        age = age_entry.get()
        user_name = f"{first_name}_{last_name}_{age}"
        dialog.destroy()
        root.destroy()
        start_leg_movement_tracking(user_name)

    # Button to confirm input
    ok_button = tk.Button(dialog, text="OK", command=get_input, font=("Arial", 12))
    ok_button.pack(pady=10)

    # Center the dialog box on the screen after it appears
    dialog.update_idletasks()
    center_window()

    # Keep the dialog box open until user input is provided
    dialog.wait_window()


def start_leg_movement_tracking(user_name):
    # Create main window
    root = tk.Tk()
    root.title(f"Leg Movement Scorer - {user_name}")

    # Maximize the window
    root.state('zoomed')

    # Initialize pose model and video capture
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    cap = cv2.VideoCapture(0)

    # Function to update frame
    def update_frame():
        global frame
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame)
            if results.pose_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            label.config(image=photo)
            label.image = photo
            label.after(10, update_frame)
    
    

    # Function to calculate and display score
    def calculate_score():
        import os

import subprocess

 #This will take a video and put a the points over it

 #Once openpose is installed, you can then run this and input a video for the code to add points

def newVideos():



 if not os.path.exists("/content/videos/"):

  os.mkdir("/content/videos/")



 from google.colab import files

 var = input('do you want to input a new video Y/N: ')

 while var == "Y":

  if var == "Y":


   uploaded = files.upload()

   var = input('do you want to input a new video Y/N: ')

 VideoPath = '/content/videos/'

 if not os.path.exists("/content/output/"):

  os.mkdir("/content/output/")



 for video in os.listdir(VideoPath):

  VideoName = video[:-4]

  InputVideo = VideoPath + video

  OutputDir = "/content/output/output_" + VideoName + "/"



  if not os.path.exists(OutputDir):

   os.mkdir(OutputDir)

  process = "cd /content/openpose && /content/openpose/build/examples/openpose/openpose.bin --video /content/videos/" + video + " --part_candidates --write_json " + OutputDir + "keypoints/ --write_coco_json " + OutputDir + "keypoints.json --display 0 --write_video " + OutputDir + "openpose.mp4"



  # pipe = subprocess.run(process, shell=True)

  try:
          !{process}

  except:

   print("process failed")   "Back Straight: " + str(backStraight) +" :Back curved, lowest back straightness reached " + str(backLeastPercent) + "%, try to keep it straight \n"

print("Back Straight: " + str(backStraight) + ": back was not kept straight, dipped below: " + str(backLeastPercent)[0:5] + "%")

fin.write(printer)

if heelCount < frame and heelcheck != 0:

    heelsRaised = False

    print("Heels Raised: " + str(heelsRaised) + ": Max Angle Reached: " + str(heelsemiMax)[0:5])

    printer = "Heels Raised: " + str(heelsRaised) + ": Heels Appeared to stay on the ground, never went above " + str(heelsemiMax)[0:5] + " degrees above the ground \n"

    fin.write(printer)

elif heelcheck != 0:

    heelsRaised = True

    print("Heels Raised: " + str(heelsRaised) + ": Max Angle Reached: " + str(heelmaxAngle)[0:5])

    printer = "Heels Raised: " + str(heelsRaised) + ": Heels Appeared to elevate off of the ground, heels reached " + str(heelmaxAngle)[0:5] + " degrees above the ground \n"

    fin.write(printer)

else:

    heelsRaised = True

    heelies = "Heels Raised: True: Not enough accurate points counted"

    print(heelies)

    printer = "Heels Raised: Programmed didn't have enough accurate points for a reading, do eye test \n"

    fin.write(printer)

if handsCount < frame*2 and handschecker != 0:

    handsAligned = True

    print("Hands aligned: " + str(handsAligned) + ": Least Angle Reached: " + str(handssemiMax)[0:5])

    printer = "Hands aligned: " + str(handsAligned) + ": Hands Appeared to be aligned with ankles, never went strayed more than " + str(handssemiMax)[0:5] + " degrees \n"

    fin.write(printer)

elif handschecker != 0:

    handsAligned = False

    print("Hands aligned: " + str(handsAligned) + ": Least Angle Reached: " + str(handsmaxAngle)[0:5])

    printer = "Hands aligned: " + str(handsAligned) + ":Hands Appeared to not be aligned with ankles, strayed more than " + str(handsmaxAngle)[0:5] + " degrees, try to keep hands straight up \n"

    fin.write(printer)

else:

    handsAligned = False

    print("Hands aligned: " + str(handsAligned) + ": Not Enough Points for Accurate Reading")

    printer = "Hands Aligned: Not enough accurate points for a reading, do eye test \n"

    fin.write(printer)

if chestCount < frame and squarechecker != 0:

    chestAligned = True

    print("Shoulders Aligned: " + str(chestAligned) + ": Max Angle Reached: " + str(squaresemiMax)[0:5])

    printer = "Shoulders Aligned: " + str(chestAligned) + ": Shoulders appear aligned, never seperated by more than " + str(squaresemiMax)[0:5] + " degrees \n"

    fin.write(printer)

elif squarechecker != 0:

    chestAligned = False

    print("Shoulders Aligned: " + str(chestAligned) + ": Max Angle Reached: " + str(squaremaxAngle)[0:5])

    printer = "Shoulders Aligned: " + str(chestAligned) + ": Shoulder appear to seperate to much, more than " + str(squaremaxAngle)[0:5] + " degrees of offset, try to square up your chest \n"

    fin.write(printer)

else:

    chestAligned = False

    print("Shoulders Aligned: " + str(chestAligned) + ": Not Enough Accurate Points For Reading")

    printer = "Shoulders Aligned: Not enough confident points for an accurate reading, do eye test \n"

    fin.write(printer)

if hipCount < frame and boxchecker != 0:

    hipAligned = True

    print("Hip Aligned: " + str(hipAligned) + ": Max Angle Reached: " + str(boxsemiMax)[0:5])

    printer = "Hip Aligned: " + str(hipAligned) + ": Hips appear to be aligned, never seperated by more than " + str(boxsemiMax)[0:5] + " degrees \n"

    fin.write(printer)

elif boxchecker != 0:

    hipsAligned = False

    print("Hip Aligned: " + str(hipAligned) + ": Max Angle Reached: " + str(boxmaxAngle)[0:5])

    printer = "Hip Aligned: " + str(hipAligned) + ": Hips appear to be offset, seperated by more than " + str(boxmaxAngle)[0:5] + " degrees, try to kip your hips level \n"

    fin.write(printer)

else:

    hipAligned = False

    print("Hip Aligned: " + str(hipAligned) + ": Not Enough Accurate Points for Reading")

    printer = "Hips Aligned: Not Enough accurate points for a reading, do eye test \n"

    fin.write(printer)

if heelsRaised == False and falseCount == 0:

   print("Score: 3")

   printer = "Score: 3 \n"

   fin.write(printer)

elif falseCount == 1:

   print("Score: 2")

   printer = "Score: 2 \n"

   fin.write(printer)

else:

   print("Score: 1")

   printer = "Score: 1 \n"

   fin.write(printer)

fin.close()



#import code taken from the source code share from google colab

#to run evyerhting together, you have to run from the start up in the runtime tab

#this is code I found for a Google Colab addition of OpenPose

import os

from os.path import exists, join, basename, splitext

 #!cd /content/drive/MyDrive

def downloadOpenPose():

 git_repo_url = 'https://github.com/CMU-Perceptual-Computing-Lab/openpose.git'

 project_name = splitext(basename(git_repo_url))[0]

 if not exists(project_name):

  # see: https://github.com/CMU-Perceptual-Computing-Lab/openpose/issues/949

  # install new CMake becaue of CUDA10

  !wget -q https://cmake.org/files/v3.13/cmake-3.13.0-Linux-x86_64.tar.gz

  !tar xfz cmake-3.13.0-Linux-x86_64.tar.gz --strip-components=1 -C /usr/local

  # clone openpose

  !git clone -q --depth 1 $git_repo_url

  !sed -i 's/execute_process(COMMAND git checkout master WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}\/3rdparty\/caffe)/execute_process(COMMAND git checkout f019d0dfe86f49d1140961f8c7dec22130c83154 WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}\/3rdparty\/caffe)/g' openpose/CMakeLists.txt

  # install system dependencies

  !apt-get -qq install -y libatlas-base-dev libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler libgflags-dev libgoogle-glog-dev liblmdb-dev opencl-headers ocl-icd-opencl-dev libviennacl-dev

  # install python dependencies

  !pip install -q youtube-dl

  # install microprocess

  !pip install multiprocess

  # build openpose

  !cd openpose && rm -rf build || true && mkdir build && cd build && cmake .. && make -j`nproc`



  return "Done installing Openpose"

# import dependencies

from IPython.display import display, Javascript, Image

from google.colab.output import eval_js

from base64 import b64decode, b64encode

import cv2

import numpy as np

import PIL

import io

import html

import time



# function to convert the JavaScript object into an OpenCV image

def js_to_image(js_reply):

 """

 Params:

     js_reply: JavaScript object containing image from webcam

 Returns:

     img: OpenCV BGR image

 """

 # decode base64 image

 image_bytes = b64decode(js_reply.split(',')[1])

 # convert bytes to numpy array

 jpg_as_np = np.frombuffer(image_bytes, dtype=np.uint8)

 # decode numpy array into OpenCV BGR image

 img = cv2.imdecode(jpg_as_np, flags=1)



 return img



# function to convert OpenCV Rectangle bounding box image into base64 byte string to be overlayed on video stream

def bbox_to_bytes(bbox_array):

 """

 Params:

     bbox_array: Numpy array (pixels) containing rectangle to overlay on video stream.

 Returns:

    bytes: Base64 image byte string

 """

 # convert array into PIL image

 bbox_PIL = PIL.Image.fromarray(bbox_array, 'RGBA')

 iobuf = io.BytesIO()

 # format bbox into png for return

 bbox_PIL.save(iobuf, format='png')

 # format return string

 bbox_bytes = 'data:image/png;base64,{}'.format((str(b64encode(iobuf.getvalue()), 'utf-8')))



 return bbox_bytes

# JavaScript to properly create our live video stream using our webcam as input

def video_streamSingle():

 js = Javascript('''

  var video;

  var div = null;

  var stream;

  var captureCanvas;

  var imgElement;

  var labelElement;



  var pendingResolve = null;

  var shutdown = false;



  function removeDom() {

    stream.getVideoTracks()[0].stop();

    video.remove();

    div.remove();

    video = null;

    div = null;

    stream = null;

    imgElement = null;

    captureCanvas = null;

    labelElement = null;

  }



  function onAnimationFrame() {

   if (!shutdown) {

    window.requestAnimationFrame(onAnimationFrame);

   }

   if (pendingResolve) {

    var result = "";

    if (!shutdown) {

     captureCanvas.getContext('2d').drawImage(video, 0, 0, 640, 480);

     result = captureCanvas.toDataURL('image/jpeg', 0.8)

    }

    var lp = pendingResolve;

    pendingResolve = null;

    lp(result);

   }

  }



  async function createDom() {

   if (div !== null) {

    return stream;

   }



   div = document.createElement('div');

   div.style.border = '2px solid black';

   div.style.padding = '3px';

   div.style.width = '100%';

   div.style.maxWidth = '600px';

   document.body.appendChild(div);



   const modelOut = document.createElement('div');

   modelOut.innerHTML = "<span>Status:</span>";

   labelElement = document.createElement('span');

   labelElement.innerText = 'No data';

   labelElement.style.fontWeight = 'bold';

   modelOut.appendChild(labelElement);

   div.appendChild(modelOut);



   video = document.createElement('video');

   video.style.display = 'block';

   video.width = div.clientWidth - 6;

   video.setAttribute('playsinline', '');

   video.onclick = () => { shutdown = true; };

   const myVideos = [];

   await navigator.mediaDevices.enumerateDevices().then(answers => {

    answers.forEach(answer => {

     if (answer.kind === 'videoinput'){

      myVideos.push(answer);

     }

    })

   })

   .catch(error => {

    console.log(error);

   });

   stream = await navigator.mediaDevices.getUserMedia({

     video: {

      deviceId: myVideos[0].deviceId

     }

   });

   //navigator.mediaDevices.enumerateDevices().then(function(devices =>{console.log(devices)}));

   /*stream = await navigator.mediaDevices.getUserMedia(

     {video: { facingMode: "environment"}});

   //stream = await navigator.mediaDevices.getUserMedia(

     //{video: { deviceId: {exact: camera1ID }}});*/



   var videoTrack = stream.getVideoTracks();



   div.appendChild(video);



   imgElement = document.createElement('img');

   imgElement.style.position = 'absolute';

   imgElement.style.zIndex = 1;

   imgElement.onclick = () => { shutdown = true; };

   div.appendChild(imgElement);



   const instruction = document.createElement('div');

   instruction.innerHTML =

     '<span style="color: red; font-weight: bold;">' +

     'When finished, click here or on the video to stop this demo</span>';

   div.appendChild(instruction);

   instruction.onclick = () => { shutdown = true; };



   video.srcObject = stream;

   await video.play();

   captureCanvas = document.createElement('canvas');

   captureCanvas.width = 640; //video.videoWidth;

   captureCanvas.height = 480; //video.videoHeight;

   window.requestAnimationFrame(onAnimationFrame);



   return stream;

  }

  async function stream_frame(label, imgData) {

   if (shutdown) {

    removeDom();

    shutdown = false;

    return '';

   }



   var preCreate = Date.now();

   stream = await createDom();



   var preShow = Date.now();

   if (label != "") {

    labelElement.innerHTML = label;

   }



   if (imgData != "") {

    var videoRect = video.getClientRects()[0];

    imgElement.style.top = videoRect.top + "px";

    imgElement.style.left = videoRect.left + "px";

    imgElement.style.width = videoRect.width + "px";

    imgElement.style.height = videoRect.height + "px";

    imgElement.src = imgData;

   }



   var preCapture = Date.now();

   var result = await new Promise(function(resolve, reject) {

    pendingResolve = resolve;

   });

   shutdown = false;



   return {'create': preShow - preCreate,

       'show': preCapture - preShow,

       'capture': Date.now() - preCapture,

       'img': result};

  }

  ''')



 display(js)



def video_frame(label, bbox):

 data = eval_js('stream_frame("{}", "{}")'.format(label, bbox))

 return data                def videoStreams():

 js = Javascript('''

  var video;

  var div = null;

  var stream;

  var captureCanvas;

  var imgElement;

  var labelElement;



  var pendingResolve = null;

  var shutdown = false;

  var video2;

  var div2 = null;

  var stream2;

  var captureCanvas2;

  var imgElement2;

  var labelElement2;



  var pendingResolve2 = null;

  var shutdown2 = false;



  function removeDom() {

    stream.getVideoTracks()[0].stop();

    video.remove();

    div.remove();

    video = null;

    div = null;

    stream = null;

    imgElement = null;

    captureCanvas = null;

    labelElement = null;

  }

  function removeDom2() {

    stream2.getVideoTracks()[0].stop();

    video2.remove();

    div2.remove();

    video2 = null;

    div2 = null;

    stream2 = null;

    imgElement2 = null;

    captureCanvas2 = null;

    labelElement2 = null;

  }



  function onAnimationFrame() {

   if (!shutdown) {

    window.requestAnimationFrame(onAnimationFrame);

   }

   if (pendingResolve) {

    var result = "";

    if (!shutdown) {

     captureCanvas.getContext('2d').drawImage(video, 0, 0, 640, 480);

     result = captureCanvas.toDataURL('image/jpeg', 0.8)

    }

    var lp = pendingResolve;

    pendingResolve = null;

    lp(result);

   }

  }

  function onAnimationFrame2() {

   if (!shutdown2) {

    window.requestAnimationFrame(onAnimationFrame2);

   }

   if (pendingResolve2) {

    var result2 = "";

    if (!shutdown2) {

     captureCanvas2.getContext('2d').drawImage(video2, 0, 0, 640, 480);

     result2 = captureCanvas2.toDataURL('image/jpeg', 0.8)

    }

    var lp2 = pendingResolve2;

    pendingResolve2 = null;

    lp2(result2);

   }

  }

  async function createDom() {

   if (div !== null) {

    return stream;

   }



   div = document.createElement('div');

   div.style.border = '2px solid black';

   div.style.padding = '3px';

   div.style.width = '100%';

   div.style.maxWidth = '600px';

   div.onclick = () => { shutdown = true; };

   document.body.appendChild(div);



   const modelOut = document.createElement('div');

   modelOut.innerHTML = "<span>Status:</span>";

   labelElement = document.createElement('span');

   labelElement.innerText = 'No data';

   labelElement.style.fontWeight = 'bold';

   modelOut.appendChild(labelElement);

   div.appendChild(modelOut);



   video = document.createElement('video');

   video.style.display = 'block';

   video.width = div.clientWidth - 6;

   video.setAttribute('playsinline', '');

   video.onclick = () => { shutdown = true; };

   const myVideos = [];

   await navigator.mediaDevices.enumerateDevices().then(answers => {

    answers.forEach(answer => {

     if (answer.kind === 'videoinput'){

      myVideos.push(answer);

     }

    })

   })

   .catch(error => {

    console.log(error);

   });

   stream = await navigator.mediaDevices.getUserMedia({

     video: {

      deviceId: myVideos[0].deviceId

     }

   });



   //navigator.mediaDevices.enumerateDevices().then(function(devices =>{console.log(devices)}));

   /*stream = await navigator.mediaDevices.getUserMedia(

     {video: { facingMode: "environment"}});

   //stream = await navigator.mediaDevices.getUserMedia(

     //{video: { deviceId: {exact: camera1ID }}});*/



   var videoTrack = stream.getVideoTracks();



   div.appendChild(video);



   imgElement = document.createElement('img');

   imgElement.style.position = 'absolute';

   imgElement.style.zIndex = 1;

   imgElement.onclick = () => { shutdown = true; };

   div.appendChild(imgElement);



   const instruction = document.createElement('div');

   instruction.innerHTML =

     '<span style="color: red; font-weight: bold;">' +

     'When finished, click here or on the video to stop this demo</span>';

   div.appendChild(instruction);

   instruction.onclick = () => { shutdown = true; };



   video.srcObject = stream;

   await video.play();

   captureCanvas = document.createElement('canvas');

   captureCanvas.width = 640; //video.videoWidth;

   captureCanvas.height = 480; //video.videoHeight;

   window.requestAnimationFrame(onAnimationFrame);



   return stream;

  }



  async function createDom2() {

   if (div2 !== null) {

    return stream2;

   }



   div2 = document.createElement('div');

   div2.style.border = '2px solid black';

   div2.style.padding = '3px';

   div2.style.width = '100%';

   div2.style.maxWidth = '600px';

   div2.onclick = () => { shutdown2 = true; };

   document.body.appendChild(div2);



   const modelOut2 = document.createElement('div');

   modelOut2.innerHTML = "<span>Status:</span>";

   labelElement2 = document.createElement('span');

   labelElement2.innerText = 'No data';

   labelElement2.style.fontWeight = 'bold';

   modelOut2.appendChild(labelElement2);

   div2.appendChild(modelOut2);



   video2 = document.createElement('video');

   video2.style.display = 'block';

   video2.width = div2.clientWidth - 6;

   video2.setAttribute('playsinline', '');

   video2.onclick = () => { shutdown2 = true; };

   const myVideos2 = [];

   await navigator.mediaDevices.enumerateDevices().then(answers2 => {

    answers2.forEach(answer2 => {

     if (answer2.kind === 'videoinput'){

      myVideos2.push(answer2);

     }

    })

   })

   .catch(error => {

    console.log(error);

   });

   stream2 = await navigator.mediaDevices.getUserMedia({

     video: {

      deviceId: myVideos2[1].deviceId

     }

   });

   //navigator.mediaDevices.enumerateDevices().then(function(devices =>{console.log(devices)}));

   /*stream = await navigator.mediaDevices.getUserMedia(

     {video: { facingMode: "environment"}});

   //stream = await navigator.mediaDevices.getUserMedia(

     //{video: { deviceId: {exact: camera1ID }}});*/



   var videoTrack2 = stream2.getVideoTracks();



   div2.appendChild(video2);



   imgElement2 = document.createElement('img');

   imgElement2.style.position = 'absolute';

   imgElement2.style.zIndex = 1;

   imgElement2.onclick = () => { shutdown2 = true; };

   div2.appendChild(imgElement2);



   const instruction2 = document.createElement('div');

   instruction2.innerHTML =

     '<span style="color: red; font-weight: bold;">' +

     'When finished, click here or on the video to stop this demo</span>';

   div2.appendChild(instruction2);

   instruction2.onclick = () => { shutdown2 = true; };



   video2.srcObject = stream2;

   await video2.play();

   captureCanvas2 = document.createElement('canvas');

   captureCanvas2.width = 640; //video.videoWidth;

   captureCanvas2.height = 480; //video.videoHeight;

   window.requestAnimationFrame(onAnimationFrame);



   return stream2;

  }



  async function stream_frame(label, imgData) {

   if (shutdown) {

    removeDom();

    shutdown = false;

    removeDom2();

    shutdown2 = false;

    return '';

   }

   if (shutdown2) {

    removeDom2();

    shutdown2 = false;

    removeDom();

    shutdown = false;

    return '';

   }

   var preCreate = Date.now();

   stream = await createDom();

   console.log('created first dom');



   var preShow = Date.now();

   if (label != "") {

    labelElement.innerHTML = label;

   }



   if (imgData != "") {

    var videoRect = video.getClientRects()[0];

    imgElement.style.top = videoRect.top + "px";

    imgElement.style.left = videoRect.left + "px";

    imgElement.style.width = videoRect.width + "px";

    imgElement.style.height = videoRect.height + "px";

    imgElement.src = imgData;

   }



   var preCapture = Date.now();

   var result = await new Promise(function(resolve, reject) {

    pendingResolve = resolve;

   });

   shutdown = false;



   var preCreate2 = Date.now();

   stream2 = await createDom2();

   console.log('created second dom');



   var preShow2 = Date.now();

   if (label != "") {

    labelElement2.innerHTML = label;

   }



   if (imgData != "") {

    var videoRect2 = video2.getClientRects()[0];

    imgElement2.style.top = videoRect2.top + "px";

    imgElement2.style.left = videoRect2.left + "px";

    imgElement2.style.width = videoRect2.width + "px";

    imgElement2.style.height = videoRect2.height + "px";

    imgElement2.src = imgData;

   }



   var preCapture2 = Date.now();

   if (!shutdown2) {

     captureCanvas2.getContext('2d').drawImage(video2, 0, 0, 640, 480);

     result2 = captureCanvas2.toDataURL('image/jpeg', 0.8)

   }

   shutdown2 = false;



   return {'create': preShow - preCreate,

       'show': preCapture - preShow,

       'capture': Date.now() - preCapture,

       'img': result,

       'create2': preShow2 - preCreate2,

       'show2': preCapture2 - preShow2,

       'capture2': Date.now() - preCapture2,

       'img2': result2};

  }

  ''')



 display(js)



def video_frame(label, bbox):

 data = eval_js('stream_frame("{}", "{}")'.format(label, bbox))

 return data           import time

def liveStreamSideCam():

 video_streamSingle()

 # label for video

 label_html = 'Capturing...'

 # initialze bounding box to empty

 bbox = ''

 count = 0

 imgNum = 0

 while True:

   js_reply = video_frame(label_html, bbox)

   if not js_reply:

     break

   # convert JS response to OpenCV Image

   img = js_to_image(js_reply["img"])

   result=cv2.imwrite('/content/livestream/pictures/sideways/' + str(imgNum) + ".jpg", img)

   imgNum = imgNum+1

   bbox_array = np.zeros([480,640,4], dtype=np.uint8)

   bbox_bytes = bbox_to_bytes(bbox_array)

   bbox = bbox_bytes

 screen_clear()

 return imgNum     

import time

def liveStream(testCam):

 videoStreams()

 # label for video

 label_html = 'Capturing...'

 # initialze bounding box to empty

 bbox = ''

 count = 0

 imgNum = 0

 while True:

   js_reply = video_frame(label_html, bbox)

   if not js_reply:

     break

   # convert JS response to OpenCV Image

   img = js_to_image(js_reply["img"])

   img2 = js_to_image(js_reply["img2"])

   result=cv2.imwrite('/content/livestream/pictures/sideways/' + str(imgNum) + ".jpg", img)

   result2=cv2.imwrite('/content/livestream/pictures/front/' + str(imgNum) + ".jpg", img2)

   imgNum = imgNum+1

   bbox_array = np.zeros([480,640,4], dtype=np.uint8)

   bbox_bytes = bbox_to_bytes(bbox_array)

   bbox = bbox_bytes



 screen_clear()

 if testCam != 1:

  for i in range(imgNum-1):

   process = "cd /content/openpose && /content/openpose/build/examples/openpose/openpose.bin --video /content/livestream/pictures/sideways/"+str(i)+".jpg --part_candidates --write_json /content/livestream/pictures/sideways/keypoints/ --display 0 + --write_video /content/livestream/pictures/sideways/keypoints/openpose.mp4"

   pipe = subprocess.run(process, shell=True)

   process = "cd /content/openpose && /content/openpose/build/examples/openpose/openpose.bin --video /content/livestream/pictures/front/"+str(i)+".jpg --part_candidates --write_json /content/livestream/pictures/front/keypoints/ --display 0 + --write_video /content/livestream/pictures/front/keypoints/openpose.mp4"

   pipe = subprocess.run(process, shell=True)           import time

def liveStreamFrontCam():

 video_streamSingle()

 # label for video

 label_html = 'Capturing...'

 # initialze bounding box to empty

 bbox = ''

 count = 0

 imgNum = 0

 while True:

   js_reply = video_frame(label_html, bbox)

   if not js_reply:

     break



   # convert JS response to OpenCV Image

   img = js_to_image(js_reply["img"])

   result=cv2.imwrite('/content/livestream/pictures/front/' + str(imgNum) + ".jpg", img)

   imgNum = imgNum+1

   # create transparent overlay for bounding box

   bbox_array = np.zeros([480,640,4], dtype=np.uint8)

   bbox_bytes = bbox_to_bytes(bbox_array)

   bbox = bbox_to_bytes

 screen_clear()

 return imgNum              def cameraCheckJavaScript():

 js = Javascript('''

   async function findCameras(){

    var number = 0;

    await navigator.mediaDevices.enumerateDevices().then(answers2 => {

     answers2.forEach(answer2 => {

      if (answer2.kind === 'videoinput'){

       number = number + 1;

      }

     })

    })

    .catch(error => {

     console.log(error);

    });

    return number;

   }

 ''')

 display(js)

 data = eval_js('findCameras()')

 return data                  import subprocess

import glob

from threading import *

import os

# from multiprocess import Process

import cv2

# start streaming video from webcam

#see if they want to upload videos, send to one code chunk, or do a livestream, or see if they already manually uploaded videos

#have them type in what they want probably

data = cameraCheckJavaScript()

prevChoice = "T"

print("Would you like to do livestream(L), test video cameras (T)?")

choice = input('Please enter L/T: ')

while choice != "L" and choice != "N" and choice != "U" and choice != "T" and choice != "D":

 choice = input('Please enter L/T: ')

while prevChoice == "T":

 if choice == 'L':

  #maybe add like a ten second count down for them to get in position? this would be nice to have

  if not os.path.exists("/content/livestream/"):

   os.mkdir("/content/livestream/")

  if not os.path.exists("/content/livestream/pictures/"):

   os.mkdir("/content/livestream/pictures/")

  if not os.path.exists("/content/livestream/pictures/sideways/"):

   os.mkdir("/content/livestream/pictures/sideways/")

  else:

   files = "/content/livestream/pictures/sideways/"

   for f in os.listdir(files):

     if f != ".ipynb_checkpoints" and f != "keypoints":

      f = files + f

      os.remove(f)

  if not os.path.exists("/content/livestream/pictures/front/"):

   os.mkdir("/content/livestream/pictures/front/")

  else:

   files = "/content/livestream/pictures/front/"

   for f in os.listdir(files):

    if f != ".ipynb_checkpoints" and f != "keypoints":

      f = files + f

      os.remove(f)

  if not os.path.exists("/content/livestream/pictures/sideways/keypoints/"):

   os.mkdir("/content/livestream/pictures/sideways/keypoints/")

  else:

   files = "/content/livestream/pictures/sideways/keypoints/"

   for f in os.listdir(files):

     if f != ".ipynb_checkpoints" and f != "keypoints":

      f = files + f

      os.remove(f)

  if not os.path.exists("/content/livestream/pictures/front/keypoints/"):

   os.mkdir("/content/livestream/pictures/front/keypoints/")

  else:

   files = "/content/livestream/pictures/front/keypoints/"

   for f in os.listdir(files):

     if f != ".ipynb_checkpoints" and f != "keypoints":

      f = files + f

      os.remove(f)



  #if data is one then only one camera is sumbitted so we will do it, other wise do 2

  if data == 1:

   trash = input('press enter to proceed to the squat facing sideways to camera, a ten second countdown will start: ')

   temp = 10

   for i in range(10):

    print(temp)

    temp = temp - 1

    time.sleep(1)

    screen_clear()

   imgNum1 = liveStreamSideCam()

   trash = input('press enter to proceed to the squat facing towards the camera, a ten second countdown will start: ')

   temp = 10

   for i in range(10):

    print(temp)

    temp = temp - 1

    time.sleep(1)

    screen_clear()

   imgNum2 = liveStreamFrontCam()

   print(imgNum2)

   for i in range(imgNum1-1):

    process = "cd /content/openpose && /content/openpose/build/examples/openpose/openpose.bin --video /content/livestream/pictures/sideways/"+str(i)+".jpg --part_candidates --write_json /content/livestream/pictures/sideways/keypoints/ --display 0 + --write_video /content/livestream/pictures/sideways/keypoints/openpose.mp4"

    pipe = subprocess.run(process, shell=True)

   for i in range(imgNum2-1):

    process = "cd /content/openpose && /content/openpose/build/examples/openpose/openpose.bin --video /content/livestream/pictures/front/"+str(i)+".jpg --part_candidates --write_json /content/livestream/pictures/front/keypoints/ --display 0 + --write_video /content/livestream/pictures/front/keypoints/openpose.mp4"

    pipe = subprocess.run(process, shell=True)

  else:

   trash = input('press enter to proceed to the squat, a ten second countdown will start: ')

   temp = 10

   for i in range(10):

    print(temp)

    temp = temp - 1

    time.sleep(1)

    screen_clear()

   liveStream(0)

  imgNum = 0

  name = input('Please type in your first name: ')



  squat("/content/livestream/pictures/sideways/keypoints/", "/content/livestream/pictures/front/keypoints", name)

  prevChoice = choice


 elif choice == 'T':

  if data == 1:

   liveStreamSideCam()

   liveStreamFrontCam()

  else:

   liveStream(1)



  print("Would you like to do livestream(L), test video cameras (T)?")

  choice = input('Please enter L/N/U: ')

  while choice != "L" and choice != "N" and choice != "U" and choice != "T" and choice != "D":

   choice = input('Please enter L/N/U/T: ')

   prevChoice = choice

 elif choice == "D":

  print(downloadOpenPose())

  prevChoice = "T"

  print("Would you like to do livestream(L), enter new videos(N), run already uploaded videos(U), test video cameras (T), or Download OpenPose (D)")

  choice = input('Please enter L/N/U: ')

  while choice != "L" and choice != "N" and choice != "U" and choice != "T" and choice != "D":

   choice = input('Please enter L/N/U/T: ')

   prevChoice = choice

 else:

  #upladed videos already

  squat("pre-uploaded", "videos", "na")

  prevChoice = choice

i

# Load OpenPose output
output_dir = sorted(os.listdir("/Users/dibidadahal/Library/Mobile Documents/com~apple~CloudDocs/output"))[-1]  
keypoints_file = os.path.join("/Users/dibidadahal/Library/Mobile Documents/com~apple~CloudDocs/output", output_dir, "keypoints.json")

try:
            with open(keypoints_file) as f:
                keypoints_data = json.load(f)

            landmarks = extract_relevant_landmarks(keypoints_data)  
            angles = calculate_angles(landmarks) 
            score = calculate_score(angles)
            feedback = generate_feedback(score, angles, landmarks)  # New!

            # Display score and feedback
            score_label.config(text=f"Score: {score}")
            feedback_label.config(text=feedback)

except FileNotFoundError:
            print("OpenPose output not found")

def extract_relevant_landmarks(keypoints_data):
        # Implement based on your landmarks and OpenPose output
        pass 

def generate_feedback(score, angles, landmarks):
        # Replace with your detailed feedback logic
        return "Feedback based on score and angles"

    # UI Additions for Score & Feedback
score_label = tk.Label(root, text="Score: ")
score_label.pack()
feedback_label = tk.Label(root, text="")
feedback_label.pack()

    # Create button to calculate score
score_button = tk.Button(root, text="Calculate Score", command=calculate_score)
score_button.pack()

    # Create button to change user details
change_user_button = tk.Button(root, text="Change User", command=get_user_details)
change_user_button.pack()

    # Create label for camera feed
label = tk.Label(root)
label.pack()

    # Run frame update function
update_frame()

    # Run GUI main loop
root.mainloop()

    # Release resources
cap.release()
cv2.destroyAllWindows()

# Get user details and start leg movement tracking
get_user_details()
