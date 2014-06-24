__author__ = 'james'

# //---- SERIAL PORT ---------------------------------------------------------------
# #define USART_WORD_LENGTH_8B                ((unsigned short)0x0000)
# #define USART_WORD_LENGTH_9B                ((unsigned short)0x1000)
#
# #define USART_STOP_BITS_1                   ((unsigned short)0x0000)
# #define USART_STOP_BITS_0_5                 ((unsigned short)0x1000)
# #define USART_STOP_BITS_2                   ((unsigned short)0x2000)
# #define USART_STOP_BITS_1_5                 ((unsigned short)0x3000)
#
# #define USART_PARITY_NO                     ((unsigned short)0x0000)
# #define USART_PARITY_EVEN                   ((unsigned short)0x0400)
# #define USART_PARITY_ODD                    ((unsigned short)0x0600)
#
# #define USART_HARDWARE_FLOW_CONTROL_NONE    ((unsigned short)0x0000)
# #define USART_HARDWARE_FLOW_CONTROL_RTS     ((unsigned short)0x0100)
# #define USART_HARDWARE_FLOW_CONTROL_CTS     ((unsigned short)0x0200)
# #define USART_HARDWARE_FLOW_CONTROL_RTS_CTS ((unsigned short)0x0300)
#
# #define USART_MODE_RX                       ((unsigned short)0x0004)
# #define USART_MODE_TX                       ((unsigned short)0x0008)
#
# #define RX_QUEUE_SIZE 64
# #define TX_QUEUE_SIZE 64
#
# void OpenSerialPort(unsigned char ucPort, unsigned long ulBaudRate);
# void OpenSerialPortEx(unsigned char ucPort, unsigned long ulBaudRate,
# unsigned short usWordLength,
# unsigned short usStopBits,
#                       unsigned short usParity,
#                       unsigned short usHardwareFlowControl,
#                       unsigned short usMode);
# unsigned char ReadSerialPort(unsigned char ucPort);
# void WriteSerialPort(unsigned char ucPort, char cData);
# unsigned char GetSerialPortByteCount(unsigned char ucPort);