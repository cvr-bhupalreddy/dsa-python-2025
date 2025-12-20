# Problem Statement
#
# You are given n jobs where each job has:
#     A deadline d[i] (time by which it should be finished), and
#     A profit p[i] (earned if the job is completed on or before its deadline).
#
# Goal: Schedule the jobs to maximize total profit assuming:
#
# Each job takes 1 unit of time.
# Only one job can be scheduled at a time.
# Jobs must finish on or before their deadlines.


# Core Idea (Greedy Approach)
#
# Sort jobs by descending profit → highest profit first.
# Iterate over jobs:
#     For each job, try to schedule it in the latest available slot before its deadline.
#     If no slot is free, skip this job.
#     Add up the profits of scheduled jobs.
#
# The greedy choice works because picking the highest profit job first ensures that we maximize total profit.


def job_sequencing(jobs):
    """
    jobs: List of tuples [(deadline, profit), ...]
    Returns the maximum total profit achievable
    """
    # Step 1: Sort jobs by profit descending
    jobs.sort(key=lambda x: -x[1])  # x[1] is profit

    # Step 2: Find maximum deadline to create slots
    max_deadline = max(job[0] for job in jobs)

    # Step 3: Initialize time slots (all free)
    slots = [False] * (max_deadline + 1)
    total_profit = 0

    # Step 4: Schedule jobs greedily
    for deadline, profit in jobs:
        # Try to schedule in latest free slot <= deadline
        for t in range(deadline, 0, -1):
            if not slots[t]:
                slots[t] = True
                total_profit += profit
                break  # move to next job

    return total_profit
