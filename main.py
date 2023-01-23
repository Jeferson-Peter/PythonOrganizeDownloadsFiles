import shutil
import os
from typing import Final

HOME_PATH: Final = os.path.expanduser('~')
DOWNLOAD_PATH: Final = f"{HOME_PATH}{os.sep}Downloads"
PDF_PATH: Final = f'{DOWNLOAD_PATH}{os.sep}PDF'
DOCX_PATH: Final = f'{DOWNLOAD_PATH}{os.sep}DOCX'
CSV_PATH: Final = f'{DOWNLOAD_PATH}{os.sep}CSV'
XSLX_PATH: Final = f'{DOWNLOAD_PATH}{os.sep}XLSX'
TXT_PATH: Final = f'{DOWNLOAD_PATH}{os.sep}TXT'
FILE_EXT_TO_SEP: Final = (PDF_PATH, DOCX_PATH, CSV_PATH, XSLX_PATH, TXT_PATH)

[os.makedirs(x) for x in FILE_EXT_TO_SEP if not os.path.exists(x)]
all_files = [os.path.splitext(x) for x in os.listdir(DOWNLOAD_PATH)
             if os.path.isfile(os.path.join(DOWNLOAD_PATH, x)) and not x.startswith('~')]

for file, ext in all_files:
    filename = f'{file}{ext}'
    source_dir = os.path.join(DOWNLOAD_PATH, filename)
    if ext.lower() == '.csv':
        shutil.move(source_dir, os.path.join(CSV_PATH, filename))
    elif ext.lower() == '.pdf':
        shutil.move(source_dir, os.path.join(PDF_PATH, filename))
    elif ext.lower() == '.docx':
        shutil.move(source_dir, os.path.join(DOCX_PATH, filename))
    elif ext.lower() == '.xslx':
        shutil.move(source_dir, os.path.join(XSLX_PATH, filename))
    elif ext.lower() == '.txt':
        shutil.move(source_dir, os.path.join(TXT_PATH, filename))
