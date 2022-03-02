sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update
sudo apt-get update
sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
sudo apt-get install gdal-bin
sudo apt-get install libgdal-dev
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
gdal-config --version
pip install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}') localtileserver

sudo apt-get install python3-pip
pipenv shell

sudo apt-get install gcc libpq-dev -y
pip install wheel

pip install -r requirements.txt

# run app
pipenv shell
streamlit run app.py

# to run streamlit config like email
rm -rf ~/.streamlit