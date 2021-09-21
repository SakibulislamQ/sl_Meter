''' 1 miter = 39.37007874 inchi
    1 foot = 12 inchi
    1 cm = 0.03280839895 inchi
    1 inchi = 1 inchi
'''

class oupt:
    def __init__(miter, num, froms ,tos):
        miter.num = num
        miter.froms = froms
        miter.tos = tos

    def conv_cm(miter, num, froms, tos):
        if froms == 'meter':
            main_num = num * 39.37007874
        if froms == 'foot':
            main_num = num * 12
        if froms == 'cm':
            main_num = num * 0.03280839895
        if froms == 'inchi':
            main_num = num * 1

    def conv_tos(miter, num, froms, tos):
        if tos == 'meter':
            oupts = main_num / 39.37007874
        if tos == 'foot':
            oupts = main_num / 12
        if tos == 'cm':
            oupts = main_num / 0.03280839895
        if tos == 'inchi':
            oupts = main_num / 1









