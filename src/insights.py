from src.jobs import read


def get_unique_job_types(path):
    job_list = read(path)
    job_type_list = []
    for job in job_list:
        if job["job_type"] not in job_type_list:
            job_type_list.append(job["job_type"])
    return job_type_list


def filter_by_job_type(jobs, job_type):
    filtered_job_list = [job for job in jobs if job["job_type"] == job_type]
    return filtered_job_list


def get_unique_industries(path):
    job_list = read(path)
    industry_list = []
    for job in job_list:
        if job["industry"] not in industry_list and job["industry"] != "":
            industry_list.append(job["industry"])
    return industry_list


def filter_by_industry(jobs, industry):
    filtered_industry_list = [
        job for job in jobs if job["industry"] == industry
    ]
    return filtered_industry_list


def get_max_salary(path):
    job_list = read(path)
    salary_list = []
    for job in job_list:
        if job["max_salary"].isdigit():
            salary_list.append(int(job["max_salary"]))
    return max(salary_list)


def get_min_salary(path):
    job_list = read(path)
    salary_list = []
    for job in job_list:
        if job["min_salary"].isdigit():
            salary_list.append(int(job["min_salary"]))
    return min(salary_list)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary doesn't exists")
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("min_salary or max_salary aren't valid integers")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")
    if type(salary) != int:
        raise ValueError("salary isn't a valid integer")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
