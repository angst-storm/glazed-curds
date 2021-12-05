from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import json

districts = {}

regions = json.load(open("data/moscow.json", "r", encoding="utf-8"))
for region in regions:
    for district in region["childs"]:
        districts[district["name"]] = Polygon(
            [(float(point["coords"]["lat"]), float(point["coords"]["lon"])) for point in district["points"]])

camera2district = {}

district_locates = []
for district in districts:
    center = districts[district].centroid.coords
    district_locates.append({"name": district, "lat": center[0][0], "lng": center[0][1]})
json.dump(district_locates, open("data/districts.json", "w", encoding="utf-8"), ensure_ascii=False)

cameras = json.load(open("data/cameras.json", "r", encoding="utf-8"))
for camera in cameras:
    p = Point(camera["lat"], camera["lng"])
    for dist_name in districts:
        if districts[dist_name].contains(p):
            camera2district[camera["name"]] = dist_name
            continue

insert_file = open("insert.sql", "w", encoding="utf-8")
for cam_name in camera2district:
    insert_file.write(
        f"INSERT INTO camera_to_district (camera, district) VALUES('{cam_name}', '{camera2district[cam_name]}');\n")
