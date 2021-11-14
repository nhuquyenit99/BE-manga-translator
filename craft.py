from craft_text_detector import Craft
# from craft_text_detector import (
#     read_image,
#     load_craftnet_model,
#     load_refinenet_model,
#     get_prediction,
#     export_detected_regions,
#     export_extra_results,
# )

# set image path and export folder dic
image_path = 'inputs/003.jpg'
output_dir = 'outputs/003'

# create a craft instance
craft = Craft(output_dir=output_dir, crop_type="poly", cuda=False)

# apply craft text detection and export detected regions to output dic
prediction_result = craft.detect_text(image_path)
print(prediction_result['polys'])

# unload models from ram/gpu
craft.unload_craftnet_model()
craft.unload_refinenet_model()

# image = read_image(image_path)

# # load models
# refine_net = load_refinenet_model(cuda=False)
# craft_net = load_craftnet_model(cuda=False)

# # perform prediction
# prediction_result = get_prediction(
#     image=image,
#     craft_net=craft_net,
#     refine_net=refine_net,
#     text_threshold=0.7,
#     link_threshold=0.4,
#     low_text=0.4,
#     cuda=False,
#     long_size=1280,
#     poly=True
# )

# # export detected text regions
# exported_file_paths = export_detected_regions(
#     image=image,
#     regions=prediction_result["boxes"],
#     output_dir=output_dir,
#     rectify=True
# )

# # export heatmap, detection points, box visualization
# export_extra_results(
#     image=image,
#     regions=prediction_result["boxes"],
#     heatmaps=prediction_result["heatmaps"],
#     output_dir=output_dir
# )

# # unload models from gpu

