# Hangman CLI Mini Game (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A simple **command-line Hangman word guessing game** built in Python.  
I created this project back in **2020** as one of my first Python learning exercises.  

The game has **two modes**:
1. **Player vs Computer** → Computer randomly selects a secret word, and the player tries to guess it.
2. **Player vs Player** → One player enters a secret word, and the other player tries to guess it.

---

## 🎮 How to Play
- Choose your game mode (vs Computer or vs Player).
- Guess the hidden word one letter at a time.
- Each wrong guess reduces your remaining attempts.
- Win if you guess the word before attempts run out. Lose if the hangman is complete.

---

## 📂 Project Structure
```bash
HangMan/
│── HangMan.py    # Main game file
│── .gitignore    # Ignored files (vscode, pycache, etc.)
│── README.md     # README File for description
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Clone this repository
```bash
git clone https://github.com/your-username/HANGMAN-CLI-MiniGame-Python.git
cd HANGMAN-CLI-MiniGame-Python
```

### Run the game
```bash
python HangMan.py
```