import textwrap

import gemmi


def quote(string: str, wrapping=80) -> str:
    """
    Quotes a cif string and wraps it. The shorter strings are directly handled by cif.quote().
    """
    if len(string) < 80:
        return gemmi.cif.quote(string)
    lines = '\n'
    for line in string.split('\n'):
        if len(line) > wrapping:
            line = textwrap.fill(line, width=wrapping)
            lines += line + '\n'
        else:
            lines += line + '\n'
    quoted = gemmi.cif.quote(lines.rstrip('\n'))
    return quoted


charcters = { 
    '±'      : r'+-',
    '×'      : r'\\times',
    '≠'      : r'\\neq',
    '→'      : '\\rightarrow',
    '←'      : '\\leftarrow',
    '∞'      : '\\infty',
    '≈'      : '\\sim',
    '≃'      : '\\simeq',
    'ß'      : r'\&s',
    'ü'      : r'u\"',
    'Ü'      : r'U\"',
    'ö'      : r'o\"',  # 'LATIN SMALL LETTER O WITH DIAERESIS'
    'Ö'      : r'O\"',
    'ä'      : r'a\"',
    'Ä'      : r'a\"',
    'é'      : r"\'e",
    'É'      : r"\'E",
    'è'      : r'\`e',
    'È'      : r'\`E',
    'ó'      : r"\'o",
    'Ó'      : r"\'O",
    'ò'      : r'\`o',
    'Ò'      : r'\`O',
    'ȯ'      : r'\.o',
    'ø'      : r'\/o',
    'á'      : r'\'a',
    'Á'      : r'\'A',
    'à'      : r'\`a',
    'À'      : r'\`A',
    'â'      : r'\^a',
    'Â'      : r'\^A',
    'å'      : r'\%a',
    'ê'      : r'\^e',
    'î'      : r'\^i',
    'Î'      : r'\^I',
    'ô'      : r'\^o',
    'Ô'      : r'\^O',
    'û'      : r'\^u',
    'Û'      : r'\^U',
    'ç'      : r'\,c',
    'ñ'      : r'\~n',
    'ł'      : r'\/l',
    'đ'      : r'\/d',
    'Å'      : r'\%A',  # 'LATIN CAPITAL LETTER A WITH RING ABOVE'
    'Å'      : r'\%A',  # unicodedata.name('Å'): 'ANGSTROM SIGN'
    u'\u2079': r'^9^',
    u'\u2078': r'^8^',
    u'\u2077': r'^7^',
    u'\u2076': r'^6^',
    u'\u2075': r'^5^',
    u'\u2074': r'^4^',
    u'\u00B3': r'^3^',
    u'\u00B2': r'^2^',
    u'\u2081': r'~1~',
    u'\u2082': r'~2~',
    u'\u2083': r'~3~',
    u'\u2084': r'~4~',
    u'\u2085': r'~5~',
    u'\u2086': r'~6~',
    u'\u2087': r'~7~',
    u'\u2088': r'~8~',
    u'\u2089': r'~9~',
    u'\u0131': r'\?i',
    u"\u03B1": r'\a',  # alpha
    u"\u03B2": r'\b',  # beta
    u"\u03B3": r'\g',  # ...
    u"\u03B4": r'\d',
    u"\u03B5": r'\e',
    u"\u03B6": r'\z',
    u"\u03B7": r'\h',
    u"\u03B8": r'\q',
    u"\u03B9": r'\i',
    u"\u03BA": r'\k',
    u"\u03BB": r'\l',
    u"\u03BC": r'\m',
    u"\u03BD": r'\n',
    u"\u03BE": r'\x',
    u"\u03BF": r'\o',
    u"\u03C0": r'\p',
    u"\u03C1": r'\r',
    u"\u03C3": r'\s',
    u"\u03C4": r'\t',
    u"\u03C5": r'\u',
    u"\u03C6": r'\F',
    u"\u03C9": r'\w',
    u"\u03A9": r'\W',
    u"\u03D5": r'\f',
    u"\u00B0": r"\%",
    # "1̄": r'\=1',  # Does not work in QT?
}


def set_pair_delimited(block, key: str, txt: str):
    """
    Converts special characters to their markup counterparts.
    """
    txt = utf8_to_str(txt)
    try:
        # bad hack to get the numbered values correct
        float(txt)
        block.set_pair(key, txt)
    except (TypeError, ValueError):
        # prevent _key '?' in cif:
        if txt == '?':
            block.set_pair(key, txt)
        else:
            block.set_pair(key, quote(txt))


def utf8_to_str(txt) -> str:
    """
    Translates an utf-8 text to a CIF ascii string.
    """
    for char in txt:
        if char in charcters:
            txt = txt.replace(char, charcters[char])
    return txt


def retranslate_delimiter(txt: str) -> str:
    """
    Translates delimited cif characters back to unicode characters.
    """
    inv_map = {v: k for k, v in charcters.items()}
    for char in inv_map.keys():
        txt = txt.replace(char, inv_map[char])
    return txt
