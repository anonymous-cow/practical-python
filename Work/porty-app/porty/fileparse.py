# fileparse.py
#
# Exercise 3.3
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter = ',', silence_errors=False ):
    ''' 
        Parse a CSV into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
    
    rows = csv.reader(lines, delimiter=delimiter)
    
    #read file headers
    headers=next(rows) if has_headers else []
    if select:
        indicies = [headers.index(colname) for colname in select]
        headers=select
        
    records =[]
    for rowno, row in enumerate(rows,1):
        if not row: #skip rows with no data
            continue
    
        if select: #select columns
            row = [row[index] for index in indicies]
        if types: #type conversions
            try:
                row = [func(val) for func,val in zip(types,row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s",rowno, row)
                    log.debug("row %d: Reason %s", rowno, e)
                continue
        if headers:
            record = dict(zip(headers,row))
        else:
            record=tuple(row)
        records.append(record)
    return records