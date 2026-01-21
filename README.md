# 🌧️ Weather Alert SMS Automation (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Challenge](https://img.shields.io/badge/Challenge-90DaysOfCode-orange)

---

## 📌 Overview

The Weather Alert SMS Automation is a Python-based script that monitors short-term weather forecasts and sends an SMS alert when rain is expected.

The application integrates the OpenWeatherMap API for forecast data and Twilio for SMS delivery. All sensitive credentials are loaded securely using environment variables. This project was built as part of my **#90DaysOfCode** journey to practice real-world automation and API-driven workflows.

---

## 🚀 Key Features

🌦️ Weather forecast monitoring using OpenWeatherMap API  

📊 Conditional rain detection based on weather codes  

📨 Automated SMS alerts using Twilio  

🔐 Secure configuration using environment variables  

⚙️ Clean and readable automation logic  

---

## 📁 Project Structure
```
weather-alert-sms-env-automation/
│
├── main.py
│ └── Weather monitoring and SMS notification logic
│
└── README.md
└── Project documentation
```
---

## 🛠️ Application Workflow

1. Weather forecast data is fetched from the OpenWeatherMap API.

2. Upcoming weather conditions are analyzed.

3. If rain-related conditions are detected:
   - An SMS alert is sent using Twilio.

4. If no rain is expected, the script exits silently.

This project demonstrates event-based automation driven by real-time external data.

---

## ▶️ Execution Instructions

### 1️⃣ Clone the Repository

```git clone https://github.com/your-username/weather-alert-sms-env-automation.git
cd weather-alert-sms-env-automation
```
---

### 2️⃣ Install Dependencies

```
pip install requests twilio
```

---

### 3️⃣ Configure Environment Variables (IMPORTANT)

Set the following environment variables **before running the script**:

| Variable Name | Description |
|--------------|------------|
| `API_KEY` | OpenWeatherMap API key |
| `ACC_SID` | Twilio Account SID |
| `TOKEN` | Twilio Auth Token |
| `TWILIO_NUM` | Twilio phone number |
| `MY_PHONE` | Destination phone number |

#### PowerShell (Windows)
```
$env:API_KEY="your_openweather_api_key"

$env:ACC_SID="your_twilio_account_sid"

$env:TOKEN="your_twilio_auth_token"

$env:TWILIO_NUM="+1234567890"

$env:MY_PHONE="+91xxxxxxxxxx"
```

---

### 4️⃣ Run the Script
```
python main.py
```
---

## ⚠️ Important Notes

- Python 3.x is required

- Internet connection is required

- API credentials must be valid

- Environment variables must be set in the same terminal session

- Intended for educational and personal automation use

---

## 🧠 Concepts Demonstrated

API integration and JSON parsing  

Conditional automation logic  

Third-party service integration (Twilio)  

Environment variable usage  

Secure handling of sensitive data  

---

## 🎯 Project Significance

This project demonstrates how Python can be used to build secure, notification-based automation systems using external APIs. It highlights real-world patterns used in monitoring, alerting, and productivity tools.

---

## 👨‍💻 Author

**Faiz Hasan**  
BCA Final Year — Graphic Era University  

🚀 Python Learner | **#90DaysOfCode**

---

*“Good automation delivers the right message at the right time.”*
