import os
import re
import requests

# Specify the directory containing your notes
notes_dir = os.path.join("C:", os.sep, "Users", "G", "CODE", "CoPilot", "12_Machine_Learning")

# Create a new directory to save downloaded images
download_dir = os.path.join(notes_dir, "downloaded_images")
if not os.path.exists(download_dir):
    os.mkdir(download_dir)

# Define the regular expression to match imgur links
imgur_regex = r"!\[\]\((https?://i\.imgur\.com/[^\)]+)\)"

# Loop through all files in the notes directory
for filename in os.listdir(notes_dir):
    # Check if the file is a markdown file
    if filename.endswith(".md"):
        # Read the contents of the file
        with open(os.path.join(notes_dir, filename), "r", encoding="utf-8") as f:
            contents = f.read()
        
        # Find all imgur links using regular expressions
        imgur_links = re.findall(imgur_regex, contents)
        
        # Loop through all imgur links and download the images
        for imgur_link in imgur_links:
            img_data = requests.get(imgur_link).content
            img_filename = os.path.basename(imgur_link)
            with open(os.path.join(download_dir, img_filename), "wb") as f:
                f.write(img_data)
