# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Linux x86 (64-bit) (January 29, 2022)
# Date: Wed 30 Nov 2022 14:20:50



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

###############################################################
###############################################################
###You may paste your values here##############################
###############################################################
###############################################################
###############################################################
MZp = Parameter(name = 'MZp',
                 nature = 'external',
                 type = 'real',
                 value = 1.0000000000e-01,
                 texname = '\text{MZp}',
                 lhablock = 'MASS',
                 lhacode = [ 9900032 ])
MnH1 = Parameter(name = 'MnH1',
                  nature = 'external',
                  type = 'real',
                  value = 1.4885897292e+02,
                  texname = '\text{MnH1}',
                  lhablock = 'MASS',
                  lhacode = [ 9910012 ])
MnH2 = Parameter(name = 'MnH2',
                  nature = 'external',
                  type = 'real',
                  value = 2.6556925793e+02,
                 texname = '\text{MnH2}',
                  lhablock = 'MASS',
                  lhacode = [ 9910014 ])
MnH3 = Parameter(name = 'MnH3',
                  nature = 'external',
                  type = 'real',
                  value = 3.0984628874e+02,
                  texname = '\text{MnH3}',
                  lhablock = 'MASS',
                  lhacode = [ 9910016 ])
g1p = Parameter(name = 'g1p',
                 nature = 'external',
                 type = 'real',
                 value = 9.0000000000e-04,
                 texname = 'g_p',
                 lhablock = 'LmuLtauINPUTS',
                 lhacode = [ 1 ])
MH2 = Parameter(name = 'MH2',
                 nature = 'external',
                 type = 'real',
                 value = 5.0000000000e+01,
                 texname = '\text{MH2}',
                 lhablock = 'MASS',
                 lhacode = [ 9900026 ])
Sa = Parameter(name = 'Sa',
                nature = 'external',
                type = 'real',
                value = 6.0000000000e-03,
                texname = '\text{Sa}',
                lhablock = 'LmuLtauINPUTS',
                lhacode = [ 3 ])
Mee = Parameter(name = 'Mee',
                 nature = 'external',
                 type = 'real',
                 value = 1.9281569311e+02,
                 texname = '\text{Mee}',
                 lhablock = 'LmuLtauINPUTS',
                 lhacode = [ 4 ])
Vemu = Parameter(name = 'Vemu',
                  nature = 'external',
                  type = 'real',
                  value = 1.2760576309e+02,
                  texname = '\text{Vemu}',
                  lhablock = 'LmuLtauINPUTS',
                  lhacode = [ 5 ])
Vetau = Parameter(name = 'Vetau',
                   nature = 'external',
                   type = 'real',
                   value = 1.8636866934e+02,
                   texname = '\text{Vetau}',
                   lhablock = 'LmuLtauINPUTS',
                   lhacode = [ 6 ])
Mmutau = Parameter(name = 'Mmutau',
                    nature = 'external',
                    type = 'real',
                    value = 1.5728927545e+02,
                    texname = '\text{Mmutau}',
                    lhablock = 'LmuLtauINPUTS',
                    lhacode = [ 7 ])
Ximt = Parameter(name = 'Ximt',
                  nature = 'external',
                  type = 'real',
                  value = 3.1830634288e+00,
                  texname = '\text{Ximt}',
                  lhablock = 'LmuLtauINPUTS',
                  lhacode = [ 8 ])
fe = Parameter(name = 'fe',
                nature = 'external',
                type = 'real',
                value = 1.0865230449e-04,
                texname = '\text{fe}',
                lhablock = 'LmuLtauINPUTS',
                lhacode = [ 9 ])
fmu = Parameter(name = 'fmu',
                 nature = 'external',
                 type = 'real',
                 value = 9.0030220418e-05,
                 texname = '\text{fmu}',
                 lhablock = 'LmuLtauINPUTS',
                 lhacode = [ 10 ])
ftau = Parameter(name = 'ftau',
                  nature = 'external',
                  type = 'real',
                  value = 1.0770791242e-04,
                  texname = '\text{ftau}',
                  lhablock = 'LmuLtauINPUTS',
                  lhacode = [ 11 ])
WRROT11 = Parameter(name = 'WRROT11',
                     nature = 'external',
                     type = 'real',
                     value = 1.81933130722723046535e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 1 ])
