#######################################################
########## 1. Modules #################################
#######################################################
import urllib2
import gzip
import os
from StringIO import StringIO
import pandas as pd
import numpy as np

#######################################################
########## 2. Function ################################
#######################################################

def fetch_dataset(dataset_accession):

    # Data
    dataset = {}

    # Get dataset URL
    dataset_url = 'https://s3.amazonaws.com/mssm-seq-series-platform/{dataset_accession}_series_matrix.txt.gz'.format(**locals())

    # Open URL
    request = urllib2.Request(dataset_url)

    # Add header
    request.add_header('Accept-encoding', 'gzip')

    # Read response
    response = urllib2.urlopen(request)

    # Convert response
    buf = StringIO(response.read())

    # Open gzip file
    f = gzip.GzipFile(fileobj=buf)

    # Read data
    data = f.read()

    # Get platform
    platform_accession = os.path.basename(dataset_url).split('_')[1]

    # Check platform
    if platform_accession in ['GPL11154', 'GPL13112', 'GPL16791', 'GPL17021']:

        # Get expression dataframe
        rawcount_dataframe = pd.DataFrame([x.split('\t') for x in data.split('\n')[1:] if '!' not in x])

        # Fix axis names
        rawcount_dataframe = rawcount_dataframe.rename(columns=rawcount_dataframe.iloc[0]).drop(0).set_index('ID_REF').fillna(0).astype('int')

        # Get metadata dataframe
        metadata_dataframe = pd.DataFrame([x.split('\t') for x in data.split('\n')[1:] if any(y in x for y in ['!Sample', '!^SAMPLE'])]).set_index(0)

        # Get title conversion
        sample_title_dict = {sample_accession: '{sample_title} ({sample_accession})'.format(**locals()) for sample_accession, sample_title in metadata_dataframe.loc[['!^SAMPLE', '!Sample_title']].T.as_matrix() if sample_accession}

        # Get metadata dict
        metadata_dict = [{term_string.split(': ')[0]: term_string.split(': ')[1] for term_string in term_list} for term_list in np.array_split(metadata_dataframe.loc['!Sample_characteristics_ch1'].dropna().tolist(), len(sample_title_dict.keys()))]

        # Create dict
        sample_metadata_dataframe = pd.DataFrame({sample_accession: metadata_dict for sample_accession, metadata_dict in zip(metadata_dataframe.loc['!^SAMPLE'], metadata_dict)}).T

        # Return
        return rawcount_dataframe, sample_metadata_dataframe
