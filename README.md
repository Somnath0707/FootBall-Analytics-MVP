# ⚽ Football Analytics MVP (Powered by YOLO11)

A computer vision system that analyzes football matches in real-time. Built with the cutting-edge **YOLO11** model, this MVP performs player tracking, team identification, and ball possession analysis with ball interpolation logic to handle occlusion.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![YOLO11](https://img.shields.io/badge/Model-YOLO11_Large-brightgreen.svg)
![OpenCV](https://img.shields.io/badge/Computer_Vision-OpenCV-orange.svg)

---

## 🎥 Demo

![Demo Preview](http://img.youtube.com/vi/neBZ6huolkg/0.jpg)(http://www.youtube.com/watch?v=neBZ6huolkg)
*Click the image to watch the full analysis in action.*

---

## 🚀 Key Modules

This repository is modularized to handle specific aspects of the game:

### 1. 🕵️ Tracker (`/tracker`)
-   Utilizes **YOLO11 Large (`yolo11l.pt`)** for high-accuracy detection of players, referees, and the ball.
-   Implements persistent tracking to follow entities across frames.

### 2. 👕 Team Assigner (`/team_assigner`)
-   Uses K-Means clustering (color quantization) to analyze jersey colors.
-   Automatically assigns players to teams (e.g., Team 1 vs. Team 2) based on pixel histograms.

### 3. ⚽ Player & Ball Assigner (`/player_ball_assigner`)
-   Calculates the bounding box distance between players and the ball.
-   Assigns "Ball Possession" to the nearest player within a dynamic threshold.
-   **Ball Interpolation:** Handles cases where the ball is occluded (hidden) or flickers in detection by interpolating its position across missing frames.

---

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/Somnath0707/FootBall-Analytics-MVP.git](https://github.com/Somnath0707/FootBall-Analytics-MVP.git)
   cd FootBall-Analytics-MVP
