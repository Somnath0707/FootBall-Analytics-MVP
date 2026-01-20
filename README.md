# ⚽ Football Analytics MVP (Powered by YOLO11)

A state-of-the-art computer vision system that analyzes football matches in real-time. Built with the cutting-edge **YOLO11** model, this project performs player tracking, jersey color clustering, and advanced ball possession analysis with occlusion handling.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![YOLO11](https://img.shields.io/badge/Model-YOLO11_Large-brightgreen.svg?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/Computer_Vision-OpenCV-orange.svg?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/Data-NumPy-013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

</div>

---

## 🎞️ Input vs Output

Witness the transformation from raw footage to actionable analytics.

### 1. Raw Input Footage
*Original broadcast video used for inference.*

https://github.com/user-attachments/assets/c13d529e-6fd7-45f5-a305-d5034d39e424

### 2. AI-Processed Output
*Real-time analysis featuring player tracking, team assignment, and possession stats.*

https://github.com/user-attachments/assets/388a236e-f0c5-4f43-b970-582174178a0a

---

## 🚀 Key Modules

This repository is architected with modularity in mind, separating detection, assignment, and analysis logic:

### 1. 🕵️ Advanced Tracking (`/tracker`)
-   **Engine:** Utilizes **YOLO11 Large (`yolo11l.pt`)** for industry-leading detection accuracy.
-   **Function:** Detects players, referees, and the ball, implementing ID persistence to track entities across frames.

### 2. 👕 Team Assignment (`/team_assigner`)
-   **Algorithm:** Uses **K-Means Clustering** (Color Quantization) on player bounding boxes.
-   **Logic:** Automatically separates players into two distinct teams based on jersey pixel histograms, ensuring accurate team attribution even in dynamic lighting.

### 3. ⚽ Ball Possession & Interpolation (`/player_ball_assigner`)
-   **Possession Logic:** Calculates spatial proximity between players and the ball to assign "control" dynamically.
-   **Interpolation Engine:** Handles critical edge cases where the ball is occluded by players. It mathematically interpolates the ball's missing coordinates to maintain a smooth, unbroken trajectory.

---
## 📂 Project Structure

```text
FootBall-Analytics-MVP/
├── player_ball_assigner/   # Logic for ball possession & interpolation
├── team_assigner/          # K-Means clustering for team separation
├── tracker/                # YOLO11 tracking implementation
├── utils/                  # Helper functions for video I/O
├── main.py                 # Main execution script
├── proj.py                 # Development & testing script
├── yolo11l.pt              # YOLO11 Large model weights
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
