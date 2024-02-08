import os
from zipfile import ZipFile

def split_zip(input_zip, max_chunk_size, output_folder):
    with open(input_zip, 'rb') as zip_file:
        current_chunk_size = 0
        current_chunk_files = []
        chunk_number = 1

        while True:
            content = zip_file.read(1024 * 1024)  # читаем 1MB за раз

            if not content:
                break  # конец файла

            current_chunk_size += len(content)
            current_chunk_files.append(content)

            if current_chunk_size > max_chunk_size:
                create_chunk(current_chunk_files, output_folder, chunk_number)
                current_chunk_files = []
                current_chunk_size = 0
                chunk_number += 1

        # Handle the last chunk
        create_chunk(current_chunk_files, output_folder, chunk_number)

def create_chunk(files, output_folder, chunk_number):
    chunk_zip = os.path.join(output_folder, f"part_{chunk_number}.zip")

    with open(chunk_zip, 'wb') as chunk:
        for content in files:
            chunk.write(content)

if __name__ == "__main__":
    input_zip_file = "input_file.zip"
    max_chunk_size = 50 * 1024 * 1024  # 50MB in bytes
    output_folder = "output_folder"

    split_zip(input_zip_file, max_chunk_size, output_folder)
