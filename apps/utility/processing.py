import streamlit as st
import os
import pandas as pd
import numpy as np
import timeit
from PIL import Image, ImageDraw, ImageStat
from skimage.filters import threshold_otsu
from skimage.draw import ellipse

from utility.yolo_func import run
from utility.crop_func import reconstruct
from utility.logger import setup_logging
if 'logger' not in st.session_state:
    st.session_state['logger'] = setup_logging()
    st.session_state['logger'].info('Processing loaded')

# Create intensity column
def find_intensity(pil_image, mode='all'):
    # Convert the image to grayscale
    grayscale_image = pil_image.convert("L")

    if mode == 'all':
        intensity = ImageStat.Stat(grayscale_image).mean[0]
    if mode == 'foreground':
        # Convert the PIL image to a NumPy array
        np_image = np.array(grayscale_image)

        # Calculate the Otsu threshold value
        threshold_value = threshold_otsu(np_image)

        # Calculate the intensity of the foreground only
        foreground_mask = grayscale_image.point(lambda x: 255 if x > threshold_value else 0, "1")
        foreground_intensity = ImageStat.Stat(grayscale_image, mask=foreground_mask).mean[0]
        intensity = foreground_intensity

    return intensity

# Create number on bounding box
def draw_no(pil_image, df):
    for index, row in df.iterrows():
        # Get the bounding box coordinates
        ymin, xmax = row['ymin'], row['xmax']

        # Draw the number in the top-right corner of the bounding box
        draw = ImageDraw.Draw(pil_image)
        text = str(index)
        text_size = draw.textsize(text)
        text_x = xmax - text_size[0]
        text_y = ymin
        draw.text((text_x, text_y), text, fill=(255, 255, 255))

    return pil_image

# Create ellipse on bounding box
def draw_ellipse(pil_image, df):
    # Convert PIL to numpy
    pil_image = np.array(pil_image)

    # Create empty list
    h_r = []
    v_r = []
    area = []
    for index, row in df.iterrows():
        # Get the bounding box coordinates
        xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']

        # Determine center and radius values
        center_x = (xmax + xmin) / 2
        center_y = (ymax + ymin) / 2
        horizontal_radius = (xmax - xmin) / 2
        vertical_radius = (ymax - ymin) / 2
        h_r.append(horizontal_radius)
        v_r.append(vertical_radius)

        # Draw the ellipse on the image
        rr, cc = ellipse(center_y, center_x, vertical_radius, horizontal_radius)
        pil_image[rr, cc] = 255

        # Calculate area
        area.append(np.pi * horizontal_radius * vertical_radius)
    
    # Convert numpy to PIL
    pil_image = Image.fromarray(pil_image)

    return pil_image, h_r, v_r, area

def clean_up():
    # Clean up
    # Delete temp.jpg
    folder_path = 'temp/'
    for file in os.listdir(folder_path):
        os.remove(os.path.join(folder_path, file))
    st.session_state['logger'].info('Deleting all file in temp/')

    # Delete runs/detect
    os.system('rm -rf runs')
    st.session_state['logger'].info('Deleting runs')

