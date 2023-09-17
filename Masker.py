import random
import base64
import requests
import subprocess
import os
import sys
import json

def check_and_update_repo(repo_url):
    try:
        
      
        subprocess.check_call(['git', 'fetch'])

       
        status_output = subprocess.check_output(['git', 'status', '-uno']).decode('utf-8')

        # If the local repository is up to date, there's nothing to do
        if 'Your branch is up to date' in status_output:
            print("Up to date.")
        else:
            # Pull the latest changes if updates are available
            subprocess.check_call(['git', 'pull'])
            print("Updated successfully")
            
            # Restart the script
            python = sys.executable
            os.execl(python, python, *sys.argv)
    except subprocess.CalledProcessError:
        print("Error updating")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    repo_url = "https://github.com/SamJ2104/Masker"  
    check_and_update_repo(repo_url)

ascii_art = """
   __  ___         __          
  /  |/  /__ ____ / /_____ ____
 / /|_/ / _ `(_-</  '_/ -_) __/
/_/  /_/\_,_/___/_/\_\\__/_/   
"""

print(ascii_art)

# Clear function
def clear():
  
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    print(ascii_art)

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

# Function to create a short URL
def create_short_url2(DestUrl,MaskURL):
	url = "https://api.shrtco.de/v2/shorten"
	headers = {
    "Host": "api.shrtco.de",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://shrtco.de/tools/custom",
    "Content-Length": "38",
    "Origin": "https://shrtco.de",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

# Define the payload as raw data using the variables
	payload = f"url={DestUrl}&custom_code={id}"

# Send the POST request
	response = requests.post(url, headers=headers, data=payload)
	data = json.loads(response.text)
# Check the response
	if response.status_code == 201:
        	shortened_url = data["result"]["full_short_link2"]
        	MaskURL = MaskURL.replace("https://", "")
        	MaskURL = MaskURL.replace("/", "Ⳇ")
        	shortened_url = shortened_url.replace("https://", "")  # Remove https://
        	print("No Blacklist Mask:","https://" + MaskURL + "@" + shortened_url)
	else:
        	print("Error:", response.status_code, response.text)

# Generate a random number and encode it as Base64
id = encode_base64(generate_random_number())

clear()

# Ask for Destination URL
dest_url_choice = input("Destination URL?\n1. Rickrolls\n2. Custom\n")

clear()

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
    clear()
    DestURL = input("Enter Custom Destination URL: ")
else:
    DestURL = "Invalid choice"

clear()

# Ask for Mask URL
mask_url_choice = input("Mask URL?\n1. Social Media\n2. Google Services\n3. Login Pages\n4. Custom\n")

clear()

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
    clear()
  
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
elif mask_url_choice == '4':
    MaskURL = input("Enter Custom Mask URL: ")
elif mask_url_choice == '3':
    clear()
    id = generate_random_number()
    print("Choose from:\n1. Microsoft\n2. Facebook\n3. Google\n4. Instagram\n5. Twitter\n6. Tiktok\n7. Roblox\n8. YouTube\n9. Reddit\n10. Spotify\n11. PayPal\n12. Discord\n13. Netflix\n14. Github\n15. iCloud\n16. Snapchat\n17. Amazon")
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
        print("Invalid choice")

custom_path_choice = input("Do you want to add a custom path to the Mask URL? (y/n): ")
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
short_url2 = create_short_url2(DestURL, MaskURL)
