from PIL import Image

def process_image(input_path, output_path):
    with Image.open(input_path) as img:
        # Exemplo de processamento: converter para escala de cinza
        gray_img = img.convert('L')
        gray_img.save(output_path)
