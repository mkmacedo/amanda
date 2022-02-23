def floatfy(rCurrentValue):
    splitCurrentValue = rCurrentValue.split('.')
    currentValue = ''
    for cSlice in splitCurrentValue:
        currentValue += cSlice
    comma = currentValue.find(',')
    if comma != -1:
        currentValue = currentValue[:comma]+'.'+currentValue[comma+1:]

    return eval(currentValue)