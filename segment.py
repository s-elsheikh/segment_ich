import patchwork

model = "model_patchwork.json"
input_contrast = "s_002.nii"
out = "pred_drain_icb_02.nii.gz"

model_kid = patchwork.PatchWorkModel.load(model)
res,r = model_kid.apply_on_nifti(input_contrast,
                                 out,
                                 generate_type='random',
                                 repetitions=100,
                                 num_chunks=4,
                                 align_physical=False,
                                 snapper=[1,1,1,1,1],
                                 scale_to_original=False,
                                 branch_factor=2,
                                 lazyEval=0.5
                                )



