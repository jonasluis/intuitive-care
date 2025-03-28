# Main entry point for the application
# This file imports and runs the main function from the backend module

import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Import the main function from the backend module
from backend.main import main

if __name__ == '__main__':
    main()