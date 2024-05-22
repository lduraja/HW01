
# Definice konstant hranicnich tlaku a tepove frekvence
LOW_SYSTOLIC = 90
HIGH_SYSTOLIC = 140
LOW_DIASTOLIC = 60
HIGH_DIASTOLIC = 90
LOW_HEART_RATE = 60
HIGH_HEART_RATE = 100


def measurement(blood_pressure_systolic, blood_pressure_diastolic, average_heart_rate):
    """
    Returns states of measured patient
    :param int blood_pressure_systolic: measured value of systolic blood pressure in mmHg
    :param int blood_pressure_diastolic: measured value of diastolic blood pressure in mmHg
    :param int average_heart_rate: measured value of heart beat rate in BPM
    :rtype: (bool, bool, bool, bool, bool)
    :return: Logical values of patient states - True if conditions are fulfilled
    """

    # Ulozte do promenne vysledek logicke operace "Je prumerna tepova frekvence rovna 110 tepum za minutu?"
    is_heart_rate_110 = average_heart_rate == 110
    print(f"Is average heart rate ({average_heart_rate} BPM) equal to 110 beats per minute? {is_heart_rate_110}")

    # Ulozte do promenne vysledek logicke operace "Je pacient tachykardicky (rovno nebo vyssi nez horni hranice)?"
    is_tachycardia = average_heart_rate >= HIGH_HEART_RATE
    print(f"Is average heart rate ({average_heart_rate} BPM) equal or greater than high heart rate ({HIGH_HEART_RATE}) "
          f"- tachycardia? {is_tachycardia}")

    # Ulozte do promenne vysledek logicke operace "Je prumerna tepova frekvence normalni (mezi spodni a horni hranici)?"
    is_heart_rate_normal = LOW_HEART_RATE < average_heart_rate < HIGH_HEART_RATE
    print(f"Is average heart rate ({average_heart_rate} BPM) normal? {is_heart_rate_normal == average_heart_rate }")

    # Ulozte do promenne vysledek logicke operace "Ma pacient hypertenzi (nektery krevni tlak roven nebo vyssi nez dana
    # horni mez)?"
    is_hypertension = blood_pressure_systolic >= HIGH_SYSTOLIC or blood_pressure_diastolic >=HIGH_DIASTOLIC
    print(f"Is systolic ({blood_pressure_systolic} mmHg) or diastolic ({blood_pressure_diastolic} mmHg)"
          f" blood pressure equal or higher than its upper thresholds ({HIGH_SYSTOLIC}/{HIGH_DIASTOLIC} mmHg) "
          f"- hypertension? {is_hypertension}")

    # Ulozte do promenne vysledek logicke operace "Ma normalni krevni tlak (vsechny hodnoty obou tlaku mezi hranicemi)?"
    is_blood_pressure_normal = ((LOW_SYSTOLIC < blood_pressure_systolic < HIGH_SYSTOLIC) and (LOW_DIASTOLIC < blood_pressure_diastolic < HIGH_DIASTOLIC))
    print(f"Is blood pressure ({blood_pressure_systolic}/{blood_pressure_diastolic} mmHg) "
          f"normal? {is_blood_pressure_normal}")

    return is_heart_rate_110, is_heart_rate_normal, is_tachycardia, is_hypertension, is_blood_pressure_normal


if __name__ == "__main__":
    # Do promennych ulozte libovolne namerene hodnoty krevnich tlaku a prumerne tepove frekvence
    blood_pressure_systolic = 120
    blood_pressure_diastolic = 80
    average_heart_rate = 100
    measurement(blood_pressure_systolic, blood_pressure_diastolic, average_heart_rate)
