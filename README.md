# MaRS Software Task 1 Submission 

**Candidate Name:** Yashvant A T K
**Position:** Software Team Recruitment 2026  

Welcome to my repository for the MaRS Software Task 1! This repository contains all my scripts, logs, and technical solutions for the Light, Medium, and Hard dose challenges.

---

## 1. Learning Experience
This task was an interesting dive into the exact types of problems a mars rover faces. Through these challenges, I significantly strengthened my skills in:
* **Linux/Bash Scripting:** Automating system diagnostics and file management.
* **Signal Processing:** Building Moving Average (Muchiko) and Moving Median (Sanchiko) filters to clean chaotic microgravity sensor data.
* **Optimization & Algorithms:** Using Dynamic Programming to optimize a robotic arm, and Breadth-First Search (BFS) for pathfinding.
* **Computer Vision:** Applying the Pinhole Camera Model to calculate real-world distances from pixel data using OpenCV.
* **Robotic Decision Making:** Designing and structuring Behavior Trees (BTs) for complex, state-aware obstacle avoidance.

---

## 2. Equations, Theorems, and Sketches Used

### A. Pinhole Camera Model (Hard Dose - Q2)
To calculate the distance of the arrow from the webcam, I derived the focal length using the diagonal resolution and Field of View (FOV), then applied the pinhole distance equation:
1. **Diagonal Pixels:** `D = sqrt(w^2 + h^2)`
2. **Focal Length (F):** `F = D / (2 * tan(FOV / 2))`
3. **Distance:** `Distance = (Real_Width * F) / Perceived_Pixel_Width`

### B. Dynamic Programming Cost Equation (Medium Dose - Q5)
To find the minimum wear cost of the telescopic arm, I used the following state transition formula between valid configurations:
`Cost = |Δ Inner| * W1 + |Δ Middle| * W2 + |Δ Outer| * W3`

### C. Filtering Algorithms (Medium Dose - Q4)
* **Muchiko (Moving Average):** `(x_1 + x_2 + x_3) / 3`
* **Sanchiko (Moving Median):** `Median(sorted[x_1, x_2, x_3])`

### D. Behavior Tree Sketch (Hard Dose - Q3)
*(Note: Please find the attached link for solution doc of Behavior Tree inside the file named `hard_3.txt`).*

---

## 3. Challenges Faced
1. **Flawed Sample Data in Problem Statement:** While solving the Medium Dose Q5 (Telescopic Arm), I discovered that the sample explanation output of `56` was mathematically sub-optimal. My DP algorithm proved that by transitioning through an intermediate state of `(9, 1, 5)`, the true minimum wear cost is actually **`44`**.
2. **Syntax Errors in Legacy Code:** The OpenCV code provided for Hard Dose Q2 contained several syntax errors, broken array brackets, and indentation issues. I had to debug and restructure the `detect_arrow` function before I could successfully integrate my custom math logic.
3. **Confusion in obstacle coordinates:** In the Hard Dose Q1, interpreting the `sample.txt` strings (e.g., "2303") was a bit confusing, and I am assumed x coordinate of obstacle = east - west; y coordinate of obstacle = north - south.

---

## 4. Explanation of Approach

* **Light Dose (Bash):** Created a comprehensive bash script to handle all directory generation, text searching (`grep`), and simulated system health checks. 
* **Medium Q4 (Filters):** Implemented both filters, but concluded that a **Hybrid approach** is required because Muchiko (average) is too vulnerable to the extreme, chaotic spikes caused by the microgravity environment.
* **Medium Q5 (Robotic Arm):** Used a Dynamic Programming dictionary to map the minimum cumulative cost to reach every valid mechanical state for a given target, carrying only the cheapest paths forward to the next target.
* **Hard Q1 (Arena Pathfinding):** Implemented a Breadth-First Search (BFS) using a Double-Ended Queue (`collections.deque`). Since movement costs are equal (1 meter), BFS mathematically guarantees the absolute shortest path to the [10, 10] coordinate while avoiding the parsed obstacles.
* **Hard Q3 (Behavior Tree):** Structured the decision tree using Fallback nodes to provide the rover with graceful degradation (e.g., turning off cameras instead of aborting the mission, or trying to bypass a rock before stopping).

---

## 5. Resources Used
* **Official Documentation:** Python 3.12,3, Docs, OpenCV (cv2) Documentation, Numpy Reference.
* **Tools:** Ubuntu Terminal, Git/GitHub, Canva (for Behavior Tree mapping).
* **Algorithms:** Standard computer science literature for BFS and Dynamic Programming concepts.