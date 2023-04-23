# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Linux x86 (64-bit) (January 29, 2022)
# Date: Wed 30 Nov 2022 14:20:50


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '-0.5*(Ca*ee**2)/cw',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '(Ca*ee**2)/(2.*cw)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-G',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*g1p)',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'complex(0,1)*g1p',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(Ca*g1p)',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '2*complex(0,1)*g1p**2',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '2*Ca**2*complex(0,1)*g1p**2',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-2*complex(0,1)*lam1',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '-4*complex(0,1)*lam1',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-6*complex(0,1)*lam1',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-6*complex(0,1)*lam2',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(complex(0,1)*lam3)',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-0.5*(ee**2*Sa)/cw',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(ee**2*Sa)/(2.*cw)',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = 'g1p*Sa',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-2*Ca*complex(0,1)*g1p**2*Sa',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '2*complex(0,1)*g1p**2*Sa**2',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '2*Ca*complex(0,1)*lam2*Sa - Ca*complex(0,1)*lam3*Sa',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-2*Ca*complex(0,1)*lam1*Sa + Ca*complex(0,1)*lam3*Sa',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '-(Ca**2*complex(0,1)*lam3) - 2*complex(0,1)*lam1*Sa**2',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-(Ca**2*complex(0,1)*lam3) - 2*complex(0,1)*lam2*Sa**2',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-2*Ca**2*complex(0,1)*lam1 - complex(0,1)*lam3*Sa**2',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-2*Ca**2*complex(0,1)*lam2 - complex(0,1)*lam3*Sa**2',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '-6*Ca**3*complex(0,1)*lam1*Sa + 3*Ca**3*complex(0,1)*lam3*Sa + 6*Ca*complex(0,1)*lam2*Sa**3 - 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '6*Ca**3*complex(0,1)*lam2*Sa - 3*Ca**3*complex(0,1)*lam3*Sa - 6*Ca*complex(0,1)*lam1*Sa**3 + 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '-6*Ca**4*complex(0,1)*lam2 - 6*Ca**2*complex(0,1)*lam3*Sa**2 - 6*complex(0,1)*lam1*Sa**4',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-6*Ca**4*complex(0,1)*lam1 - 6*Ca**2*complex(0,1)*lam3*Sa**2 - 6*complex(0,1)*lam2*Sa**4',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-(Ca**4*complex(0,1)*lam3) - 6*Ca**2*complex(0,1)*lam1*Sa**2 - 6*Ca**2*complex(0,1)*lam2*Sa**2 + 4*Ca**2*complex(0,1)*lam3*Sa**2 - complex(0,1)*lam3*Sa**4',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(Ca**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(Ca*ee**2*complex(0,1)*Sa)/(2.*sw**2)',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(ee**2*complex(0,1)*Sa**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '-0.5*(ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-0.5*(Ca*ee)/sw',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-0.5*(ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '-0.5*(Ca*ee**2)/sw',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(Ca*ee**2)/(2.*sw)',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '-0.5*(ee*Sa)/sw',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-0.5*(ee**2*Sa)/sw',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee**2*Sa)/(2.*sw)',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-0.5*(Ca*cw*ee)/sw - (Ca*ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '-0.5*(cw*ee*Sa)/sw - (ee*Sa*sw)/(2.*cw)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = 'Ca**2*ee**2*complex(0,1) + (Ca**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (Ca**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = 'Ca*ee**2*complex(0,1)*Sa + (Ca*cw**2*ee**2*complex(0,1)*Sa)/(2.*sw**2) + (Ca*ee**2*complex(0,1)*Sa*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = 'ee**2*complex(0,1)*Sa**2 + (cw**2*ee**2*complex(0,1)*Sa**2)/(2.*sw**2) + (ee**2*complex(0,1)*Sa**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-0.5*(ee**2*vev)/cw',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(ee**2*vev)/(2.*cw)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(Ca*ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee**2*complex(0,1)*Sa*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-0.5*(ee**2*vev)/sw',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = 'Ca*ee**2*complex(0,1)*vev + (Ca*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (Ca*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = 'ee**2*complex(0,1)*Sa*vev + (cw**2*ee**2*complex(0,1)*Sa*vev)/(2.*sw**2) + (ee**2*complex(0,1)*Sa*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(ee*complex(0,1)*WRROTATION1x1)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(ee*complex(0,1)*WRROTATION1x2)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(ee*complex(0,1)*WRROTATION1x3)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(ee*complex(0,1)*WRROTATION1x4)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(ee*complex(0,1)*WRROTATION1x5)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(ee*complex(0,1)*WRROTATION1x6)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(ee*complex(0,1)*WRROTATION2x1)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee*complex(0,1)*WRROTATION2x2)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(ee*complex(0,1)*WRROTATION2x3)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee*complex(0,1)*WRROTATION2x4)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(ee*complex(0,1)*WRROTATION2x5)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ee*complex(0,1)*WRROTATION2x6)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(ee*complex(0,1)*WRROTATION3x1)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(ee*complex(0,1)*WRROTATION3x2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(ee*complex(0,1)*WRROTATION3x3)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(ee*complex(0,1)*WRROTATION3x4)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(ee*complex(0,1)*WRROTATION3x5)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(ee*complex(0,1)*WRROTATION3x6)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '2*Ca*complex(0,1)*g1p**2*xev',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-2*complex(0,1)*g1p**2*Sa*xev',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(complex(0,1)*lam3*Sa*vev) - 2*Ca*complex(0,1)*lam2*xev',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-2*complex(0,1)*lam1*Sa*vev - Ca*complex(0,1)*lam3*xev',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(Ca*complex(0,1)*lam3*vev) + 2*complex(0,1)*lam2*Sa*xev',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-2*Ca*complex(0,1)*lam1*vev + complex(0,1)*lam3*Sa*xev',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-6*Ca**2*complex(0,1)*lam1*Sa*vev + 2*Ca**2*complex(0,1)*lam3*Sa*vev - complex(0,1)*lam3*Sa**3*vev - Ca**3*complex(0,1)*lam3*xev - 6*Ca*complex(0,1)*lam2*Sa**2*xev + 2*Ca*complex(0,1)*lam3*Sa**2*xev',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-3*Ca**2*complex(0,1)*lam3*Sa*vev - 6*complex(0,1)*lam1*Sa**3*vev - 6*Ca**3*complex(0,1)*lam2*xev - 3*Ca*complex(0,1)*lam3*Sa**2*xev',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-6*Ca**3*complex(0,1)*lam1*vev - 3*Ca*complex(0,1)*lam3*Sa**2*vev + 3*Ca**2*complex(0,1)*lam3*Sa*xev + 6*complex(0,1)*lam2*Sa**3*xev',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-(Ca**3*complex(0,1)*lam3*vev) - 6*Ca*complex(0,1)*lam1*Sa**2*vev + 2*Ca*complex(0,1)*lam3*Sa**2*vev + 6*Ca**2*complex(0,1)*lam2*Sa*xev - 2*Ca**2*complex(0,1)*lam3*Sa*xev + complex(0,1)*lam3*Sa**3*xev',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((Ca*complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((complex(0,1)*Sa*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-((Ca*complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((complex(0,1)*Sa*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((Ca*complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-((complex(0,1)*Sa*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((Ca*complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-((complex(0,1)*Sa*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-((Ca*complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((complex(0,1)*Sa*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(2*complex(0,1)*Sa*Vemu*WRROTATION4x1*WRROTATION5x1)/xev + (2*complex(0,1)*Sa*Vetau*WRROTATION4x1*WRROTATION6x1)/xev - Ca*complex(0,1)*WRROTATION1x1*WRROTATION4x1*ynd1*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION2x1*WRROTATION5x1*ynd2*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION3x1*WRROTATION6x1*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(-2*Ca*complex(0,1)*Vemu*WRROTATION4x1*WRROTATION5x1)/xev - (2*Ca*complex(0,1)*Vetau*WRROTATION4x1*WRROTATION6x1)/xev - complex(0,1)*Sa*WRROTATION1x1*WRROTATION4x1*ynd1*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION2x1*WRROTATION5x1*ynd2*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION3x1*WRROTATION6x1*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x2*WRROTATION5x1)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x1*WRROTATION5x2)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x2*WRROTATION6x1)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x1*WRROTATION6x2)/xev - (Ca*complex(0,1)*WRROTATION1x2*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x1*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x2*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x1*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x2*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x1*WRROTATION6x2*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x2*WRROTATION5x1)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x1*WRROTATION5x2)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x2*WRROTATION6x1)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x1*WRROTATION6x2)/xev - (complex(0,1)*Sa*WRROTATION1x2*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x1*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x2*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x1*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x2*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x1*WRROTATION6x2*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(2*complex(0,1)*Sa*Vemu*WRROTATION4x2*WRROTATION5x2)/xev + (2*complex(0,1)*Sa*Vetau*WRROTATION4x2*WRROTATION6x2)/xev - Ca*complex(0,1)*WRROTATION1x2*WRROTATION4x2*ynd1*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION2x2*WRROTATION5x2*ynd2*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION3x2*WRROTATION6x2*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(-2*Ca*complex(0,1)*Vemu*WRROTATION4x2*WRROTATION5x2)/xev - (2*Ca*complex(0,1)*Vetau*WRROTATION4x2*WRROTATION6x2)/xev - complex(0,1)*Sa*WRROTATION1x2*WRROTATION4x2*ynd1*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION2x2*WRROTATION5x2*ynd2*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION3x2*WRROTATION6x2*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x3*WRROTATION5x1)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x1*WRROTATION5x3)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x3*WRROTATION6x1)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x1*WRROTATION6x3)/xev - (Ca*complex(0,1)*WRROTATION1x3*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x1*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x3*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x1*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x3*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x1*WRROTATION6x3*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x3*WRROTATION5x1)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x1*WRROTATION5x3)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x3*WRROTATION6x1)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x1*WRROTATION6x3)/xev - (complex(0,1)*Sa*WRROTATION1x3*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x1*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x3*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x1*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x3*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x1*WRROTATION6x3*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x3*WRROTATION5x2)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x2*WRROTATION5x3)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x3*WRROTATION6x2)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x2*WRROTATION6x3)/xev - (Ca*complex(0,1)*WRROTATION1x3*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x2*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x3*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x2*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x3*WRROTATION6x2*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x2*WRROTATION6x3*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x3*WRROTATION5x2)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x2*WRROTATION5x3)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x3*WRROTATION6x2)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x2*WRROTATION6x3)/xev - (complex(0,1)*Sa*WRROTATION1x3*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x2*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x3*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x2*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x3*WRROTATION6x2*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x2*WRROTATION6x3*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(2*complex(0,1)*Sa*Vemu*WRROTATION4x3*WRROTATION5x3)/xev + (2*complex(0,1)*Sa*Vetau*WRROTATION4x3*WRROTATION6x3)/xev - Ca*complex(0,1)*WRROTATION1x3*WRROTATION4x3*ynd1*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION2x3*WRROTATION5x3*ynd2*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION3x3*WRROTATION6x3*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(-2*Ca*complex(0,1)*Vemu*WRROTATION4x3*WRROTATION5x3)/xev - (2*Ca*complex(0,1)*Vetau*WRROTATION4x3*WRROTATION6x3)/xev - complex(0,1)*Sa*WRROTATION1x3*WRROTATION4x3*ynd1*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION2x3*WRROTATION5x3*ynd2*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION3x3*WRROTATION6x3*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x4*WRROTATION5x1)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x1*WRROTATION5x4)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x4*WRROTATION6x1)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x1*WRROTATION6x4)/xev - (Ca*complex(0,1)*WRROTATION1x4*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x1*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x4*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x1*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x4*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x1*WRROTATION6x4*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x4*WRROTATION5x1)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x1*WRROTATION5x4)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x4*WRROTATION6x1)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x1*WRROTATION6x4)/xev - (complex(0,1)*Sa*WRROTATION1x4*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x1*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x4*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x1*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x4*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x1*WRROTATION6x4*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x4*WRROTATION5x2)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x2*WRROTATION5x4)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x4*WRROTATION6x2)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x2*WRROTATION6x4)/xev - (Ca*complex(0,1)*WRROTATION1x4*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x2*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x4*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x2*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x4*WRROTATION6x2*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x2*WRROTATION6x4*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x4*WRROTATION5x2)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x2*WRROTATION5x4)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x4*WRROTATION6x2)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x2*WRROTATION6x4)/xev - (complex(0,1)*Sa*WRROTATION1x4*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x2*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x4*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x2*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x4*WRROTATION6x2*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x2*WRROTATION6x4*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x4*WRROTATION5x3)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x3*WRROTATION5x4)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x4*WRROTATION6x3)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x3*WRROTATION6x4)/xev - (Ca*complex(0,1)*WRROTATION1x4*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x3*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x4*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x3*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x4*WRROTATION6x3*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x3*WRROTATION6x4*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x4*WRROTATION5x3)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x3*WRROTATION5x4)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x4*WRROTATION6x3)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x3*WRROTATION6x4)/xev - (complex(0,1)*Sa*WRROTATION1x4*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x3*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x4*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x3*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x4*WRROTATION6x3*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x3*WRROTATION6x4*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(2*complex(0,1)*Sa*Vemu*WRROTATION4x4*WRROTATION5x4)/xev + (2*complex(0,1)*Sa*Vetau*WRROTATION4x4*WRROTATION6x4)/xev - Ca*complex(0,1)*WRROTATION1x4*WRROTATION4x4*ynd1*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION2x4*WRROTATION5x4*ynd2*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION3x4*WRROTATION6x4*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(-2*Ca*complex(0,1)*Vemu*WRROTATION4x4*WRROTATION5x4)/xev - (2*Ca*complex(0,1)*Vetau*WRROTATION4x4*WRROTATION6x4)/xev - complex(0,1)*Sa*WRROTATION1x4*WRROTATION4x4*ynd1*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION2x4*WRROTATION5x4*ynd2*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION3x4*WRROTATION6x4*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x5*WRROTATION5x1)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x1*WRROTATION5x5)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x5*WRROTATION6x1)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x1*WRROTATION6x5)/xev - (Ca*complex(0,1)*WRROTATION1x5*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x1*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x5*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x1*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x5*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x1*WRROTATION6x5*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x5*WRROTATION5x1)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x1*WRROTATION5x5)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x5*WRROTATION6x1)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x1*WRROTATION6x5)/xev - (complex(0,1)*Sa*WRROTATION1x5*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x1*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x5*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x1*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x5*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x1*WRROTATION6x5*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x5*WRROTATION5x2)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x2*WRROTATION5x5)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x5*WRROTATION6x2)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x2*WRROTATION6x5)/xev - (Ca*complex(0,1)*WRROTATION1x5*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x2*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x5*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x2*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x5*WRROTATION6x2*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x2*WRROTATION6x5*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x5*WRROTATION5x2)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x2*WRROTATION5x5)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x5*WRROTATION6x2)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x2*WRROTATION6x5)/xev - (complex(0,1)*Sa*WRROTATION1x5*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x2*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x5*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x2*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x5*WRROTATION6x2*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x2*WRROTATION6x5*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x5*WRROTATION5x3)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x3*WRROTATION5x5)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x5*WRROTATION6x3)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x3*WRROTATION6x5)/xev - (Ca*complex(0,1)*WRROTATION1x5*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x3*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x5*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x3*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x5*WRROTATION6x3*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x3*WRROTATION6x5*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x5*WRROTATION5x3)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x3*WRROTATION5x5)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x5*WRROTATION6x3)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x3*WRROTATION6x5)/xev - (complex(0,1)*Sa*WRROTATION1x5*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x3*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x5*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x3*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x5*WRROTATION6x3*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x3*WRROTATION6x5*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x5*WRROTATION5x4)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x4*WRROTATION5x5)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x5*WRROTATION6x4)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x4*WRROTATION6x5)/xev - (Ca*complex(0,1)*WRROTATION1x5*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x4*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x5*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x4*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x5*WRROTATION6x4*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x4*WRROTATION6x5*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x5*WRROTATION5x4)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x4*WRROTATION5x5)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x5*WRROTATION6x4)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x4*WRROTATION6x5)/xev - (complex(0,1)*Sa*WRROTATION1x5*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x4*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x5*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x4*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x5*WRROTATION6x4*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x4*WRROTATION6x5*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(2*complex(0,1)*Sa*Vemu*WRROTATION4x5*WRROTATION5x5)/xev + (2*complex(0,1)*Sa*Vetau*WRROTATION4x5*WRROTATION6x5)/xev - Ca*complex(0,1)*WRROTATION1x5*WRROTATION4x5*ynd1*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION2x5*WRROTATION5x5*ynd2*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION3x5*WRROTATION6x5*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(-2*Ca*complex(0,1)*Vemu*WRROTATION4x5*WRROTATION5x5)/xev - (2*Ca*complex(0,1)*Vetau*WRROTATION4x5*WRROTATION6x5)/xev - complex(0,1)*Sa*WRROTATION1x5*WRROTATION4x5*ynd1*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION2x5*WRROTATION5x5*ynd2*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION3x5*WRROTATION6x5*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x6*WRROTATION5x1)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x1*WRROTATION5x6)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x6*WRROTATION6x1)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x1*WRROTATION6x6)/xev - (Ca*complex(0,1)*WRROTATION1x6*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x1*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x6*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x1*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x6*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x1*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x6*WRROTATION5x1)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x1*WRROTATION5x6)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x6*WRROTATION6x1)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x1*WRROTATION6x6)/xev - (complex(0,1)*Sa*WRROTATION1x6*WRROTATION4x1*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x1*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x6*WRROTATION5x1*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x1*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x6*WRROTATION6x1*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x1*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x6*WRROTATION5x2)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x2*WRROTATION5x6)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x6*WRROTATION6x2)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x2*WRROTATION6x6)/xev - (Ca*complex(0,1)*WRROTATION1x6*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x2*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x6*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x2*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x6*WRROTATION6x2*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x2*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x6*WRROTATION5x2)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x2*WRROTATION5x6)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x6*WRROTATION6x2)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x2*WRROTATION6x6)/xev - (complex(0,1)*Sa*WRROTATION1x6*WRROTATION4x2*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x2*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x6*WRROTATION5x2*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x2*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x6*WRROTATION6x2*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x2*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x6*WRROTATION5x3)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x3*WRROTATION5x6)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x6*WRROTATION6x3)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x3*WRROTATION6x6)/xev - (Ca*complex(0,1)*WRROTATION1x6*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x3*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x6*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x3*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x6*WRROTATION6x3*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x3*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x6*WRROTATION5x3)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x3*WRROTATION5x6)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x6*WRROTATION6x3)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x3*WRROTATION6x6)/xev - (complex(0,1)*Sa*WRROTATION1x6*WRROTATION4x3*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x3*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x6*WRROTATION5x3*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x3*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x6*WRROTATION6x3*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x3*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x6*WRROTATION5x4)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x4*WRROTATION5x6)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x6*WRROTATION6x4)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x4*WRROTATION6x6)/xev - (Ca*complex(0,1)*WRROTATION1x6*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x4*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x6*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x4*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x6*WRROTATION6x4*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x4*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x6*WRROTATION5x4)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x4*WRROTATION5x6)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x6*WRROTATION6x4)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x4*WRROTATION6x6)/xev - (complex(0,1)*Sa*WRROTATION1x6*WRROTATION4x4*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x4*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x6*WRROTATION5x4*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x4*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x6*WRROTATION6x4*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x4*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '(complex(0,1)*Sa*Vemu*WRROTATION4x6*WRROTATION5x5)/xev + (complex(0,1)*Sa*Vemu*WRROTATION4x5*WRROTATION5x6)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x6*WRROTATION6x5)/xev + (complex(0,1)*Sa*Vetau*WRROTATION4x5*WRROTATION6x6)/xev - (Ca*complex(0,1)*WRROTATION1x6*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION1x5*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x6*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION2x5*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x6*WRROTATION6x5*ynd3)/cmath.sqrt(2) - (Ca*complex(0,1)*WRROTATION3x5*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-((Ca*complex(0,1)*Vemu*WRROTATION4x6*WRROTATION5x5)/xev) - (Ca*complex(0,1)*Vemu*WRROTATION4x5*WRROTATION5x6)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x6*WRROTATION6x5)/xev - (Ca*complex(0,1)*Vetau*WRROTATION4x5*WRROTATION6x6)/xev - (complex(0,1)*Sa*WRROTATION1x6*WRROTATION4x5*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION1x5*WRROTATION4x6*ynd1)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x6*WRROTATION5x5*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION2x5*WRROTATION5x6*ynd2)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x6*WRROTATION6x5*ynd3)/cmath.sqrt(2) - (complex(0,1)*Sa*WRROTATION3x5*WRROTATION6x6*ynd3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '(2*complex(0,1)*Sa*Vemu*WRROTATION4x6*WRROTATION5x6)/xev + (2*complex(0,1)*Sa*Vetau*WRROTATION4x6*WRROTATION6x6)/xev - Ca*complex(0,1)*WRROTATION1x6*WRROTATION4x6*ynd1*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION2x6*WRROTATION5x6*ynd2*cmath.sqrt(2) - Ca*complex(0,1)*WRROTATION3x6*WRROTATION6x6*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(-2*Ca*complex(0,1)*Vemu*WRROTATION4x6*WRROTATION5x6)/xev - (2*Ca*complex(0,1)*Vetau*WRROTATION4x6*WRROTATION6x6)/xev - complex(0,1)*Sa*WRROTATION1x6*WRROTATION4x6*ynd1*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION2x6*WRROTATION5x6*ynd2*cmath.sqrt(2) - complex(0,1)*Sa*WRROTATION3x6*WRROTATION6x6*ynd3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((Ca*complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-((complex(0,1)*Sa*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((Ca*complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '-((complex(0,1)*Sa*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '-((Ca*complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '-((complex(0,1)*Sa*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-((Ca*complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '-((complex(0,1)*Sa*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION1x4))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION1x5))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION1x6))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION2x4))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION2x5))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION2x6))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x1*complexconjugate(WRROTATION1x1))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION1x1*complexconjugate(WRROTATION1x1))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION2x1*complexconjugate(WRROTATION2x1))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION2x1*complexconjugate(WRROTATION2x1))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION3x1*complexconjugate(WRROTATION3x1))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION3x1*complexconjugate(WRROTATION3x1))/(2.*cw)',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x2*complexconjugate(WRROTATION1x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x2*complexconjugate(WRROTATION1x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x1*complexconjugate(WRROTATION1x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x1*complexconjugate(WRROTATION1x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x2*complexconjugate(WRROTATION2x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x2*complexconjugate(WRROTATION2x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x1*complexconjugate(WRROTATION2x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x1*complexconjugate(WRROTATION2x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x2*complexconjugate(WRROTATION3x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x2*complexconjugate(WRROTATION3x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x1*complexconjugate(WRROTATION3x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x1*complexconjugate(WRROTATION3x2))/(4.*cw)',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x2*complexconjugate(WRROTATION1x2))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION1x2*complexconjugate(WRROTATION1x2))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION2x2*complexconjugate(WRROTATION2x2))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION2x2*complexconjugate(WRROTATION2x2))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION3x2*complexconjugate(WRROTATION3x2))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION3x2*complexconjugate(WRROTATION3x2))/(2.*cw)',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x3*complexconjugate(WRROTATION1x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x3*complexconjugate(WRROTATION1x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x1*complexconjugate(WRROTATION1x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x1*complexconjugate(WRROTATION1x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x3*complexconjugate(WRROTATION2x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x3*complexconjugate(WRROTATION2x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x1*complexconjugate(WRROTATION2x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x1*complexconjugate(WRROTATION2x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x3*complexconjugate(WRROTATION3x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x3*complexconjugate(WRROTATION3x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x1*complexconjugate(WRROTATION3x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x1*complexconjugate(WRROTATION3x3))/(4.*cw)',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x3*complexconjugate(WRROTATION1x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x3*complexconjugate(WRROTATION1x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x2*complexconjugate(WRROTATION1x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x2*complexconjugate(WRROTATION1x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x3*complexconjugate(WRROTATION2x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x3*complexconjugate(WRROTATION2x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x2*complexconjugate(WRROTATION2x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x2*complexconjugate(WRROTATION2x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x3*complexconjugate(WRROTATION3x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x3*complexconjugate(WRROTATION3x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x2*complexconjugate(WRROTATION3x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x2*complexconjugate(WRROTATION3x3))/(4.*cw)',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x3*complexconjugate(WRROTATION1x3))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION1x3*complexconjugate(WRROTATION1x3))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION2x3*complexconjugate(WRROTATION2x3))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION2x3*complexconjugate(WRROTATION2x3))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION3x3*complexconjugate(WRROTATION3x3))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION3x3*complexconjugate(WRROTATION3x3))/(2.*cw)',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION3x4))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x4*complexconjugate(WRROTATION1x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x4*complexconjugate(WRROTATION1x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x1*complexconjugate(WRROTATION1x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x1*complexconjugate(WRROTATION1x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x4*complexconjugate(WRROTATION2x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x4*complexconjugate(WRROTATION2x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x1*complexconjugate(WRROTATION2x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x1*complexconjugate(WRROTATION2x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x4*complexconjugate(WRROTATION3x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x4*complexconjugate(WRROTATION3x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x1*complexconjugate(WRROTATION3x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x1*complexconjugate(WRROTATION3x4))/(4.*cw)',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x4*complexconjugate(WRROTATION1x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x4*complexconjugate(WRROTATION1x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x2*complexconjugate(WRROTATION1x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x2*complexconjugate(WRROTATION1x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x4*complexconjugate(WRROTATION2x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x4*complexconjugate(WRROTATION2x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x2*complexconjugate(WRROTATION2x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x2*complexconjugate(WRROTATION2x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x4*complexconjugate(WRROTATION3x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x4*complexconjugate(WRROTATION3x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x2*complexconjugate(WRROTATION3x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x2*complexconjugate(WRROTATION3x4))/(4.*cw)',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x4*complexconjugate(WRROTATION1x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x4*complexconjugate(WRROTATION1x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x3*complexconjugate(WRROTATION1x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x3*complexconjugate(WRROTATION1x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x4*complexconjugate(WRROTATION2x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x4*complexconjugate(WRROTATION2x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x3*complexconjugate(WRROTATION2x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x3*complexconjugate(WRROTATION2x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x4*complexconjugate(WRROTATION3x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x4*complexconjugate(WRROTATION3x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x3*complexconjugate(WRROTATION3x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x3*complexconjugate(WRROTATION3x4))/(4.*cw)',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x4*complexconjugate(WRROTATION1x4))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION1x4*complexconjugate(WRROTATION1x4))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION2x4*complexconjugate(WRROTATION2x4))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION2x4*complexconjugate(WRROTATION2x4))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION3x4*complexconjugate(WRROTATION3x4))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION3x4*complexconjugate(WRROTATION3x4))/(2.*cw)',
                  order = {'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION3x5))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x5*complexconjugate(WRROTATION1x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x5*complexconjugate(WRROTATION1x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x1*complexconjugate(WRROTATION1x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x1*complexconjugate(WRROTATION1x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x5*complexconjugate(WRROTATION2x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x5*complexconjugate(WRROTATION2x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x1*complexconjugate(WRROTATION2x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x1*complexconjugate(WRROTATION2x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x5*complexconjugate(WRROTATION3x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x5*complexconjugate(WRROTATION3x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x1*complexconjugate(WRROTATION3x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x1*complexconjugate(WRROTATION3x5))/(4.*cw)',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x5*complexconjugate(WRROTATION1x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x5*complexconjugate(WRROTATION1x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x2*complexconjugate(WRROTATION1x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x2*complexconjugate(WRROTATION1x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x5*complexconjugate(WRROTATION2x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x5*complexconjugate(WRROTATION2x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x2*complexconjugate(WRROTATION2x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x2*complexconjugate(WRROTATION2x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x5*complexconjugate(WRROTATION3x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x5*complexconjugate(WRROTATION3x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x2*complexconjugate(WRROTATION3x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x2*complexconjugate(WRROTATION3x5))/(4.*cw)',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x5*complexconjugate(WRROTATION1x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x5*complexconjugate(WRROTATION1x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x3*complexconjugate(WRROTATION1x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x3*complexconjugate(WRROTATION1x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x5*complexconjugate(WRROTATION2x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x5*complexconjugate(WRROTATION2x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x3*complexconjugate(WRROTATION2x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x3*complexconjugate(WRROTATION2x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x5*complexconjugate(WRROTATION3x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x5*complexconjugate(WRROTATION3x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x3*complexconjugate(WRROTATION3x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x3*complexconjugate(WRROTATION3x5))/(4.*cw)',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x5*complexconjugate(WRROTATION1x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x5*complexconjugate(WRROTATION1x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x4*complexconjugate(WRROTATION1x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x4*complexconjugate(WRROTATION1x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x5*complexconjugate(WRROTATION2x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x5*complexconjugate(WRROTATION2x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x4*complexconjugate(WRROTATION2x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x4*complexconjugate(WRROTATION2x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x5*complexconjugate(WRROTATION3x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x5*complexconjugate(WRROTATION3x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x4*complexconjugate(WRROTATION3x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x4*complexconjugate(WRROTATION3x5))/(4.*cw)',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x5*complexconjugate(WRROTATION1x5))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION1x5*complexconjugate(WRROTATION1x5))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION2x5*complexconjugate(WRROTATION2x5))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION2x5*complexconjugate(WRROTATION2x5))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION3x5*complexconjugate(WRROTATION3x5))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION3x5*complexconjugate(WRROTATION3x5))/(2.*cw)',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(ee*complex(0,1)*complexconjugate(WRROTATION3x6))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x6*complexconjugate(WRROTATION1x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x6*complexconjugate(WRROTATION1x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x1*complexconjugate(WRROTATION1x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x1*complexconjugate(WRROTATION1x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x6*complexconjugate(WRROTATION2x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x6*complexconjugate(WRROTATION2x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x1*complexconjugate(WRROTATION2x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x1*complexconjugate(WRROTATION2x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x6*complexconjugate(WRROTATION3x1))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x6*complexconjugate(WRROTATION3x1))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x1*complexconjugate(WRROTATION3x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x1*complexconjugate(WRROTATION3x6))/(4.*cw)',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x6*complexconjugate(WRROTATION1x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x6*complexconjugate(WRROTATION1x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x2*complexconjugate(WRROTATION1x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x2*complexconjugate(WRROTATION1x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x6*complexconjugate(WRROTATION2x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x6*complexconjugate(WRROTATION2x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x2*complexconjugate(WRROTATION2x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x2*complexconjugate(WRROTATION2x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x6*complexconjugate(WRROTATION3x2))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x6*complexconjugate(WRROTATION3x2))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x2*complexconjugate(WRROTATION3x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x2*complexconjugate(WRROTATION3x6))/(4.*cw)',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x6*complexconjugate(WRROTATION1x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x6*complexconjugate(WRROTATION1x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x3*complexconjugate(WRROTATION1x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x3*complexconjugate(WRROTATION1x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x6*complexconjugate(WRROTATION2x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x6*complexconjugate(WRROTATION2x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x3*complexconjugate(WRROTATION2x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x3*complexconjugate(WRROTATION2x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x6*complexconjugate(WRROTATION3x3))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x6*complexconjugate(WRROTATION3x3))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x3*complexconjugate(WRROTATION3x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x3*complexconjugate(WRROTATION3x6))/(4.*cw)',
                  order = {'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x6*complexconjugate(WRROTATION1x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x6*complexconjugate(WRROTATION1x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x4*complexconjugate(WRROTATION1x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x4*complexconjugate(WRROTATION1x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x6*complexconjugate(WRROTATION2x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x6*complexconjugate(WRROTATION2x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x4*complexconjugate(WRROTATION2x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x4*complexconjugate(WRROTATION2x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x6*complexconjugate(WRROTATION3x4))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x6*complexconjugate(WRROTATION3x4))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x4*complexconjugate(WRROTATION3x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x4*complexconjugate(WRROTATION3x6))/(4.*cw)',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x6*complexconjugate(WRROTATION1x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x6*complexconjugate(WRROTATION1x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION1x5*complexconjugate(WRROTATION1x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION1x5*complexconjugate(WRROTATION1x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x6*complexconjugate(WRROTATION2x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x6*complexconjugate(WRROTATION2x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION2x5*complexconjugate(WRROTATION2x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION2x5*complexconjugate(WRROTATION2x6))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x6*complexconjugate(WRROTATION3x5))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x6*complexconjugate(WRROTATION3x5))/(4.*cw) + (cw*ee*complex(0,1)*WRROTATION3x5*complexconjugate(WRROTATION3x6))/(4.*sw) + (ee*complex(0,1)*sw*WRROTATION3x5*complexconjugate(WRROTATION3x6))/(4.*cw)',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '(cw*ee*complex(0,1)*WRROTATION1x6*complexconjugate(WRROTATION1x6))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION1x6*complexconjugate(WRROTATION1x6))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION2x6*complexconjugate(WRROTATION2x6))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION2x6*complexconjugate(WRROTATION2x6))/(2.*cw) + (cw*ee*complex(0,1)*WRROTATION3x6*complexconjugate(WRROTATION3x6))/(2.*sw) + (ee*complex(0,1)*sw*WRROTATION3x6*complexconjugate(WRROTATION3x6))/(2.*cw)',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = 'complex(0,1)*g1p*WRROTATION2x1*complexconjugate(WRROTATION2x1) - complex(0,1)*g1p*WRROTATION3x1*complexconjugate(WRROTATION3x1) - complex(0,1)*g1p*WRROTATION5x1*complexconjugate(WRROTATION5x1) + complex(0,1)*g1p*WRROTATION6x1*complexconjugate(WRROTATION6x1)',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '(-2*Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x1))/xev - (2*Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x1))/xev - complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x1)*cmath.sqrt(2) - complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x1)*cmath.sqrt(2) - complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x1)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '(2*complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x1))/xev + (2*complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x1))/xev - Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x1)*cmath.sqrt(2) - Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x1)*cmath.sqrt(2) - Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x1)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '(complex(0,1)*g1p*WRROTATION2x2*complexconjugate(WRROTATION2x1))/2. + (complex(0,1)*g1p*WRROTATION2x1*complexconjugate(WRROTATION2x2))/2. - (complex(0,1)*g1p*WRROTATION3x2*complexconjugate(WRROTATION3x1))/2. - (complex(0,1)*g1p*WRROTATION3x1*complexconjugate(WRROTATION3x2))/2. - (complex(0,1)*g1p*WRROTATION5x2*complexconjugate(WRROTATION5x1))/2. - (complex(0,1)*g1p*WRROTATION5x1*complexconjugate(WRROTATION5x2))/2. + (complex(0,1)*g1p*WRROTATION6x2*complexconjugate(WRROTATION6x1))/2. + (complex(0,1)*g1p*WRROTATION6x1*complexconjugate(WRROTATION6x2))/2.',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = 'complex(0,1)*g1p*WRROTATION2x2*complexconjugate(WRROTATION2x2) - complex(0,1)*g1p*WRROTATION3x2*complexconjugate(WRROTATION3x2) - complex(0,1)*g1p*WRROTATION5x2*complexconjugate(WRROTATION5x2) + complex(0,1)*g1p*WRROTATION6x2*complexconjugate(WRROTATION6x2)',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x1))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x2))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x1))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x2))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x1))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x2))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x1))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x2))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(-2*Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x2))/xev - (2*Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x2))/xev - complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x2)*cmath.sqrt(2) - complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x2)*cmath.sqrt(2) - complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x2)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(2*complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x2))/xev + (2*complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x2))/xev - Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x2)*cmath.sqrt(2) - Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x2)*cmath.sqrt(2) - Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x2)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '(complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x1))/2. + (complex(0,1)*g1p*WRROTATION2x1*complexconjugate(WRROTATION2x3))/2. - (complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x1))/2. - (complex(0,1)*g1p*WRROTATION3x1*complexconjugate(WRROTATION3x3))/2. - (complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x1))/2. - (complex(0,1)*g1p*WRROTATION5x1*complexconjugate(WRROTATION5x3))/2. + (complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x1))/2. + (complex(0,1)*g1p*WRROTATION6x1*complexconjugate(WRROTATION6x3))/2.',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '(complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x2))/2. + (complex(0,1)*g1p*WRROTATION2x2*complexconjugate(WRROTATION2x3))/2. - (complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x2))/2. - (complex(0,1)*g1p*WRROTATION3x2*complexconjugate(WRROTATION3x3))/2. - (complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x2))/2. - (complex(0,1)*g1p*WRROTATION5x2*complexconjugate(WRROTATION5x3))/2. + (complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x2))/2. + (complex(0,1)*g1p*WRROTATION6x2*complexconjugate(WRROTATION6x3))/2.',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '-(complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x3)) + complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x3) + complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x3) - complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x3)',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = 'complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x3) - complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x3) - complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x3) + complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x3)',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x1))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x3))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x1))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x3))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x1))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x3))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x1))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x3))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x2))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x3))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x2))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x3))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x2))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x3))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x2))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x3))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '(-2*Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x3))/xev - (2*Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x3))/xev - complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x3)*cmath.sqrt(2) - complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x3)*cmath.sqrt(2) - complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x3)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '(2*complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x3))/xev + (2*complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x3))/xev - Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x3)*cmath.sqrt(2) - Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x3)*cmath.sqrt(2) - Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x3)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '(complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x1))/2. + (complex(0,1)*g1p*WRROTATION2x1*complexconjugate(WRROTATION2x4))/2. - (complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x1))/2. - (complex(0,1)*g1p*WRROTATION3x1*complexconjugate(WRROTATION3x4))/2. - (complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x1))/2. - (complex(0,1)*g1p*WRROTATION5x1*complexconjugate(WRROTATION5x4))/2. + (complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x1))/2. + (complex(0,1)*g1p*WRROTATION6x1*complexconjugate(WRROTATION6x4))/2.',
                  order = {'QED':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '-0.5*(complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x2)) - (complex(0,1)*g1p*WRROTATION2x2*complexconjugate(WRROTATION2x4))/2. + (complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x2))/2. + (complex(0,1)*g1p*WRROTATION3x2*complexconjugate(WRROTATION3x4))/2. + (complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x2))/2. + (complex(0,1)*g1p*WRROTATION5x2*complexconjugate(WRROTATION5x4))/2. - (complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x2))/2. - (complex(0,1)*g1p*WRROTATION6x2*complexconjugate(WRROTATION6x4))/2.',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '(complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x2))/2. + (complex(0,1)*g1p*WRROTATION2x2*complexconjugate(WRROTATION2x4))/2. - (complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x2))/2. - (complex(0,1)*g1p*WRROTATION3x2*complexconjugate(WRROTATION3x4))/2. - (complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x2))/2. - (complex(0,1)*g1p*WRROTATION5x2*complexconjugate(WRROTATION5x4))/2. + (complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x2))/2. + (complex(0,1)*g1p*WRROTATION6x2*complexconjugate(WRROTATION6x4))/2.',
                  order = {'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '-(complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x3))/2. - (complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x4))/2. + (complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x3))/2. + (complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x4))/2. + (complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x3))/2. + (complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x4))/2. - (complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x3))/2. - (complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x4))/2.',
                  order = {'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '(complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x3))/2. + (complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x4))/2. - (complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x3))/2. - (complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x4))/2. - (complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x3))/2. - (complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x4))/2. + (complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x3))/2. + (complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x4))/2.',
                  order = {'QED':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '-(complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x4)) + complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x4) + complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x4) - complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x4)',
                  order = {'QED':1})

GC_248 = Coupling(name = 'GC_248',
                  value = 'complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x4) - complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x4) - complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x4) + complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x4)',
                  order = {'QED':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x1))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x4))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x1))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x4))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x1))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x4))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x1))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x4))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x2))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x4))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x2))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x4))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x2))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x4))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x2))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x4))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x3))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x4))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x3))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x4))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x3))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x4))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x3))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x4))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_255 = Coupling(name = 'GC_255',
                  value = '(-2*Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x4))/xev - (2*Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x4))/xev - complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x4)*cmath.sqrt(2) - complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x4)*cmath.sqrt(2) - complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x4)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '(2*complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x4))/xev + (2*complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x4))/xev - Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x4)*cmath.sqrt(2) - Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x4)*cmath.sqrt(2) - Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x4)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '(complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x1))/2. + (complex(0,1)*g1p*WRROTATION2x1*complexconjugate(WRROTATION2x5))/2. - (complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x1))/2. - (complex(0,1)*g1p*WRROTATION3x1*complexconjugate(WRROTATION3x5))/2. - (complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x1))/2. - (complex(0,1)*g1p*WRROTATION5x1*complexconjugate(WRROTATION5x5))/2. + (complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x1))/2. + (complex(0,1)*g1p*WRROTATION6x1*complexconjugate(WRROTATION6x5))/2.',
                  order = {'QED':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '-0.5*(complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x2)) - (complex(0,1)*g1p*WRROTATION2x2*complexconjugate(WRROTATION2x5))/2. + (complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x2))/2. + (complex(0,1)*g1p*WRROTATION3x2*complexconjugate(WRROTATION3x5))/2. + (complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x2))/2. + (complex(0,1)*g1p*WRROTATION5x2*complexconjugate(WRROTATION5x5))/2. - (complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x2))/2. - (complex(0,1)*g1p*WRROTATION6x2*complexconjugate(WRROTATION6x5))/2.',
                  order = {'QED':1})

