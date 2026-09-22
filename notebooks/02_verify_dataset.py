from pathlib import Path
from PIL import Image

dataset_dir = Path("dataset")

print("Checking AgroShield AI dataset...\n")

total_images = 0

for class_dir in sorted(dataset_dir.iterdir()):

    if not class_dir.is_dir():
        continue

    images = list(class_dir.glob("*.JPG"))

    valid_images = 0

    for image_path in images:
        try:
            with Image.open(image_path) as img:
                img.verify()
            valid_images += 1
        except Exception:
            print("Invalid image:", image_path)

    print(f"{class_dir.name}: {valid_images} images")

    total_images += valid_images

print("\n-----------------------------")
print(f"Total valid images: {total_images}")
print("-----------------------------")