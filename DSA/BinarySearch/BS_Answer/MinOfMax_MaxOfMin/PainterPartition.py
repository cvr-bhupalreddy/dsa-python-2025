# 1. Painter’s Partition Problem
#
# Statement:
#     You have boards[] where each element is the length of a board.
#     You have painters available.
#
# Rules:
#     Each painter paints continuous boards only.
#     Each painter paints at the same speed (time proportional to board length).
#
# Goal: Minimize the maximum time taken by any painter.
#
# Observation:
#     Maximum time for a painter = sum of lengths of boards assigned to them.
#     So we want to split the array into continuous segments to minimize the maximum segment sum.

# 2. Array Split Problem / Allocate Books
#
# Problem Statement:
#     You have books[] where each element = number of pages.
#     You have students available.
#
# Rules:
#     Each student gets continuous books only.
#
# Goal: Minimize maximum pages assigned to a student.
#
# Observation:
#     Maximum pages per student = sum of pages of books assigned.
#     Again, split the array into continuous segments to minimize the maximum sum.


# Array Split Problem
#
# The generic Array Split Problem is any problem where you want to split an array into k contiguous segments
# and minimize the maximum segment sum.
# This is exactly the same template as Book Allocation and Painter Partition.
# Examples:
#     Allocate Minimum Pages → array = pages, groups = students
#     Painter Partition → array = boards, groups = painters
#     Split Array Largest Sum (Leetcode 410) → same template


# 3. Connection Between Painter Partition and Book Allocation
#
# | Feature     | Painter Partition                                  | Allocate Books / Array Split
# | ----------- | -------------------------------------------------- | ---------------------------------------------
# | Array       | board lengths                                      | book pages
# | Groups      | painters                                           | students
# | Goal        | Minimize maximum time per painter                  | Minimize maximum pages per student
# | Constraint  | continuous allocation                              | continuous allocation
# | Feasibility | Can boards be painted by k painters in `max_time`? | Can books be assigned to k students in max_pages
# | Pattern     | Min-Max                                            | Min-Max
