"""Auto-generated file, do not edit by hand. CN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CN = PhoneMetadata(id='CN', country_code=86, international_prefix='(1(?:[12]\\d{3}|79\\d{2}|9[0-7]\\d{2}))?00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-7]\\d{6,11}|8[0-357-9]\\d{6,9}|9\\d{7,10}', possible_length=(7, 8, 9, 10, 11, 12), possible_length_local_only=(5, 6)),
    fixed_line=PhoneNumberDesc(national_number_pattern='21(?:100\\d{2}|95\\d{3,4}|\\d{8,10})|(?:10|2[02-57-9]|3(?:11|7[179])|4(?:[15]1|3[1-35])|5(?:1\\d|2[37]|3[12]|51|7[13-79]|9[15])|7(?:31|5[457]|6[09]|91)|8(?:[57]1|98))(?:100\\d{2}|95\\d{3,4}|\\d{8})|(?:3(?:1[02-9]|35|49|5\\d|7[02-68]|9[1-68])|4(?:1[02-9]|2[179]|3[3-9]|5[2-9]|6[4789]|7\\d|8[23])|5(?:3[03-9]|4[36]|5[02-9]|6[1-46]|7[028]|80|9[2-46-9])|6(?:3[1-5]|6[0238]|9[12])|7(?:01|[17]\\d|2[248]|3[04-9]|4[3-6]|5[0-4689]|6[2368]|9[02-9])|8(?:078|1[236-8]|2[5-7]|3\\d|5[1-9]|7[02-9]|8[3678]|9[1-7])|9(?:0[1-3689]|1[1-79]|[379]\\d|4[13]|5[1-5]))(?:100\\d{2}|95\\d{3,4}|\\d{7})', example_number='1012345678', possible_length=(7, 8, 9, 10, 11, 12), possible_length_local_only=(5, 6)),
    mobile=PhoneNumberDesc(national_number_pattern='1(?:[38]\\d{3}|4[57]\\d{2}|5[0-35-9]\\d{2}|66\\d{2}|7(?:[0-35-8]\\d{2}|40[0-5])|9[89]\\d{2})\\d{6}', example_number='13123456789', possible_length=(11,)),
    toll_free=PhoneNumberDesc(national_number_pattern='(?:10)?800\\d{7}', example_number='8001234567', possible_length=(10, 12)),
    premium_rate=PhoneNumberDesc(national_number_pattern='16[08]\\d{5}', example_number='16812345', possible_length=(8,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='400\\d{7}|950\\d{7,8}|(?:10|2[0-57-9]|3(?:[157]\\d|35|49|9[1-68])|4(?:[17]\\d|2[179]|[35][1-9]|6[4789]|8[23])|5(?:[1357]\\d|2[37]|4[36]|6[1-46]|80|9[1-9])|6(?:3[1-5]|6[0238]|9[12])|7(?:01|[1579]\\d|2[248]|3[014-9]|4[3-6]|6[023689])|8(?:1[236-8]|2[5-7]|[37]\\d|5[14-9]|8[3678]|9[1-8])|9(?:0[1-3689]|1[1-79]|[379]\\d|4[13]|5[1-5]))96\\d{3,4}', example_number='4001234567', possible_length=(7, 8, 9, 10, 11), possible_length_local_only=(5, 6)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='(?:4|(?:10)?8)00\\d{7}|950\\d{7,8}', example_number='4001234567', possible_length=(10, 11, 12)),
    preferred_international_prefix='00',
    national_prefix='0',
    national_prefix_for_parsing='(1(?:[12]\\d{3}|79\\d{2}|9[0-7]\\d{2}))|0',
    number_format=[NumberFormat(pattern='([48]00)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[48]00']),
        NumberFormat(pattern='(\\d{5,6})', format='\\1', leading_digits_pattern=['100|95']),
        NumberFormat(pattern='(\\d{2})(\\d{5,6})', format='\\1 \\2', leading_digits_pattern=['(?:10|2\\d)[19]', '(?:10|2\\d)(?:10|9[56])', '(?:10|2\\d)(?:100|9[56])'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='$CC \\1'),
        NumberFormat(pattern='(\\d{3})(\\d{5,6})', format='\\1 \\2', leading_digits_pattern=['[3-9]', '[3-9]\\d\\d[19]', '[3-9]\\d\\d(?:10|9[56])'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='$CC \\1'),
        NumberFormat(pattern='(\\d{3,4})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['[2-9]']),
        NumberFormat(pattern='(21)(\\d{4})(\\d{4,6})', format='\\1 \\2 \\3', leading_digits_pattern=['21'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True, domestic_carrier_code_formatting_rule='$CC \\1'),
        NumberFormat(pattern='([12]\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['10[1-9]|2[02-9]', '10[1-9]|2[02-9]', '10(?:[1-79]|8(?:0[1-9]|[1-9]))|2[02-9]'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True, domestic_carrier_code_formatting_rule='$CC \\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['3(?:1[02-9]|35|49|5|7[02-68]|9[1-68])|4(?:1[02-9]|2[179]|[35][2-9]|6[47-9]|7|8[23])|5(?:3[03-9]|4[36]|5[02-9]|6[1-46]|7[028]|80|9[2-46-9])|6(?:3[1-5]|6[0238]|9[12])|7(?:01|[1579]|2[248]|3[04-9]|4[3-6]|6[2368])|8(?:1[236-8]|2[5-7]|3|5[1-9]|7[02-9]|8[36-8]|9[1-7])|9(?:0[1-3689]|1[1-79]|[379]|4[13]|5[1-5])'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True, domestic_carrier_code_formatting_rule='$CC \\1'),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['3(?:11|7[179])|4(?:[15]1|3[1-35])|5(?:1|2[37]|3[12]|51|7[13-79]|9[15])|7(?:[39]1|5[457]|6[09])|8(?:[57]1|98)'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True, domestic_carrier_code_formatting_rule='$CC \\1'),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['807', '8078'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True, domestic_carrier_code_formatting_rule='$CC \\1'),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:[3-57-9]|66)'], domestic_carrier_code_formatting_rule='$CC \\1'),
        NumberFormat(pattern='(10800)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['108', '1080', '10800']),
        NumberFormat(pattern='(\\d{3})(\\d{7,8})', format='\\1 \\2', leading_digits_pattern=['950'])],
    intl_number_format=[NumberFormat(pattern='([48]00)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[48]00']),
        NumberFormat(pattern='(\\d{2})(\\d{5,6})', format='\\1 \\2', leading_digits_pattern=['(?:10|2\\d)[19]', '(?:10|2\\d)(?:10|9[56])', '(?:10|2\\d)(?:100|9[56])']),
        NumberFormat(pattern='(\\d{3})(\\d{5,6})', format='\\1 \\2', leading_digits_pattern=['[3-9]', '[3-9]\\d\\d[19]', '[3-9]\\d\\d(?:10|9[56])']),
        NumberFormat(pattern='(21)(\\d{4})(\\d{4,6})', format='\\1 \\2 \\3', leading_digits_pattern=['21']),
        NumberFormat(pattern='([12]\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['10[1-9]|2[02-9]', '10[1-9]|2[02-9]', '10(?:[1-79]|8(?:0[1-9]|[1-9]))|2[02-9]']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['3(?:1[02-9]|35|49|5|7[02-68]|9[1-68])|4(?:1[02-9]|2[179]|[35][2-9]|6[47-9]|7|8[23])|5(?:3[03-9]|4[36]|5[02-9]|6[1-46]|7[028]|80|9[2-46-9])|6(?:3[1-5]|6[0238]|9[12])|7(?:01|[1579]|2[248]|3[04-9]|4[3-6]|6[2368])|8(?:1[236-8]|2[5-7]|3|5[1-9]|7[02-9]|8[36-8]|9[1-7])|9(?:0[1-3689]|1[1-79]|[379]|4[13]|5[1-5])']),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['3(?:11|7[179])|4(?:[15]1|3[1-35])|5(?:1|2[37]|3[12]|51|7[13-79]|9[15])|7(?:[39]1|5[457]|6[09])|8(?:[57]1|98)']),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['807', '8078']),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:[3-57-9]|66)']),
        NumberFormat(pattern='(10800)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['108', '1080', '10800']),
        NumberFormat(pattern='(\\d{3})(\\d{7,8})', format='\\1 \\2', leading_digits_pattern=['950'])])