WRROT12 = Parameter(name = 'WRROT12',
                     nature = 'external',
                     type = 'real',
                     value = -3.95434336846753775596e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 2 ])
WRROT13 = Parameter(name = 'WRROT13',
                     nature = 'external',
                     type = 'real',
                     value = -3.01428639167629916842e-03,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 3 ])
WRROT14 = Parameter(name = 'WRROT14',
                     nature = 'external',
                     type = 'real',
                     value = 1.43614861171581298160e-07,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 4 ])
WRROT15 = Parameter(name = 'WRROT15',
                     nature = 'external',
                     type = 'real',
                     value = 2.02670135216064884172e-08,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 5 ])
WRROT16 = Parameter(name = 'WRROT16',
                     nature = 'external',
                     type = 'real',
                     value = -3.07007435017378317393e-07,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 6 ])
WRROT21 = Parameter(name = 'WRROT21',
                     nature = 'external',
                     type = 'real',
                     value = -2.65231989717465976852e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 7 ])
WRROT22 = Parameter(name = 'WRROT22',
                     nature = 'external',
                     type = 'real',
                     value = 5.62041092092284366721e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 8 ])
WRROT23 = Parameter(name = 'WRROT23',
                     nature = 'external',
                     type = 'real',
                     value = 1.92239723519942694308e-02,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 9 ])
WRROT24 = Parameter(name = 'WRROT24',
                     nature = 'external',
                     type = 'real',
                     value = 4.75691601089045692561e-07,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 10 ])
WRROT25 = Parameter(name = 'WRROT25',
                     nature = 'external',
                     type = 'real',
                     value = -2.25426566908159031737e-09,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 11 ])
WRROT26 = Parameter(name = 'WRROT26',
                     nature = 'external',
                     type = 'real',
                     value = -3.66945152682995186857e-08,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 12 ])
WRROT31 = Parameter(name = 'WRROT31',
                     nature = 'external',
                     type = 'real',
                     value = -2.73994219964435736792e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 13 ])
WRROT32 = Parameter(name = 'WRROT32',
                     nature = 'external',
                     type = 'real',
                     value = 5.90828757884667377098e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 14 ])
WRROT33 = Parameter(name = 'WRROT33',
                     nature = 'external',
                     type = 'real',
                     value = -9.64375988439699315113e-03,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 15 ])
WRROT34 = Parameter(name = 'WRROT34',
                     nature = 'external',
                     type = 'real',
                     value = -4.23235146467605112188e-07,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 16 ])
WRROT35 = Parameter(name = 'WRROT35',
                     nature = 'external',
                     type = 'real',
                     value = 9.68950933613735721978e-09,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 17 ])
WRROT36 = Parameter(name = 'WRROT36',
                     nature = 'external',
                     type = 'real',
                     value = -1.61052445034202586275e-07,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 18 ])
WRROT41 = Parameter(name = 'WRROT41',
                     nature = 'external',
                     type = 'real',
                     value = 6.27878764381199896627e-08,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 19 ])
WRROT42 = Parameter(name = 'WRROT42',
                     nature = 'external',
                     type = 'real',
                     value = -1.39965045767957737225e-07,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 20 ])
WRROT43 = Parameter(name = 'WRROT43',
                     nature = 'external',
                     type = 'real',
                     value = -1.74344833914540627093e-09,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 21 ])
WRROT44 = Parameter(name = 'WRROT44',
                     nature = 'external',
                     type = 'real',
                     value = 1.96759386099790239966e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 22 ])
WRROT45 = Parameter(name = 'WRROT45',
                     nature = 'external',
                     type = 'real',
                     value = 4.95368760610668396049e-02,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 23 ])
WRROT46 = Parameter(name = 'WRROT46',
                     nature = 'external',
                     type = 'real',
                     value = -8.75500200370875059086e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 24 ])
WRROT51 = Parameter(name = 'WRROT51',
                     nature = 'external',
                     type = 'real',
                     value = -1.10469028300161414871e-07,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 25 ])
WRROT52 = Parameter(name = 'WRROT52',
                     nature = 'external',
                     type = 'real',
                     value = 2.40084382611815527827e-07,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 26 ])
WRROT53 = Parameter(name = 'WRROT53',
                     nature = 'external',
                     type = 'real',
                     value = 1.34189437403018850435e-08,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 27 ])
