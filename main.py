huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_OBJECT_RECOGNITION)

def on_forever():
    huskylens.request()
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        pins.digital_write_pin(DigitalPin.P11, 1)
        basic.show_icon(IconNames.HAPPY)
    else:
        pins.digital_write_pin(DigitalPin.P11, 0)
        basic.show_icon(IconNames.ASLEEP)
basic.forever(on_forever)
