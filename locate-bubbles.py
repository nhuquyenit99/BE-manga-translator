from dataclasses import dataclass
from math import sqrt 
from os import system 
import cv2

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

#main 
#get cordinates of polys
f = open("outputs/opm-1/opm-1_text_detection.txt")
lines = f.readlines()

poly_cordinates = []
poly_center_cordinates = []
polys = []
distance_threshold = 70

#process cordinates of polys
for line in lines: 
    cordinate_list = line[:-1].split(',')
    cordinate_list_int = []
    for index in cordinate_list:
        cordinate_list_int.append(int(index))
    poly_cordinates.append(cordinate_list_int)

def sort_func(e):
    return e[0]

poly_cordinates.sort(key=sort_func)

for poly_cordinates in poly_cordinates: 
    poly = Poly()
    poly.set_poly(poly_cordinates)
    polys.append(poly)
    poly_center_cordinates.append(poly.get_center_point())

#merge polys that are next to each other
merge_poly_idxs = []

for idx, poly in enumerate(polys): 
    for compare_idx, compare_poly in enumerate(polys[idx+1:]): 
        # print(poly.__dict__, compare_poly.__dict__)
        # print('distance', get_distance_between_2_polys(poly, compare_poly))
        if get_distance_between_2_polys(poly, compare_poly) <= distance_threshold:
            merge_poly_idxs.append((idx, idx + 1 + compare_idx))

#merge polys
print('merged_poly_idxs', merge_poly_idxs)

for idx, compare_idx in merge_poly_idxs: 
    polys[compare_idx] = merge_poly(polys[idx], polys[compare_idx])

#remove duplicated idx

def get_merged_idx(two_idx):
    return two_idx[0]

merge_idxs = map(get_merged_idx, merge_poly_idxs)
merge_idxs = list(dict.fromkeys(merge_idxs))

#remove merge idx
merge_idxs.sort(reverse=True)
for idx in merge_idxs:
    print('Remove index', idx)
    polys.pop(idx)

#print result
print('\nResult:')
for poly in polys:
    print(poly.__dict__)

#crop image using cv2
system('mkdir cv2-output-opm-1')
img = cv2.imread('inputs/opm-1.jpg')
for idx, poly in enumerate(polys): 
    crop_img = img[poly.y2:poly.y1, poly.x1:poly.x2]
    # export images of bubbles
    cv2.imwrite("cv2-output-opm-1/bubble-" + str(idx) + ".png", crop_img)
    #clear bubble in original image
    img = cv2.rectangle(img, (poly.x1, poly.y1), (poly.x2, poly.y2), (255,255,255), -1)

#export clear img
cv2.imwrite("cv2-output-opm-1/img-blank-bubble.png", img)