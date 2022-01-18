from craft_text_detector import Craft
import urllib.request

def craft_text(image_url: str, file_name: str):
    # set image path and export folder dic
    urllib.request.urlretrieve(image_url, '{}.png'.format(file_name))
    output_dir = 'outputs/{}'.format(file_name)

    # create a craft instance
    craft = Craft(output_dir=output_dir, crop_type="poly", cuda=False)

    # apply craft text detection and export detected regions to output dic
    prediction_result = craft.detect_text('{}.png'.format(file_name))
    print(prediction_result['polys'])

    # unload models from ram/gpu
    craft.unload_craftnet_model()
    craft.unload_refinenet_model()

