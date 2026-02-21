# Nuwan Colors 




A lightweight Python package for adding customizable text coloring and styling to terminal output — making console applications more visually appealing and readable.
Author: Shashika Nuwan (DevNuwancat)
Version: 0.1
License: MIT
GitHub: DevNuwancat/NuwanColors

🚀 Installation

Option 1  — Install from PyPl
pip install nuwan_colors  (Recommended)
https://pypi.org/project/nuwan-colors/

Option 2 — Install from GitHub 
pip install git+https://github.com/DevNuwancat/NuwanColors.git
​
Option 3 — Install Locally (Development)
# Clone the repository
git clone https://github.com/DevNuwancat/NuwanColors.git

# Go into the folder
cd NuwanColors

# Install locally
pip install -e .
​
Verify Installation
python3 -c "from nuwan_colors import Colors; print(Colors.green('NuwanColors installed!'))"
​
If you see green text — it works. ✅
📦 What's Inside
NuwanColors gives you two classes:
Class
What It Does
Colors
Change text color and background color
Texts
Change text style (bold, italic, underline)
# Import both
from nuwan_colors import Colors
from nuwan_colors import Texts

# Or import together
from nuwan_colors import Colors, Texts
​
🎨 Colors Class
Text Colors
from nuwan_colors import Colors

print(Colors.black("Hello World"))    # Black text
print(Colors.red("Hello World"))      # Red text
print(Colors.green("Hello World"))    # Green text
print(Colors.yellow("Hello World"))   # Yellow text
print(Colors.blue("Hello World"))     # Blue text
print(Colors.magneta("Hello World"))  # Magenta text
print(Colors.cyan("Hello World"))     # Cyan text
print(Colors.white("Hello World"))    # White text
​
Background Colors
print(Colors.bg_black("Hello World"))         # Black background
print(Colors.bg_red("Hello World"))           # Red background
print(Colors.bg_green("Hello World"))         # Green background
print(Colors.bg_yellow("Hello World"))        # Yellow background
print(Colors.bg_blue("Hello World"))          # Blue background
print(Colors.bg_magneta("Hello World"))       # Magenta background
print(Colors.bg_cyan("Hello World"))          # Cyan background
print(Colors.bg_white("Hello World"))         # White background
print(Colors.bg_reverse_white("Hello World")) # Reversed white
​
🖋️ Texts Class
from nuwan_colors import Texts

print(Texts.bold("Hello World"))      # Bold text
print(Texts.italic("Hello World"))    # Italic text
print(Texts.underline("Hello World")) # Underlined text
print(Texts.blink("Hello World"))     # Blinking text
print(Texts.concealed("Hello World")) # Hidden text
​
✨ Combining Colors and Styles
The most powerful feature — you can nest Colors and Texts together:
from nuwan_colors import Colors, Texts

# Green + Bold
print(Colors.green(Texts.bold("Success!")))

# Red + Italic
print(Colors.red(Texts.italic("Error occurred")))

# Blue + Underline
print(Colors.blue(Texts.underline("Processing...")))

# Yellow + Bold
print(Colors.yellow(Texts.bold("Warning!")))

# Cyan + Italic
print(Colors.cyan(Texts.italic("Info message")))

# Background + Bold text
print(Colors.bg_red(Texts.bold("CRITICAL ERROR")))
​
📊 Complete Method Reference
Colors — Text
Method
Color
Colors.black(text)
⬛ Black
Colors.red(text)
🔴 Red
Colors.green(text)
🟢 Green
Colors.yellow(text)
🟡 Yellow
Colors.blue(text)
🔵 Blue
Colors.magneta(text)
🟣 Magenta
Colors.cyan(text)
🟦 Cyan
Colors.white(text)
⚪ White
Colors — Background
Method
Background
Colors.bg_black(text)
Black background
Colors.bg_red(text)
Red background
Colors.bg_green(text)
Green background
Colors.bg_yellow(text)
Yellow background
Colors.bg_blue(text)
Blue background
Colors.bg_magneta(text)
Magenta background
Colors.bg_cyan(text)
Cyan background
Colors.bg_white(text)
White background
Colors.bg_reverse_white(text)
Reversed white
Texts — Styles
Method
Style
Texts.bold(text)
Bold
Texts.italic(text)
Italic
Texts.underline(text)
Underlined
Texts.blink(text)
Blinking
Texts.concealed(text)
Hidden
💡 Recommended Color System
For consistent, readable terminal output across any project:
from nuwan_colors import Colors, Texts

