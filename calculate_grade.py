def calculate_percentage(count, total):
    """
    Helper function to calculate a percentage.
    param count: The number of instances (e.g., S, M, E).
    param total: The total number of instances.
    returns: The percentage of instances.
    """
    if total == 0:
        return None
    return (count / total) * 100

def count_conditions_for_half_grade(grade_conditions):
    """
    Helper function to count how many conditions are satisfied for a half-grade.
    param grade_conditions: A list of boolean conditions or None (for skipped conditions).
    returns: The number of conditions satisfied.
    """
    return sum(1 for condition in grade_conditions if condition is True)

def get_totals_and_percentages(data):
    """
    Extracts the totals and calculates percentages for quizzes, labs, and exams.
    param data: Dictionary containing quiz, lab, and exam results.
    returns: A dictionary of calculated totals and percentages.
    """
    quizzes_data = data.get('quizzes', {'S': 0, 'NY': 0})
    matlab_labs_data = data.get('matlab', {'S': 0, 'NY': 0})
    rtdsp_labs_data = data.get('rtdsp', {'M': 0, 'E': 0, 'X': 0})
    exams_data = data.get('exams', {'M': 0, 'E': 0})

    quizzes_total = quizzes_data['S'] + quizzes_data.get('NY', 0)
    matlab_labs_total = matlab_labs_data['S'] + matlab_labs_data.get('NY', 0)
    rtdsp_labs_total = (rtdsp_labs_data.get('M', 0) + 
                        rtdsp_labs_data.get('E', 0) + 
                        rtdsp_labs_data.get('X', 0))
    exams_total = exams_data['M'] + exams_data.get('E', 0)

    # calculate percentages
    quizzes_percentage = calculate_percentage(quizzes_data['S'], quizzes_total)
    matlab_labs_percentage = calculate_percentage(matlab_labs_data['S'], matlab_labs_total)
    rtdsp_labs_m_or_e = calculate_percentage(rtdsp_labs_data.get('M', 0) + rtdsp_labs_data.get('E', 0), rtdsp_labs_total)
    rtdsp_labs_x = calculate_percentage(rtdsp_labs_data.get('X', 0), rtdsp_labs_total)
    exams_m_percentage = calculate_percentage(exams_data['M'], exams_total)
    exams_e_percentage = calculate_percentage(exams_data.get('E', 0), exams_total)

    return {
        'quizzes_percentage': quizzes_percentage,
        'matlab_labs_percentage': matlab_labs_percentage,
        'rtdsp_labs_m_or_e': rtdsp_labs_m_or_e,
        'rtdsp_labs_x': rtdsp_labs_x,
        'exams_m_percentage': exams_m_percentage,
        'exams_e_percentage': exams_e_percentage
    }

def check_grade_conditions(percentages, grade):
    def valid_condition(condition):
        return condition is None or condition is True  # Skip if condition is None
    
    match grade:
        case 'A':
            return [
                valid_condition(percentages['quizzes_percentage'] >= 90 if percentages['quizzes_percentage'] is not None else None),
                valid_condition(percentages['matlab_labs_percentage'] >= 90 if percentages['matlab_labs_percentage'] is not None else None),
                valid_condition(percentages['rtdsp_labs_m_or_e'] >= 90 if percentages['rtdsp_labs_m_or_e'] is not None else None),
                valid_condition(percentages['rtdsp_labs_x'] <= 10 if percentages['rtdsp_labs_x'] is not None else None),
                valid_condition(percentages['exams_m_percentage'] >= 90 if percentages['exams_m_percentage'] is not None else None)
            ]
        case 'B':
            return [
                valid_condition(percentages['quizzes_percentage'] >= 80 if percentages['quizzes_percentage'] is not None else None),
                valid_condition(percentages['matlab_labs_percentage'] >= 80 if percentages['matlab_labs_percentage'] is not None else None),
                valid_condition(percentages['rtdsp_labs_m_or_e'] >= 80 if percentages['rtdsp_labs_m_or_e'] is not None else None),
                valid_condition(percentages['rtdsp_labs_x'] <= 20 if percentages['rtdsp_labs_x'] is not None else None),
                valid_condition(percentages['exams_m_percentage'] >= 80 if percentages['exams_m_percentage'] is not None else None)
            ]
        case 'C':
            return [
                valid_condition(percentages['quizzes_percentage'] >= 50 if percentages['quizzes_percentage'] is not None else None),
                valid_condition(percentages['matlab_labs_percentage'] >= 50 if percentages['matlab_labs_percentage'] is not None else None),
                valid_condition(percentages['rtdsp_labs_m_or_e'] >= 50 if percentages['rtdsp_labs_m_or_e'] is not None else None),
                valid_condition(percentages['rtdsp_labs_x'] <= 34 if percentages['rtdsp_labs_x'] is not None else None),
                valid_condition(percentages['exams_m_percentage'] >= 70 if percentages['exams_m_percentage'] is not None else None)
            ]
        case 'D':
            return [
                valid_condition(percentages['matlab_labs_percentage'] >= 50 if percentages['matlab_labs_percentage'] is not None else None),
                valid_condition(percentages['rtdsp_labs_m_or_e'] >= 33 if percentages['rtdsp_labs_m_or_e'] is not None else None),
                valid_condition(percentages['rtdsp_labs_x'] <= 50 if percentages['rtdsp_labs_x'] is not None else None),
                valid_condition(percentages['exams_m_percentage'] >= 50 if percentages['exams_m_percentage'] is not None else None)
            ]
        case _:
            return []

def determine_final_grade(percentages):
    """
    Determine the final grade (A, AB, B, BC, C, CD, D, or F) based on percentages.
    param percentages: A dictionary of calculated percentages.
    returns: The final letter grade.
    """
    a_grade_conditions = check_grade_conditions(percentages, 'A')
    if all(a_grade_conditions):
        return 'A'

    b_grade_conditions = check_grade_conditions(percentages, 'B')
    if all(b_grade_conditions):
        if count_conditions_for_half_grade(a_grade_conditions) >= 4:
            return 'AB'
        return 'B'

    c_grade_conditions = check_grade_conditions(percentages, 'C')
    if all(c_grade_conditions):
        if count_conditions_for_half_grade(b_grade_conditions) >= 4:
            return 'BC' 
        return 'C'

    d_grade_conditions = check_grade_conditions(percentages, 'D')
    if all(d_grade_conditions):
        if count_conditions_for_half_grade(c_grade_conditions) >= 4:
            return 'CD'
        return 'D'

    return 'F'

def calculate_grade(data):
    """
    Main function to calculate the final grade.
    param data: Dictionary containing quiz, lab, and exam results.
    returns: The computed letter grade (A, AB, B, BC, C, CD, D, or F).
    """
    percentages = get_totals_and_percentages(data)
    return determine_final_grade(percentages)
