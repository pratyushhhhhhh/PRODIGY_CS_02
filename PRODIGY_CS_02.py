from PIL import Image
import numpy as np
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img_array = np.array(img)
    key = np.resize(key, img_array.shape)
    encrypted_array = np.bitwise_xor(img_array, key)
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")
def decrypt_image(encrypted_image_path, key):

    encrypted_img = Image.open(encrypted_image_path)

    encrypted_array = np.array(encrypted_img)
    key = np.resize(key, encrypted_array.shape)
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    decrypted_img = Image.fromarray(decrypted_array)

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")


def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

    # image_path = 'C:\Users\praty\PycharmProjects\PRODIGY_CS_02\Fireblade.png'. enter your image path as input
    image_path = input("Enter the path to the image file: ")

    key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)

    encrypt_image(image_path, key)

    decrypt_image("encrypted_image.png", key)

if __name__ == "__main__":
    main()
