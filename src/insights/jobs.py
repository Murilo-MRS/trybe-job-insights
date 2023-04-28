from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        keys, *jobs = csv.reader(file, delimiter=",", quotechar='"')
        # zip une 2 listas, dict transforma em dicionario
        jobs_list = [dict(zip(keys, job)) for job in jobs]
        return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)

    job_types = [
        job_type
        for job in jobs_list
        for job_type in job["job_type"].split(",")
    ]
# https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python
    set_types = set(job_types)

    return list(set_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_filtered = [
        job_filtered
        for job_filtered in jobs
        if job_type == job_filtered["job_type"]
    ]

    return jobs_filtered
