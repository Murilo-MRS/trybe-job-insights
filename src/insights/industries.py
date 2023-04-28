from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)

    industries = [
        industry
        for job in jobs_list
        for industry in job["industry"].split("',")
        if industry != ""
    ]

    set_industries = set(industries)

    return list(set_industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_filtered = [
        job_filtered
        for job_filtered in jobs
        if industry == job_filtered["industry"]
    ]

    return jobs_filtered
