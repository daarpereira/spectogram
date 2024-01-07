import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

def createColorMap(usePink = True, useOrange = True, useGreen = True, useSkyblue = True, useBrown = True, useLightgreen = True, usePurple = True, useBeje = True, useVividgreen = True,useBlue = True, useLightPink = True, useBlack = True):
    
    colors = []
    N = 256

    #PINK
    pink = np.ones((N, 3))
    pink[:, 0] = np.linspace(214/256, 1, N)
    pink[:, 1] = np.linspace(183/256, 1, N)
    pink[:, 2] = np.linspace(201/256, 1, N)
    pink_cmp = ListedColormap(pink)

    #ORANGE
    orange = np.ones((N, 3))
    orange[:, 0] = np.linspace(189/256, 1, N)
    orange[:, 1] = np.linspace(103/256, 1, N)
    orange[:, 2] = np.linspace(52/256, 1, N)
    orange_cmp = ListedColormap(orange)

    #GREEN
    green = np.ones((N, 3))
    green[:, 0] = np.linspace(108/256, 1, N)
    green[:, 1] = np.linspace(99/256, 1, N)
    green[:, 2] = np.linspace(46/256, 1, N)
    green_cmp = ListedColormap(green)

    #SKY_BLUE
    skyblue = np.ones((N, 3))
    skyblue[:, 0] = np.linspace(131/256, 1, N)
    skyblue[:, 1] = np.linspace(153/256, 1, N)
    skyblue[:, 2] = np.linspace(203/256, 1, N)
    skyblue_cmp = ListedColormap(skyblue)

    #BROWN
    brown = np.ones((N, 3))
    brown[:, 0] = np.linspace(112/256, 1, N)
    brown[:, 1] = np.linspace(54/256, 1, N)
    brown[:, 2] = np.linspace(35/256, 1, N)
    brown_cmp = ListedColormap(brown)

    #LIGHT_GREEN
    lightgreen = np.ones((N, 3))
    lightgreen[:, 0] = np.linspace(167/256, 1, N)
    lightgreen[:, 1] = np.linspace(179/256, 1, N)
    lightgreen[:, 2] = np.linspace(165/256, 1, N)
    lightgreen_cmp = ListedColormap(lightgreen)

    #PURPLE
    purple = np.ones((N, 3))
    purple[:, 0] = np.linspace(165/256, 1, N)
    purple[:, 1] = np.linspace(88/256, 1, N)
    purple[:, 2] = np.linspace(151/256, 1, N)
    purple_cmp = ListedColormap(purple)

    #BEJE
    beje = np.ones((N, 3))
    beje[:, 0] = np.linspace(240/256, 1, N)
    beje[:, 1] = np.linspace(237/256, 1, N)
    beje[:, 2] = np.linspace(220/256, 1, N)
    beje_cmp = ListedColormap(beje)

    #VIVIDGREEN
    vividgreen = np.ones((N, 3))
    vividgreen[:, 0] = np.linspace(228/256, 1, N)
    vividgreen[:, 1] = np.linspace(226/256, 1, N)
    vividgreen[:, 2] = np.linspace(110/256, 1, N)
    vividgreen_cmp = ListedColormap(vividgreen)

    #BLUE
    blue = np.ones((N, 3))
    blue[:, 0] = np.linspace(41/256, 1, N)
    blue[:, 1] = np.linspace(50/256, 1, N)
    blue[:, 2] = np.linspace(111/256, 1, N)
    blue_cmp = ListedColormap(blue)

    #LIGHTPINK
    lightpink = np.ones((N, 3))
    lightpink[:, 0] = np.linspace(238/256, 1, N)
    lightpink[:, 1] = np.linspace(218/256, 1, N)
    lightpink[:, 2] = np.linspace(214/256, 1, N)
    lightpink_cmp = ListedColormap(lightpink)

    #BLACK
    black = np.ones((N, 3))
    black[:, 0] = np.linspace(13/256, 1, N)
    black[:, 1] = np.linspace(30/256, 1, N)
    black[:, 2] = np.linspace(24/256, 1, N)
    black_cmp = ListedColormap(black)

    
    if usePink:
        colors.append(pink_cmp(np.linspace(0,0, 256)))   
    if useLightgreen:
        colors.append(lightgreen_cmp(np.linspace(0,0, 256))) 
    if useOrange:
        colors.append(orange_cmp(np.linspace(0,0, 256)))
    if useGreen:
        colors.append(green_cmp(np.linspace(0,0, 256)))    
    if useSkyblue:
        colors.append(skyblue_cmp(np.linspace(0,0, 256)))
    if useBrown:
        colors.append(brown_cmp(np.linspace(0,0, 256)))          
    if usePurple:
        colors.append(purple_cmp(np.linspace(0,0, 256)))   
    if useBeje:
        colors.append(beje_cmp(np.linspace(0,0, 256)))   
    if useVividgreen:
        colors.append(vividgreen_cmp(np.linspace(0,0, 256)))    
    if useBlue:
        colors.append(blue_cmp(np.linspace(0,0, 256)))  
    if useLightPink:
        colors.append(lightpink_cmp(np.linspace(0,0, 256)))
    if useBlack:
        colors.append(black_cmp(np.linspace(0,0, 256)))
 
    return np.vstack(colors)