#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, NoReturn, Optional

service_dirs = [
    Path("portal_backend"),
    Path("portal-gateway"),
    Path("mailing-api"),
    Path("users-service"),
]

default_compose_files = {
    "base": Path("docker-compose.yaml"),
    "debug": Path("docker-compose-debug.yaml"),
}


def main() -> None:
    parser = parse_args()
    args, compose_args = parser.parse_known_args()
    
    compose_files = get_compose_files(args.mode, args.disable)
    
    if not compose_files:
        die("No compose files found to run!")
    
    print(f"Starting Docker Compose in {args.mode} mode")
    run_compose(compose_files, Path(args.env_file), compose_args)


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage Docker Compose configurations", add_help=True)
    parser.add_argument(
        "-m", "--mode",
        choices=["main", "debug"],
        default="debug",
        help="Specify operation mode: 'main' for production/test or 'debug' for development (default: debug)"
    )
    parser.add_argument(
        "-e", "--env-file",
        default=".env",
        help="Specify environment file (default: .env)"
    )
    parser.add_argument(
        "-D", "--disable",
        nargs="+",
        help="Comma-separated list of services to disable"
    )
    return parser

def get_compose_files(mode: str, disabled_services: Optional[List[str]] = None) -> Dict[Path, List[Path]]:
    """Get list of compose files to use based on mode and disabled services."""
    disabled_services = set(disabled_services or [])
    compose_files = {}
    
    for service_dir in service_dirs:
        if service_dir.name in disabled_services:
            continue
        
        base_file = service_dir / default_compose_files["base"]
        debug_file = service_dir / default_compose_files["debug"]
        
        assert base_file.exists(), f"Base file {base_file} does not exist"
        assert debug_file.exists(), f"Debug file {debug_file} does not exist"

        service_files = [base_file]
        if mode == "debug":
            service_files.append(debug_file)
        
        compose_files[service_dir] = service_files
    
    return compose_files

def run_compose(compose_files: Dict[Path, List[Path]], env_file: Path, compose_args: Optional[List[str]]) -> None:
    """Run docker compose with the specified files and options."""
    for service_dir, files in compose_files.items():
        cmd = get_compose_cmd(service_dir, files, env_file, compose_args)
        
        print(f"[{service_dir.name}] Running: {' '.join(cmd)}")
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            die(f"Error running docker compose for {service_dir}: {e}")
        except Exception as e:
            die(f"Error running compose for {service_dir}: {e}")

def get_compose_cmd(service_dir: Path, files: List[Path], env_file: Path, compose_args: Optional[List[str]]) -> List[str]:
    """Get the command to run docker compose for a service."""
    cmd = ["docker", "compose"]
    cmd.extend(["--project-directory", str(service_dir.absolute())])
    for file in files:
        cmd.extend(["-f", str(file.absolute())])
    cmd.extend(["--env-file", str(env_file.absolute())])
    if compose_args:
        cmd.extend(compose_args)
    return cmd

def die(message: str) -> NoReturn:
    print(message, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main() 
