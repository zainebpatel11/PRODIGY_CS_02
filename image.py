from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(input_path, output_path, key):
    # Open the image
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Encrypt by performing XOR operation on each pixel
    encrypted_pixels = pixels ^ key  # XOR with the key
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt the image
def decrypt_image(input_path, output_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(input_path)
    encrypted_pixels = np.array(encrypted_image)
    
    # Decrypt by performing XOR operation on each pixel again
    decrypted_pixels = encrypted_pixels ^ key  # XOR with the same key
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Main function
def main():
    print("Choose an option:")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        input_path = input("Enter the path of the image to encrypt: ")
        output_path = input("Enter the path to save the encrypted image: ")
        key = int(input("Enter an encryption key (integer): "))
        encrypt_image(input_path, output_path, key)
    elif choice == 2:
        input_path = input("Enter the path of the encrypted image: ")
        output_path = input("Enter the path to save the decrypted image: ")
        key = int(input("Enter the decryption key (same as encryption key): "))
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
