import numpy as np
import os

os.makedirs('data/samples', exist_ok=True)
data = np.load(r'D:\Projects and Coding\Version Control Systems\Aether_Data\kaggle_dataset\patches\psr\train.npy')
single_patch = data[0]
np.save('data/samples/sample_patch.npy', single_patch)
print(f'Saved patch with shape {single_patch.shape} to data/samples/sample_patch.npy')
