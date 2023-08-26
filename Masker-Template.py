import random
import base64
import requests
import subprocess
import os
import sys
import json


  
    

# Function to generate a random number
def generate_random_number():
 return random.randint(10000000, 99999999)

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


# Function to create a short URL
def create_short_url(destination_url,MaskURL):
    # URL and payload data
    url = "https://www.url.zip/api/shortUrl"
    payload = {"url": destination_url}

    # Set headers
    headers = {
        "Host": "www.url.zip",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    # Convert payload to JSON format
    json_payload = json.dumps(payload)

    # Send the POST request
    response = requests.post(url, data=json_payload, headers=headers)

    # Check the response
    if response.status_code == 200:
        shortened_url = response.json()["shortUrl"]
        MaskURL = MaskURL.replace("https://", "")
        MaskURL = MaskURL.replace("/", "Ⳇ")
        shortened_url = shortened_url.replace("https://", "")  # Remove https://
        print(".Zip Mask:","https://" + MaskURL + "@" + shortened_url)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python3 Masker-Template.py <dest_url_choice> <rickroll_choice> <mask_url_choice> <mask_url_choice2> <custom_path_choice> <mask_url> <destination_url>")
        sys.exit(1)

    dest_url_choice = sys.argv[1]
    rickroll_choice = sys.argv[2]
    mask_url_choice = sys.argv[3]
    login_service_choice = sys.argv[4]
    custom_path_choice = sys.argv[5]
    mask_url = sys.argv[6]
    destination_url = sys.argv[7]



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
mask_url_choice = input("")



if mask_url_choice == '1':
    print("Choose from:\n1. TikTok Video\n2. TikTok Account\n3. Snapchat Account\n4. Snapchat Reel\n5. Youtube Video (Youtu.be)\n6. Youtube Video (Youtube.com)\n7. Youtube Short")
    social_media_choice = input()
    if social_media_choice == '1':
        MaskURL = "https://vm.tiktok.com/account"
    elif social_media_choice == '2':
        MaskURL = "https://www.tiktok.com/"
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
elif mask_url_choice == '4':
    MaskURL = input("")
elif mask_url_choice == '3':
    
    id = generate_random_number()
    print("")
    login_service_choice = input()
    if login_service_choice == '1':
        MaskURL = "https://login.microsoftonline.com/"
    elif login_service_choice == '2':
        MaskURL = "https://m.facebook.com/"
    elif login_service_choice == '3':
        MaskURL = "https://accounts.google.com/v3/signin/"
    elif login_service_choice == '4':
        MaskURL = "https://www.instagram.com/accounts/login/"
    elif login_service_choice == '5':
        MaskURL = "https://twitter.com/i/flow/login/"
    elif login_service_choice == '6':
        MaskURL = "https://www.tiktok.com/login/"
    elif login_service_choice == '7':
        MaskURL = "https://www.roblox.com/LOGIN/"
    elif login_service_choice == '8':
        MaskURL = "https://m.youtube.com/?login/"
    elif login_service_choice == '9':
        MaskURL = "https://www.reddit.com/login/"
    elif login_service_choice == '10':
        MaskURL = "https://accounts.spotify.com/en/login/"
    elif login_service_choice == '11':
        MaskURL = "https://www.paypal.com/signin/"
    elif login_service_choice == '12':
        MaskURL = "https://discord.com/login/"
    elif login_service_choice == '13':
        MaskURL = "https://www.netflix.com/login/"
    elif login_service_choice == '14':
        MaskURL = "https://github.com/login/"
    elif login_service_choice == '15':
        MaskURL = "https://www.icloud.com/login/"
    elif login_service_choice == '16':
        MaskURL = "https://accounts.snapchat.com/accounts/login/"
    elif login_service_choice == '17':
        MaskURL = "https://www.amazon.co.uk/signin/"
    else:
        custom_path_choice = input("")
if custom_path_choice.lower() == 'y':
    custom_path = input("Enter the custom path: ")
    MaskURL += custom_path

# Process MaskURL
ReplacedMaskURL = process_mask_url(MaskURL)

# Print the FinalURL
final_url = f"{ReplacedMaskURL}@is.gd/{id}"
print("Your MaskUrl's are:")
print("Is.Gd Mask", final_url)

# Activate Is.gd
isgd_url1 = f"http://is.gd/create.php?format=simple&shorturl={id}&url={DestURL}"
response = requests.get(isgd_url1)

# Create a short URL using the custom API
short_url = create_short_url(DestURL, MaskURL)