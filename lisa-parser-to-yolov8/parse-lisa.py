import os
import csv

# Set the path to your CSV file containing the annotations
csv_file = 'training-annotations-night.csv'
foldername = 'train'

# Define the class labels for your dataset (0-indexed)
class_labels = ['go', 'stop', 'warning', 'stopLeft', 'goLeft', 'goForward', 'warningLeft']

# Create the annotations folder if it doesn't exist
if not os.path.exists(foldername):
    os.makedirs(foldername)

# Iterate over each row of the CSV file
with open(csv_file, 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        # Extract the image filename, class label, and bounding box coordinates
        filename = row[0]
        class_label = class_labels.index(row[3])
        x1, y1, x2, y2 = float(row[4]), float(row[5]), float(row[6]), float(row[7])
        width, height = float(row[1]), float(row[2])
        
        # Calculate the normalized coordinates and dimensions for the bounding box
        x = (x1 + x2) / (2 * width)
        y = (y1 + y2) / (2 * height)
        box_width = abs(x2 - x1) / width
        box_height = abs(y2 - y1) / height
        
        # Create a text file with the same name as the image file and write the YOLOv8 annotation
        with open(os.path.join(foldername, filename.replace('.jpg', '.txt')), 'a') as txt_file:
            txt_file.write(f"{class_label} {x} {y} {box_width} {box_height}\n")

print("koniec")