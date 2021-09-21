''' 1 miter = 39.37007874 inchi
    1 foot = 12 inchi
    1 cm = 0.03280839895 inchi
    1 inchi = 1 inchi
'''

class Oupt:
    def __init__(miter, num, froms ,tos):
        miter.num = num
        miter.froms = froms
        miter.tos = tos

    def conv_cm(miter):
        if miter.froms == 'meter':
            main_num = miter.num * 39.37007874
            return main_num
        if miter.froms == 'foot':
            main_num = miter.num * 12
            return main_num
        if miter.froms == 'cm':
            main_num = miter.num * 0.03280839895
            return main_num
        if miter.froms == 'inchi':
            main_num = miter.num * 1
            return main_num

    def conv_tos(miter, main_num):
        if miter.tos == 'meter':
            oupts = main_num / 39.37007874
            return oupts
        if miter.tos == 'foot':
            oupts = main_num / 12
            return oupts
        if miter.tos == 'cm':
            oupts = main_num / 0.03280839895
            return oupts
        if miter.tos == 'inchi':
            oupts = main_num / 1
            return oupts
    

mit = Oupt(50,'foot', 'meter')
def out_put():
    asas = mit.conv_tos(mit.conv_cm())
    print(asas)
out_put()










