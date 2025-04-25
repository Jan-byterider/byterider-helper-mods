
# Logdoc Makefile Usage Guide

This document provides instructions on using the `Makefile` included in the **logdoc** repository.

---

## 🛠️ Available Commands

| Command          | Description                                            | Usage                                  |
|------------------|--------------------------------------------------------|----------------------------------------|
| **install**      | Installs `logdoc` CLI in editable mode                 | `make install`                         |
| **check-env**    | Checks if a virtual environment is active              | `make check-env`                       |
| **test**         | Runs pytest for tests                                  | `make test`                            |
| **lint**         | Lints Python code with `flake8`                        | `make lint`                            |
| **format**       | Formats Python code with `black`                       | `make format`                          |
| **clean**        | Cleans temporary files (`__pycache__`, `.pyc`, etc.)   | `make clean`                           |
| **link**         | Copies and injects logdoc into target project          | `make link`                            |
| **inject**       | Injects headers into existing files of target project  | `make inject`                          |
| **unlink**       | Removes deployed logdoc from target project            | `make unlink`                          |
| **freeze**       | Generates `requirements.txt` from `requirements.in`    | `make freeze`                          |
| **help**         | Shows help message with all available commands         | `make help`                            |

---

## ✅ Recommended Workflow

Follow this recommended workflow when actively developing or maintaining the project:

```bash
# Ensure virtual environment is active
make check-env

# Install logdoc CLI (editable mode)
make install

# Run tests
make test

# Lint and format your code
make lint
make format

# Clean temporary files after changes
make clean
```

---

## 🚩 Specific Usage Examples

### Link and Inject to Another Project

```bash
make link
```

This command will copy and inject logdoc into the sibling project (`../scannest-ml`).

### Inject Only (Without Linking)

```bash
make inject
```

Inject logging/documentation headers into files in an existing deployment.

---

## 📦 Requirements Management

```bash
make freeze
```

Generates `requirements.txt` from your existing `requirements.in`. Ensure `pip-tools` is installed.

---

## 🧹 Cleaning Temporary Files

To remove build artifacts, `.pyc` files, and `__pycache__`:

```bash
make clean
```

---

## 📚 Getting Help

To quickly see available commands and usage:

```bash
make help
```

---

## 🛠️ Using Makefile Commands from Other Repositories

To invoke the `logdoc` Makefile commands from another repository, use the `-C` flag as shown below:

```bash
make -C /path/to/logdoc <target>
```

### Example Usage

```bash
make -C ~/development/byterider-helper-mods install
make -C ~/development/byterider-helper-mods link
```

Replace `/path/to/logdoc` with the actual path to your logdoc repository.

---

## ⚠️ Important Notes

- Ensure paths specified in the Makefile are accurate.
- Confirm `requirements.in` exists before running `make freeze`.

