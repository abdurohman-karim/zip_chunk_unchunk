import os

def merge_parts(input_folder, output_zip):
    parts = [f for f in os.listdir(input_folder) if f.startswith("part_") and f.endswith(".zip")]
    parts.sort()

    with open(output_zip, 'wb') as full_zip:
        for part in parts:
            part_path = os.path.join(input_folder, part)

            with open(part_path, 'rb') as part_file:
                full_zip.write(part_file.read())

if __name__ == "__main__":
    input_folder = "output_folder"  # Здесь укажите папку, в которой находятся части
    output_zip_file = "output_file.zip"  # Имя для объединенного файла

    merge_parts(input_folder, output_zip_file)
