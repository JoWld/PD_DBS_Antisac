
import os
# select all subjects and conditions to be analyzed
subjects = {
        '50_FHH_2403',
        '52_MKA_1308',
        '56_MAC_1108',
        '58_MSA_1402',
        '60_MHG_0703',
        "63_FBE_2310",
        '66_MKS_2008',
        '67_MVM_2905',
        '74_FHH_2906',
        '80_MGS_3006'
    }

condition = {
        'off',
        '60',
        '130'
    }

# OR choose individual subject and condition
subj= ''
cond='off'

#%% Define paths as used in your setup
raw_path = '/Users/jowld/Documents/'
subjects_dir        = os.path.join(raw_path, 'subjects')
eeg_path            = os.path.join(raw_path, 'EEG_data')
et_path             = os.path.join(raw_path, 'Eyelinkdata')
eeg_groupdir        = os.path.join(raw_path, 'groupanalysis')
subjects_dir_tmp    = os.path.join('/Users/jowld/Documents/subjects')
