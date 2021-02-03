package argParser

class ArgParser() {
    fun inputParse(input: String): ArrayList<List<String>> {
        val inputLst: List<String> = input.split("\n")
        val res = ArrayList<List<String>>()
        inputLst.filter { it.isNotEmpty() }
                .forEach { res.add(it.split("=")) }
        return res
    }
}