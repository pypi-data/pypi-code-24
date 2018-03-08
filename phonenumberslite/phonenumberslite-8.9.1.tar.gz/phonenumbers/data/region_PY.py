"""Auto-generated file, do not edit by hand. PY metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_PY = PhoneMetadata(id='PY', country_code=595, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='5[0-5]\\d{4,7}|[2-46-9]\\d{5,8}', possible_length=(6, 7, 8, 9), possible_length_local_only=(5, 6)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[26]1|3[289]|4[124678]|7[123]|8[1236])\\d{5,7}|(?:2(?:2[4568]|7[15]|9[1-5])|3(?:18|3[167]|4[2357]|51)|4(?:18|2[45]|3[12]|5[13]|64|71|9[1-47])|5(?:[1-4]\\d|5[0234])|6(?:3[1-3]|44|7[1-4678])|7(?:17|4[0-4]|6[1-578]|75|8[0-8])|858)\\d{5,6}', example_number='212345678', possible_length=(7, 8, 9), possible_length_local_only=(5, 6)),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:6[12]|[78][1-6]|9[1-5])\\d{6}', example_number='961456789', possible_length=(9,)),
    voip=PhoneNumberDesc(national_number_pattern='8700[0-4]\\d{4}', example_number='870012345', possible_length=(9,)),
    uan=PhoneNumberDesc(national_number_pattern='[2-9]0\\d{4,7}', example_number='201234567', possible_length=(6, 7, 8, 9)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['[26]1|3[289]|4[1246-8]|7[1-3]|8[1-36]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[26]1|3[289]|4[1246-8]|7[1-3]|8[1-36]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{3})(\\d{3,6})', format='\\1 \\2', leading_digits_pattern=['[2-9]0'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{6})', format='\\1 \\2', leading_digits_pattern=['9[1-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['870', '8700']),
        NumberFormat(pattern='(\\d{3})(\\d{4,5})', format='\\1 \\2', leading_digits_pattern=['[2-8][1-9]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[2-8][1-9]'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
