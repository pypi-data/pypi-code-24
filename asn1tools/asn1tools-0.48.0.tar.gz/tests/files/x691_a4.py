EXPECTED = {'X691-A4': {'extensibility-implied': False,
             'imports': {},
             'object-classes': {},
             'object-sets': {},
             'tags': 'AUTOMATIC',
             'types': {'Ax': {'members': [{'name': 'a',
                                           'restricted-to': [(250, 253)],
                                           'type': 'INTEGER'},
                                          {'name': 'b', 'type': 'BOOLEAN'},
                                          {'members': [{'name': 'd',
                                                        'type': 'INTEGER'},
                                                       '...',
                                                       [{'name': 'e',
                                                         'type': 'BOOLEAN'},
                                                        {'name': 'f',
                                                         'type': 'IA5String'}],
                                                       '...'],
                                           'name': 'c',
                                           'type': 'CHOICE'},
                                          '...',
                                          [{'name': 'g',
                                            'type': 'NumericString'},
                                           {'name': 'h',
                                            'optional': True,
                                            'type': 'BOOLEAN'}],
                                          '...',
                                          {'name': 'i',
                                           'optional': True,
                                           'type': 'BMPString'},
                                          {'name': 'j',
                                           'optional': True,
                                           'type': 'PrintableString'}],
                              'type': 'SEQUENCE'}},
             'values': {}}}