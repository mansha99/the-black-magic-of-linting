# Variables
OPENAPI_SPEC := build/smithy/source/openapi/TodoService.openapi.json
SPECTRAL_RULESET := .spectral.yaml

# Default target runs both build and lint
.PHONY: all
all: lint

# Step 1: Generate the OpenAPI spec using Smithy
.PHONY: build
build:
	@echo "Running Smithy build..."
	smithy build

# Step 2: Lint the generated OpenAPI spec using Spectral
.PHONY: lint
lint: build
	@echo "Linting $(OPENAPI_SPEC) with Spectral..."
	spectral lint $(OPENAPI_SPEC) -r $(SPECTRAL_RULESET)

# Optional: Clean the Smithy build directory
.PHONY: clean
clean:
	@echo "Cleaning build directory..."
	smithy clean
