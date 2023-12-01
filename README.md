# Segmentation of ICH and drain following Minimally Invasive Surgery

Follow up CT after minimally invasive surgery for acute intracerebral hemorrhage (ICH) is a common indication for CT-scans. ICH volume is of prognostic and therapeutic importance. However, manual volumetry is a cumbersome task and the ABC/2 method is prone to inaccuracies. Aim of this model is to segment ICH and the drain, allowing automated volumetry of the ICH following minimally invasive surgery.

We developed a CNN-based model for segmentation of ICH and the drain. 

## Description of scripts
### segment.py:
1. expects a non-contrast CT in NIfTI format.
2. produces prediction.nii.gz. A 4D NIfTI object with two 3D 1-mm isotropic NIfTI volumes, indicating the probability of each voxel belonging to ICH/drain or the background.
 
## Recreating Environment
The last line in the yaml file (prefix) need to be changed to the local path, where the environment should be setup. Default location for Miniconda3: `C:\Users\your_user_name\Miniconda3\envs\segment_ich`. The choice is yours!!

*Running the yaml file without change will produce an error. Please update before creating the environment.*

```
rem Did you change the last line in yaml file???
conda env create -f 02_patchwork.yml
conda activate segment_ich
python segment.py
```

License
Please see LICENSE for information of the license and uses.
