from PyInstaller.compat import is_linux
from PyInstaller.utils.hooks import collect_data_files

if is_linux:
    hiddenimports = ['termux']
    datas = collect_data_files('termux')
