package ShiCrypto

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

        val Crypto = JScrollPane()
        //Crypto.addChangeListener { textArea=(Crypto.selectedComponent as JScrollPane).viewport.view as JTextArea }
        tabbedPane.addTab("Crypto", null, Crypto, null)
    }
}