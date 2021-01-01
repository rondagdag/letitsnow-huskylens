
huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.ALGORITHM_OBJECT_TRACKING)

basic.forever(function () {
    huskylens.request()
    if (huskylens.isAppear(1, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
        pins.digitalWritePin(DigitalPin.P11, 1)
        basic.showIcon(IconNames.Happy)
    } else {
        pins.digitalWritePin(DigitalPin.P11, 0)
        basic.showIcon(IconNames.Asleep)
    }
})
