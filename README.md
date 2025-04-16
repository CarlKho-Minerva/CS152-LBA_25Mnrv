# CS152-LBA_25Mnrv

Study Spot Recommender in San Francisco (Prolog + Python GUI)

## Overview
This project is an expert system that helps students find suitable study spots in San Francisco based on their preferences. It uses a Prolog knowledge base and a Python GUI (tkinter) for an interactive, user-friendly experience.

## Features
- Interactive GUI: Answer a series of questions about your study spot preferences.
- Real-time feedback: See your choices as you make them.
- Natural language: All options and results are presented in clear, conversational English.
- Recommendations: Get a list of matching study spots based on your answers.

## How to Run

### 1. Set up your environment
If you haven't already, create and activate a Python virtual environment:

```zsh
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```zsh
pip install -r requirements.txt
```

### 3. Run the application

```zsh
python main.py
```

A window will open. Answer each question using your mouse or keyboard. Your choices and recommendations will be displayed in the GUI.

## Requirements
- Python 3.8+
- tkinter (comes with most Python installations)
- pyswip (installed via requirements.txt)
- SWI-Prolog (must be installed on your system)

### Install SWI-Prolog (if needed)
On macOS:
```zsh
brew install swi-prolog
```
On Ubuntu:
```sh
sudo apt-get install swi-prolog
```

## Development Log
See `devlog.md` for a summary of the development process and features.

## License
See `LICENSE` for details.

