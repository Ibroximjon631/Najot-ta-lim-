def assign_employee_ids(employee_ids:list, prefix:str):
    prefix_assign_employee_ids = []
    for id in employee_ids:
        prefix_assign_employee_ids.append(prefix + str(id))
    return prefix_assign_employee_ids
