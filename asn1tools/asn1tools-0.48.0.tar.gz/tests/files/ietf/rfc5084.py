EXPECTED = {'CMS-AES-CCM-and-AES-GCM': {'extensibility-implied': False,
                             'imports': {},
                             'object-classes': {},
                             'object-sets': {},
                             'tags': 'IMPLICIT',
                             'types': {'AES-CCM-ICVlen': {'restricted-to': [4,
                                                                            6,
                                                                            8,
                                                                            10,
                                                                            12,
                                                                            14,
                                                                            16],
                                                          'type': 'INTEGER'},
                                       'AES-GCM-ICVlen': {'restricted-to': [12,
                                                                            13,
                                                                            14,
                                                                            15,
                                                                            16],
                                                          'type': 'INTEGER'},
                                       'CCMParameters': {'members': [{'name': 'aes-nonce',
                                                                      'size': [(7,
                                                                                13)],
                                                                      'type': 'OCTET '
                                                                              'STRING'},
                                                                     {'default': 12,
                                                                      'name': 'aes-ICVlen',
                                                                      'type': 'AES-CCM-ICVlen'}],
                                                         'type': 'SEQUENCE'},
                                       'GCMParameters': {'members': [{'name': 'aes-nonce',
                                                                      'type': 'OCTET '
                                                                              'STRING'},
                                                                     {'default': 12,
                                                                      'name': 'aes-ICVlen',
                                                                      'type': 'AES-GCM-ICVlen'}],
                                                         'type': 'SEQUENCE'}},
                             'values': {'aes': {'type': 'OBJECT IDENTIFIER',
                                                'value': [('joint-iso-itu-t',
                                                           2),
                                                          ('country', 16),
                                                          ('us', 840),
                                                          ('organization', 1),
                                                          ('gov', 101),
                                                          ('csor', 3),
                                                          ('nistAlgorithm', 4),
                                                          1]},
                                        'id-aes128-CCM': {'type': 'OBJECT '
                                                                  'IDENTIFIER',
                                                          'value': ['aes', 7]},
                                        'id-aes128-GCM': {'type': 'OBJECT '
                                                                  'IDENTIFIER',
                                                          'value': ['aes', 6]},
                                        'id-aes192-CCM': {'type': 'OBJECT '
                                                                  'IDENTIFIER',
                                                          'value': ['aes', 27]},
                                        'id-aes192-GCM': {'type': 'OBJECT '
                                                                  'IDENTIFIER',
                                                          'value': ['aes', 26]},
                                        'id-aes256-CCM': {'type': 'OBJECT '
                                                                  'IDENTIFIER',
                                                          'value': ['aes', 47]},
                                        'id-aes256-GCM': {'type': 'OBJECT '
                                                                  'IDENTIFIER',
                                                          'value': ['aes',
                                                                    46]}}}}