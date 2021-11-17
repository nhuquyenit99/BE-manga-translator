from dataclasses import dataclass
from math import sqrt 

@dataclass
class Poly:

    def __init__(self, **kwagrs) -> None:
        self.x1 = kwagrs.get("x1", 0)
        self.y1 = kwagrs.get("y1", 0)
        self.x2 = kwagrs.get("x2", 0)
        self.y2 = kwagrs.get("y2", 0)

    def get_center_point(self):
        return (self.x1 + self.x2)/2, (self.y1 + self.y2)/2, 

    def set_poly(self, list_index):
        list_x = []
        list_y = []
        for idx, value in enumerate(list_index):
            if idx % 2 == 0:
                list_x.append(value)
            else:
                list_y.append(value)
        self.x1, self.y1, self.x2, self.y2 = min(list_x), max(list_y), max(list_x), min(list_y)

def merge_poly(poly_1: Poly, poly_2: Poly)-> Poly:
    poly_merged = Poly(**{
        "x1" : min(poly_1.x1, poly_2.x1),
        "y1" : max(poly_1.y1, poly_2.y1),
        "x2" : max(poly_1.x2, poly_2.x2),
        "y2" : min(poly_1.y2, poly_2.y2)
    })
    return poly_merged

def get_distance_between_2_polys(poly_1: Poly, poly_2: Poly): 
    center_point_1 = poly_1.get_center_point()
    center_point_2 = poly_2.get_center_point()
    return sqrt((center_point_1[0] - center_point_2[0])**2 + (center_point_1[1] - center_point_2[1])**2)