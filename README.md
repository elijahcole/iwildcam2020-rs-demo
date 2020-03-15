# iwildcam2020-rs-demo
Code demonstrating how to parse the remote sensing data from the iWildCam 2020 competition.

The script `iwildcam_rs_minimal.py` (together with `iwildcam_rs_utils.py`) is meant to demonstrate the structure of the remote sensing data. 

Running the command
```
python iwildcam_rs_minimal.py --rs-path /path/to/rs/data/iwildcam_rs_npy --site 107
```
will choose a random time point for site `107` and extract the corresponding infrared imagery and a mask representing the pixels classified as *clear* according to the automatically generated `pixelqa` data. Files are saved to the same directory as the script. 
