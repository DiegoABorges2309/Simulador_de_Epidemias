import QtQuick
import QtQuick.Controls
import SimCore_Designs

Rectangle {
    id: rectangle2
    property color bg_color_base_dark: '#121316'
    property color bg_color_base: '#181a1e'
    property color color_base: '#363943'
    property color color_text: '#d0d4e4'

    color: bg_color_base_dark

    // Rectangle {
    //     x: -300
    //     width: 300
    //     height: App.height * 0.975
    //     anchors.left: anchors.left
    //     color: bg_color_base
    //     radius: 20
    //     anchors.verticalCenter: parent.verticalCenter
    // }
    Rectangle {
        id: rectangle1
        x: 0
        width: 65
        color: bg_color_base
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.topMargin: 0
        anchors.bottomMargin: 0

        Image {
            id: background_biohazard_2
            y: 16
            width: 60
            height: 60
            opacity: 0.8
            source: "images/background_biohazard_logo.png"
            anchors.horizontalCenter: parent.horizontalCenter
            fillMode: Image.PreserveAspectFit
            antialiasing: true
            smooth: true
            mipmap: true
        }

        Button {
            id: button
            x: 0
            y: 655
            width: 65
            height: 65
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            icon.height: 60
            icon.width: 60
            icon.cache: true
            icon.color: "#373a44"
            icon.source: "images/play.png"
            display: AbstractButton.IconOnly
            highlighted: false
            flat: true
        }
    }

    Rectangle {
        x: -350
        width: 300
        height: 563
        color: bg_color_base
        radius: 18
        anchors.verticalCenter: parent.verticalCenter
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 77
        anchors.verticalCenterOffset: 2
    }

    Rectangle {
        x: 930
        width: 275
        height: 720
        color: bg_color_base
        anchors.verticalCenter: parent.verticalCenter
        anchors.right: parent.right
        anchors.rightMargin: 0
        anchors.verticalCenterOffset: 2
    }

    Rectangle {
        id: rectangle
        color: "#121316"
        radius: 18
        border.color: "#81363943"
        border.width: 2
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: 99
        anchors.rightMargin: 304
        anchors.topMargin: 35
        anchors.bottomMargin: 35

        Image {
            id: image
            width: 500
            opacity: 0.35
            source: "images/background_biohazard.png"
            anchors.centerIn: parent
            fillMode: Image.PreserveAspectCrop
        }

        Text {
            id: text1
            color: color_text
            text: qsTr("Esperando datos epidemiológicos")
            font.pixelSize: 16
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.styleName: "Regular"
            font.family: "Google Sans"
            anchors.centerIn: parent
        }
    }
}
