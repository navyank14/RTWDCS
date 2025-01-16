from ultralytics import YOLO

# Initialize the model from a configuration file or a pretrained weights file
model = YOLO('yolov5l.pt')

# Path to the dataset configuration file
data_path = '/content/datasets/waste-detection-9/data.yaml'

# Train the model
results = model.train(data=data_path, epochs=50)

# Validate the model
val_results = model.val()

# Export the model to ONNX format
success = model.export(format='onnx')

# Check if the export was successful
if success:
    print("Model exported successfully to ONNX format")
else:
    print("Failed to export the model")