##
##

# File auto-generated against equivalent DynamicSerialize Java class and
# modified.
#
#      SOFTWARE HISTORY
#
#     Date            Ticket#       Engineer       Description
#     ------------    ----------    -----------    --------------------------
#     Sep 8, 2014                   kustert        Initial Creation
#     Apr 24, 2015    4425          nabowle        Bring in.

class DoubleDataRecord(object):

    def __init__(self):
        self.sizes = None
        self.dimension = None
        self.maxChunkSize = None
        self.name = None
        self.fillValue = None
        self.dataAttributes = None
        self.group = None
        self.minIndex = None
        self.props = None
        self.doubleData = None
        self.maxSizes = None

    def getSizes(self):
        return self.sizes

    def setSizes(self, sizes):
        self.sizes = sizes

    def getDimension(self):
        return self.dimension

    def setDimension(self, dimension):
        self.dimension = dimension

    def getMaxChunkSize(self):
        return self.maxChunkSize

    def setMaxChunkSize(self, maxChunkSize):
        self.maxChunkSize = maxChunkSize

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getFillValue(self):
        return self.fillValue

    def setFillValue(self, fillValue):
        self.fillValue = fillValue

    def getDataAttributes(self):
        return self.dataAttributes

    def setDataAttributes(self, dataAttributes):
        self.dataAttributes = dataAttributes

    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group

    def getMinIndex(self):
        return self.minIndex

    def setMinIndex(self, minIndex):
        self.minIndex = minIndex

    def getProps(self):
        return self.props

    def setProps(self, props):
        self.props = props

    def getDoubleData(self):
        return self.doubleData

    def setDoubleData(self, doubleData):
        self.doubleData = doubleData

    def getMaxSizes(self):
        return self.maxSizes

    def setMaxSizes(self, maxSizes):
        self.maxSizes = maxSizes

    def retrieveDataObject(self):
        return self.getDoubleData()

    def putDataObject(self, obj):
        self.setDoubleData(obj)
