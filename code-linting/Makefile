# # Default target runs the full linting pipeline followed by tests
# .PHONY: all
# all: test

# STAGE 1: Ruff (Syntax, Formatting, Import Sort, Unused Imports)
.PHONY: lint-ruff
lint-ruff:
	@echo "=== STAGE 1: Running Ruff ==="
	ruff check .

# STAGE 2: Vulture (Dead functions, classes, methods, properties)
.PHONY: lint-vulture
lint-vulture: lint-ruff
	@echo "=== STAGE 2: Running Vulture ==="
	vulture .

# STAGE 3: Import-Linter (Layered architecture & domain independence contracts)
.PHONY: lint-imports
lint-imports: lint-vulture
	@echo "=== STAGE 3: Running Import-Linter ==="
	lint-imports

# Run all 3 linting stages in order
.PHONY: lint
lint: lint-imports
	@echo "=== All linting stages passed! ==="

# # Final Step: Run tests after all lint checks succeed
# .PHONY: test
# test: lint
# 	@echo "=== Running tests ==="
# 	pytest
