def rom2dec(roman: str) -> int:
  ''' Convert Roman numerals to decimal
  '''
    convert = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    roman = roman.upper()
    dec = 0
    for n in range(len(roman) -1, -1, -1):
        if n == len(roman) - 1:
            dec += convert[roman[n]]
        else:
            right = convert[roman[n+1]]
            left = convert[roman[n]]
            if right > left:
                dec -= left
            else:
                dec += left
    return dec

if __name__ == '__main__':
  rom2dec('XCII')
