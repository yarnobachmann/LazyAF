# Contributing to LazyAF 4.20 🚀

Thank you for your interest in contributing to LazyAF! This document provides guidelines and information for contributors.

## 🎯 Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

## 🚀 Getting Started

### 📋 Prerequisites
- **Python 3.8+** (3.10 recommended)
- **Git** for version control
- **Windows 10/11** for testing (primary platform)

### 🛠️ Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/yarnobachmann/LazyAF.git
   cd LazyAF
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-cov flake8 black
   ```

4. **Run Tests**
   ```bash
   python test_installation.py
   python -m pytest
   ```

5. **Test the Application**
   ```bash
   python auto_clicker.py
   ```

## 📚 Project Structure

```
LazyAF/
├── auto_clicker.py          # Main application file
├── build.py                 # Build script for executable
├── requirements.txt         # Python dependencies
├── test_installation.py     # Test script
├── README.md               # Project documentation
├── CONTRIBUTING.md         # This file
├── LICENSE                 # MIT License
├── .gitignore             # Git ignore rules
├── .github/
│   ├── workflows/
│   │   └── build.yml      # GitHub Actions CI/CD
│   ├── ISSUE_TEMPLATE/    # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
└── dist/                  # Build output (ignored)
```

## 🎨 Code Style

### 🐍 Python Guidelines
- Follow **PEP 8** style guide
- Use **meaningful variable names**
- Add **docstrings** for functions and classes
- Keep functions **focused and small**
- Use **type hints** where appropriate

### 🏗️ Architecture Principles
- **SOLID principles**: Single responsibility, Open/closed, etc.
- **DRY**: Don't repeat yourself
- **Loose coupling**: Minimize dependencies between components
- **Thread safety**: Proper handling of concurrent operations

### 📝 Code Examples

**Good:**
```python
def calculate_total_interval_ms(hours: int, minutes: int, seconds: int, milliseconds: int) -> int:
    """
    Calculate total interval in milliseconds.
    
    Args:
        hours: Number of hours
        minutes: Number of minutes  
        seconds: Number of seconds
        milliseconds: Number of milliseconds
        
    Returns:
        Total interval in milliseconds
    """
    return (hours * 3600000 + minutes * 60000 + seconds * 1000 + milliseconds)
```

**Bad:**
```python
def calc(h, m, s, ms):  # Unclear function name and parameters
    return h*3600000+m*60000+s*1000+ms  # No spacing, no documentation
```

## 🧪 Testing

### 🔍 Running Tests
```bash
# Run installation tests
python test_installation.py

# Run unit tests
python -m pytest

# Run with coverage
python -m pytest --cov=auto_clicker

# Run linting
flake8 auto_clicker.py
```

### 📋 Test Requirements
- **Unit tests** for new functions
- **Integration tests** for UI components
- **Manual testing** on Windows 10/11
- **Build testing** with PyInstaller

## 🔄 Contributing Process

### 1. 🍴 Fork & Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 2. 🛠️ Development
- Make your changes
- Follow code style guidelines
- Add tests for new functionality
- Update documentation if needed

### 3. 🧪 Testing
```bash
# Test locally
python test_installation.py
python -m pytest

# Test build
python build.py

# Manual testing
python auto_clicker.py
```

### 4. 📤 Submit PR
- Push your branch to your fork
- Create a pull request
- Fill out the PR template
- Link related issues

## 🎯 Contribution Types

### 🐛 Bug Fixes
- Check existing issues first
- Create minimal reproduction case
- Fix the root cause, not just symptoms
- Add tests to prevent regression

### ✨ New Features
- Discuss in an issue first
- Keep features focused and simple
- Maintain backward compatibility
- Update documentation

### 📚 Documentation
- Keep documentation up to date
- Use clear, concise language
- Include examples where helpful
- Test all instructions

### 🎨 UI/UX Improvements
- Follow existing design patterns
- Test on different screen sizes
- Ensure accessibility
- Get feedback from users

## 🏷️ Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature request
- `documentation` - Documentation improvements
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `priority: high` - Critical issues
- `priority: medium` - Important improvements
- `priority: low` - Nice to have

## 📦 Build Process

### 🔨 Local Build
```bash
python build.py
```

### 🤖 CI/CD Pipeline
- **Tests**: Run on Python 3.8, 3.9, 3.10, 3.11
- **Build**: Create executable on Windows
- **Security**: Scan for vulnerabilities
- **Release**: Automated release on tags

## 🛡️ Security

### 🔒 Security Guidelines
- Never commit sensitive data
- Use secure coding practices
- Report security issues privately
- Follow principle of least privilege

### 📧 Security Reports
For security vulnerabilities, please email directly rather than creating a public issue.

## 🎉 Recognition

Contributors are recognized in:
- GitHub contributors list
- Release notes for significant contributions
- Special thanks in documentation

## 📞 Getting Help

### 💬 Communication Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code review and feedback

### 📖 Resources
- [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/)
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)
- [Pynput Documentation](https://pynput.readthedocs.io/)
- [PyInstaller Documentation](https://pyinstaller.readthedocs.io/)

## 🔄 Release Process

### 📈 Versioning
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Current version: 4.20
- Next version: 4.21 (patch), 4.30 (minor), 5.0 (major)

### 🚀 Release Steps
1. Update version numbers
2. Update changelog
3. Create release tag
4. GitHub Actions builds automatically
5. Upload release assets

## 📋 Checklist for Contributors

Before submitting a PR:

- [ ] **Code Quality**
  - [ ] Code follows project style guidelines
  - [ ] Functions are well-documented
  - [ ] No unnecessary code or files
  - [ ] Proper error handling

- [ ] **Testing**
  - [ ] Local testing completed
  - [ ] All tests pass
  - [ ] New tests added if needed
  - [ ] Manual testing on Windows

- [ ] **Documentation**
  - [ ] README updated if needed
  - [ ] Code comments added
  - [ ] PR description is clear
  - [ ] Related issues linked

- [ ] **Build**
  - [ ] Application runs from source
  - [ ] Executable builds successfully
  - [ ] No new dependencies without justification

Thank you for contributing to LazyAF! 🎉 