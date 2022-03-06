import imp
from flask import Flask, redirect, render_template, send_from_directory, request
import geemap.foliumap as geemap
import ee
import os
import geopandas as gpd
import uuid
from ndvi import ndvi

try:
    ee.Initialize()
except Exception as e:
    ee.Authenticate()
    ee.Initialize()


def uploaded_file_to_gdf(data):
    import tempfile
    import os
    import uuid

    _, file_extension = os.path.splitext(data.name)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(tempfile.gettempdir(), f"{file_id}{file_extension}")

    with open(file_path, "wb") as file:
        file.write(data.getbuffer())

    if file_path.lower().endswith(".kml"):
        gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
        gdf = gpd.read_file(file_path, driver="KML")
    else:
        gdf = gpd.read_file(file_path)

    return gdf


app = Flask(__name__, static_folder='./static')


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory(path)


@app.route("/")
def login():
    return render_template('index.html')

@app.route("/open")
def open():
    return render_template('open.html')


@app.route("/signin")
def signin():
    return render_template('signin.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/upload")
def upload_page():
    return render_template('upload.html')

@app.route("/timelapse")
def timelapse():
    if not os.path.exists(os.getcwd() + '/static/ignore/base.html'):
        m = geemap.Map(
            basemap="HYBRID",
            plugin_Draw=True,
            draw_export=True,
            locate_control=True,
            plugin_LatLngPopup=False,
        )
        m.add_basemap("ROADMAP")
        m.save(os.getcwd() + '/static/ignore/base.html')
    return render_template('timelapse.html', map="base.html")


@app.route('/geotogif', methods=['POST'])
def geotogif():
    rand_name = uuid.uuid4()
    file_name = request.form['file']
    geo_file = f'upload/{file_name}.geojson'
    # check condition if file exists
    gdf = gpd.read_file(geo_file)
    roi = geemap.geopandas_to_ee(gdf, geodesic=False)
    path_to_save = os.getcwd() + f'/static/ignore/{rand_name}.gif'

    collection = request.form.get('collection', 'landsat')
    start_year = request.form.get('start_date', 1984)
    end_year = request.form.get('end_date', 2021)
    bands = request.form.get('bands', 'Red/Green/Blue').split('/')
    print('bands', bands)
    frequency = request.form.get('frequency', 'year')
    if collection == 'landsat':
        out_gif = geemap.landsat_timelapse(
            roi=roi,
            out_gif=path_to_save,
            start_year=int(start_year or 1984),
            end_year=int(end_year or 2021),
            start_date='01-01',
            end_date='12-30',
            bands=bands,
            apply_fmask=True,
            date_format=None,
            title='Landsat Timelapse',
            frames_per_second=5,
            dimensions=768,
            frequency=frequency,
            title_xy=("2%", "90%"),
            add_text=True,
            text_xy=("2%", "2%"),
            text_sequence=None,
            add_progress_bar=True,
            progress_bar_color='#0000ff',
            progress_bar_height=5,
            loop=0,
        )
    else:
        out_gif = geemap.sentinel2_timelapse(
            roi=roi,
            out_gif=path_to_save,
            start_year=int(start_year or 2015),
            end_year=int(end_year or 2021),
            start_date='01-01',
            end_date='12-30',
            bands=bands,
            apply_fmask=True,
            date_format=None,
            title='Sentinel Timelapse',
            frames_per_second=5,
            dimensions=768,
            frequency=frequency,
            title_xy=("2%", "90%"),
            add_text=True,
            text_xy=("2%", "2%"),
            text_sequence=None,
            add_progress_bar=True,
            progress_bar_color='#0000ff',
            progress_bar_height=5,
            loop=0,
        )
    print(out_gif)
    return {
        'gif': f'/static/ignore/{rand_name}.gif'
    }


@app.route('/upload-geojson', methods=['POST'])
def upload_geo():
    rand_name = uuid.uuid4()
    m = geemap.Map(
        basemap="HYBRID",
        plugin_Draw=True,
        draw_export=True,
        locate_control=True,
        plugin_LatLngPopup=False,
    )
    m.add_basemap("ROADMAP")
    geo_file = request.files['file']
    geo_file.save(f'upload/{rand_name}.geojson')
    gdf = uploaded_file_to_gdf(geo_file)
    m.add_gdf(gdf, "ROI")
    m.save(os.getcwd() + f'/static/ignore/{rand_name}.html')
    return {
        'map': f'/static/ignore/{rand_name}.html',
        'file': f'{rand_name}'
    }

@app.route('/upload', methods=['POST'])
def handle_upload_image():
    if 'files[]' not in request.files:
        return redirect('/upload')
    files = request.files.getlist('files[]')
    file_names = []
    for file in files:
        filename =  f'{uuid.uuid4()}.tiff'
        file_names.append(f'static/ignore/{filename}')
        file.save(f'static/ignore/{filename}')

    result = ndvi(file_names)
    for file in file_names:
        if os.path.exists(file):
            os.remove(file)
    return render_template('upload.html', filenames=result)





app.run(debug=True)
