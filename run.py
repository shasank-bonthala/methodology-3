#!/usr/bin/env python

import sys
import json

sys.path.insert(0, 'test/testdata')

from testdata import get_data

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''

    if 'data' in targets:
        # make the data target
        data = get_data('20211015T175337_200-5000-iperf.csv')

    return


if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
