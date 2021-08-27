from stateIO import stateReset,stateRead,stateReadJSON


def stateReadFun():
    gar, gat = stateReadJSON()
    garStr = 'gar'+str(gar)
    gatStr = 'gat'+str(gat)
    return (garStr,gatStr)


if __name__ == '__main__':
    stateReadFun()
