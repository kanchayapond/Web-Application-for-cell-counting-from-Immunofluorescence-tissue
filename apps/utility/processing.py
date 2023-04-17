import streamlit as st
import os
import pandas as pd
import timeit
from PIL import Image

from utility.yolo_func import run
from utility.crop_func import reconstruct
from utility.logger import setup_logging
if 'logger' not in st.session_state:
    st.session_state['logger'] = setup_logging()
    st.session_state['logger'].info('Processing loaded')

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
                df_result['xmin'] = df_result['xmin'] + j * st.session_state['crop_size'][0]
                df_result['ymin'] = df_result['ymin'] + i * st.session_state['crop_size'][1]
                df_result['xmax'] = df_result['xmax'] + j * st.session_state['crop_size'][0]
                df_result['ymax'] = df_result['ymax'] + i * st.session_state['crop_size'][1]

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
    
    # Delete temp.jpg
    folder_path = 'temp/'
    for file in os.listdir(folder_path):
        os.remove(os.path.join(folder_path, file))
    st.session_state['logger'].info('Deleting all file in temp/')

    # Delete runs/detect
    os.system('rm -rf runs')
    st.session_state['logger'].info('Deleting runs')

    return imagee, df_result