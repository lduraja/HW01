import pytest

from assignment_1_1 import measurement

@pytest.mark.parametrize(
    ("blood_pressure_systolic", "blood_pressure_diastolic", "average_heart_rate",
     "sol_a", "sol_b", "sol_c", "sol_d", "sol_e"),
    [(80, 70, 55, False, False, False, False, False),
     (90, 80, 60, False, False, False, False, False),
     (91, 80, 61, False, True, False, False, True),
     (120, 80, 70, False, True, False, False, True),
     (139, 80, 99, False, True, False, False, True),
     (140, 80, 100, False, False, True, True, False),
     (120, 50, 101, False, False, True, False, False),
     (120, 60, 110, True, False, True, False, False),
     (120, 61, 120, False, False, True, False, True),
     (120, 89, 55, False, False, False, False, True),
     (120, 90, 60, False, False, False, True, False),
     (80, 50, 70, False, True, False, False, False),
     (90, 60, 100, False, False, True, False, False),
     (91, 60, 100, False, False, True, False, False),
     (90, 61, 100, False, False, True, False, False),
     (139, 89, 110, True, False, True, False, True),
     (140, 90, 120, False, False, True, True, False),
     ]
)
def test_assignment(blood_pressure_systolic, blood_pressure_diastolic, average_heart_rate, sol_a, sol_b, sol_c, sol_d,
                    sol_e):
    measure_a, measure_b, measure_c, measure_d, measure_e = measurement(blood_pressure_systolic,
                                                                        blood_pressure_diastolic, average_heart_rate)
    assert measure_a == sol_a
    assert measure_b == sol_b
    assert measure_c == sol_c
    assert measure_d == sol_d
    assert measure_e == sol_e
