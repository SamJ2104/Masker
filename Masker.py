import random
import base64
import requests
import subprocess

def check_and_update_repo(repo_url):
    try:
        # Check for updates
        subprocess.check_call(['git', 'fetch'])

        # Check the status of the repo
        status_output = subprocess.check_output(['git', 'status', '-uno']).decode('utf-8')

        # If the repo is up to date, there's nothing to do
        if 'Your branch is up to date' in status_output:
            print("Up to date")
        else:
            # Pull the latest changes if updates are available
            subprocess.check_call(['git', 'pull'])
            print("Repository updated successfully.")
    except subprocess.CalledProcessError:
        print("Error updating repository.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    repo_url = "https://github.com/SamJ2104/Masker"  # Replace with your repository URL
    check_and_update_repo(repo_url)

print("   __  ___         __          ")
print("  /  |/  /__ ____ / /_____ ____")
print(" / /|_/ / _ `(_-</  '_/ -_) __/")
print("/_/  /_/\_,_/___/_/\_\\__/_/   ")

# Function to generate a random number
def generate_random_number():
    return random.randint(1000000000, 9999999999)

# Function to encode a number in Base64 without = 
def encode_base64(number):
    return base64.b64encode(str(number).encode('utf-8')).decode('utf-8').rstrip('=').rstrip("/").rstrip("+")

# Function to replace spaces with underscores
def replace_spaces_with_underscores(input_str):
    return input_str.replace(" ", "_")

# Function to process the Mask URL
def process_mask_url(url):
    # Split the URL into components
    parts = url.split("://")

    if len(parts) > 1:
        scheme = parts[0]
        path = parts[1].replace("/", "Ⳇ")
        return f"{scheme}://{path}"
    else:
        return url.replace("/", "Ⳇ")

# Generate a random number and encode it as Base64
id = encode_base64(generate_random_number())

# Ask for Destination URL
dest_url_choice = input("Destination URL?\n1. Rickrolls\n2. Custom\n")

if dest_url_choice == '1':
    print("Choose from:\n1. Classic\n2. Yout-ube\n3. Autoplay")
    rickroll_choice = input()
    if rickroll_choice == '1':
        DestURL = "https://youtube.com/watch?v=dQw4w9WgXcQ"
    elif rickroll_choice == '2':
        DestURL = "https://yout-ube.com/watch?v=dQw4w9WgXcQ"
    elif rickroll_choice == '3':
        DestURL = "https://shattereddisk.github.io/rickroll/rickroll.mp4"
    else:
        DestURL = "Invalid choice"
elif dest_url_choice == '2':
    DestURL = input("Enter Custom Destination URL: ")
else:
    DestURL = "Invalid choice"

# Ask for Mask URL
mask_url_choice = input("Mask URL?\n1. Social Media\n2. Google Services\n3. Custom\n")

if mask_url_choice == '1':
    print("Choose from:\n1. TikTok Video\n2. TikTok Account\n3. Snapchat Account\n4. Snapchat Reel\n5. Youtube Video (Youtu.be)\n6. Youtube Video (Youtube.com)\n7. Youtube Short")
    social_media_choice = input()
    if social_media_choice == '1':
        MaskURL = "https://vm.tiktok.com/"
    elif social_media_choice == '2':
        MaskURL = "https://www.tiktok.com"
    elif social_media_choice == '3':
        MaskURL = "https://t.snapchat.com/add/"
    elif social_media_choice == '4':
        MaskURL = "https://t.snapchat.com/reels/"
    elif social_media_choice == '5':
        MaskURL = "https://youtu.be/"
    elif social_media_choice == '6':
        MaskURL = "https://m.youtube.com/watch/v="
    elif social_media_choice == '7':
        MaskURL = "https://youtube.com/shorts/"
    else:
        MaskURL = "Invalid choice"
elif mask_url_choice == '2':
    print("Choose from:\n1. Search\n2. Drive\n3. Maps")
    google_service_choice = input()
    if google_service_choice == '1':
        search_input = input("Enter your search query: ")
        id = replace_spaces_with_underscores(search_input)
        MaskURL = "https://www.google.co.uk/search?q="
    elif google_service_choice == '2':
        MaskURL = "https://drive.google.com/file/d/"
    elif google_service_choice == '3':
        id = generate_random_number()
        MaskURL = "https://maps.google.com/locationid="
    else:
        MaskURL = "Invalid choice"
elif mask_url_choice == '3':
    MaskURL = input("Enter Custom Mask URL: ")
else:
    MaskURL = "Invalid choice"

# Process MaskURL
ReplacedMaskURL = process_mask_url(MaskURL)

# Print the FinalURL
final_url = f"{ReplacedMaskURL}@is.gd/{id}"
print("Your MaskUrl is:")
print(final_url)

# Activate Is.gd
isgd_url1 = f"http://is.gd/create.php?format=simple&shorturl={id}&url={DestURL}"
response = requests.get(isgd_url1)
