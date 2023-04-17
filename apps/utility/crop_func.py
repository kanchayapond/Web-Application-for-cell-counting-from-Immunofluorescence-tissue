import streamlit as st
from PIL import Image
import numpy as np
import timeit
import os
import skimage.io as io

from utility.logger import setup_logging, check_pwd, tree
if 'logger' not in st.session_state:
    st.session_state['logger'] = setup_logging()
    st.session_state['logger'].info('Utility loaded')

# Check resolution of image
# If resolution is correct, save image to temp folder pepare to analyze
# If resolution is not correct, crop and save batch image to temp folder for prepare to analyze
def check_resolution(img):
    # Debugging
    st.session_state['logger'].info('Current working directory: {}'.format(check_pwd()))
    st.session_state['logger'].info('Current directory tree: /n{}'.format(tree('.')))

    width, height = img.size    # Use PIL
    #width, height = img.shape[1], img.shape[0]    # Use skimage
    width, height = int(width), int(height)
    st.session_state['image_size'] = [width, height]
    if 300 < width < 400:
        if 240 < height < 340:
            # State update
            st.session_state['is_batch'] = False
            st.session_state['logger'].info("st.session_state['is_batch'] = {}".format(st.session_state['is_batch']))
            # Save image
            file_path = os.path.join('temp', '{}.jpg'.format('temp'))
            #io.imsave(file_path, img) # Use skimage
            img.save(file_path) # Use PIL
            return st.session_state['is_batch']
    else:
        st.session_state['is_batch'] = True
        croping(img, width, height)
        return st.session_state['is_batch']

def croping(img, r_width, r_height):
    # State update
    st.session_state['logger'].info("st.session_state['is_batch'] = {}".format(st.session_state['is_batch']))
    st.session_state['logger'].info('Start deconstructing image...')

    # Crop image
    st.session_state['crop_size'] = [320, 256]
    i_width, i_height = st.session_state['crop_size']
    if r_width % i_width != 0:
        if r_height % i_height != 0:
            n_width, n_height = [(r_width//i_width) + 1, (r_height//i_height) + 1]
        elif r_height % i_height == 0:
            n_width, n_height = [(r_width//i_width) + 1, r_height//i_height]
    elif r_width % i_width == 0:
        if r_height % i_height != 0:
            n_width, n_height = [r_width//i_width, (r_height//i_height) + 1]
        elif r_height % i_height == 0:
            n_width, n_height = [r_width//i_width, r_height//i_height]
    else:
        st.session_state['logger'].error('Error when deconstructing image... Set it to default')
        n_width, n_height = [(r_width//i_width) + 1, (r_height//i_height) + 1]
    # If use batch array
    #batch = np.zeros((n_width * n_height, i_height, i_width, 3), dtype=np.uint8)
    st.session_state['batch_size'] = [n_width, n_height]
    st.session_state['logger'].info('Batch size: {}'.format(st.session_state['batch_size']))

    # Batch generator
    start_time = timeit.default_timer()
    for i in range(n_width):
        for j in range(n_height):
            x, y = i * i_width, j * i_height
            if x + i_width > r_width:
                x = r_width - i_width
            if y + i_height > r_height:
                y = r_height - i_height
            #crop = img[y:y + i_height, x:x + i_width] # Use skimage
            crop = img.crop((x, y, x + i_width, y + i_height))  # Use PIL
            # Append to batch
            #batch[i * n_height + j] = np.array(crop)
            # Save batch image
            file_path = os.path.join('temp', '{}_{}_{}.jpg'.format('temp', i, j))
            #io.imsave(file_path, np.array(crop)) # Use skimage
            Image.fromarray(np.array(crop)).save(file_path)     # Use PIL
    end_time = timeit.default_timer()
    st.session_state['logger'].info('Deconstructing image done in {} seconds'.format(end_time - start_time))

# Reconstruct image from batch to single image
def reconstruct(img_list):
    # State update
    st.session_state['logger'].info('Start reconstructing image...')
    st.session_state['logger'].info('Batch size: {}'.format(st.session_state['batch_size']))
    # Get image size
    width, height = st.session_state['image_size']
    i_width, i_height = st.session_state['crop_size']
    n_width, n_height = st.session_state['batch_size']
    # Reconstruct image
    img = np.zeros((height, width, 3), dtype=np.uint8)
    start_time = timeit.default_timer()
    for i in range(n_width):
        for j in range(n_height):
            x, y = i * i_width, j * i_height
            if x + i_width > width:
                x = width - i_width
            if y + i_height > height:
                y = height - i_height
            img[y:y + i_height, x:x + i_width] = img_list[i * n_height + j]
    end_time = timeit.default_timer()
    st.session_state['logger'].info('Reconstructing image done in {} seconds'.format(end_time - start_time))
    img = Image.fromarray(img)  # Use PIL
    #img = img.astype(np.uint8)  # Use skimage
    return img