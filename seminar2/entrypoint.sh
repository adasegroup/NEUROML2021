#! /bin/bash

printf 'Neurodocker startup - success\n'

source $FREESURFER_HOME/SetUpFreeSurfer.sh

printf 'FREESURFER - check\n' 

./opt/miniconda-latest/envs/neuro/bin/jupyter-lab --ip=0.0.0.0 --port=8080 --no-browser --allow-root --notebook-dir='/workspace' --NotebookApp.token=''
#./opt/miniconda-latest/envs/neuro/bin/jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser --allow-root --notebook-dir='/workspace' --NotebookApp.token=''
