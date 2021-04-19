def remove_char_at(str, n):
    if n >= 0:
        str = ("{:s}{:s}".format(str[:n], str[n+1:]))
    else:
        str
    return str
