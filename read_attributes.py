from shapely.geometry import Point, LineString, Polygon
from read_geometries import point, polygon

def getCentroid(geometry):
    if (isinstance(geometry, Point) or isinstance(geometry, LineString) or isinstance(geometry, Polygon)):
        cen = geometry.centroid
        return cen

cent = getCentroid(point)
print(cent)
    


def getArea(geometry):
    if (isinstance(geometry, Polygon)):
        ar = geometry.area
        return ar

area = getArea(polygon)
print(area)

def getLength(geometry):
    if (isinstance(geometry, Polygon)or isinstance(geometry, LineString)):
        return geometry.length
    else:
        msg = "Error: LineString or Polygon geometries required!"
        return msg
    

Length = getLength(point)
print(Length)
