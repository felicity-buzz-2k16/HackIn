sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo -E pip install --upgrade virtualenv
virtualenv --no-site-packages --distribute venv
source venv/bin/activate
pip install -r requirements.txt
bash resetdb.sh
