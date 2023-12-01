# Segmentation of ICH and drain following Minimally Invasive Surgery

Follow up CT after minimally invasive surgery for acute intracerebral hemorrhage (ICH) is a common indication for CT-scans. ICH volume is of prognostic and therapeutic importance. Manual volumetry is a time consuming task. ABC/2 method is prone to inaccuracies. Aim of this model is to segment ICH and the drain, allowing volumetry of the ICH.

We developed a CNN-based model for segmentation of ICH and the drain. 

## Description of scripts
### segment.py:
1. expects a non-contrast CT in NIfTI format.
2. produces prediction.nii.gz. A 4D NIfTI object with two 3D 1-mm isotropic NIfTI volumes, indicating the probability of each voxel belonging to ICH/drain or the background.
 
## Recreating Environment
```
conda env create -f 02_patchwork.yml
conda activate segment_ich
python segment.py
```

License
Please see LICENSE for information of the license and uses.