GC_259 = Coupling(name = 'GC_259',
                  value = '(complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x2))/2. + (complex(0,1)*g1p*WRROTATION2x2*complexconjugate(WRROTATION2x5))/2. - (complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x2))/2. - (complex(0,1)*g1p*WRROTATION3x2*complexconjugate(WRROTATION3x5))/2. - (complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x2))/2. - (complex(0,1)*g1p*WRROTATION5x2*complexconjugate(WRROTATION5x5))/2. + (complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x2))/2. + (complex(0,1)*g1p*WRROTATION6x2*complexconjugate(WRROTATION6x5))/2.',
                  order = {'QED':1})

GC_260 = Coupling(name = 'GC_260',
                  value = '-0.5*(complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x3)) - (complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x5))/2. + (complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x3))/2. + (complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x5))/2. + (complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x3))/2. + (complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x5))/2. - (complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x3))/2. - (complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x5))/2.',
                  order = {'QED':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '(complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x3))/2. + (complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x5))/2. - (complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x3))/2. - (complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x5))/2. - (complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x3))/2. - (complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x5))/2. + (complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x3))/2. + (complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x5))/2.',
                  order = {'QED':1})

GC_262 = Coupling(name = 'GC_262',
                  value = '-0.5*(complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x4)) - (complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x5))/2. + (complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x4))/2. + (complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x5))/2. + (complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x4))/2. + (complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x5))/2. - (complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x4))/2. - (complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x5))/2.',
                  order = {'QED':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '(complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x4))/2. + (complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x5))/2. - (complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x4))/2. - (complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x5))/2. - (complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x4))/2. - (complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x5))/2. + (complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x4))/2. + (complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x5))/2.',
                  order = {'QED':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '-(complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x5)) + complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x5) + complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x5) - complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x5)',
                  order = {'QED':1})

GC_265 = Coupling(name = 'GC_265',
                  value = 'complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x5) - complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x5) - complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x5) + complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x5)',
                  order = {'QED':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x1))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x5))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x1))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x5))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x1))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x5))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x1))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x5))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x2))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x5))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x2))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x5))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x2))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x5))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x2))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x5))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x3))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x5))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x3))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x5))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x3))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x5))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x3))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x5))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x4))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x5))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x4))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x5))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x4))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x5))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x4))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x5))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '(-2*Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x5))/xev - (2*Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x5))/xev - complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x5)*cmath.sqrt(2) - complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x5)*cmath.sqrt(2) - complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x5)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '(2*complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x5))/xev + (2*complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x5))/xev - Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x5)*cmath.sqrt(2) - Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x5)*cmath.sqrt(2) - Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x5)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x1))/2. + (complex(0,1)*g1p*WRROTATION2x1*complexconjugate(WRROTATION2x6))/2. - (complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x1))/2. - (complex(0,1)*g1p*WRROTATION3x1*complexconjugate(WRROTATION3x6))/2. - (complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x1))/2. - (complex(0,1)*g1p*WRROTATION5x1*complexconjugate(WRROTATION5x6))/2. + (complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x1))/2. + (complex(0,1)*g1p*WRROTATION6x1*complexconjugate(WRROTATION6x6))/2.',
                  order = {'QED':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '-0.5*(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x2)) - (complex(0,1)*g1p*WRROTATION2x2*complexconjugate(WRROTATION2x6))/2. + (complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x2))/2. + (complex(0,1)*g1p*WRROTATION3x2*complexconjugate(WRROTATION3x6))/2. + (complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x2))/2. + (complex(0,1)*g1p*WRROTATION5x2*complexconjugate(WRROTATION5x6))/2. - (complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x2))/2. - (complex(0,1)*g1p*WRROTATION6x2*complexconjugate(WRROTATION6x6))/2.',
                  order = {'QED':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x2))/2. + (complex(0,1)*g1p*WRROTATION2x2*complexconjugate(WRROTATION2x6))/2. - (complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x2))/2. - (complex(0,1)*g1p*WRROTATION3x2*complexconjugate(WRROTATION3x6))/2. - (complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x2))/2. - (complex(0,1)*g1p*WRROTATION5x2*complexconjugate(WRROTATION5x6))/2. + (complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x2))/2. + (complex(0,1)*g1p*WRROTATION6x2*complexconjugate(WRROTATION6x6))/2.',
                  order = {'QED':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '-0.5*(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x3)) - (complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x6))/2. + (complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x3))/2. + (complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x6))/2. + (complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x3))/2. + (complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x6))/2. - (complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x3))/2. - (complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x6))/2.',
                  order = {'QED':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x3))/2. + (complex(0,1)*g1p*WRROTATION2x3*complexconjugate(WRROTATION2x6))/2. - (complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x3))/2. - (complex(0,1)*g1p*WRROTATION3x3*complexconjugate(WRROTATION3x6))/2. - (complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x3))/2. - (complex(0,1)*g1p*WRROTATION5x3*complexconjugate(WRROTATION5x6))/2. + (complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x3))/2. + (complex(0,1)*g1p*WRROTATION6x3*complexconjugate(WRROTATION6x6))/2.',
                  order = {'QED':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '-0.5*(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x4)) - (complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x6))/2. + (complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x4))/2. + (complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x6))/2. + (complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x4))/2. + (complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x6))/2. - (complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x4))/2. - (complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x6))/2.',
                  order = {'QED':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x4))/2. + (complex(0,1)*g1p*WRROTATION2x4*complexconjugate(WRROTATION2x6))/2. - (complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x4))/2. - (complex(0,1)*g1p*WRROTATION3x4*complexconjugate(WRROTATION3x6))/2. - (complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x4))/2. - (complex(0,1)*g1p*WRROTATION5x4*complexconjugate(WRROTATION5x6))/2. + (complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x4))/2. + (complex(0,1)*g1p*WRROTATION6x4*complexconjugate(WRROTATION6x6))/2.',
                  order = {'QED':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '-0.5*(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x5)) - (complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x6))/2. + (complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x5))/2. + (complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x6))/2. + (complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x5))/2. + (complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x6))/2. - (complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x5))/2. - (complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x6))/2.',
                  order = {'QED':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x5))/2. + (complex(0,1)*g1p*WRROTATION2x5*complexconjugate(WRROTATION2x6))/2. - (complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x5))/2. - (complex(0,1)*g1p*WRROTATION3x5*complexconjugate(WRROTATION3x6))/2. - (complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x5))/2. - (complex(0,1)*g1p*WRROTATION5x5*complexconjugate(WRROTATION5x6))/2. + (complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x5))/2. + (complex(0,1)*g1p*WRROTATION6x5*complexconjugate(WRROTATION6x6))/2.',
                  order = {'QED':1})

