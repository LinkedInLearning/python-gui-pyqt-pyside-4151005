import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: appWindow
    visible: true
    width: 400
    height: 300
    title: "QML + Python Backend"

    Column {
        anchors.centerIn: parent
        spacing: 20

        Text {
            id: label
            text: "Hallo Welt!"
            font.pointSize: 20
        }

        Button {
            text: "Klicke mich"
            onClicked: backend.button_clicked()
        }
    }
}
