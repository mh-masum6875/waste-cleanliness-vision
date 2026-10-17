# Waste and Cleanliness Vision

Part of my [applied computer vision portfolio](https://github.com/mh-masum6875/enterprise-computer-vision-solutions).

[![Smart City](https://img.shields.io/badge/Domain-Smart%20City%20%26%20Sanitation-brightgreen)](https://github.com/mh-masum6875/waste-cleanliness-vision)
[![Waste Management](https://img.shields.io/badge/Task-Conveyor%20Waste%20Sorting-orange)](https://github.com/mh-masum6875/waste-cleanliness-vision)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A smart city and industrial recycling vision system for automated conveyor waste sorting, approximate mass estimation, public littering detection, and public cleanliness auditing.

---

## Core Capabilities

### 1. Conveyor Waste Sorting & Weight Estimation (`conveyor_waste_sorter.py`)
- Background subtraction and multi-class waste categorization (Plastics, Metals, Organics, Cardboard).
- **Geometric Volume-to-Weight Mapping**: Estimates item volume based on bounding area and camera focal depth to approximate conveyor waste tonnage.

### 2. Public Spitting & Wall Defacement Detection
- Hand-to-face spatial trajectory analysis identifying rapid spitting actions (Pan/Ghutka defacement) in public transit and station corridors.

### 3. Public Littering & Street Waste Detection
- Detects discarded trash items and correlates with pedestrian detachment actions.

### 4. Surface Dust & Clean-Floor Auditing
- Evaluates floor reflectivity and footprint accumulation to trigger automated cleaning dispatch.

---

## Quickstart

```bash
git clone https://github.com/mh-masum6875/waste-cleanliness-vision.git
cd waste-cleanliness-vision
pip install -r requirements.txt

# Run Conveyor Waste Sorter Demo
python src/conveyor_waste_sorter.py --source waste_conveyor.mp4
```

---

## License
This project is licensed under the MIT License.
