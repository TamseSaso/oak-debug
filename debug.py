#!/usr/bin/env python3
"""
Debug wrapper script that automatically initializes web-pdb and executes main.py.
This allows debugging without modifying the main application code.
"""
import sys
import os
from pathlib import Path
import runpy
import web_pdb

WEB_PDB_PORT = 5555
WEB_PDB_HOST = "0.0.0.0"

if __name__ == "__main__":
    print(f"Starting with web-pdb debugger (will be available at http://<device_ip>:{WEB_PDB_PORT})")
    print("The debugger will automatically start if an exception occurs.")
    
    script_dir = Path(__file__).parent
    main_script = script_dir / "main.py"
    
    with web_pdb.catch_post_mortem(host=WEB_PDB_HOST, port=WEB_PDB_PORT):
        runpy.run_path(str(main_script), run_name="__main__")

