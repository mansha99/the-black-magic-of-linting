# Prerequisite
- Python 3.11.X or higher
- uv

# Installation
## Project Initilaization
uv init                         # Initliaze
uv add --dev ruff               # Add ruff to your project
uv add --dev vulture            # Add vulture
uv add --dev import-linter      # Add import-linter
uv sync

# Configuration [pyproject.toml]
## ruff
```toml
[tool.ruff.lint]
select = [
    # pycodestyle
    "E",
    # Pyflakes
    "F",
    # pyupgrade
    "UP",
    # flake8-bugbear
    "B",
    # flake8-simplify
    "SIM",
    # isort
    "I",
    # Naming
    "N",
]
```
## vulture
```toml
[tool.vulture]
paths = ["."]       # Specify the files, directories, and whitelist files to analyze
min_confidence = 60 # Set the minimum confidence threshold 
verbose = false
```

## import-linter
```toml

[tool.importlinter]
root_package = "backend"
include_external_packages = true
exclude_type_checking_imports = true

# Rule 1: Domain cannot depend on application layer and infrastructure layer
[[tool.importlinter.contracts]]
name = "Domain independence"
type = "forbidden"
source_modules = ["backend.domain"]
forbidden_modules = ["backend.application"]

# Rule 2: Application cannot depend on infrastructure layer
[[tool.importlinter.contracts]]
name = "Application independence"
type = "forbidden"
source_modules = ["backend.application"]
forbidden_modules = ["backend.infrastructure"]
```


# Usage
## Ruff
### Linting
```shell
ruff check          # Lint all files in the current directory.
ruff check . --fix  # Lint and fix
```
### Formatting
```shell
ruff format  # Format all files in the current directory.
```

## vulture
```shell
uv run vulture 07-vulture.py
```
## import-linter
```shell
uv run lint-imports     
```

## Makefile : automate multi-step workflows
```bash
make
```