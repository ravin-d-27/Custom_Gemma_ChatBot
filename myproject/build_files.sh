# build_files.sh
apt python3-pip
pip install -r requirements.txt
python3.9 manage.py collectstatic --no-input