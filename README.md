# Plants Vs. Zombies Memory Toolkit 🧠🌻

A Python-based memory editing toolkit thta demonstrates how in-game values in **Plants vs. Zombies** (PvZ) can be modified using pointer chains and the `pymem` library.

> ⚠️ For educational purposes only. Do not use on online or commerical games.

---


🚀 **Live Demo Website**:  
https://pvz-cheat-website-git-main-johnsummit3rds-projects.vercel.app/

## 🚀 Features

- 🌞 **Infinite Sun** - Set sun value to any amount instantly.
- 🧟‍♂️ **One-Hit Zombies** - Make your plants unkillable.
- ⏳ **No Cooldowns** - Instantly replant plants without delay.
- 💰 **Unlimited Coins** - Manipulate in-game currency.

## 🔧 How It Works

This tool uses **pointer chaining** to reliably access memory addresses of game values.

### Step-by-step:
1. **Static Address Discovery**:
   Used **Cheat Engine** to find static base addresses and offset chains for each variable.

2. **Python Implementation**:
   With `pymem`, the tool:
   - Attaches to the PvZ process (`popcapgame1.exe`)
   - Resolves the full pointer chain
   - Edits memory directly to change game values

---

## 🛠️ Setup Instructions
> Tested on **Windows**, with **Plants vs. Zombies (Game of the Year Edition)**.
> Only works on **Windows**

### 1. Instally Python dependecies:
```bash
pip install pymem
```

### 2. Launch PvZ
Make sure the game is running (windowed mode recommended).

### 3. Run the Script
python main.py
