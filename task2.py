pip install Pillow numpy


from PIL import Image
import numpy as np

def load_image(path):
    img = Image.open('/content/image.jpg')
    img = img.convert('RGB')
    return np.array(img)

def save_image(pixels, path):
    img = Image.fromarray(pixels.astype('uint8'), 'RGB')
    img.save(path)

def encrypt_image(pixels, key=50):
    return (pixels + key) % 256

def decrypt_image(pixels, key=50):
    return (pixels - key) % 256

if __name__ == "__main__":
    img_path = input("Enter the image path: ")
    action = input("Encrypt (E) or Decrypt (D): ").strip().upper()

    key = 50  # You can also ask the user for the key
    pixels = load_image(img_path)

    if action == 'E':
        encrypted_pixels = encrypt_image(pixels, key)
        save_image(encrypted_pixels, 'encrypted_image.png')
        print("Image encrypted and saved as 'encrypted_image.png'")
    elif action == 'D':
        decrypted_pixels = decrypt_image(pixels, key)
        save_image(decrypted_pixels, 'decrypted_image.png')
        print("Image decrypted and saved as 'decrypted_image.png'")