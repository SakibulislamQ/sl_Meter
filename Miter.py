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
        if num == 'meter':
            main_num = num * 39.37007874
        if num == 'foot':
            main_num = num * 12
        if num == 'cm':
            main_num = num * 0.03280839895
        if num == 'meter':
            main_num = num * 1
