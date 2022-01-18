from os import system 
import cv2

from poly import Poly, get_distance_between_2_polys, merge_poly

# get cordinates of polys
def get_bubbles(file_name: str):
    f = open("outputs/{}/{}_text_detection.txt".format(file_name, file_name))
    lines = f.readlines()

    poly_cordinates = []
    poly_center_cordinates = []
    polys = []
    distance_threshold = 70

    # process cordinates of polys
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

    # merge polys that are next to each other
    merge_poly_idxs = []

    for idx, poly in enumerate(polys): 
        for compare_idx, compare_poly in enumerate(polys[idx+1:]): 
            # print(poly.__dict__, compare_poly.__dict__)
            # print('distance', get_distance_between_2_polys(poly, compare_poly))
            if get_distance_between_2_polys(poly, compare_poly) <= distance_threshold:
                merge_poly_idxs.append((idx, idx + 1 + compare_idx))

    # merge polys
    print('merged_poly_idxs', merge_poly_idxs)

    for idx, compare_idx in merge_poly_idxs: 
        polys[compare_idx] = merge_poly(polys[idx], polys[compare_idx])

    # remove duplicated idx

    def get_merged_idx(two_idx):
        return two_idx[0]

    merge_idxs = map(get_merged_idx, merge_poly_idxs)
    merge_idxs = list(dict.fromkeys(merge_idxs))

    # remove merge idx
    merge_idxs.sort(reverse=True)
    for idx in merge_idxs:
        print('Remove index', idx)
        polys.pop(idx)

    # print result
    # print('\nResult:')
    # for poly in polys:
    #     print(poly.__dict__)

    # crop image using cv2
    system('cd cv2-output && mkdir {} && cd ..'.format(file_name))
    img = cv2.imread('{}.png'.format(file_name))
    for idx, poly in enumerate(polys): 
        crop_img = img[poly.y2:poly.y1, poly.x1:poly.x2]
        # export images of bubbles
        cv2.imwrite("cv2-output/{}/bubble-{}.png".format(file_name, idx), crop_img)
        # clear bubble in original image
        img = cv2.rectangle(img, (poly.x1, poly.y1), (poly.x2, poly.y2), (255,255,255), -1)

    # export blank img
    cv2.imwrite("cv2-output/{}/img-blank-bubble.png".format(file_name), img)
    return polys


