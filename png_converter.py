import sys
import os
from PIL import Image


def get_argument(index, default):
    try:
        path = sys.argv[index]
    except IndexError:
        path = default
    finally:
        return path


def verificar_diretorio(url):
    if not os.path.isdir(url):
        os.mkdir(url)


source = get_argument(1, 'default/')
destiny = get_argument(2, 'converted_images/')

while not os.path.isdir(source):
    print('Pasta fonte não encontrada.')
    source = input('Insira um caminho válido: ')

verificar_diretorio(destiny)

for item in os.listdir(source):
    path = source + '/' + item
    img = Image.open(path)
    path = destiny + '/' + os.path.splitext(item)[0]
    img.save(f'{path}.png', 'png')

print("all done")
