import os
import csv
from deepface import DeepFace

# Function to process an image and return age, ethnicity, and gender
def process_image(image_path):
    try:
        result = DeepFace.analyze(image_path)
        age = result["age"]
        ethnicity = result["dominant_race"]
        gender = result["gender"]
        return age, ethnicity, gender
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None, None, None

# Function to process all images in a folder and write results to a CSV file
def process_folder(input_folder, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['Filename', 'Age', 'Ethnicity', 'Gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(input_folder, filename)
                age, ethnicity, gender = process_image(image_path)
                
                if age is not None:
                    writer.writerow({
                        'Filename': filename,
                        'Age': age,
                        'Ethnicity': ethnicity,
                        'Gender': gender
                    })
                else:
                    print(f"Skipping {filename}")

if __name__ == "__main__":
    input_folder = r"C:\Users\19109\Documents\faceimages"
    output_csv = "results.csv"
    
    process_folder(input_folder, output_csv)
    print(f"Processing complete. Results saved to {output_csv}")
