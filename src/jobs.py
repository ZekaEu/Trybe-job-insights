from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        jobs_csv = csv.DictReader(file)
        job_list = [job for job in jobs_csv]
    return job_list

# Please, ignore this comment
