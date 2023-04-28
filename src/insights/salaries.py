from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)

    max_salaries = [
        int(max_salary)
        for job in jobs_list
        for max_salary in job["max_salary"].split(",")
        if max_salary.isdigit()
    ]

    return max(max_salaries)


def get_min_salary(path: str) -> int:
    jobs_list = read(path)

    min_salaries = [
        int(min_salary)
        for job in jobs_list
        for min_salary in job["min_salary"].split(",")
        if min_salary.isdigit()
    ]

    return min(min_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        job_salary = int(salary)

        if min_salary > max_salary:
            raise ValueError

        return min_salary <= job_salary <= max_salary
    except Exception:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered_by_salary = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_by_salary.append(job)
        except ValueError:
            continue

    return filtered_by_salary
