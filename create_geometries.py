from shapely.geometry import Point, LineString, Polygon

def createPointGeom(x_cord, y_cord):
    return Point(x_cord, y_cord)

point = createPointGeom(2.2, 4.2)
print(point)


def createLineGeom(lst_points): 
    line = []
    
    for elem in lst_points:
        if (isinstance(elem, Point)):
            line.append(elem)
            
    return LineString(line)

coord_list = [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)]
point_list = []
for elem in coord_list:
    point_list.append(createPointGeom(elem[0],elem[1]))
line_string = createLineGeom(point_list)
print(line_string)


def createPolyGeom(lst_points):
    line = []
    
    for elem in lst_points:
        if (isinstance(elem, Point) or isinstance(elem, tuple)):
            line.append(elem)
            
    return Polygon(line)


polygon = createPolyGeom(point_list)
print(polygon)
    
