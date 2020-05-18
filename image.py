from PIL import Image, ImageFilter

img = Image.open('./sudoku.png')
new_img = img.resize((600, 600))
new_img.save('thumb.png', 'png')
new_img.show()
