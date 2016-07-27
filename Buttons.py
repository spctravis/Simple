__buttonA = 5
__buttonB = 6
__buttonC = 13
__buttonReset = 26

button = [__buttonA, __buttonB, __buttonC, __buttonReset]

__code = {__buttonA: "a", __buttonB: "b", __buttonC: "c"}

def is_reset(channel):
    return channel == __buttonReset

def get_code(channel):
    return __code[channel]