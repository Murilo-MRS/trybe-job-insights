from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def job_01():
    return {
        "job_title": "Data Engineer, Mid with Security Clearance",
        "company": "Booz Allen Hamilton",
        "state": "VA",
        "city": "Herndon",
        "min_salary": "60000",
        "max_salary": "120999",
        "job_desc": "desc",
        "industry": "Business Services",
        "rating": "3.7",
        "date_posted": "2020-05-07",
        "valid_until": "2020-06-06",
        "job_type": "FULL_TIME",
        "id": "1",
    }


@pytest.fixture
def job_02():
    return {
        "job_title": "Data Modeler, Senior with Security Clearance",
        "company": "Fooz Allen Hamilton",
        "state": "VA",
        "city": "Springfield",
        "min_salary": "87500",
        "max_salary": "152000",
        "job_desc": "desc",
        "industry": "Business Services",
        "rating": "3.7",
        "date_posted": "2020-04-28",
        "valid_until": "2020-06-06",
        "job_type": "FULL_TIME",
        "id": "2",
    }


@pytest.fixture
def job_03():
    return {
        "job_title": "Data Modeler, Senior with Security Clearance",
        "company": "Cooz Allen Hamilton",
        "state": "VA",
        "city": "Springfield",
        "min_salary": "92000",
        "max_salary": "160000",
        "job_desc": "desc",
        "industry": "Business Services",
        "rating": "3.7",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-06",
        "job_type": "FULL_TIME",
        "id": "2",
    }


def test_sort_by_criteria(job_01, job_02, job_03):
    to_sort = [job_01, job_02, job_03]
    sort_by(to_sort, "date_posted")
    assert to_sort[2]["id"] == job_03["id"]

    sort_by(to_sort, "max_salary")
    assert to_sort[0]["id"] == job_03["id"]

    sort_by(to_sort, "min_salary")
    assert to_sort[0]["id"] == job_01["id"]

    with pytest.raises(ValueError, match="invalid sorting criteria: invalid"):
        sort_by(to_sort, "invalid")
