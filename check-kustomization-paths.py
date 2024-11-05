#!/usr/bin/env python

import os
import sys
import yaml
from termcolor import colored


def line_number(file, target):
    with open(file, "r") as f:
        content = f.readlines()
    for i, line in enumerate(content):
        if target in line:
            return i + 1
    return None


def main(file_path):
    all_paths_exist = True
    with open(file_path, "r") as f:
        try:
            kustomization_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error reading file {file_path}: {e}")
            sys.exit(1)

    resources = kustomization_data.get("resources", [])

    # Verifying each path. Paths are relative to the kustomization.yaml file
    for resource_path in resources:
        # Get the directory of the current file
        directory = os.path.dirname(file_path)

        # Create a full path to the resource
        resolved_path = os.path.join(directory, resource_path)

        # Make sure the path is absolute and normalized
        resolved_path = os.path.abspath(resolved_path)

        # Now verify if the resource path exists and it's either a file or a directory
        if not os.path.exists(resolved_path):
            print(
                f'\n{file_path}\n  {line_number(file_path, resource_path)}:1      {colored("error", "red")}   Path {resolved_path} does not exist'
            )
            all_paths_exist = False

    if not all_paths_exist:
        sys.exit(1)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        main(arg)
