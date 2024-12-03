### By Hossein Haeri #######
#### haeri.hsn@gmail.com ###
############################

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from moviepy.editor import AudioFileClip, ImageClip, ColorClip, CompositeVideoClip

# Define available resolutions and their dimensions
resolutions = {
    "1080p (1920x1080)": (1920, 1080),
    "720p (1280x720)": (1280, 720),
    "480p (640x480)": (640, 480),
    "360p (480x360)": (480, 360),
}
# Function to create video from selected audio files and a cover image
def create_videos(audio_files, cover_image, output_dir, resolution):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    width, height = resolutions[resolution]

    try:
        progress_bar["maximum"] = len(audio_files)
        for i, audio_file in enumerate(audio_files, start=1):
            audio_clip = AudioFileClip(audio_file)
            image_clip = ImageClip(cover_image)

            # Resize image to fit within the chosen resolution, maintaining aspect ratio
            img_ratio = image_clip.w / image_clip.h
            target_ratio = width / height

            # Scale based on aspect ratio
            if img_ratio > target_ratio:
                # Image is wider than the target; fit to width
                image_clip = image_clip.resize(width=width)
            else:
                # Image is taller than the target; fit to height
                image_clip = image_clip.resize(height=height)

            # Position the image at the center of the background
            image_clip = image_clip.set_position("center").set_duration(audio_clip.duration)

            # Create a black background with the chosen resolution
            background = ColorClip(size=(width, height), color=(0, 0, 0))
            background = background.set_duration(audio_clip.duration)

            # Overlay the resized image on the black background
            video = CompositeVideoClip([background, image_clip]).set_audio(audio_clip)

            # Define output file path
            audio_file_name = os.path.splitext(os.path.basename(audio_file))[0]
            output_path = os.path.join(output_dir, f"{audio_file_name}.mp4")

            # Export video file
            video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac", audio_bitrate="192k")

            # Close clips to release memory
            audio_clip.close()
            image_clip.close()
            background.close()

            # Update progress bar
            progress_bar["value"] = i
            root.update_idletasks()

        messagebox.showinfo("Success", f"Videos have been created and saved in {output_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open file dialog for selecting audio files
def select_audio_files():
    files = filedialog.askopenfilenames(title="Select Audio Files", filetypes=[("Audio Files", "*.mp3 *.wav")])
    audio_files_list.delete(0, tk.END)
    for file in files:
        audio_files_list.insert(tk.END, file)

# Function to open file dialog for selecting cover image
def select_cover_image():
    file = filedialog.askopenfilename(title="Select Cover Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    cover_image_entry.delete(0, tk.END)
    cover_image_entry.insert(tk.END, file)

# Function to open directory dialog for selecting output directory
def select_output_directory():
    directory = filedialog.askdirectory(title="Select Output Directory")
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(tk.END, directory)

# GUI Setup
root = tk.Tk()
root.title("Audio to Video Converter")
root.geometry("500x800")

# Select Audio Files
tk.Label(root, text="Select Audio Files:").pack()
audio_files_list = tk.Listbox(root, selectmode=tk.MULTIPLE, height=5)
audio_files_list.pack(pady=5)
tk.Button(root, text="Browse Audio Files", command=select_audio_files).pack()

# Select Cover Image
tk.Label(root, text="Select Cover Image:").pack(pady=10)
cover_image_entry = tk.Entry(root, width=50)
cover_image_entry.pack()
tk.Button(root, text="Browse Cover Image", command=select_cover_image).pack()

# Select Output Directory
tk.Label(root, text="Select Output Directory:").pack(pady=10)
output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.pack()
tk.Button(root, text="Browse Output Directory", command=select_output_directory).pack()

# Select Resolution
tk.Label(root, text="Select Resolution:").pack(pady=10)
resolution_var = tk.StringVar(value="1080p (1920x1080)")
resolution_menu = ttk.Combobox(root, textvariable=resolution_var, values=list(resolutions.keys()))
resolution_menu.pack()

# Progress Bar
tk.Label(root, text="Conversion Progress:").pack(pady=10)
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=5)

# Convert Button
def convert():
    audio_files = list(audio_files_list.get(0, tk.END))
    cover_image = cover_image_entry.get()
    output_dir = output_dir_entry.get()
    resolution = resolution_var.get()
    
    if not audio_files or not cover_image or not output_dir or resolution not in resolutions:
        messagebox.showwarning("Warning", "Please select audio files, a cover image, an output directory, and a resolution.")
        return
    
    create_videos(audio_files, cover_image, output_dir, resolution)

tk.Button(root, text="Convert to Videos", command=convert).pack(pady=20)

root.mainloop()

