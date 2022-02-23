import ee
import os
import datetime
import geopandas as gpd
import folium
import streamlit as st
import geemap.colormaps as cm
import geemap.foliumap as geemap
from datetime import date



@st.cache
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


def app():

    today = date.today()

    row1_col1, row1_col2 = st.columns([2, 1])

    if st.session_state.get("zoom_level") is None:
        st.session_state["zoom_level"] = 4

    st.session_state["ee_asset_id"] = None
    st.session_state["bands"] = None
    st.session_state["palette"] = None
    st.session_state["vis_params"] = None

    with row1_col1:
        m = geemap.Map(
            basemap="HYBRID",
            plugin_Draw=True,
            draw_export=True,
            locate_control=True,
            plugin_LatLngPopup=False,
        )
        m.add_basemap("ROADMAP")

    with row1_col2:

        keyword = st.text_input("Search for a location:", "")
        if keyword:
            locations = geemap.geocode(keyword)
            if locations is not None and len(locations) > 0:
                str_locations = [str(g)[1:-1] for g in locations]
                location = st.selectbox("Select a location:", str_locations)
                loc_index = str_locations.index(location)
                selected_loc = locations[loc_index]
                lat, lng = selected_loc.lat, selected_loc.lng
                folium.Marker(location=[lat, lng], popup=location).add_to(m)
                m.set_center(lng, lat, 12)
                st.session_state["zoom_level"] = 12

        collection = st.selectbox(
            "Select a satellite image collection: ",
            [
                "Landsat TM-ETM-OLI Surface Reflectance",
                "Sentinel-2 MSI Surface Reflectance",
            ],
            index=1,
        )

        if collection in [
            "Landsat TM-ETM-OLI Surface Reflectance",
            "Sentinel-2 MSI Surface Reflectance",
        ]:
            sample_roi = "Uploaded GeoJSON"

        

    with row1_col1:


        data = st.file_uploader(
            "",
            type=["geojson"],
        )

        crs = "epsg:4326"
        if sample_roi == "Uploaded GeoJSON":
           
            if collection in [
                "Landsat TM-ETM-OLI Surface Reflectance",
                "Sentinel-2 MSI Surface Reflectance",
            ]:
                gdf = gpd.GeoDataFrame(
                    index=[0], crs=crs
                )
            

        if sample_roi != "Uploaded GeoJSON":

            if collection in [
                "Landsat TM-ETM-OLI Surface Reflectance",
                "Sentinel-2 MSI Surface Reflectance",
            ]:
                gdf = gpd.GeoDataFrame(
                    index=[0], crs=crs
                )
            
            st.session_state["roi"] = geemap.geopandas_to_ee(gdf, geodesic=False)
            m.add_gdf(gdf, "ROI")

        elif data:
            gdf = uploaded_file_to_gdf(data)
            st.session_state["roi"] = geemap.geopandas_to_ee(gdf, geodesic=False)
            m.add_gdf(gdf, "ROI")

        m.to_streamlit(height=600)

    with row1_col2:

        if collection in [
            "Landsat TM-ETM-OLI Surface Reflectance",
            "Sentinel-2 MSI Surface Reflectance",
        ]:

            if collection == "Landsat TM-ETM-OLI Surface Reflectance":
                sensor_start_year = 1984
                timelapse_title = "Landsat Timelapse"
                timelapse_speed = 5
            elif collection == "Sentinel-2 MSI Surface Reflectance":
                sensor_start_year = 2015
                timelapse_title = "Sentinel-2 Timelapse"
                timelapse_speed = 5
            

            with st.form("submit_landsat_form"):

                roi = None
                if st.session_state.get("roi") is not None:
                    roi = st.session_state.get("roi")
                out_gif = geemap.temp_file_path(".gif")

                title = st.text_input(
                    "Enter a title to show on the timelapse: ", timelapse_title
                )
                RGB = st.selectbox(
                    "Select an RGB band combination:",
                    [
                        "Red/Green/Blue",
                        "SWIR2/NIR/Green",
                    ]  
                )

                frequency = st.selectbox(
                    "Select a temporal frequency:",
                    ["year", "month"],
                    index=0,
                )

                with st.expander("Customize timelapse"):

                    speed = st.slider("Frames per second:", 1, 30, timelapse_speed)
                    dimensions = st.slider(
                        "Maximum dimensions (Width*Height) in pixels", 768, 2000, 768
                    )
                    progress_bar_color = st.color_picker(
                        "Progress bar color:", "#0000ff"
                    )
                    years = st.slider(
                        "Start and end year:",
                        sensor_start_year,
                        today.year,
                        (sensor_start_year, today.year - 1),
                    )
                    months = st.slider("Start and end month:", 1, 12, (1, 12))
                    
                    apply_fmask = st.checkbox(
                        "Apply fmask (remove clouds, shadows, snow)", True
                    )
                    

                empty_text = st.empty()
                empty_image = st.empty()
                submitted = st.form_submit_button("Submit")
                if submitted:

                    if sample_roi == "Uploaded GeoJSON" and data is None:
                        empty_text.warning(
                            "Steps to create a timelapse: Draw a rectangle on the map -> Export it as a GeoJSON -> Upload it back to the app -> Click the Submit button. Alternatively, you can select a sample ROI from the dropdown list."
                        )
                    else:

                        empty_text.text("Computing... Please wait...")

                        start_year = years[0]
                        end_year = years[1]
                        start_date = str(months[0]).zfill(2) + "-01"
                        end_date = str(months[1]).zfill(2) + "-30"
                        bands = RGB.split("/")

                        try:
                            if collection == "Landsat TM-ETM-OLI Surface Reflectance":
                                out_gif = geemap.landsat_timelapse(
                                    roi=roi,
                                    out_gif=out_gif,
                                    start_year=start_year,
                                    end_year=end_year,
                                    start_date=start_date,
                                    end_date=end_date,
                                    bands=bands,
                                    apply_fmask=apply_fmask,
                                    frames_per_second=speed,
                                    dimensions=dimensions,
                                    frequency=frequency,
                                    date_format=None,
                                    title=title,
                                    title_xy=("2%", "90%"),
                                    add_text=True,
                                    text_xy=("2%", "2%"),
                                    text_sequence=None,
        
                                    add_progress_bar=True,
                                    progress_bar_color=progress_bar_color,
                                    progress_bar_height=5,
                                    loop=0,
                                )
                            elif collection == "Sentinel-2 MSI Surface Reflectance":
                                out_gif = geemap.sentinel2_timelapse(
                                    roi=roi,
                                    out_gif=out_gif,
                                    start_year=start_year,
                                    end_year=end_year,
                                    start_date=start_date,
                                    end_date=end_date,
                                    bands=bands,
                                    apply_fmask=apply_fmask,
                                    frames_per_second=speed,
                                    dimensions=dimensions,
                                    frequency=frequency,
                                    date_format=None,
                                    title=title,
                                    title_xy=("2%", "90%"),
                                    add_text=True,
                                    text_xy=("2%", "2%"),
                                    text_sequence=None,
                                    add_progress_bar=True,
                                    progress_bar_color=progress_bar_color,
                                    progress_bar_height=5,
                                    loop=0,
                                )
                        except:
                            empty_text.error(
                                "An error occurred while computing the timelapse. Your probably requested too much data. Try reducing the ROI or timespan."
                            )
                            st.stop()

                        if out_gif is not None and os.path.exists(out_gif):

                            empty_text.text(
                                "Right click the GIF to save it to your computer"
                            )
                            empty_image.image(out_gif)
                        else:
                            empty_text.error(
                                "Something went wrong. You probably requested too much data. Try reducing the ROI or timespan."
                            )