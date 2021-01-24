package jsonParser

import com.squareup.moshi.Moshi
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import org.junit.Test

class JsonParserTest {

    @Test
    fun jsonParser() {
        println("This is jsonParserTest")
        val json = """
        {
          "api": [
            {
              "name": "CRT",
              "id": "50712f7ea0e9a5641483f7a60c06c11712404f8a",
              "path": "./src/CRT.py",
              "func": [
                {
                  "name": "CRT",
                  "id": "ac2165fd21d3580257b7a1bd636f4973d13984f0",
                  "help": "Usage: python CRT.py [<b-list>] -- [<m-list>]\n eg. python CRT.py 1 2 -- 4 5",
                  "column": {
                    "num": 2,
                    "input": [
                      { "name": "b", "inf": true },
                      { "name": "p", "inf": true }
                    ]
                  },
                  "param": [
                    { "option": ["--"], "pos": 1 }
                  ]
                }
              ]
            }
          ]
        }
        """

        val moshi = Moshi.Builder()
            .add(KotlinJsonAdapterFactory())
            .build()

        val issueAdapter = moshi.adapter(APIJson::class.java)

        val parsed = issueAdapter.fromJson(json)

        println(parsed)
        println(parsed!!.api[0].func[0].help)
    }

    @Test
    fun APIInfoTest() {
        println("This is APIInfoTest")
        val inf = APIInfo("D:\\Projects\\Gitexercise\\ShiCrypto\\plugin\\\\api\\\\api.json")
        println(inf.getInfoFromAPIJson())
    }

}