# 🦖 Chrome Dino Bot with Selenium, OpenCV & PyAutoGUI

A Python automation bot that plays the Chrome Dinosaur game by detecting obstacles using computer vision and making the dino jump automatically. The script uses Selenium to open the game, OpenCV to detect the dinosaur, and PyAutoGUI to control the keyboard.

---

## 🚀 Features

- 🕹️ Automatically plays the Chrome Dinosaur offline game
- 🧠 Uses image recognition (OpenCV) to locate the dinosaur and detect obstacles
- 🧼 Clean keyboard control with PyAutoGUI for jumping
- 🌐 Launches the game automatically using Selenium WebDriver

---

## ⚙️ How It Works

- Selenium opens the [Chrome Dino Game](https://chromedino.com/)
- OpenCV finds the dinosaur’s position via a template image
- A specific region ahead of the dinosaur is monitored for dark pixels (obstacles)
- If an obstacle is detected, the bot makes the dino jump using the space key

---

## 🧰 Technologies

- **Python 3**
- **Selenium** for browser automation
- **OpenCV** for template matching
- **Pillow** and **PyAutoGUI** for screen capture and keyboard control
- **WebDriver Manager** to automatically manage the ChromeDriver

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/CelmarPA/Dino_Chrome_Bot
cd dino_chrome_bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install selenium opencv-python numpy pyautogui pillow webdriver-manager
```

### 3. Add the Dino Template

Place the `dino.png` image inside a folder named `dino_temp/` at the root of your project.

### 4. Run the Bot

```bash
python dino_bot.py
```

Press `Ctrl+C` to stop the bot.

---

## 📂 Project Structure

```
Dino_Chrome_Bot
├── README.md                  # Fora da pasta principal
└── chrome_dino_bot/
    ├── dino_bot.py           # Script principal 
    ├── requirements.txt      # Dependências
    └── dino_temp/
        └── dino.png
```

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Your Name Here**

- [GitHub](https://github.com/CelmarPA)
- [LinkedIn](https://linkedin.com/in/celmar-pereira-de-andrade-039830181)
- [Portfolio](https://yourportfolio.com)

---

## 💬 Feedback

Suggestions and contributions are welcome! Feel free to open issues or pull requests.
