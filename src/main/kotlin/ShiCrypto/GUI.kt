package ShiCrypto

import jsonParser.API
import jsonParser.APIInfo
import jsonParser.APIJson
import java.awt.*
import java.awt.event.*
import javax.swing.*

class GUI: JFrame() {
    init {
        createGUI("ShiCrypto")
    }

    private fun createGUI(titleInput: String) {
        title = titleInput
        isVisible = true
        defaultCloseOperation = WindowConstants.EXIT_ON_CLOSE
        setSize(1000, 600)
        setLocationRelativeTo(null)

        contentPane=JPanel()
        contentPane.layout=BorderLayout()

        // add panel of whole UI
        val panel = JPanel()
        panel.addContainerListener(object : ContainerAdapter() {
            override fun componentRemoved(e: ContainerEvent?) {}
        })
        val gblPanel=GridBagLayout()
        gblPanel.columnWeights=doubleArrayOf(1.0, Double.MIN_VALUE)
        gblPanel.rowWeights=doubleArrayOf(1.0, Double.MIN_VALUE)
        panel.layout=gblPanel
        // contentPane add panel
        contentPane.add(panel, BorderLayout.CENTER)

        // tabbed pane at top of panel
        val tabbedPane = JTabbedPane(JTabbedPane.TOP)
        val gbcTabbedPane=GridBagConstraints()
        gbcTabbedPane.fill=GridBagConstraints.BOTH
        gbcTabbedPane.gridheight=0
        gbcTabbedPane.gridx=0
        gbcTabbedPane.gridy=0
        panel.add(tabbedPane, gbcTabbedPane)

        // get json info from APIInfo
        val apiPath: String = "D:\\Projects\\Gitexercise\\ShiCrypto\\plugin\\\\api\\\\api.json"
        val apiInfoObj = APIInfo(apiPath)
        val apiJson = apiInfoObj.getInfoFromAPIJson()
        addModuleTabbedPanelFromAPIJson(tabbedPane, apiJson)
    }

    private fun addModuleTabbedPanelFromAPIJson(tabbedPane: JTabbedPane, apiJson: APIJson?) {
        // emm !!. or ?.
        val apiArray: List<API> = apiJson!!.api
        for (api in apiArray) {
            val tabbedPanelModuleTmp = JTabbedPane(JTabbedPane.TOP)
            addFuncTabbedPanelFromAPI(tabbedPanelModuleTmp, api)
            tabbedPane.addTab(api.name, null, tabbedPanelModuleTmp, null)
        }
    }

    private fun addFuncTabbedPanelFromAPI(tabbedPanelModule: JTabbedPane, api: API) {
        for (func in api.func) {
            val tabbedPaneFuncTmp = JTabbedPane(JTabbedPane.TOP)
            tabbedPanelModule.addTab(func.name, null, tabbedPaneFuncTmp, null)
        }
    }
}