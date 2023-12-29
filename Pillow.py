from PIL import Image
from PIL import ImageDraw,ImageChops
img = Image.open(r"test.png")

print(f"Image Mode is : {img.mode}")
print(f"Image Size is : {img.size}")
print(f"Image Format is : {img.format}")

r_img = img.rotate(70)
# r_img.show()

resize_image = img.resize((40,40))
# resize_image.save("resized_test.png")
# resize_image.show()

cropped_img = img.crop((120,130,140,150))
# cropped_img.show()

draw = ImageDraw.Draw(img)
draw.text((50, 110), "Hello World!", (255, 255, 255))
# img.show()

img.save("high_res.jpg",quality =95)
img.save("medium_res.jpg",quality = 25)
img.save("low_res.jpg",quality =10)

inv_image = ImageChops.invert(img)
# inv_image.show()

img_copy = img.copy()
inv_image.paste(img_copy,(100,100))
inv_image.show()

