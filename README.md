# M/M/S Queue Simulation with Multi-language Support

This project simulates a system of `m` linearly connected M/M/S type stations, where each station has multiple servers (S servers) and each station provides service at a certain rate (μ). The system calculates the **average number of clients (L)** in the system and the **average waiting time (W)**. The user can choose between three languages: **English**, **French**, and **Arabic** for interaction and visualization.

### Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
  - [Installation on Windows](#installation-on-windows)
  - [Installation on macOS](#installation-on-macos)
  - [Installation on Linux (Ubuntu/Debian)](#installation-on-linux-ubuntudebian)
- [Running the Project](#running-the-project)
  - [Running with Python](#running-with-python)
  - [Running with IDE (VSCode, PyCharm)](#running-with-ide-vscode-pycharm)
- [Arabic Language Issue](#arabic-language-issue)
- [Contributing](#contributing)
- [License](#license)

---

## Project Description

This project simulates a queueing system where multiple stations (servers) are connected in series, and each station has its own service rate (μ). The customer arrives at the first station, and then proceeds to each subsequent station, receiving service at each station. If a station is fully occupied, the customer waits in a queue until a server becomes available.

The simulation also calculates the **average number of customers (L)** in the system and the **average waiting time (W)** for all customers.

---

## Features

- Multi-language support: English, French, and Arabic.
- Visualization: Arrival and departure times of customers are plotted.
- Configurable number of stations, service rates, and number of servers.
- Option to simulate up to a given number of clients.

---

## Installation

### Installation on Windows

1. **Install Python**:
   - Download the latest version of Python from the [official website](https://www.python.org/downloads/).
   - Ensure that you check the box "Add Python to PATH" during installation.

2. **Install Dependencies**:
   Open the Command Prompt (`cmd`) and run the following command to install necessary Python packages:

   ```bash
   pip install numpy matplotlib

3. **Clone the Project**:
    - You can clone this repository using Git:

    ```bash
    git clone https://github.com/messafa/MEPS-TP-Final.git

4. **Navigate to the Project Directory:**
    ```bash
    cd meps-tp-final

## Installation on macOS

1. **Install Python:** macOS usually comes with Python pre-installed. However, if it's not installed or you need to upgrade, you can use Homebrew to install Python:

    ```bash
    brew install python
2. **Install Dependencies:** Use pip to install the required libraries:

         pip3 install numpy matplotlib
3. **Clone the Project**:

    ```bash
    git clone https://github.com/messafa/MEPS-TP-Final.git

4. **Navigate to the Project Directory:**

        cd meps-tp-final


## Installation on Linux (Ubuntu/Debian)
1. **Install Python:** Most Linux distributions come with Python pre-installed. If not, you can install it via the terminal:

    ```bash
    sudo apt update
    sudo apt install python3 python3-pip

2. **Install Dependencies:** Use pip3 to install the required libraries:

         pip3 install numpy matplotlib
3. **Clone the Project**:

    ```bash
    git clone https://github.com/messafa/MEPS-TP-Final.git

4. **Navigate to the Project Directory:**

        cd meps-tp-final

## Running the Project
### 1 . Running with Python

- Run the script:
    ```bash
    python3 last.py

The program will prompt you to select a language (English, French, or Arabic), simulate the M/M/S queue, and display the results in the chosen language.

## Running with IDE (VSCode, PyCharm)
### You can also run the project using an IDE like Visual Studio Code or PyCharm:
  ####  1 . Open the project folder in your IDE.
  ####  2 . Make sure the required Python interpreter is selected (usually Python 3.x).
  ####  3 . Run the last.py script within the IDE.


# Arabic Language Issue
## Problem Description
Arabic is a right-to-left (RTL) language, and displaying Arabic text in some environments, including matplotlib, can be tricky. By default, many systems or plotting libraries do not support the proper rendering of RTL languages like Arabic, leading to issues such as reversed text or improper alignment.

# Contributing
We welcome contributions to this project! To contribute:
 #### 1 . Fork the repository.
 #### 2 . Create a new branch (git checkout -b feature-xyz).
 #### 3 . Commit your changes (git commit -m 'Add new feature').
 #### 4 . Push to the branch (git push origin feature-xyz).
 #### 5 . Create a pull request.

 # License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

