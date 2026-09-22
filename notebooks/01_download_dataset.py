from huggingface_hub import hf_hub_download
from zipfile import ZipFile
from pathlib import Path

print("Finding PlantVillage dataset...")

zip_path = hf_hub_download(
    repo_id="mohanty/PlantVillage",
    filename="data.zip",
    repo_type="dataset"
)

# Our 9 classes
classes = [
    "Tomato___healthy",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Potato___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Corn_(maize)___healthy",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot"
]

output_dir = Path("dataset")
output_dir.mkdir(exist_ok=True)

print("\nExtracting selected classes...\n")

with ZipFile(zip_path, "r") as zip_file:

    all_files = zip_file.namelist()

    for class_name in classes:

        prefix = f"raw/color/{class_name}/"

        matching_files = [
            file for file in all_files
            if file.startswith(prefix) and not file.endswith("/")
        ]

        if not matching_files:
            print(f"NOT FOUND: {class_name}")
            continue

        class_dir = output_dir / class_name
        class_dir.mkdir(parents=True, exist_ok=True)

        print(f"{class_name}: {len(matching_files)} images")

        for file in matching_files:
            filename = Path(file).name
            destination = class_dir / filename

            with zip_file.open(file) as source:
                with open(destination, "wb") as target:
                    target.write(source.read())

print("\nDataset preparation complete!")
print(f"Location: {output_dir.resolve()}")