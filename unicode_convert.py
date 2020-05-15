# covert unicode composite to unicode
def convert(uc):
    unicode_composite_character = ['á', 'ả', 'ã', 'à', 'ạ',
        'ắ', 'ẳ', 'ẵ', 'ằ', 'ặ',
        'ấ', 'ẩ', 'ẫ', 'ầ', 'ậ',
        'é', 'ẻ', 'ẽ', 'è', 'ẹ',
        'ý', 'ỷ', 'ỹ', 'ỳ', 'ỵ',
        'ú', 'ủ', 'ũ', 'ù', 'ụ',
        'í', 'ỉ', 'ĩ', 'ì', 'ị',
        'ó', 'ỏ', 'õ', 'ò', 'ọ',
        'ố', 'ổ', 'ỗ', 'ồ', 'ộ',
        'ớ', 'ở', 'ỡ', 'ờ', 'ợ'
    ]

    unicode_character = ['á', 'ả', 'ã', 'à', 'ạ',
        'ắ', 'ẳ', 'ẵ', 'ằ', 'ặ',
        'ấ', 'ẩ', 'ẫ', 'ầ', 'ậ',
        'é', 'ẻ', 'ẽ', 'è', 'ẹ',
        'ý', 'ỷ', 'ỹ', 'ỳ', 'ỵ',
        'ú', 'ủ', 'ũ', 'ù', 'ụ',
        'í', 'ỉ', 'ĩ', 'ì', 'ị',
        'ó', 'ỏ', 'õ', 'ò', 'ọ',
        'ố', 'ổ', 'ỗ', 'ồ', 'ộ',
        'ớ', 'ở', 'ỡ', 'ờ', 'ợ'
    ]

    for i in range(len(unicode_character)):
        uc = uc.replace(unicode_composite_character[i], unicode_character[i])
    return uc
# so sánh chuỗi ở 2 bảng mã khác nhau
def compare(s1, s2):
    return convert(s1) == convert(s2)

# Test
s1 = 'bùi ngọc dương'
s2 = 'bùi ngọc dương'


print(compare(s2, s1))