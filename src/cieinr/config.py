"""
Configuration management for CIEINR.

This module handles loading and validating environment variables required 
for the CIEINR package to function properly, including API keys and endpoint URLs.
"""

import os
from pathlib import Path
from typing import Any, Optional
from dotenv import load_dotenv

# Constants
ENV_VARS = [
    "BIOPORTAL_API_TOKEN",
    "REDCAP_URL",
    "REDCAP_PROJECT_ID",
    "REDCAP_API_TOKEN",
    "REDCAP_PROJECT_NAME",
    "CREATED_BY"
]

class Config:
    """
    Configuration manager for the CIEINR package. 
    Handles loading and validating environment variables.
    """
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
            
        # Find and load the .env file
        self.env_path = self._find_env_file()
        load_dotenv(self.env_path)
        
        # Load environment variables
        self.env = {}
        for var in ENV_VARS:
            self.env[var] = os.getenv(var)
        
        self._initialized = True
    
    def _find_env_file(self) -> Path:
        """
        Find the .env file by starting in the current directory and moving upward.
        
        Returns:
            Path: Path to the .env file.
        """
        current_dir = Path.cwd()
        env_path = current_dir / ".env"
        
        # Look for .env file in current directory or its parents
        while not env_path.exists():
            parent = current_dir.parent
            if parent == current_dir:  # Reached the filesystem root
                # Default to current directory if not found
                return Path(".env")  
            current_dir = parent
            env_path = current_dir / ".env"
        
        return env_path
    
    def validate(self, required_vars: Optional[list] = None) -> bool:
        """
        Validate that required environment variables are present.
        
        Args:
            required_vars: List of required environment variables. If None, validates all.
            
        Returns:
            bool: True if all required variables are present, False otherwise.
            
        Raises:
            ValueError: If validation fails with details on missing variables.
        """
        if required_vars is None:
            required_vars = ENV_VARS
        
        missing = [var for var in required_vars if not self.env.get(var)]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        
        return True
    
    def get(self, var_name: str) -> Any:
        """
        Get an environment variable.
        
        Args:
            var_name: Name of the environment variable.
            
        Returns:
            The value of the environment variable.
        """
        return self.env.get(var_name)
    
    def set(self, var_name: str, value: str) -> None:
        """
        Set an environment variable in memory and update the .env file.
        
        Args:
            var_name: Name of the environment variable.
            value: Value to set.
        """
        self.env[var_name] = value
        os.environ[var_name] = value
        
        # Update the .env file
        self._update_env_file(var_name, value)
    
    def _update_env_file(self, var_name: str, value: str) -> None:
        """
        Update a specific variable in the .env file.
        
        Args:
            var_name: Name of the environment variable.
            value: Value to set.
        """
        if not self.env_path.exists():
            # Create the file if it doesn't exist
            with open(self.env_path, "w") as f:
                f.write(f"{var_name}={value}\n")
            return
        
        # Read the existing file
        with open(self.env_path, "r") as f:
            lines = f.readlines()
        
        # Check if the variable already exists
        var_exists = False
        new_lines = []
        for line in lines:
            if line.strip() and line.strip()[0] != "#":  # Skip comments
                if line.startswith(f"{var_name}="):
                    new_lines.append(f"{var_name}={value}\n")
                    var_exists = True
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        
        # Add the variable if it doesn't exist
        if not var_exists:
            new_lines.append(f"{var_name}={value}\n")
        
        # Write the updated file
        with open(self.env_path, "w") as f:
            f.writelines(new_lines)