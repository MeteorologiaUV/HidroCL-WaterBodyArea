import geopandas as gpd

servacc_cred = ''
service_account = ''

vpath = 'Data/hidrocl_boundaries.geojson'
dbpath = 'Output/hi_o_gww_rs_tot_b_none_d1_p0d.csv'

def configure_layers(option='old'):
    """Set layers to be used in the code

    Args:
        option (str, optional): 'old' or 'new'. Defaults to 'old'.

    Returns:
        list: list of waterbodies ids
        str: layer name
    """

    if option=='old':
        gdf = gpd.read_file("Data/waterbodies_chile.geojson",
                            driver='GeoJSON')
        ids = gdf.fid.to_list()

        lyr = "projects/global-water-watch/assets/reservoirs-all-v1-0"

    if option=='new':
        gdf = gpd.read_file("Data/water_bodies.geojson",
                           driver='GeoJSON')
        ids = gdf.fid.to_list()

        lyr = "projects/ee-atapia/assets/waterbodies"

    return gdf, ids, lyr