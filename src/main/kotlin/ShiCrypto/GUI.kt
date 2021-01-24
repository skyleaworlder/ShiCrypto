package ShiCrypto

import jsonParser.API
import jsonParser.APIFunc
import jsonParser.APIInfo
import jsonParser.APIJson
import java.awt.*
import java.awt.event.*
import javax.swing.*
import javax.swing.border.Border

class GUI: JFrame() {
    init {
        createGUI("ShiCrypto")
    }

    private fun createGUI(titleInput: String) {
        // total info
        title = titleInput
        isVisible = true
        defaultCloseOperation = WindowConstants.EXIT_ON_CLOSE
        isResizable = false
        setSize(1000, 600)
        setLocationRelativeTo(null)

        contentPane=JPanel()
        contentPane.layout=BorderLayout()

        // add panel of whole UI
        val panel = JPanel()
        val gblPanel=GridBagLayout()
        gblPanel.columnWeights=doubleArrayOf(1.0, Double.MIN_VALUE)
        gblPanel.rowWeights=doubleArrayOf(1.0, Double.MIN_VALUE)

        panel.layout=gblPanel
        // contentPane add panel
        // PAGE_START is important
        contentPane.add(panel, BorderLayout.PAGE_START)

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
            val gbcTabbedPaneModule = GridBagConstraints()
            val tabbedPanelModuleTmp = JTabbedPane(JTabbedPane.TOP)
            tabbedPane.add(tabbedPanelModuleTmp, gbcTabbedPaneModule)

            addFuncTabbedPanelFromAPI(tabbedPanelModuleTmp, api)
            tabbedPane.addTab(api.name, null, tabbedPanelModuleTmp, null)
        }
    }

    private fun addFuncTabbedPanelFromAPI(tabbedPanelModule: JTabbedPane, api: API) {
        for (func in api.func) {
            val gbcTabbedPaneFunc = GridBagConstraints()
            gbcTabbedPaneFunc.anchor = GridBagConstraints.NORTHWEST
            val tabbedPaneFuncTmp = JPanel()
            tabbedPanelModule.add(tabbedPaneFuncTmp, gbcTabbedPaneFunc)

            addWindowsFromAPI(tabbedPaneFuncTmp, func)
            tabbedPanelModule.addTab(func.name, null, tabbedPaneFuncTmp, null)
        }
    }

    private fun addWindowsFromAPI(tabbedPanelFunc: JPanel, func: APIFunc) {
        // set layout of input func-tabbed-panel
        tabbedPanelFunc.layout = GridBagLayout()

        // set gbc of func-tabbed-panel
        val g = GridBagConstraints()
        g.weightx = 0.5
        g.ipadx = 0
        g.fill = GridBagConstraints.BOTH
        g.anchor = GridBagConstraints.NORTHWEST
        g.insets = Insets(0,0,0,0)
        g.gridx = 0
        g.gridy = 0

        var i: Int = 0
        while (i < func.column.num+1) {
            g.gridx = i
            println(i)
            val tmpScrollPane = JScrollPane()

            // column param in input panel
            var tmpTextContent: String = ""
            // column param is infinite list
            if (i < func.column.num && func.column.input[i].inf) {
                for (j in 0..2 step 1) {
                    tmpTextContent += (func.column.input[i].name + j.toString() + " = \n")
                }
            } else if (i < func.column.num) {
                for (input in func.column.input) {
                    tmpTextContent += (input.name + " = \n")
                }
            }

            val tmpTextArea = JTextArea(tmpTextContent)
            tmpTextArea.lineWrap = true
            tmpTextArea.rows = 18
            tmpTextArea.font = Font("黑体", Font.PLAIN, 20)

            tmpScrollPane.setViewportView(tmpTextArea)
            tabbedPanelFunc.add(tmpScrollPane, g)
            i += 1
        }

        val helpTextField = JTextField(func.help)
        val gbcHelpTextField = GridBagConstraints()
        gbcHelpTextField.fill = GridBagConstraints.BOTH
        gbcHelpTextField.ipady = 50
        gbcHelpTextField.gridx = 0
        gbcHelpTextField.gridy = 1
        gbcHelpTextField.gridwidth = 0
        tabbedPanelFunc.add(helpTextField, gbcHelpTextField)
    }
}