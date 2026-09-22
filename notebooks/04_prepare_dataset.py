from pathlib import Path
import random
import shutil

SOURCE_DIR = Path("dataset")
OUTPUT_DIR = Path("processed_dataset")

TRAIN_RATIO = 0.80
VAL_RATIO = 0.10
TEST_RATIO = 0.10

random.seed(42)

# Create output folders
for split in ["train", "val", "test"]:
    (OUTPUT_DIR / split).mkdir(parents=True, exist_ok=True)

print("Preparing dataset...\n")

for class_dir in sorted(SOURCE_DIR.iterdir()):

    if not class_dir.is_dir():
        continue

    images = list(class_dir.glob("*.JPG"))

    random.shuffle(images)

    total = len(images)

    train_end = int(total * TRAIN_RATIO)
    val_end = train_end + int(total * VAL_RATIO)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    print(f"{class_dir.name}")
    print(f"  Total: {total}")
    print(f"  Train: {len(train_images)}")
    print(f"  Val:   {len(val_images)}")
    print(f"  Test:  {len(test_images)}")

    for split, split_images in [
        ("train", train_images),
        ("val", val_images),
        ("test", test_images)
    ]:

        destination_dir = OUTPUT_DIR / split / class_dir.name
        destination_dir.mkdir(parents=True, exist_ok=True)

        for image in split_images:
            shutil.copy2(
                image,
                destination_dir / image.name
            )

print("\nDataset preparation complete!")
print(f"Output: {OUTPUT_DIR.resolve()}")