#!/bin/bash

echo "Input the parent directory name: "
read dir

# Assign the user input to a variable
DIR="$dir"

# Check if the directory does not exist
if [ ! -d "$DIR" ]; then
    # Create the base directory
    # mkdir -p "$DIR"

    # Define the base directory
    BASE_DIR="$DIR"

    # Create the main project directory
    mkdir -p "$BASE_DIR/src"

    # Create subdirectories inside src
    mkdir -p "$BASE_DIR/src/controller"
    mkdir -p "$BASE_DIR/src/utils"
    mkdir -p "$BASE_DIR/src/models"
    mkdir -p "$BASE_DIR/src/validation"
    mkdir -p "$BASE_DIR/src/middleware"
    mkdir -p "$BASE_DIR/src/routes"

    # Create test directories
    mkdir -p "$BASE_DIR/test/unit_test"
    mkdir -p "$BASE_DIR/test/integration_test"

    echo "Project structure created successfully in '$BASE_DIR'!"
else
    echo "Directory '$DIR' already exists. Please choose a different name."
fi