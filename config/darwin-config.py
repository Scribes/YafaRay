
PREFIX = '/usr/local'
CCFLAGS = '-Wall -fno-common'
REL_CCFLAGS = '-O2 -ffast-math'
DEBUG_CCFLAGS = '-ggdb'
YF_SHLINKFLAGS = '-undefined dynamic_lookup'
YF_LIBOUT = '${PREFIX}/lib'
YF_PLUGINPATH = '${PREFIX}/lib/yafaray'
YF_BINPATH = '${PREFIX}/bin'

BASE_LPATH = '/usr/lib'
BASE_IPATH = '/usr/include'

### pthreads
YF_PTHREAD_LIB = 'pthread'

### OpenEXR
YF_EXR_INC = '${BASE_IPATH}/OpenEXR'
YF_EXR_LIB = 'Half Iex Imath IlmImf IlmThread'
YF_EXR_LIBPATH = '${BASE_LPATH}'

### libXML
YF_XML_INC = '${BASE_IPATH}/libxml2'
YF_XML_LIB = 'xml2'

### JPEG
YF_JPEG_INC = ''
YF_JPEG_LIB = 'jpeg'

### PNG
WITH_YF_PNG = 'true'
YF_PNG_INC = ''
YF_PNG_LIB = 'png'

### TIFF
WITH_YF_TIFF = 'true'
YF_TIFF_INC = ''
YF_TIFF_LIB = 'tiff'

### zlib
WITH_YF_ZLIB = 'true'
YF_ZLIB_INC = ''
YF_ZLIB_LIB = 'z'

### Freetype 2
WITH_YF_FREETYPE = 'true'
YF_FREETYPE_INC = '${BASE_IPATH}/freetype2'
YF_FREETYPE_LIB = 'freetype'

### Miscellaneous
YF_MISC_LIB = 'dl'

### Qt
YF_QTDIR = '/usr'
YF_QT4_LIB = '' # added through framework var

