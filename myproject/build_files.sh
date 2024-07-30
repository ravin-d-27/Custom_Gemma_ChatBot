# build_files.sh

apt-get update && apt-get install -y python3-distutils
pip install -r requirements.txt
python3.9 manage.py collectstatic --no-input