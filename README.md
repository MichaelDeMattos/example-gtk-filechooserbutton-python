# upload-file-gtk

Upload any file (Photo, PDF, ...) to database using Python, Gtk and Orm Peewee

### Install to Ubuntu/Debian:

```bash
sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 python3-venv
git clone https://github.com/MichaelDeMattos/pyc-file.git && cd pyc-file
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run App

```bash
python3 main.py
```

### If you want to create a package

```bash
pip install pyinstaller
pyinstaller pyc-file.spec
./dist/pyc-file/pyc-file
```
