from collections import defaultdict
import re


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group

    SeqInfo(total_files_till_now=15,
    example_dcm_file='1.2.840.113619.2.312.6945.1127356.11111.1520442292.27.dcm',
    series_id='1-RESTING STATE NEW/1',
    dcm_dir_name='1.2.840.113619.2.312.6945.1127356.12562.1520442107.776',
    unspecified2='-',
    unspecified3='-',
    dim1=256,
    dim2=256,
    dim3=15,
    dim4=1,
    TR=0.004888,
    TE=1.3,
    protocol_name=u'RESTING STATE NEW/1',
    is_motion_corrected=False,
    is_derived=False,
    patient_id=u'13832',
    study_description=u'RESTING STATE',
    referring_physician_name='',
    series_description=u'3 Plane Localizer',
    sequence_name='fgre',
    image_type=('ORIGINAL', 'PRIMARY', 'OTHER'),
    accession_number=u'',
    patient_age='025Y',
    patient_sex='F',
    date='20180101',
    series_uid='1.2.840.113619.2.312.6945.1127356.12562.1520442107.776')
    """
    #key_template = 'sub-{{subject}}/{}/sub-{{subject}}_{}'
    key_template = 'sub-{{subject}}/{}/sub-{{subject}}_acq-{}'

    info = defaultdict(list)

    for header in seqinfo:
        if 'EPI' in str(header.image_type) and 'EPI' in str(header.sequence_name.upper()):
            task = 'task-' + re.sub('[^a-zA-Z0-9]', '', header.series_description.title())
            task += '_bold'
            key = create_key(key_template.format('func', task))
        elif 'T2' in str(header.protocol_name.upper()) and 'FL' in str(header.protocol_name.upper()):
            series = re.sub('[^a-zA-Z0-9]', '', header.series_description.title())
            key = create_key(key_template.format('anat', series + '_FLAIR'))
        elif 'T2' in str(header.protocol_name.upper()):
            series = re.sub('[^a-zA-Z0-9]', '', header.series_description.title())
            key = create_key(key_template.format('anat', series + '_T2w'))
        else:
            series = re.sub('[^a-zA-Z0-9]', '', header.series_description.title())
            key = create_key(key_template.format('anat', series + '_T1w'))
        info[key].append(header.series_id)
    return info