# Analyze image
def analyzing(state):
    # If single image
    if not state:
        # Status update
        st.session_state['logger'].info('Start running YOLOv5...')
        # Run YOLOv5
        #image_src = os.path.join(os.path.abspath("temp"), '{}.jpg'.format('temp'))
        image_src = 'temp/{}.jpg'.format('temp')
        #weight_path = os.path.join(os.path.abspath("weights"), 'best.pt')
        img, df_result = run(source=image_src, weights='weights/best.pt')
        #imagee = img.copy()   # Use skimage
        imagee = Image.fromarray(img[:,:,::-1])    # Use PIL
        st.session_state['logger'].info('YOLOv5 finished')

    # If batch image
    else:
        warn = st.empty()
        warn.warning("The uploaded DAPI image does not meet the recommended resolution, it will be automatically cropped and analyzed. Please wait for processing.", icon="⚠️")

        # Add progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()

        # Deconstruction
        imagee_list = []
        df_list = []
        start_time = timeit.default_timer()
        for i in range(st.session_state['batch_size'][0]):
            for j in range(st.session_state['batch_size'][1]):
                # Status update
                st.session_state['logger'].info('Start analyzing image {}_{}'.format(i, j))
                st.session_state['logger'].info('Start running YOLOv5...')

                # Run YOLOv5
                #image_src = os.path.join(os.path.abspath("temp"), '{}_{}_{}.jpg'.format('temp', i, j))
                image_src = 'temp/{}_{}_{}.jpg'.format('temp', i, j)
                #weight_path = os.path.join(os.path.abspath("weights"), 'best.pt')
                img, df_result = run(source=image_src, weights='weights/best.pt')
                #imagee = img.copy()   # Use skimage
                imagee = Image.fromarray(img[:,:,::-1])   # Use PIL
                st.session_state['logger'].info('YOLOv5 finished')
                
                # Fixing dataframe
                df_result['xmin'] = df_result['xmin'] + i * st.session_state['crop_size'][0]
                df_result['ymin'] = df_result['ymin'] + j * st.session_state['crop_size'][1]
                df_result['xmax'] = df_result['xmax'] + i * st.session_state['crop_size'][0]
                df_result['ymax'] = df_result['ymax'] + j * st.session_state['crop_size'][1]

                # Appending
                imagee_list.append(imagee)
                df_list.append(df_result)

                # Update progress bar
                n_prog = st.session_state['batch_size'][0] * st.session_state['batch_size'][1]
                progress_bar.progress((i * st.session_state['batch_size'][1] + j) / n_prog)
                status_text.text('Processing image {} of {}'.format((i * st.session_state['batch_size'][1] + j) + 1, n_prog))
        end_time = timeit.default_timer()
        st.session_state['logger'].info('Analyzing image done in {} seconds'.format(end_time - start_time))

        # Reconstruction
        imagee = reconstruct(imagee_list)
        df_result = pd.concat(df_list, ignore_index=True)
        warn.empty()
        progress_bar.empty()
        status_text.empty()

    # Add position from boundingbox
    df_result['x (px)'] = df_result.apply(lambda x: int((x['xmin'] + x['xmax']) // 2), axis=1)
    df_result['y (px)'] = df_result.apply(lambda x: int((x['ymin'] + x['ymax']) // 2), axis=1)
    st.session_state['logger'].info('Position calculation finished')

    # Sort dataframe
    df_result.sort_values(by=['x (px)', 'y (px)'], inplace=True, ascending = [True, True], kind='quicksort', na_position='first', ignore_index=True)
    df_result.reset_index(drop=True, inplace=True)
    df_result.index = np.arange(1, len(df_result) + 1)

    # Draw number
    imagee = draw_no(imagee, df_result)
    st.session_state['logger'].info('Drawing number finished')

    # Calculate intensity
    df_result['Mean Intensity'] = df_result.apply(
        lambda x: find_intensity(
            imagee.crop(
                (x['xmin'], x['ymin'], x['xmax'], x['ymax'])
            )
        ), axis=1)
    st.session_state['logger'].info('Intensity calculation finished')

    # Calculate ellipse
    image_add_ellipse, h_r, v_r, area = draw_ellipse(imagee, df_result)

    for i in range(len(df_result)):
        if h_r[i] < v_r[i]:
            temp = h_r[i]
            h_r[i] = v_r[i]
            v_r[i] = temp
    df_result['Major radius (px)'] = h_r
    df_result['Minor radius (px)'] = v_r
    df_result['Area (px^2)'] = area
    df_result= df_result.drop(columns=['class'])

    df_result = df_result.astype({"Mean Intensity":"int","Major radius (px)":"int","Minor radius (px)":"int","Area (px^2)":"int"})
    # Clean temporary files
    clean_up()

    return imagee, df_result

if __name__ == '__main__':
    print('Start running main.py')
