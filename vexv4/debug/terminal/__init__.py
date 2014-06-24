# -*- coding: utf-8 -*-
__author__ = 'james'


def printf(*strings):
    """
    void PrintToScreen(const char *fmt, ...);

    :rtype : object
    :param *strings: anything to be converted into strings
    :return: C source
    """
    output = ''
    for content in strings:
        output += str(content)

    return_r = 'PrintToScreen("%s", "' + output + '");'
    print(return_r)
    return return_r


if __name__ == "__main__":
    # test
    printf(1, 2, 3)
    printf("a", "b", "c")
    printf(1, "a", 2)