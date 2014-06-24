# -*- coding: utf-8 -*-
__author__ = 'james'

# void PrintTextToGD(unsigned char ucRow, unsigned char ucCol, unsigned long ulColor, const char *szText, ...);
# void PrintFrameToGD(unsigned char ucRow1, unsigned char ucCol1, unsigned char ucRow2, unsigned char ucCol2, unsigned long ulColor);


class GDFrame():
    """
    定义图形显示界面的一个矩形区域。四个参数依次为：左上角点的行/列，右下角点的行/列。

    """

    def __init__(self, row1, col1, row2, col2):
        self.row1 = row1
        self.col1 = col1
        self.row2 = row2
        self.col2 = col2


def reset():
    """
    void ResetGD(void);
    :return:
    """

    return_r = "void ResetGD(void);"
    print(return_r)
    return return_r


def clear_area_text(frame):
    """
    void ClearGD(unsigned char ucRow1, unsigned char ucCol1, unsigned char ucRow2, unsigned char ucCol2, unsigned char ucFrame);
    :param frame:
    :return:
    """
    # try:
    return_r = 'ClearGD(' + str(frame.row1) + ', ' + str(frame.col1) + ', ' + str(frame.row2) + ', ' + str(frame.col2) \
               + ', 0);'
    print(return_r)
    return return_r
    # except AttributeError as e:
    #sys.exit("clear_area: Not a frame.")


def clear_area_frame(frame):
    """
    void ClearGD(unsigned char ucRow1, unsigned char ucCol1, unsigned char ucRow2, unsigned char ucCol2, unsigned char ucFrame);
    :param frame:
    :return:
    """
    # try:
    return_r = 'ClearGD(' + str(frame.row1) + ', ' + str(frame.col1) + ', ' + str(frame.row2) + ', ' + str(frame.col2) \
               + ', 1);'
    print(return_r)
    return return_r
    # except AttributeError as e:
    #sys.exit("clear_area: Not a frame.")


if __name__ == '__main__':
    a = GDFrame(1, 1, 3, 5)
    clear_area_text(a)
    clear_area_frame(a)