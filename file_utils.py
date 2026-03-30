import os
import json
import csv

def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json(filepath, data, indent=2):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=indent)

def read_csv(filepath):
    with open(filepath, 'r') as f:
        return list(csv.DictReader(f))

def list_files(directory, extension=None):
    files = []
    for f in os.listdir(directory):
        if extension is None or f.endswith(extension):
            files.append(os.path.join(directory, f))
    return files

def file_size(filepath):
    size = os.path.getsize(filepath)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"