GC_285 = Coupling(name = 'GC_285',
                  value = '-(complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x6)) + complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x6) + complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x6) - complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x6)',
                  order = {'QED':1})

GC_286 = Coupling(name = 'GC_286',
                  value = 'complex(0,1)*g1p*WRROTATION2x6*complexconjugate(WRROTATION2x6) - complex(0,1)*g1p*WRROTATION3x6*complexconjugate(WRROTATION3x6) - complex(0,1)*g1p*WRROTATION5x6*complexconjugate(WRROTATION5x6) + complex(0,1)*g1p*WRROTATION6x6*complexconjugate(WRROTATION6x6)',
                  order = {'QED':1})

GC_287 = Coupling(name = 'GC_287',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x1))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x6))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x1))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x6))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_288 = Coupling(name = 'GC_288',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x1))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION5x6))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x1))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x1)*complexconjugate(WRROTATION6x6))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x1)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x1)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x1))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x1)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x2))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x6))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x2))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x6))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_290 = Coupling(name = 'GC_290',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x2))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION5x6))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x2))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x2)*complexconjugate(WRROTATION6x6))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x2)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x2)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x2))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x2)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_291 = Coupling(name = 'GC_291',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x3))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x6))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x3))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x6))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x3))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION5x6))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x3))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x3)*complexconjugate(WRROTATION6x6))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x3)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x3)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x3))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x3)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_293 = Coupling(name = 'GC_293',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x4))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x6))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x4))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x6))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_294 = Coupling(name = 'GC_294',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x4))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION5x6))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x4))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x4)*complexconjugate(WRROTATION6x6))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x4)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x4)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x4))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x4)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_295 = Coupling(name = 'GC_295',
                  value = '-((Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x5))/xev) - (Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x6))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x5))/xev - (Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x6))/xev - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2) - (complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_296 = Coupling(name = 'GC_296',
                  value = '(complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x5))/xev + (complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION5x6))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x5))/xev + (complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x5)*complexconjugate(WRROTATION6x6))/xev - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x5)*complexconjugate(WRROTATION4x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x5)*complexconjugate(WRROTATION5x6))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x5))/cmath.sqrt(2) - (Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x5)*complexconjugate(WRROTATION6x6))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_297 = Coupling(name = 'GC_297',
                  value = '(-2*Ca*complex(0,1)*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x6))/xev - (2*Ca*complex(0,1)*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x6))/xev - complex(0,1)*Sa*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x6)*cmath.sqrt(2) - complex(0,1)*Sa*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x6)*cmath.sqrt(2) - complex(0,1)*Sa*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x6)*cmath.sqrt(2)',
                  order = {'QED':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '(2*complex(0,1)*Sa*Vemu*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION5x6))/xev + (2*complex(0,1)*Sa*Vetau*complexconjugate(WRROTATION4x6)*complexconjugate(WRROTATION6x6))/xev - Ca*complex(0,1)*ynd1*complexconjugate(WRROTATION1x6)*complexconjugate(WRROTATION4x6)*cmath.sqrt(2) - Ca*complex(0,1)*ynd2*complexconjugate(WRROTATION2x6)*complexconjugate(WRROTATION5x6)*cmath.sqrt(2) - Ca*complex(0,1)*ynd3*complexconjugate(WRROTATION3x6)*complexconjugate(WRROTATION6x6)*cmath.sqrt(2)',
                  order = {'QED':1})

