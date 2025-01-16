This project aims to detect and classify waste using a YOLO-based object detection model. The model is trained on datasets from **Roboflow** and deployed using a **Streamlit** web application.

---

## **Project Features**

- Detects waste objects in images.
- Supports training with custom datasets in COCO format.
- Includes pre-trained YOLO model weights for quick deployment.
- Provides an interactive interface using Streamlit.

---

## **Project Structure**

```
RTWDCS/
├── assets/                     # Contains assets like logos or example images
├── datasets/                   # Folder for datasets
│   ├── version_1/              # Extracted COCO dataset folder
│   │   ├── images/             # Images for training/testing
│   │   ├── annotations/        # COCO-format annotations
├── scripts/                    # Contains all scripts for preprocessing and training
│   ├── preprocess.py           # Dataset preprocessing script
│   ├── train_model.py          # Training script for YOLO
├── weights/                    # Folder for model weights
│   ├── best.pt                 # Best YOLO model weights
│   ├── last.pt                 # YOLO weights from the last training epoch
├── app.py                      # Main Streamlit app
├── download_weights.py         # Script to download model weights
├── README.md                   # Documentation file
```

---

## **Setup Instructions**

### **Step 1: Clone the Repository**

To get started, clone the project repository:

```bash
git clone https://github.com/yourusername/waste-detection.git
cd waste-detection
```

---

### **Step 2: Install Dependencies**

1. Create a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

---

### **Step 3: Download the Dataset**

1. Go to [Roboflow](https://roboflow.com/) and log in.
2. Select your dataset (e.g., waste-detection) and download it in **COCO format** (ZIP file).
3. Extract (unzip) the dataset:
   - Right-click the ZIP file and select **Extract All...**.
   - Move the extracted folder to the `datasets/` directory.

   Your folder structure should look like this:

   ```
   datasets/
       version_1/
           images/
           annotations/
   ```

---

### **Step 4: Download Model Weights**

Run the `download_weights.py` script to download YOLO model weights:

```bash
python scripts/download_weights.py
```

Alternatively, manually place the weights file (`best.pt`, `last.pt`) in the `weights/` folder.

---

### **Step 5: Train the Model**

To train the YOLO model with your dataset, run the following command:

```bash
python scripts/train_model.py
```

This will train the model and save the best weights in the `weights/` folder.

---

### **Step 6: Run the Streamlit App**

Start the Streamlit app to use the waste-detection system:

```bash
streamlit run app.py
```

Open the app in your browser at **http://localhost:8501**. Upload an image to detect waste and see the results.

---

## **How It Works**

1. **Training**: The YOLO model is trained on datasets stored in the `datasets/` folder.
2. **Weights**: Pre-trained weights are used to speed up detection.
3. **Streamlit**: The web app allows users to upload images and displays detection results in real-time.

---

## **Dependencies**

The project requires the following Python libraries:
- **torch**
- **numpy**
- **opencv-python**
- **streamlit**
- **matplotlib**

Install all dependencies using the command:
```bash
pip install -r requirements.txt
```

---

## **Folder Details**

| Folder/File         | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `assets/`           | Contains project assets (e.g., logos, example images).                     |
| `datasets/`         | Contains the datasets for training.                                        |
| `weights/`          | Pre-trained YOLO weights for waste detection.                              |
| `scripts/`          | Python scripts for preprocessing and training the model.                   |
| `app.py`            | Streamlit app to detect waste from images.                                 |
| `README.md`         | This file. Documentation for the project.                                  |

---

## **Acknowledgments**

- **YOLOv5**: Used for object detection.
- **Roboflow**: For dataset management and labeling tools.
- **Streamlit**: To build the user interface.

---

## **Contributing**

Feel free to fork this repository, make changes, and submit a pull request.

---

## **License**

This project is licensed under the MIT License.
