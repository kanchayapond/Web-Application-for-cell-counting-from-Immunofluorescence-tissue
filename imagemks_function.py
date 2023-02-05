# Importing libraries
import numpy as np
import scipy.ndimage as ndi
import pandas as pd
import plotly.express as px
from skimage import io
import PIL

# Importing specific functions
from skimage.morphology import remove_small_objects
from skimage.exposure import equalize_adapthist
from skimage.feature import corner_peaks
from skimage.segmentation import watershed
from skimage.color import label2rgb

# Importing imageMKS_custom functions
from imagemks_custom.filters.fftgaussian import fftgauss
from imagemks_custom.filters.fftedges import local_avg
from imagemks_custom.visualization.borders import make_boundary_image
from imagemks_custom.workflows.fluorescentcells import measure_fluor_cells

def vis(img, title=None, imgsize=(640, 512), mode='gray'):
    fig = px.imshow(img, title=title, color_continuous_scale='gray')
    fig.update_layout(autosize=False, width=imgsize[0], height=imgsize[1],)
    fig.show()

def labelvis(A, L, bg_color='b', engine='plotly'):
    bg_color_code = {
        'b': (0.1,0.1,0.5),
        'g': (0.1,0.5,0.1),
    }
        
    A = label2rgb(L, A, bg_label=0, bg_color=bg_color_code[bg_color], alpha=0.1, image_alpha=1)

    A = np.interp(A, (0,1), (0,255)).astype(np.uint8)

    A = make_boundary_image(L, A)
    if engine == 'plotly':
        vis(A, title='Labeled cells', mode='rgb')
    elif engine == 'PIL':
        A = PIL.Image.fromarray(A)
        A.show()
    elif engine== 'plotly_export':
        return A

def get_default_parameter():
    p = {
        'smooth_size': 3,
        'intensity_curve': 2,
        'short_th_radius': 20,
        'long_th_radius': 120,
        'max_size_of_small_objects_to_remove': 30,
        'peak_min_distance': 5,
        'size_after_watershed_to_remove': 50,
        'zoomLev': 1,
    }
    return p

def cell_counting(image, p=get_default_parameter()):
    # Parameters
    smooth_size = p['smooth_size']
    intensity_curve=p['intensity_curve']
    short_th_radius=p['short_th_radius']
    long_th_radius=p['long_th_radius']
    max_size_of_small_objects_to_remove=p['max_size_of_small_objects_to_remove']
    peak_min_distance=p['peak_min_distance']
    size_after_watershed_to_remove=p['size_after_watershed_to_remove']
    zoomLev = p['zoomLev']

    # Read image
    #Ni = io.imread(path)       # Read from path
    Ni = image                  # Read as array

    # Original Image convert to np.array(grayscale)
    Ni = np.sum(np.array(Ni), axis=2)
    '''
    Set thresholding for Blank image and convert to 0 image value. It's some tricky in numpy method. because it's use sum method-
    to calculate the sum of (color) value in each pixel and divided by np.ptp to normalize the value to 0-1.
    So, If blank image is not convert to 0 value, it will be normalized to 0-1 and it will be hard to thresholding.(like glitch image)
    So, I use np.where method to convert the blank image to 0 value. for bypass this error
    '''
    blank_tr = 30   # 30 is threshold value for blank image. It's can be change to fit with your image.
    Ni = np.where(Ni<=blank_tr, 1, Ni)  # Set to 1; becasuse blank image cant divide by 0
    check_dup_all = np.all(Ni == Ni[0,0])
    if not check_dup_all:       # Difference from notebook test. If image is not blank, it will be normalized to 0-1
        Ni = ( (( Ni-np.amin(Ni)) / np.ptp(Ni)) )

    # Step 1: smoothing intensity values and smoothing out peaks
    Ni = fftgauss(Ni, smooth_size, pad_type='edge')

    # Step 2: contrast enhancement by scaling intensities (from 0-1) on a curve
    ########  many other methods can be implemented for this step which could benefit the segmentation
    #np_pw = np.power(Ni/np.amax(Ni), intensity_curve)

    # Step 2: contrast enhancement with CLAHE
    smt = np.power(Ni/np.amax(Ni), intensity_curve)
    smt = equalize_adapthist(smt, clip_limit=0.01)
    # For selecting the best parameters, [np_pw, smt] can be used
    Ni = smt

    # Step 3: short range local avg threshold
    th_short = Ni > local_avg(Ni, short_th_radius)

    # Step 4: long range local avg threshold
    th_long = Ni > local_avg(Ni, long_th_radius)

    # Step 5: long && short
    th_Ni = (th_short*th_long)

    # Step 6: remove unknown value from Darkfield
    Nicvt = np.where(smt < 0.01, False, True)
    th_Ni_cvt = (Nicvt*th_Ni)

    # Step 8: remove small objects
    th_Ni_cvt = remove_small_objects(th_Ni_cvt, 20)
    th_Ni_cvt = remove_small_objects(th_Ni_cvt, max_size_of_small_objects_to_remove * (zoomLev))

    # Step 9: distance transform
    distance = ndi.distance_transform_edt(th_Ni_cvt)

    # Step 10: mark the maxima in the distance transform and assign labels
    peak_markers = corner_peaks(distance, min_distance=peak_min_distance, indices=False)
    peak_markers = ndi.label(peak_markers)[0]

    # Step 11: separate touching nuclei using the watershed markers
    label_Ni = watershed(th_Ni_cvt, peak_markers, mask=th_Ni_cvt)

    # Step 12: removing small regions after the watershed segmenation
    label_Ni = remove_small_objects(label_Ni, size_after_watershed_to_remove * (zoomLev))

    # Step 13: reassigning labels, so that they are continuously numbered
    old_labels = np.unique(label_Ni)
    for i in range(len(old_labels)):
        label_Ni[label_Ni == old_labels[i]] = i

    img_label = labelvis(Ni, label_Ni, engine='plotly_export')

    return img_label, label_Ni

def get_df(label_Ni, pix_scale=1):
    df = measure_fluor_cells(label_Ni, pixel_scale=pix_scale)
    return df