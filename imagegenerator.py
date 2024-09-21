import openai
import requests
import time
from PIL import Image
from io import BytesIO

# Replace with your actual OpenAI API key
openai.api_key = "OPENAIAPIKEY"

def generate_images_from_text(prompt, num_images=1):
    # Call the OpenAI API to generate images with higher resolution
    response = openai.Image.create(
        prompt=prompt,
        n=num_images,
        size="1024x1024"  # Requesting a higher resolution
    )
    
    image_urls = [data['url'] for data in response['data']]
    return image_urls

def download_image(image_url):
    # Download the image
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img

def main():
    user_input = input("Enter a detailed word or phrase to generate images: ")
    
    while True:
        num_images = int(input("How many images would you like to generate? (1-10): "))
        if 1 <= num_images <= 5:
            break
        print("Please enter a number between 1 and 10.")
    
    image_urls = generate_images_from_text(user_input, num_images)
    
    for idx, image_url in enumerate(image_urls):
        print(f"Generated image URL {idx + 1}: {image_url}")
        img = download_image(image_url)
        img.show()  # This will open the image using the default image viewer

        # Ask the user if they like the image
        like_image = input("Do you like this image? (yes/no): ").strip().lower()
        if like_image == 'yes':
            print("Glad you liked it!")
            break
        else:
            print("Generating a new image...")
            time.sleep(12)  # Respect the rate limit

if __name__ == "__main__":
    main()
