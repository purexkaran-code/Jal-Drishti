# 🌊 Jal-Drishti: Urban Flood Early Warning System
### *AI-Powered Real-Time Flood Resilience & Evacuation Intelligence*

## 📖 Project Overview
**Jal-Drishti** (Water Vision) is a real-time IoT and AI-driven system designed to detect urban flash floods and provide instant, localized evacuation protocols. Built for the **Green Bharat** initiative, it leverages **Pathway's data processing engine** to analyze water levels in real-time and uses **Generative AI (RAG)** to guide citizens during emergencies.

---

## 🚀 Key Features
* **Real-Time Ingestion:** Continuous monitoring of water levels via ultrasonic sensors (simulated for this prototype).
* **"Rate of Rise" Detection:** Intelligent algorithms to detect sudden flash floods before they become visible.
* **AI-Driven RAG Alerts:** Integrating Large Language Models (LLMs) with NDMA Safety Guidelines to generate context-aware evacuation instructions.
* **Digital Twin Dashboard:** A live, interactive command center for authorities to monitor sector-wise flood risks.

---

## 🛠️ Technology Stack
* **Core Framework:** [Pathway](https://pathway.com/) (For high-throughput stream processing and live data ingestion).
* **Frontend/Visualization:** Streamlit (Python).
* **IoT Simulation:** Python `random` & `os` modules (Simulating JSN-SR04T Sensor Data).
* **Data Handling:** CSV (Streaming Mode).
* **AI/LLM:** OpenAI GPT / RAG Concepts (Integrated for evacuation logic).

---

## 🏗️ System Architecture

### 1. The Production Architecture (Ideal State)
In a full deployment, **Pathway** handles the heavy lifting:
* **Input:** Kafka/MQTT streams from physical sensors.
* **Processing:** Pathway `xpack` calculates sliding windows for "Rate of Rise."
* **Output:** Real-time alerts pushed to the dashboard.

### 2. The Prototype Architecture (Current Demo)
Due to local environment constraints (Windows), this submission demonstrates a **Digital Twin Simulation**:
* **`sensor_simulator.py`**: Acts as the physical device, generating varying water level data and writing to a live stream (`water_data.csv`).
* **`main_app.py`**: Contains the **Pathway logic** for backend processing (proof of implementation).
* **`dashboard.py`**: A Streamlit interface that visualizes the stream and executes the **Safety Protocol Logic** (RAG Simulation) when thresholds are breached.

---

## 📂 File Structure
| File Name | Description |
| :--- | :--- |
| `main_app.py` | **Pathway Backend Logic.** Contains the code for data ingestion and windowing operations. |
| `dashboard.py` | **The Frontend.** Interactive dashboard showing real-time graphs and AI alerts. |
| `sensor_simulator.py` | **IoT Digital Twin.** Simulates live sensor data input for the demo. |
| `water_data.csv` | **Live Data Stream.** Stores the real-time time-series data. |
| `flood_guidelines.txt` | **Knowledge Base.** The NDMA safety manual used by the system for RAG context. |

---

## ⚡ How to Run the Prototype
To see the system in action, you need to run the **Sensor** and the **Dashboard** simultaneously.

### Step 1: Install Dependencies
```bash
pip install pathway streamlit pandas openai
