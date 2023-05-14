# Import Module
from PIL import Image


def most_common_used_color(img):
    # Get width and height of Image
    width, height = img.size

    # Initialize Variable
    r_total = 0
    g_total = 0
    b_total = 0

    count = 0

    # Iterate through each pixel
    for x in range(0, width):
        for y in range(0, height):
            # r,g,b value of pixel
            r, g, b = img.getpixel((x, y))

            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total / count, g_total / count, b_total / count)


# Read Image
image = Image.open('image.jpg')

# Convert Image into RGB
image = image.convert('RGB')

# call function
common_color = most_common_used_color(image)

print(common_color)
# Output is (R, G, B)