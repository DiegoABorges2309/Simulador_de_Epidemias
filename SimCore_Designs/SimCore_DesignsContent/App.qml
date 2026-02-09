import QtQuick
import SimCore_Designs

Window {
    id: window
    width: Constants.width
    height: Constants.height

    minimumWidth: 1024
    minimumHeight: 600

    visible: true
    visibility: Window.Maximized
    title: "SimCore_Designs"

    Screen01 {
        id: mainScreen
        anchors.fill: parent
    }
}