WRROT54 = Parameter(name = 'WRROT54',
                     nature = 'external',
                     type = 'real',
                     value = 7.86524378568503435005e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 28 ])
WRROT55 = Parameter(name = 'WRROT55',
                     nature = 'external',
                     type = 'real',
                     value = -6.64958564074994741555e-03,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 29 ])
WRROT56 = Parameter(name = 'WRROT56',
                     nature = 'external',
                     type = 'real',
                     value = -1.26287143585540467816e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 30 ])
WRROT61 = Parameter(name = 'WRROT61',
                     nature = 'external',
                     type = 'real',
                     value = -9.53886575491846056224e-08,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 31 ])
WRROT62 = Parameter(name = 'WRROT62',
                     nature = 'external',
                     type = 'real',
                     value = 2.10959055384558560654e-07,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 32 ])
WRROT63 = Parameter(name = 'WRROT63',
                     nature = 'external',
                     type = 'real',
                     value = -5.62681054050889956322e-09,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 33 ])
WRROT64 = Parameter(name = 'WRROT64',
                     nature = 'external',
                     type = 'real',
                     value = -5.84937056115111264631e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 34 ])
WRROT65 = Parameter(name = 'WRROT65',
                     nature = 'external',
                     type = 'real',
                     value = 2.38908706560617550840e-02,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 35 ])
WRROT66 = Parameter(name = 'WRROT66',
                     nature = 'external',
                     type = 'real',
                     value = -4.63303960379752410859e-01,
                     texname = '\text{IWRROT}',
                     lhablock = 'WRROT',
                     lhacode = [ 36 ])
IWRROT11 = Parameter(name = 'IWRROT11',
                     nature = 'external',
                     type = 'real',
                     value = -8.03262939126245689714e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 1 ])
IWRROT12 = Parameter(name = 'IWRROT12',
                     nature = 'external',
                     type = 'real',
                     value = -3.78338136180546791287e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 2 ])
IWRROT13 = Parameter(name = 'IWRROT13',
                     nature = 'external',
                     type = 'real',
                     value = -1.48834944159963344923e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 3 ])
IWRROT14 = Parameter(name = 'IWRROT14',
                     nature = 'external',
                     type = 'real',
                     value = -2.79257284152470918409e-09,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 4 ])
IWRROT15 = Parameter(name = 'IWRROT15',
                     nature = 'external',
                     type = 'real',
                     value = -1.79200586597511888654e-07,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 5 ])
IWRROT16 = Parameter(name = 'IWRROT16',
                     nature = 'external',
                     type = 'real',
                     value = -7.59346000169397155211e-09,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 6 ])
IWRROT21 = Parameter(name = 'IWRROT21',
                     nature = 'external',
                     type = 'real',
                     value = -1.65315426643844909371e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 7 ])
IWRROT22 = Parameter(name = 'IWRROT22',
                     nature = 'external',
                     type = 'real',
                     value = -6.40437862563465742927e-02,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 8 ])
IWRROT23 = Parameter(name = 'IWRROT23',
                     nature = 'external',
                     type = 'real',
                     value = -7.62863975078439615629e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 9 ])
IWRROT24 = Parameter(name = 'IWRROT24',
                     nature = 'external',
                     type = 'real',
                     value = 1.27462022356796370475e-08,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 10 ])
IWRROT25 = Parameter(name = 'IWRROT25',
                     nature = 'external',
                     type = 'real',
                     value = 2.04435806320524628551e-07,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 11 ])
IWRROT26 = Parameter(name = 'IWRROT26',
                     nature = 'external',
                     type = 'real',
                     value = 1.04149816903904394146e-08,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 12 ])
IWRROT31 = Parameter(name = 'IWRROT31',
                     nature = 'external',
                     type = 'real',
                     value = -3.85900188315226266855e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 13 ])
IWRROT32 = Parameter(name = 'IWRROT32',
                     nature = 'external',
                     type = 'real',
                     value = -1.77261171867891226261e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 14 ])
IWRROT33 = Parameter(name = 'IWRROT33',
                     nature = 'external',
                     type = 'real',
                     value = 6.28820376406368675148e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 15 ])
