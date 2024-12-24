import os
import shutil

# Define the dataset directories
DATASET_DIR = "C:\\Users\\omar3\\Downloads\\Compressed\\pattern dataset"
DAYTIME_DIR = os.path.join(DATASET_DIR, "voc_day", "JPEGImages")
NIGHTTIME_DIR = os.path.join(DATASET_DIR, "voc_night", "JPEGImages")
OUTPUT_DIR = os.path.join(DATASET_DIR, "organized dataset")

# List of all 17 known animal classes
ANIMAL_CLASSES = [
    "AmurLeopard", "AmurTiger", "Badger", "BlackBear", "cow", "dog",
    "leopard", "leopardcat", "muskdeer", "racoondog", "redfox", "roedeer",
    "sable", "sikadeer", "weasel", "wildboar", "y.t.marten"
]

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to extract the class name from the filename
def extract_class_name(filename):
    for animal in ANIMAL_CLASSES:
        # Normalize both animal names and filenames by removing spaces, dots, and converting to lowercase
        normalized_animal = animal.lower().replace(" ", "").replace(".", "")
        normalized_filename = filename.lower().replace(" ", "").replace(".", "")
        if normalized_animal in normalized_filename:
            return animal
    return None  # Return None if no class name is found

# Process both daytime and nighttime directories
for time_of_day in [DAYTIME_DIR, NIGHTTIME_DIR]:
    print(time_of_day)
    # Loop through each image in the folder
    for filename in os.listdir(time_of_day):
        if filename.endswith((".jpg", ".jpeg", ".png")):  # Adjust extensions if needed
            # Extract the class name using the function
            class_name = extract_class_name(filename)
            
            if class_name:  # Proceed only if a class name is found
                # Create a folder for the class if it doesn't exist
                class_folder = os.path.join(OUTPUT_DIR, class_name)
                os.makedirs(class_folder, exist_ok=True)
                
                # Move or copy the file to the class folder
                src_path = os.path.join(time_of_day, filename)
                dest_path = os.path.join(class_folder, filename)
                shutil.copy(src_path, dest_path)  # Use shutil.move() if you want to move instead of copy


def correct_misclassified_images():
    # Define the folders for leopardcat and raccoondog
    leopardcat_folder = os.path.join(OUTPUT_DIR, "leopardcat")
    raccoondog_folder = os.path.join(OUTPUT_DIR, "raccoondog")
    leopard_folder = os.path.join(OUTPUT_DIR, "leopard")
    dog_folder = os.path.join(OUTPUT_DIR, "dog")
    
    # Ensure the correct folders exist
    os.makedirs(leopardcat_folder, exist_ok=True)
    os.makedirs(raccoondog_folder, exist_ok=True)
    
    # Define a helper function to normalize filenames
    def normalize_name(name):
        return name.lower().replace(" ", "").replace(".", "").replace("_", "")
    
    # Move leopardcat images from leopard folder
    for filename in os.listdir(leopard_folder):
        if "leopardcat" in normalize_name(filename):
            src_path = os.path.join(leopard_folder, filename)
            dest_path = os.path.join(leopardcat_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved {filename} from leopard to leopardcat.")
    
    # Move raccoondog images from dog folder
    for filename in os.listdir(dog_folder):
        if "raccoondog" in normalize_name(filename):
            src_path = os.path.join(dog_folder, filename)
            dest_path = os.path.join(raccoondog_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved {filename} from dog to raccoondog.")

# Call the correction function
correct_misclassified_images()

print("Dataset organized into class-specific folders!")
