# LazyAF 4.20 🚀

A **modern, ultra-sleek** auto clicker application with support for both mouse clicks and keyboard automation. Built with Python using CustomTkinter for a professional, contemporary interface.

![Version](https://img.shields.io/badge/version-4.20-brightgreen)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![License](https://img.shields.io/badge/license-MIT-orange)
![Build](https://github.com/yourusername/LazyAF-AutoClicker/workflows/Build/badge.svg)

## ✨ Features

### 🎨 **Modern Interface**
- **Ultra-modern design** with sleek Slate/Indigo color scheme
- **Professional topbar** with clear Settings and Controls sections
- **Intuitive dashboard layout** with 6 organized cards
- **Full-screen layout** without unnecessary margins
- **Clear automation mode selection** with prominent instructions

### 🖱️ **Mouse Automation**
- **Precision timing**: Hours, minutes, seconds, and milliseconds control
- **Smart randomization**: Natural variation with configurable offset
- **Multiple buttons**: Left, Right, Middle mouse support
- **Click varieties**: Single and Double click modes
- **Flexible positioning**: 
  - Current cursor location
  - Pick custom coordinates with visual selector
- **Repeat control**: Specific count or continuous operation

### ⌨️ **Keyboard Automation**
- **Comprehensive key support**: All standard keys, letters, numbers
- **Quick selection**: Dropdown menu for common keys
- **Live key capture**: Press any key to capture it
- **Shared timing system**: Same precision as mouse automation
- **Visual feedback**: Clear display of selected key

### 🎮 **Advanced Controls**
- **Global hotkeys**: DEL key for start/stop (works system-wide)
- **Emergency failsafe**: Mouse corner detection for instant stop
- **Real-time monitoring**: Live status updates and counters
- **Professional UI**: Settings topbar with clear labels
- **Persistent settings**: Auto-save/load preferences

## 🚀 Quick Start

### 📦 **Option 1: Download & Run (Recommended)**
1. Download the latest release from [Releases](https://github.com/yourusername/LazyAF-AutoClicker/releases)
2. Extract and double-click `LazyAF_4.20.exe`
3. **No installation required!** ✅

### 🔨 **Option 2: Build from Source**
```bash
git clone https://github.com/yourusername/LazyAF-AutoClicker.git
cd LazyAF-AutoClicker
python build.py
```

### 🐍 **Option 3: Run from Source**
```bash
pip install -r requirements.txt
python auto_clicker.py
```

## 📖 How to Use

### 🎯 **Getting Started**
1. **Select Automation Mode**: Choose Mouse or Keyboard from the prominent selector
2. **Configure timing**: Set your desired interval (minimum 10ms)
3. **Choose options**: Button type, position, repeat settings
4. **Start automation**: Use topbar Controls or DEL hotkey

### 🖱️ **Mouse Automation Setup**
1. **⏱️ Click Timing**: Set precise intervals with optional randomization
2. **🖱️ Mouse Options**: Choose button (Left/Right/Middle) and click type
3. **📍 Click Position**: Select current cursor or pick custom coordinates
4. **🔄 Repeat Settings**: Choose specific count or continuous mode

### ⌨️ **Keyboard Automation Setup**
1. **Switch mode**: Select "⌨️ Keyboard" from automation mode selector
2. **⌨️ Keyboard**: Choose key from dropdown or use "🎯 Capture" for any key
3. **Configure timing**: Same precise controls as mouse automation
4. **Start pressing**: Use the same start/stop controls

### ⚙️ **Settings Management**
The professional **Settings topbar** provides:
- **Save**: Store current configuration
- **Load**: Restore previous settings  
- **Reset**: Return to defaults
- **Hotkeys**: Configure global shortcuts

### 🎮 **Controls**
The **Controls section** offers:
- **▶️ Start**: Begin automation
- **⏹️ Stop**: End automation
- **DEL hotkey**: Global start/stop (works anywhere)
- **Emergency stop**: Move mouse to screen corner

## 🛡️ Safety & Security

### 🔒 **Built-in Safety Features**
- ✅ **PyAutoGUI Failsafe**: Instant emergency stop
- ✅ **Minimum intervals**: 10ms floor prevents system overload
- ✅ **Thread safety**: Prevents UI freezing
- ✅ **Input validation**: Auto-corrects dangerous settings
- ✅ **No admin required**: Safe, permission-free operation

### 🎯 **Responsible Usage**
- Designed for **legitimate automation** tasks
- Respects application **terms of service**
- **Educational and productivity** focused
- Users responsible for **compliance** with local laws

## 💻 System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10/11 (primary), Windows 7/8 (compatible) |
| **Architecture** | 32-bit or 64-bit |
| **RAM** | 50MB minimum |
| **Storage** | 35MB for executable |
| **Permissions** | None (no admin rights needed) |
| **Python** | 3.7+ (source only) |

## 🔧 Technical Stack

### 📚 **Dependencies**
```
customtkinter==5.2.0    # Modern UI framework
pyautogui==0.9.54       # Cross-platform automation  
pynput==1.7.6           # Global input monitoring
pillow==10.0.0          # Image processing
pyinstaller==5.13.2     # Executable generation
```

### 🏗️ **Architecture**
- **SOLID principles**: Clean, maintainable design
- **DRY implementation**: Shared logic across components
- **Modern UI patterns**: Responsive, intuitive interface
- **Thread safety**: Proper async handling
- **Modular design**: Easy maintenance and extension

## 🐛 Troubleshooting

<details>
<summary><strong>🚫 Application Issues</strong></summary>

**Won't start**
- Verify Windows compatibility
- Try rebuilding: `python build.py`
- Check Windows Defender exclusions

**UI problems**
- Update graphics drivers
- Try running in compatibility mode
- Restart application

</details>

<details>
<summary><strong>🖱️ Automation Issues</strong></summary>

**Clicks not registering**
- Check application allows automation
- Verify coordinates are correct
- Some games/apps block automation

**Timing inconsistent**
- Avoid sub-10ms intervals
- Close resource-heavy applications
- Use "Current location" for better performance

</details>

<details>
<summary><strong>⌨️ Hotkey Issues</strong></summary>

**DEL key not working**
- Check no other app captures DEL
- Try running as administrator
- Restart the application

**Key capture failing**
- Ensure application has focus
- Try manual key selection
- Check keyboard layout

</details>

## 🏗️ Building & Development

### 📦 **Creating Executables**
```bash
# Automated build (recommended)
python build.py

# Manual PyInstaller
pyinstaller --onefile --windowed --name=LazyAF_4.20 auto_clicker.py
```

### 🧪 **Testing**
```bash
# Test installation
python test_installation.py

# Run development version
python auto_clicker.py
```

### 🔄 **CI/CD**
GitHub Actions automatically:
- ✅ Builds executables on push
- ✅ Runs tests
- ✅ Creates releases on tags
- ✅ Uploads artifacts

## 📈 Changelog

### 🆕 **Version 4.20** - Current
- ✨ **Complete UI redesign**: Modern slate/indigo theme
- 🎨 **Professional topbar**: Clear Settings and Controls sections
- 📱 **Full-screen layout**: No margins, maximum space usage
- 🔧 **Enhanced mode selection**: Prominent automation mode picker
- ⚡ **Improved performance**: Optimized threading and UI
- 📦 **Better build system**: Automated GitHub Actions
- 🛡️ **Enhanced safety**: Additional failsafes and validation
- 🎯 **UX improvements**: Better alignment, clearer labels

## 🤝 Contributing

We welcome contributions! Please:
1. 🍴 Fork the repository
2. 🌿 Create a feature branch
3. ✅ Test your changes
4. 📝 Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🔗 Links

- 📖 [Documentation](https://github.com/yourusername/LazyAF-AutoClicker/wiki)
- 🐛 [Issues](https://github.com/yourusername/LazyAF-AutoClicker/issues)
- 💬 [Discussions](https://github.com/yourusername/LazyAF-AutoClicker/discussions)
- 📦 [Releases](https://github.com/yourusername/LazyAF-AutoClicker/releases)

---

<div align="center">

**⭐ Star this repo if you find it useful!**

*Built with ❤️ for the automation community*

</div> 