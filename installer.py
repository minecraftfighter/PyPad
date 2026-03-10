import zipfile
import os

with zipfile.ZipFile("text_editor/Azure.zip", 'r') as zip_ref:
    zip_ref.extractall("text_editor")

os.remove('text_editor/Azure.zip')
