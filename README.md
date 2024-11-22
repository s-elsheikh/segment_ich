# Segmentation of ICH and drain following Minimally Invasive Surgery

Follow up CT after minimally invasive surgery for acute intracerebral hemorrhage (ICH) is a common indication for CT-scans. ICH volume is of prognostic and therapeutic importance. However, manual volumetry is a cumbersome task and the ABC/2 method is prone to inaccuracies. Aim of this model is to segment ICH and the drain, allowing automated volumetry of the ICH following minimally invasive surgery.

We developed a CNN-based model for segmentation of ICH and the drain. 

Complete description and validation in: [Accuracy of automated segmentation and volumetry of acute intracerebral hemorrhage following minimally invasive surgery using a patch‑based convolutional neural network in a small dataset](https://rdcu.be/dyUGM)

Elsheikh, S., Elbaz, A., Rau, A. et al. Accuracy of automated segmentation and volumetry of acute intracerebral hemorrhage following minimally invasive surgery using a patch-based convolutional neural network in a small dataset. Neuroradiology (2024). https://doi.org/10.1007/s00234-024-03311-4



## Description of scripts
### segment.py:
1. expects a non-contrast CT in NIfTI format.
2. Default input is `s_002.nii`, located in the same folder as the script. 
3. Default output is `prediction.nii.gz`. A 4D NIfTI object with two 3D 1-mm isotropic NIfTI volumes, indicating the probability of each voxel belonging to ICH/drain or the background.

 
## Recreating Environment

```
conda env create -f 02_patchwork.yml
conda activate segment_ich
python segment.py
```

License
Please see LICENSE for information of the license and uses.
