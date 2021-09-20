# NEUROML2021



## Neuroimaging and Machine Learning for Biomedicine
This is a repository containing seminars and lecture materials for the Skoltech course on Machine Learning in Neuroimaging data, Fall 2020.

## Main links

- [:brain: Notion course main page](https://spiced-brian-eff.notion.site/NeuroML2021-0b78fc5172e2437f89ddd23f78b0a3c8)
- [📄 Syllabus](https://skoltech.instructure.com/courses/3450/files/?preview=248290)
- [:cupid: Lab Page](http://adase.group/neuro/)
- [✈️ Telegram Channel](https://t.me/joinchat/K6E7ebr7FC80YWZi)


## Course description:
This course is specifically aimed at MSc and PhD students with basic knowledge of Machine Learning techniques pursuing further growth in neuroimaging data analysis, either in clinical practice or in neuroscience research. The course will provide you with training in the aspects of human neuroimaging methods, data properties and applied Machine Learning techniques. The course is focused on brain biophysics, scanning techniques and methods of data analysis. Students will develop a broad set of skills that are essential to study brain function, brain pathology and solve biomedical tasks with state-of-the-art Machine Learning and Computer Vision techniques.​


### The list of the current seminars published (will be updated with time):

* SEMINAR 0 (03.09) BASH for Engeneering pipelines, logging
   Before seminar you are to install Docker https://www.docker.com/
 
* SEMINAR 1 (06.09, 10.09) EEG analysis, Machine Learning in EEG

* SEMINAR 2 (13.09) MRI data analysis, sources, databases, tools 
  Before seminar, please, do the following:
    1) Install Docker https://docs.docker.com/get-docker/
    2) Download `NEUROML-2.0-data.zip` folder from link https://drive.google.com/file/d/152T5HcIhmlQZMle8nbxIceYQdOK5jWS7/view?usp=sharing and unzip on your local machine.
    3) Clone repository to your local machine
    4) Run docker locally and ensure it working with command `docker run hello-world`
    5) In terminal: `cd NEUROML2021/seminar2`
    6) Type command `docker build . -t neuroml/seminar2:0.0.1` and wait for successfull build (the dot . is importaint)
    7) Run `docker run --rm -it -v /directory/to/downloaded/data:/workspace/data -p 8080:8080 neuroml/seminar2:0.0.1`
    `/directory/to/downloaded/data` from 2) (for Windows mount point will begin with -v C:/path/to/dir)
    8) Open browser (preferebly Chrome) -> localhost:8080
* SEMINAR 3 (17.09) Machine Learning for structural MRI data analysis
  Before the seminar you are to get an account and granted access here https://db.humanconnectome.org/data/projects/HCP_1200
* SEMINAR 4 (20.09) fMRI data preprocessing, analysis, GLM
    1) First follow the instruction for geting the docker image: https://miykael.github.io/nipype_tutorial/notebooks/introduction_docker.html. 
    2) Clone the `seminar4` repository
    3) Run the container and mount the folder: docker run -it --rm -p 8888:8888 -v /path_to_seminar-4:/home/neuro/nipype_tutorial/notebooks/seminar miykael/nipype_tutorial jupyter notebook
    4) Dowload the data from: https://www.openfmri.org/dataset/ds000114/ 
* SEMINAR 5 (27.09) Functional connectivity analysis and Machine Learning modelling
* SEMINAR 6 (01.10) Deep Learning models and fMRI data analysis
* SEMINAR 7 (04.10) Interpretation of ML models

#### Datasets used (please get a personal account and complete data use agreement):
* Human Connectome Project https://db.humanconnectome.org/data/projects/HCP_1200
* UCLA Consortium for Neuropsychiatric Phenomics LA5c Study https://openneuro.org/datasets/ds000030/versions/1.0.0
* Autism Brain Imaging Data Exchange http://fcon_1000.projects.nitrc.org/indi/abide/
* EEG Motor Movement/Imagery Dataset https://www.physionet.org/content/eegmmidb/1.0.0/
* ADNI Alzheimer Disease Neuoroimaging Initiative https://ida.loni.usc.edu/services/NewUser.jsp

#### Software used (please get a personal account and complete usage agreement):
* FreeSurfer https://surfer.nmr.mgh.harvard.edu/
* FmriPrep https://fmriprep.org/en/stable/
* Docker https://www.docker.com/
* MNE python library https://mne.tools/stable/index.html
