from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

hc11 = SchLib(tool=SKIDL).add_parts(*[
        Part(name='MC68HC11A8CC',dest=TEMPLATE,tool=SKIDL,keywords='HC11 MCU Microcotroller',description='8K ROM, 256B RAM, 512B EEPROM',ref_prefix='U',num_units=1,do_erc=True,aliases=['MC68HC11A7CC', 'MC68HC11A1CC', 'MC68HC11A0CC'],pins=[
            Pin(num='1',name='VSS',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='MODB',do_erc=True),
            Pin(num='3',name='MODA',func=Pin.BIDIR,do_erc=True),
            Pin(num='4',name='AS',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='E',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='R/W',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='EXTAL',do_erc=True),
            Pin(num='8',name='XTAL',func=Pin.OUTPUT,do_erc=True),
            Pin(num='9',name='AD0/PC0',func=Pin.BIDIR,do_erc=True),
            Pin(num='10',name='AD1/PC1',func=Pin.BIDIR,do_erc=True),
            Pin(num='20',name='RXD/PD0',func=Pin.BIDIR,do_erc=True),
            Pin(num='30',name='PA4',func=Pin.OUTPUT,do_erc=True),
            Pin(num='40',name='A10/PB2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='50',name='PE7',do_erc=True),
            Pin(num='11',name='AD2/PC2',func=Pin.BIDIR,do_erc=True),
            Pin(num='21',name='TXD/PD1',func=Pin.BIDIR,do_erc=True),
            Pin(num='31',name='PA3',func=Pin.OUTPUT,do_erc=True),
            Pin(num='41',name='A9/PB1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='51',name='VRL',do_erc=True),
            Pin(num='12',name='AD3/PC3',func=Pin.BIDIR,do_erc=True),
            Pin(num='22',name='MIS/PD2',func=Pin.BIDIR,do_erc=True),
            Pin(num='32',name='PA2',do_erc=True),
            Pin(num='42',name='A8/PB0',func=Pin.OUTPUT,do_erc=True),
            Pin(num='52',name='VRH',do_erc=True),
            Pin(num='13',name='AD4/PC4',func=Pin.BIDIR,do_erc=True),
            Pin(num='23',name='MOS/PD3',func=Pin.BIDIR,do_erc=True),
            Pin(num='33',name='PA1',do_erc=True),
            Pin(num='43',name='PE0',do_erc=True),
            Pin(num='14',name='AD5/PC5',func=Pin.BIDIR,do_erc=True),
            Pin(num='24',name='SCK/PD4',func=Pin.BIDIR,do_erc=True),
            Pin(num='34',name='PA0',do_erc=True),
            Pin(num='44',name='PE4',do_erc=True),
            Pin(num='15',name='AD6/PC6',func=Pin.BIDIR,do_erc=True),
            Pin(num='25',name='SS/PD5',func=Pin.BIDIR,do_erc=True),
            Pin(num='35',name='A15/PB7',func=Pin.OUTPUT,do_erc=True),
            Pin(num='45',name='PE1',do_erc=True),
            Pin(num='16',name='AD7/PC7',func=Pin.BIDIR,do_erc=True),
            Pin(num='26',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='36',name='A14/PB6',func=Pin.OUTPUT,do_erc=True),
            Pin(num='46',name='PE5',do_erc=True),
            Pin(num='17',name='~RESET',do_erc=True),
            Pin(num='27',name='PA7',func=Pin.BIDIR,do_erc=True),
            Pin(num='37',name='A13/PB5',func=Pin.OUTPUT,do_erc=True),
            Pin(num='47',name='PE2',do_erc=True),
            Pin(num='18',name='~XIRQ',do_erc=True),
            Pin(num='28',name='PA6',func=Pin.OUTPUT,do_erc=True),
            Pin(num='38',name='A12/PB4',func=Pin.OUTPUT,do_erc=True),
            Pin(num='48',name='PE6',do_erc=True),
            Pin(num='19',name='~IRQ',do_erc=True),
            Pin(num='29',name='PA5',func=Pin.OUTPUT,do_erc=True),
            Pin(num='39',name='A11/PB3',func=Pin.OUTPUT,do_erc=True),
            Pin(num='49',name='PE3',do_erc=True)]),
        Part(name='MC68HC11F1CC',dest=TEMPLATE,tool=SKIDL,keywords='HC11 MCU Microcontroller',description='ROMless, 1K RAM, 512B EEPROM, PLCC-68',ref_prefix='U',num_units=1,fplist=['PLCC-68*'],do_erc=True,pins=[
            Pin(num='1',name='VSS',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='MODB',do_erc=True),
            Pin(num='3',name='MODA',func=Pin.BIDIR,do_erc=True),
            Pin(num='4',name='E',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='R/W',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='EXTAL',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='XTAL',do_erc=True),
            Pin(num='8',name='4XOUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='9',name='D0/PC0',func=Pin.BIDIR,do_erc=True),
            Pin(num='10',name='D1/PC1',func=Pin.BIDIR,do_erc=True),
            Pin(num='20',name='CSPROG/PG7',func=Pin.BIDIR,do_erc=True),
            Pin(num='30',name='MIS/PD2',func=Pin.BIDIR,do_erc=True),
            Pin(num='40',name='PA2',func=Pin.BIDIR,do_erc=True),
            Pin(num='50',name='A8/PB0',func=Pin.OUTPUT,do_erc=True),
            Pin(num='60',name='PE4',do_erc=True),
            Pin(num='11',name='D2/PC2',func=Pin.BIDIR,do_erc=True),
            Pin(num='21',name='CSGEN/PG6',func=Pin.BIDIR,do_erc=True),
            Pin(num='31',name='MOS/PD3',func=Pin.BIDIR,do_erc=True),
            Pin(num='41',name='PA1',func=Pin.BIDIR,do_erc=True),
            Pin(num='51',name='A7/PF7',func=Pin.OUTPUT,do_erc=True),
            Pin(num='61',name='PE1',do_erc=True),
            Pin(num='12',name='D3/PC3',func=Pin.BIDIR,do_erc=True),
            Pin(num='22',name='CSIO1/PG5',func=Pin.BIDIR,do_erc=True),
            Pin(num='32',name='SCK/PD4',func=Pin.BIDIR,do_erc=True),
            Pin(num='42',name='PA0',func=Pin.BIDIR,do_erc=True),
            Pin(num='52',name='A6/PF6',func=Pin.OUTPUT,do_erc=True),
            Pin(num='62',name='PE5',do_erc=True),
            Pin(num='13',name='D4/PC4',func=Pin.BIDIR,do_erc=True),
            Pin(num='23',name='CSIO2/PG4',func=Pin.BIDIR,do_erc=True),
            Pin(num='33',name='SS/PD5',func=Pin.BIDIR,do_erc=True),
            Pin(num='43',name='A15/PB7',func=Pin.OUTPUT,do_erc=True),
            Pin(num='53',name='A5/PF5',func=Pin.OUTPUT,do_erc=True),
            Pin(num='63',name='PE2',do_erc=True),
            Pin(num='14',name='D5/PC5',func=Pin.BIDIR,do_erc=True),
            Pin(num='24',name='PG3',func=Pin.BIDIR,do_erc=True),
            Pin(num='34',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='44',name='A14/PB6',func=Pin.OUTPUT,do_erc=True),
            Pin(num='54',name='A4/PF4',func=Pin.OUTPUT,do_erc=True),
            Pin(num='64',name='PE6',do_erc=True),
            Pin(num='15',name='D6/PC6',func=Pin.BIDIR,do_erc=True),
            Pin(num='25',name='PG2',func=Pin.BIDIR,do_erc=True),
            Pin(num='35',name='PA7',func=Pin.BIDIR,do_erc=True),
            Pin(num='45',name='A13/PB5',func=Pin.OUTPUT,do_erc=True),
            Pin(num='55',name='A3/PF3',func=Pin.OUTPUT,do_erc=True),
            Pin(num='65',name='PE3',do_erc=True),
            Pin(num='16',name='D7/PC7',func=Pin.BIDIR,do_erc=True),
            Pin(num='26',name='PG1',func=Pin.BIDIR,do_erc=True),
            Pin(num='36',name='PA6',func=Pin.BIDIR,do_erc=True),
            Pin(num='46',name='A12/PB4',func=Pin.OUTPUT,do_erc=True),
            Pin(num='56',name='A2/PF2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='66',name='PE7',do_erc=True),
            Pin(num='17',name='~RESET',do_erc=True),
            Pin(num='27',name='PG0',func=Pin.BIDIR,do_erc=True),
            Pin(num='37',name='PA5',func=Pin.BIDIR,do_erc=True),
            Pin(num='47',name='A11/PB3',func=Pin.OUTPUT,do_erc=True),
            Pin(num='57',name='A1/PF1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='67',name='VRL',do_erc=True),
            Pin(num='18',name='~XIRQ',do_erc=True),
            Pin(num='28',name='RXD/PD0',func=Pin.BIDIR,do_erc=True),
            Pin(num='38',name='PA4',func=Pin.BIDIR,do_erc=True),
            Pin(num='48',name='A10/PB2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='58',name='A0/PF0',func=Pin.OUTPUT,do_erc=True),
            Pin(num='68',name='VRH',do_erc=True),
            Pin(num='19',name='~IRQ',do_erc=True),
            Pin(num='29',name='TXD/PD1',func=Pin.BIDIR,do_erc=True),
            Pin(num='39',name='PA3',func=Pin.BIDIR,do_erc=True),
            Pin(num='49',name='A9/PB1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='59',name='PE0',do_erc=True)])])