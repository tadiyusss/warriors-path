from PIL import Image, ImageDraw
from sys import argv

filename = argv[1]
output = argv[2]

img = Image.open(filename)
img = img.convert("RGBA")

# Create a mask to identify the white background
mask = Image.new("L", img.size, 0)
draw = ImageDraw.Draw(mask)

# Flood-fill from the edges to detect the white background
width, height = img.size
for x in range(width):
    if img.getpixel((x, 0))[:3] == (255, 255, 255):
        draw.line([(x, 0), (x, 0)], fill=255)
    if img.getpixel((x, height - 1))[:3] == (255, 255, 255):
        draw.line([(x, height - 1), (x, height - 1)], fill=255)

for y in range(height):
    if img.getpixel((0, y))[:3] == (255, 255, 255):
        draw.line([(0, y), (0, y)], fill=255)
    if img.getpixel((width - 1, y))[:3] == (255, 255, 255):
        draw.line([(width - 1, y), (width - 1, y)], fill=255)


# Apply transparency to the white background
datas = img.getdata()
mask_data = mask.getdata()
newData = []

for i, item in enumerate(datas):
    if mask_data[i] == 255:
        newData.append((255, 255, 255, 0))  # Make white background transparent
    else:
        newData.append(item)

img.putdata(newData)
img.save(output, "PNG")
print("Successful")