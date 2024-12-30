import os
import shutil

# Organize the dataset into train/test/validation splits
def organize_dataset(dataset_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    images_path = os.path.join(dataset_path, 'images')
    annotations_path = os.path.join(dataset_path, 'annotations')

    for split in ['train', 'valid', 'test']:
        split_images_path = os.path.join(output_path, split, 'images')
        split_annotations_path = os.path.join(output_path, split, 'annotations')
        os.makedirs(split_images_path, exist_ok=True)
        os.makedirs(split_annotations_path, exist_ok=True)

        split_file = os.path.join(dataset_path, f'{split}.txt')
        if os.path.exists(split_file):
            with open(split_file, 'r') as f:
                for line in f:
                    file_name = line.strip()
                    shutil.copy(os.path.join(images_path, file_name), split_images_path)
                    shutil.copy(os.path.join(annotations_path, f'{file_name}.txt'), split_annotations_path)

if __name__ == "__main__":
    organize_dataset('./datasets/version_1', './datasets/organized')
    print("Dataset organized successfully!")
