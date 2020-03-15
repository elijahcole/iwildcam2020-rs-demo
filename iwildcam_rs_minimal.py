import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
import iwildcam_rs_utils as rs

pp = argparse.ArgumentParser(description='iWildCam 2020 Remote Sensing Demo Script')
pp.add_argument('--rs-path',type=str,default='',help='path to remote sensing data')
pp.add_argument('--site-id',type=str,default='',help='site ID (000,001,..., or 551)')
args = pp.parse_args()

site_dir = 'iwc_' + args.site_id
site_files = os.listdir(os.path.join(args.rs_path,site_dir))
site_dates = sorted(np.unique([fname.split('_')[2] for fname in site_files]))

'''
choose a random date
'''
rand_idx = np.random.permutation(len(site_dates))[0]

'''
load files
'''
load_path = os.path.join(args.rs_path,site_dir,site_dir +'_'+site_dates[rand_idx])
I_multispectral = np.load(load_path+'_multispectral.npy') # 200 x 200 x 9
I_pixelqa = np.load(load_path+'_pixelqa.npy') # 200 x 200 x 1

'''
convert pixelqa bitmap to stack of 2D arrays
'''
I_pixelqa_parsed = np.zeros((I_pixelqa.shape[0],I_pixelqa.shape[1],len(rs.pixelqa_idx)))
for r in range(I_pixelqa.shape[0]):
    for c in range(I_pixelqa.shape[1]):
        I_pixelqa_parsed[r,c,:] = rs.parse_pixelqa(int(I_pixelqa[r,c]))

'''
generate and save plots
'''
plt.figure()
plt.imshow(I_multispectral[:,:,rs.multispectral_idx['infrared']])
plt.colorbar()
plt.title('Infrared Imagery')
plt.savefig('I_multispectral_infrared.png')
plt.close()

plt.figure()
plt.imshow(I_pixelqa_parsed[:,:,rs.pixelqa_idx['clear']],vmin=0,vmax=1)
plt.colorbar()
plt.title('Pixels Classified as "Clear"')
plt.savefig('I_pixelqa_clear.png')
plt.close()