IWRROT34 = Parameter(name = 'IWRROT34',
                     nature = 'external',
                     type = 'real',
                     value = -5.36569043306556770411e-09,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 16 ])
IWRROT35 = Parameter(name = 'IWRROT35',
                     nature = 'external',
                     type = 'real',
                     value = 2.69462651360876918272e-07,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 17 ])
IWRROT36 = Parameter(name = 'IWRROT36',
                     nature = 'external',
                     type = 'real',
                     value = 1.17712935746992426050e-08,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 18 ])
IWRROT41 = Parameter(name = 'IWRROT41',
                     nature = 'external',
                     type = 'real',
                     value = 2.77218195327186017683e-07,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 19 ])
IWRROT42 = Parameter(name = 'IWRROT42',
                     nature = 'external',
                     type = 'real',
                     value = 1.33913799617245034502e-07,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 20 ])
IWRROT43 = Parameter(name = 'IWRROT43',
                     nature = 'external',
                     type = 'real',
                     value = 8.60853955082215647547e-08,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 21 ])
IWRROT44 = Parameter(name = 'IWRROT44',
                     nature = 'external',
                     type = 'real',
                     value = 3.82596141830238633749e-03,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 22 ])
IWRROT45 = Parameter(name = 'IWRROT45',
                     nature = 'external',
                     type = 'real',
                     value = 4.38004210086893219778e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 23 ])
IWRROT46 = Parameter(name = 'IWRROT46',
                     nature = 'external',
                     type = 'real',
                     value = 2.16544454456458236591e-02,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 24 ])
IWRROT51 = Parameter(name = 'IWRROT51',
                     nature = 'external',
                     type = 'real',
                     value = 6.88538157249656987147e-08,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 25 ])
IWRROT52 = Parameter(name = 'IWRROT52',
                     nature = 'external',
                     type = 'real',
                     value = 2.73572752950152787358e-08,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 26 ])
IWRROT53 = Parameter(name = 'IWRROT53',
                     nature = 'external',
                     type = 'real',
                     value = 5.32503302420671075687e-07,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 27 ])
IWRROT54 = Parameter(name = 'IWRROT54',
                     nature = 'external',
                     type = 'real',
                     value = -2.10749964253621469013e-02,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 28 ])
IWRROT55 = Parameter(name = 'IWRROT55',
                     nature = 'external',
                     type = 'real',
                     value = -6.03040458278379931656e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 29 ])
IWRROT56 = Parameter(name = 'IWRROT56',
                     nature = 'external',
                     type = 'real',
                     value = -3.58440022591428666954e-02,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 30 ])
IWRROT61 = Parameter(name = 'IWRROT61',
                     nature = 'external',
                     type = 'real',
                     value = 1.34347727905147767279e-07,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 31 ])
IWRROT62 = Parameter(name = 'IWRROT62',
                     nature = 'external',
                     type = 'real',
                     value = 6.32921957074215766973e-08,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 32 ])
IWRROT63 = Parameter(name = 'IWRROT63',
                     nature = 'external',
                     type = 'real',
                     value = -3.66895605496661079078e-07,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 33 ])
IWRROT64 = Parameter(name = 'IWRROT64',
                     nature = 'external',
                     type = 'real',
                     value = 7.41571486238215126646e-03,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 34 ])
IWRROT65 = Parameter(name = 'IWRROT65',
                     nature = 'external',
                     type = 'real',
                     value = -6.64398694193194971902e-01,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 35 ])
IWRROT66 = Parameter(name = 'IWRROT66',
                     nature = 'external',
                     type = 'real',
                     value = -3.38628012185279506086e-02,
                         texname = '\text{IWRROT}',
                     lhablock = 'IWRROT',
                     lhacode = [ 36 ])
###############################################################
###############################################################
###Do not change the values below##############################
###############################################################
###############################################################
###############################################################
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.952,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1179,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])


MnL1 = Parameter(name = 'MnL1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{MnL1}',
                 lhablock = 'MASS',
                 lhacode = [ 12 ])

MnL2 = Parameter(name = 'MnL2',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{MnL2}',
                 lhablock = 'MASS',
                 lhacode = [ 14 ])

MnL3 = Parameter(name = 'MnL3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{MnL3}',
                 lhablock = 'MASS',
                 lhacode = [ 16 ])


Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH1 = Parameter(name = 'MH1',
                nature = 'external',
                type = 'real',
                value = 125.25,
                texname = '\\text{MH1}',
                lhablock = 'MASS',
                lhacode = [ 25 ])


WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WZp = Parameter(name = 'WZp',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WZp}',
                lhablock = 'DECAY',
                lhacode = [ 9900032 ])

WnH1 = Parameter(name = 'WnH1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WnH1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9910012 ])

WnH2 = Parameter(name = 'WnH2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WnH2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9910014 ])

WnH3 = Parameter(name = 'WnH3',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WnH3}',
                 lhablock = 'DECAY',
                 lhacode = [ 9910016 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.0032,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WH2 = Parameter(name = 'WH2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WH2}',
                lhablock = 'DECAY',
                lhacode = [ 9900026 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

xev = Parameter(name = 'xev',
                nature = 'internal',
                type = 'real',
                value = 'MZp/g1p',
                texname = '\\text{xev}')

Ca = Parameter(name = 'Ca',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - Sa**2)',
               texname = '\\text{Ca}')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

WRROTATION1x1 = Parameter(name = 'WRROTATION1x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT11 + WRROT11',
                          texname = '\\text{WRROTATION1x1}')

WRROTATION1x2 = Parameter(name = 'WRROTATION1x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT12 + WRROT12',
                          texname = '\\text{WRROTATION1x2}')

WRROTATION1x3 = Parameter(name = 'WRROTATION1x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT13 + WRROT13',
                          texname = '\\text{WRROTATION1x3}')

WRROTATION1x4 = Parameter(name = 'WRROTATION1x4',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT14 + WRROT14',
                          texname = '\\text{WRROTATION1x4}')

WRROTATION1x5 = Parameter(name = 'WRROTATION1x5',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT15 + WRROT15',
                          texname = '\\text{WRROTATION1x5}')

WRROTATION1x6 = Parameter(name = 'WRROTATION1x6',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT16 + WRROT16',
                          texname = '\\text{WRROTATION1x6}')

WRROTATION2x1 = Parameter(name = 'WRROTATION2x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT21 + WRROT21',
                          texname = '\\text{WRROTATION2x1}')

WRROTATION2x2 = Parameter(name = 'WRROTATION2x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT22 + WRROT22',
                          texname = '\\text{WRROTATION2x2}')

WRROTATION2x3 = Parameter(name = 'WRROTATION2x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT23 + WRROT23',
                          texname = '\\text{WRROTATION2x3}')

WRROTATION2x4 = Parameter(name = 'WRROTATION2x4',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT24 + WRROT24',
                          texname = '\\text{WRROTATION2x4}')

WRROTATION2x5 = Parameter(name = 'WRROTATION2x5',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT25 + WRROT25',
                          texname = '\\text{WRROTATION2x5}')

WRROTATION2x6 = Parameter(name = 'WRROTATION2x6',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT26 + WRROT26',
                          texname = '\\text{WRROTATION2x6}')

WRROTATION3x1 = Parameter(name = 'WRROTATION3x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT31 + WRROT31',
                          texname = '\\text{WRROTATION3x1}')

WRROTATION3x2 = Parameter(name = 'WRROTATION3x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT32 + WRROT32',
                          texname = '\\text{WRROTATION3x2}')

WRROTATION3x3 = Parameter(name = 'WRROTATION3x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT33 + WRROT33',
                          texname = '\\text{WRROTATION3x3}')

WRROTATION3x4 = Parameter(name = 'WRROTATION3x4',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT34 + WRROT34',
                          texname = '\\text{WRROTATION3x4}')

WRROTATION3x5 = Parameter(name = 'WRROTATION3x5',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT35 + WRROT35',
                          texname = '\\text{WRROTATION3x5}')

WRROTATION3x6 = Parameter(name = 'WRROTATION3x6',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT36 + WRROT36',
                          texname = '\\text{WRROTATION3x6}')

WRROTATION4x1 = Parameter(name = 'WRROTATION4x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT41 + WRROT41',
                          texname = '\\text{WRROTATION4x1}')

WRROTATION4x2 = Parameter(name = 'WRROTATION4x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT42 + WRROT42',
                          texname = '\\text{WRROTATION4x2}')

WRROTATION4x3 = Parameter(name = 'WRROTATION4x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT43 + WRROT43',
                          texname = '\\text{WRROTATION4x3}')

WRROTATION4x4 = Parameter(name = 'WRROTATION4x4',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT44 + WRROT44',
                          texname = '\\text{WRROTATION4x4}')

WRROTATION4x5 = Parameter(name = 'WRROTATION4x5',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT45 + WRROT45',
                          texname = '\\text{WRROTATION4x5}')

WRROTATION4x6 = Parameter(name = 'WRROTATION4x6',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT46 + WRROT46',
                          texname = '\\text{WRROTATION4x6}')

WRROTATION5x1 = Parameter(name = 'WRROTATION5x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT51 + WRROT51',
                          texname = '\\text{WRROTATION5x1}')

WRROTATION5x2 = Parameter(name = 'WRROTATION5x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT52 + WRROT52',
                          texname = '\\text{WRROTATION5x2}')

WRROTATION5x3 = Parameter(name = 'WRROTATION5x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT53 + WRROT53',
                          texname = '\\text{WRROTATION5x3}')

WRROTATION5x4 = Parameter(name = 'WRROTATION5x4',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT54 + WRROT54',
                          texname = '\\text{WRROTATION5x4}')

WRROTATION5x5 = Parameter(name = 'WRROTATION5x5',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT55 + WRROT55',
                          texname = '\\text{WRROTATION5x5}')

WRROTATION5x6 = Parameter(name = 'WRROTATION5x6',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT56 + WRROT56',
                          texname = '\\text{WRROTATION5x6}')

WRROTATION6x1 = Parameter(name = 'WRROTATION6x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT61 + WRROT61',
                          texname = '\\text{WRROTATION6x1}')

WRROTATION6x2 = Parameter(name = 'WRROTATION6x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT62 + WRROT62',
                          texname = '\\text{WRROTATION6x2}')

WRROTATION6x3 = Parameter(name = 'WRROTATION6x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT63 + WRROT63',
                          texname = '\\text{WRROTATION6x3}')

WRROTATION6x4 = Parameter(name = 'WRROTATION6x4',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT64 + WRROT64',
                          texname = '\\text{WRROTATION6x4}')

WRROTATION6x5 = Parameter(name = 'WRROTATION6x5',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT65 + WRROT65',
                          texname = '\\text{WRROTATION6x5}')

WRROTATION6x6 = Parameter(name = 'WRROTATION6x6',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complex(0,1)*IWRROT66 + WRROT66',
                          texname = '\\text{WRROTATION6x6}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2 + 2*cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))/cmath.sqrt(2)',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

lam2 = Parameter(name = 'lam2',
                 nature = 'internal',
                 type = 'real',
                 value = '(Ca**2*MH2**2)/(2.*xev**2) + (MH1**2*Sa**2)/(2.*xev**2)',
                 texname = '\\text{lam2}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'real',
                 value = '(Ca**2*MH1**2)/(2.*vev**2) + (MH2**2*Sa**2)/(2.*vev**2)',
                 texname = '\\text{lam1}')

lam3 = Parameter(name = 'lam3',
                 nature = 'internal',
                 type = 'real',
                 value = '(Ca*(-MH1**2 + MH2**2)*Sa)/(vev*xev)',
                 texname = '\\text{lam3}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ynd1 = Parameter(name = 'ynd1',
                 nature = 'internal',
                 type = 'real',
                 value = '(fe*cmath.sqrt(2))/vev',
                 texname = 'y_{\\text{nd1}}')

ynd2 = Parameter(name = 'ynd2',
                 nature = 'internal',
                 type = 'real',
                 value = '(fmu*cmath.sqrt(2))/vev',
                 texname = 'y_{\\text{nd2}}')

ynd3 = Parameter(name = 'ynd3',
                 nature = 'internal',
                 type = 'real',
                 value = '(ftau*cmath.sqrt(2))/vev',
                 texname = 'y_{\\text{nd3}}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

mu2H1 = Parameter(name = 'mu2H1',
                  nature = 'internal',
                  type = 'real',
                  value = '-(lam1*vev**2) - (lam3*xev**2)/2.',
                  texname = '\\mu')

mu2H2 = Parameter(name = 'mu2H2',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.5*(lam3*vev**2) - lam2*xev**2',
                  texname = '\\text{$\\mu $prime}')

