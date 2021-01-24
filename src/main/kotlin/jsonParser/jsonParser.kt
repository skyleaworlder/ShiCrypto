package jsonParser

import com.squareup.moshi.JsonClass
import com.squareup.moshi.Moshi
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import java.io.File

@JsonClass(generateAdapter = true)
data class APIJson(
    var api: List<API>
)

data class API(
    val name: String,
    val id: String,
    val path: String,
    val func: List<APIFunc>
)

data class APIFunc(
    val name: String,
    val id: String,
    val help: String,
    val column: APIColumn,
    val param: List<APIParam>
)

data class APIColumn(
    val num: Int,
    val input: List<APIColumnInput>
)

data class APIColumnInput(
    val name: String,
    val inf: Boolean
)

data class APIParam(
    val option: List<String>,
    val pos: Int
)

class APIInfo(path: String) {

    private val apiPath: String = path
    internal var api = getInfoFromAPIJson()

    fun getInfoFromAPIJson(): APIJson? {
        val ms = Moshi.Builder()
                .add(KotlinJsonAdapterFactory())
                .build()
        val msAdapter = ms.adapter(APIJson::class.java)
        val f = File(apiPath)
        val json = f.readText()
        return msAdapter.fromJson(json)
    }
}