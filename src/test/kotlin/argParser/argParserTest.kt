package argParser

import org.junit.Test

class ArgParserTest {
    @Test fun argParserTest() {
        val ap = ArgParser()
        ap.inputParse("b0 = 1\nb1 = 2\nb2 = 3\n")
    }
}