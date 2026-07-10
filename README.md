# CryptoMatrix

A mobile cryptocurrency and matrix-based application built with Kivy and Python.

## Overview

CryptoMatrix is a cross-platform mobile application designed for [describe your use case]. The project uses:
- **Kivy** for the user interface
- **Python 3.11** for core logic
- **Buildozer** for Android APK packaging
- **SQLite** for local data persistence

## Project Structure

```
crypto-matrix-app/
├── main.py                 # Application entry point
├── buildozer.spec          # Buildozer configuration for Android builds
├── screens/                # UI screens and views
│   ├── home_screen.py      # Home/main screen
│   └── settings_screen.py  # Settings screen
├── core/                   # Core business logic
│   ├── config.py           # Configuration and constants
│   ├── logger.py           # Logging utilities
│   └── database.py         # Database management
├── utils/                  # Utility functions
│   └── validators.py       # Input validation functions
├── tests/                  # Unit tests
│   └── test_validators.py  # Validator tests
└── data/                   # Local data (generated at runtime)
```

## Quick Start

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TIGRANGR555/crypto-matrix-app.git
cd crypto-matrix-app
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

```bash
python main.py
```

### Running Tests

```bash
python -m pytest tests/
# or
python -m unittest discover tests/
```

### Building Android APK

```bash
pip install "buildozer>=1.5.0" cython
buildozer --unattended android debug
```

The APK will be available in the `bin/` directory.

### Automated Builds

Push to the `main` branch to trigger automated APK builds via GitHub Actions. Built artifacts are available in the workflow runs.

## Development

### Adding New Screens

1. Create a new file in `screens/`:
```python
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

class MyNewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout()
        # Add widgets...
        self.add_widget(layout)
```

2. Add it to the ScreenManager in `main.py`:
```python
sm.add_widget(MyNewScreen(name="myscreen"))
```

### Adding Business Logic

1. Create modules in the `core/` directory
2. Import and use them from screen classes
3. Add corresponding unit tests in `tests/`

### Configuration

Edit `core/config.py` to customize:
- App metadata (name, version)
- Directories and paths
- Database settings
- Logging configuration
- UI constants

## Contributing

1. Create a feature branch
2. Make your changes
3. Add/update tests
4. Submit a pull request

## License

[Add your license here]

## Support

For issues or questions, open an issue on GitHub.
