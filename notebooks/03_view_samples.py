from pathlib import Path
import random
import matplotlib.pyplot as plt
from PIL import Image

dataset_dir = Path("dataset")

classes = sorted([
    folder for folder in dataset_dir.iterdir()
    if folder.is_dir()
])

fig, axes = plt.subplots(3, 3, figsize=(12, 12))

for ax, class_dir in zip(axes.flat, classes):

    images = list(class_dir.glob("*.JPG"))

    image_path = random.choice(images)

    image = Image.open(image_path)

    ax.imshow(image)
    ax.set_title(class_dir.name, fontsize=9)
    ax.axis("off")

plt.tight_layout()

output_path = Path("screenshots/dataset_samples.png")
plt.savefig(output_path, dpi=150)

plt.show()

print(f"Sample image grid saved to: {output_path}")