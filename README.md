# Quantum Information Theory (Mark Wilde) - Python & Cirq Implementation

This repository contains a Python implementation of the concepts and algorithms presented in the book **"Quantum Information Theory"** by **Mark Wilde** (Cambridge University Press). The implementations utilize **Google Cirq** as the primary quantum computing framework.

## Project Overview

The goal of this project is to provide a practical, code-based companion to the theoretical concepts found in Mark Wilde's "Quantum Information Theory". By implementing the theorems, protocols, and algorithms in Python using Cirq, we aim to bridge the gap between abstract quantum information theory and concrete quantum programming.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Testing](#testing)
- [Resources](#resources)
- [License](#license)
- [Credits](#credits)

## Prerequisites

To run the code in this repository, you need:

- **Python 3.8+**
- **pip** (Python package installer)

The core dependencies are:
- [Cirq](https://github.com/quantumlib/Cirq): A python framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits.
- [NumPy](https://numpy.org/): The fundamental package for scientific computing with Python.
- [Jupyter](https://jupyter.org/): For running interactive notebooks.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/quantum-information-theory.git
    cd quantum-information-theory
    ```

2.  **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

The repository is organized to follow the structure of the book.

```text
quantum-information-theory/
├── src/
│   ├── chapter_01/       # Introduction and background
│   ├── chapter_02/       # Quantum Mechanics 101
│   ├── ...
│   └── utils/            # Shared utility functions and helpers
├── tests/                # Unit tests for the implementations
├── notebooks/            # Jupyter notebooks for interactive examples and tutorials
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Usage

You can run the python scripts directly or explore the notebooks.

### Running a script

Navigate to the `src` directory and run a module (once implemented):

```bash
# Example command
python -m src.chapter_01.basics
```

### Running Notebooks

Start the Jupyter Notebook server:

```bash
jupyter notebook
```

Then, open the desired notebook from the `notebooks/` directory in your browser.

## Testing

This project uses `pytest` for testing. To run the tests:

```bash
pytest
```

To run tests for a specific chapter:

```bash
pytest tests/test_chapter_01.py
```

## Resources

- **Book:** [Quantum Information Theory by Mark Wilde](https://www.cambridge.org/core/books/quantum-information-theory/43516572A23377F37F359670A880F571)
- **Author's Website:** [markwilde.com](http://www.markwilde.com/)
- **Cirq Documentation:** [quantumai.google/cirq](https://quantumai.google/cirq)

## License

[MIT License](LICENSE) (or appropriate license)

## Credits

- **Mark Wilde** for the excellent textbook "Quantum Information Theory".
- **Cambridge University Press**.
- **The Google Cirq Team** for the quantum computing framework.

---
*Disclaimer: This is an unofficial implementation and is not affiliated with Mark Wilde or Cambridge University Press.*
