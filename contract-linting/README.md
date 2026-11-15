# Install Smithy and Spectral
## Smithy
brew tap smithy-lang/tap && brew install smithy-cli
## Spectral
npm install -g @stoplight/spectral-cli

# Setup
Create a file models/todo.smithy and paste generated output of `ai-prompt.md`
Create another file models/validators.smithy 
Create smithy-build.json at project-root

# Generating output
smithy build
build/smithy/source/openapi/TodoService.openapi.json

# Sepctral
spectral lint build/smithy/source/openapi/TodoService.openapi.json


Create a makefile for
Step 1 : Executing `smithy build` to generate `build/smithy/source/openapi/TodoService.openapi.json`
Step 2 : Executing `spectral lint build/smithy/source/openapi/TodoService.openapi.json` for linting

# Execute makefile
make