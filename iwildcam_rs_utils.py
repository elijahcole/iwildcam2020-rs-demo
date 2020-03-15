import numpy as np

'''
map each multispectral channel name to a channel index
'''
multispectral_idx = {
    'ultrablue': 0,
    'blue': 1,
    'green': 2,
    'red': 3,
    'infrared': 4,
    'shortwave_infrared_1': 5,
    'shortwave_infrared_2': 6,
    'brightness_temp_1': 7,
    'brightness_temp_2': 8
}

'''
map each pixelqa bit name to a channel index
'''
pixelqa_idx = { 
    'fill': 0,
    'clear': 1,
    'water': 2,
    'cloud_shadow': 3,
    'snow': 4,
    'cloud': 5,
    'cloud_confidence': 6,
    'cirrus_confidence': 7,
    'terrain_occlusion': 8
}

'''
map each radsatqa bit name to a channel index
'''
radsatqa_idx = {
    'fill': 0,
    'ultrablue': 1,
    'blue': 2,
    'green': 3,
    'red': 4,
    'infrared': 5,
    'band_6_sat': 6,
    'band_7_sat': 7,
    'band_9_sat': 9,
    'band_10_sat': 10,
    'band_11_sat': 11
}

def parse_pixelqa(pixel_value):
    
    '''
    convert pixel value to bit string
    '''
    bit_string = '{0:011b}'.format(pixel_value)
    
    '''
    convert binary substrings to integers
    '''
    parsed_pixel = np.array([
        int(bit_string[10]),
        int(bit_string[9]),
        int(bit_string[8]),
        int(bit_string[7]),
        int(bit_string[6]),
        int(bit_string[5]),
        int(bit_string[3] + bit_string[4],base=2),
        int(bit_string[1] + bit_string[2],base=2),
        int(bit_string[0])
        ])
    
    return parsed_pixel

def parse_radsatqa(pixel_value):
    
    '''
    convert pixel value to bit string
    '''
    bit_string = '{0:012b}'.format(pixel_value)
    
    '''
    convert binary substrings to integers
    '''
    parsed_pixel = np.array([
        int(bit_string[11]),
        int(bit_string[10]),
        int(bit_string[9]),
        int(bit_string[8]),
        int(bit_string[7]),
        int(bit_string[6]),
        int(bit_string[5]),
        int(bit_string[4]),
        int(bit_string[2]),
        int(bit_string[1]),
        int(bit_string[0])
    ])
    
    return parsed_pixel
    