# ✅ SUCCESS — Green
print(Colors.green("Operation completed successfully"))

# ❌ ERROR — Red
print(Colors.red("Something went wrong"))

# 🔵 INFO — Blue
print(Colors.blue("Starting process..."))

# ⚠️ WARNING — Yellow
print(Colors.yellow("Skipping invalid item"))

# 📊 DATA — Cyan
print(Colors.cyan("Fetched 30 articles"))

# 🔔 CRITICAL — Red Background
print(Colors.bg_red(Texts.bold("CRITICAL FAILURE")))

# 🏆 HEADER — Bold + Color
print(Colors.blue(Texts.bold("=== AI News Agent Starting ===")))
​
🔧 Real World Usage Example
Here is a complete real-world example showing NuwanColors used in a production script:
from nuwan_colors import Colors, Texts
import requests

def fetch_data():
    # Blue for starting actions
    print(Colors.blue(Texts.bold("\n🔍 Fetching data from API...")))
    
    response = requests.get("https://api.example.com/data")
    
    # Green for success
    if response.status_code == 200:
        print(Colors.green(f"✅ HTTP Status: {response.status_code} OK"))
    else:
        # Red for failure
        print(Colors.red(f"❌ HTTP Status: {response.status_code} FAILED"))
        return []
    
    data = response.json()
    
    # Cyan for data info
    print(Colors.cyan(f"📊 Retrieved {len(data)} records"))
    
    # Yellow for warnings
    if len(data) < 10:
        print(Colors.yellow("⚠️  Warning: fewer results than expected"))
    
    # Green bold for completion
    print(Colors.green(Texts.bold("✅ Done! Data ready.")))
    
    return data
​
Terminal output:
🔍 Fetching data from API...     ← blue bold
✅ HTTP Status: 200 OK           ← green
📊 Retrieved 30 records         ← cyan
✅ Done! Data ready.             ← green bold
​
🧠 How It Works Internally
NuwanColors uses ANSI escape codes — special character sequences that terminals understand as color/style commands.
# What happens behind the scenes:
Colors.green("Hello")
# Returns: "\033[32mHello\033[0m"
#           ↑          ↑      ↑
#           start      text   reset
#           green             (back to normal)

# \033[32m = "start green color"
# \033[0m  = "reset everything back to normal"
​
Every color method wraps your text between a START code and a RESET code. The terminal reads these codes and displays the right color. No external dependencies needed — just pure Python.
⚠️ Known Limitations
Limitation
Details
Windows CMD
ANSI colors may not work in old Windows CMD. Works in PowerShell and Windows Terminal.
Non-TTY environments
Colors won't show in log files or environments that don't support ANSI
Spelling note
magneta is spelled this way intentionally in the package (vs standard magenta)
📦 Package Structure
NuwanColors/
├── nuwan_colors/
│   ├── __init__.py    ← exports Colors and Texts
│   └── core.py        ← all the color logic lives here
├── test.py            ← test all colors and styles
├── setup.py           ← package configuration
├── README.md          ← this documentation
└── LICENSE.md         ← MIT License
​
🧪 Quick Test
Run this to see every color and style available:
from nuwan_colors import Colors, Texts

# Test all text colors
print(Colors.black("black"))
print(Colors.red("red"))
print(Colors.green("green"))
print(Colors.yellow("yellow"))
print(Colors.blue("blue"))
print(Colors.magneta("magneta"))
print(Colors.cyan("cyan"))
print(Colors.white("white"))

# Test all text styles
print(Texts.bold("bold"))
print(Texts.italic("italic"))
print(Texts.underline("underline"))
print(Texts.blink("blink"))

# Test combinations
print(Colors.green(Texts.bold("green + bold")))
print(Colors.red(Texts.italic("red + italic")))
print(Colors.blue(Texts.underline("blue + underline")))
​
👉 Contributing
Fork the repository on GitHub
Create a new branch: git checkout -b feature/your-feature
Make your changes
Test with test.py
Submit a pull request
📄 License
MIT License — free to use in any project, personal or commercial.
📝 Built by: Shashika Nuwan (DevNuwancat)
🌟 Tip: Combine Colors + Texts for maximum terminal beauty!
🐛 Issues? Open an issue on GitHub

