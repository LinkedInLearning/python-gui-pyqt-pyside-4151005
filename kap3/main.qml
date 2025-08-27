import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "QML mit Python-Backend"

    Column {
        anchors.centerIn: parent
        spacing: 20

        Text {
            id: label
            text: "Hallo Welt!"
            font.pointSize: 20
            horizontalAlignment: Text.AlignHCenter
        }

        Button {
            text: "Klicke mich"
            onClicked: {
                // Python-Funktion wird aufgerufen
                label.text = backend.change_text()
            }
        }
    }
}
