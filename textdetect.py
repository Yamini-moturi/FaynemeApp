import cv2
import pytesseract

# Path to the Tesseract executable (if not in your PATH environment variable)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Read the input image using OpenCV
image_path = 'immage1.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale for better OCR accuracy
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract OCR to do image to text conversion
text = pytesseract.image_to_string(gray_image)

# Print the extracted text
print("Extracted Text:")
print(text)
