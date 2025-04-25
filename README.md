
# logdoc 🚀

**logdoc** is a powerful CLI tool designed to streamline and automate the injection of logging and documentation headers into your Python files. Developed by Jan Janssens, logdoc ensures your Python projects remain consistently documented and maintainable with minimal effort.

---

## 📌 Features

- **Automated Logging Injection**: Easily inject consistent logging headers.
- **Flexible Documentation Headers**: Automatically maintain documentation standards across Python scripts.
- **Integration-friendly**: Supports copying and symlinking into existing Python projects.
- **Developer-oriented**: Includes tooling for linting, testing, formatting, and dependency management.

---

## 🔧 Installation

### Install from GitHub (recommended)

```bash
pip install git+https://github.com/Jan-byterider/byterider-helper-mods.git@home_settings
```

### Install in editable mode (development)

```bash
git clone https://github.com/Jan-byterider/byterider-helper-mods.git
cd byterider-helper-mods
make install
```

---

## 🚩 Usage

Basic CLI usage:

```bash
logdoc <target_project> [--mode {copy, symlink}] [--inject]
```

### Parameters

- `target_project`: Path to the project where logdoc should be linked or injected.
- `--mode`: Linking mode (`copy` or `symlink`). Default is `copy`.
- `--inject`: Inject headers into the target project without linking.

### Examples

Copy and inject into a project:

```bash
logdoc ../my-python-project --mode copy --inject
```

Only inject headers:

```bash
logdoc ../my-python-project --inject
```

---

## 🛠️ Makefile Usage

For detailed Makefile commands, please refer to the [Makefile Usage Guide](logdoc_makefile_usage_with_C.md).

Quick example:

```bash
make check-env
make install
make test
make lint
make format
```

---

## 📂 Project Structure

```
byterider-helper-mods/
├── Makefile
├── pyproject.toml
├── requirements.in
├── src/
│   └── logdoc/
│       ├── __init__.py
│       └── cli.py
└── tests/
```

---

## 🚨 Important Notes

- Ensure you use a virtual environment when working with logdoc.
- Regularly use `make freeze` to manage dependencies efficiently.

---

## 👨‍💻 Author

**Jan Janssens**  
📧 [jan@byterider.be](mailto:jan@byterider.be)

---

## 📜 License

Specify your license here (e.g., MIT License).

