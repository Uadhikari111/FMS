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
    
    

 
