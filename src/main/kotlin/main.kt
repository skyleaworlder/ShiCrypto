import org.python.util.PythonInterpreter
import org.python.core.*
import java.util.*

import ShiCrypto.GUI

fun main() {
    // for test, demonstrate it.
    val f = GUI()
    val props = Properties()
    props.setProperty("D:\\python\\Python27\\python.exe", "D:\\Projects\\Gitexercise\\ShiCrypto")
    PythonInterpreter.initialize(System.getProperties(), props, arrayOf(".py","--add", "4", "5", "9"))
    val interpreter = PythonInterpreter()
    interpreter.exec("import sys")
    interpreter.exec("sys.path.append('D:\\Projects\\Gitexercise\\ShiCrypto\\plugin\\\\api')")
    interpreter.exec("print sys.path")
    interpreter.exec("print sys.argv")
    interpreter.execfile("D:\\Projects\\Gitexercise\\ShiCrypto\\plugin\\api\\Calcu.py")
}