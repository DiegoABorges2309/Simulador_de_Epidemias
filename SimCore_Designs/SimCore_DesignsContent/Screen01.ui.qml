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
            opacity: 0.75
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

        Button {
            id: button1
            y: 175
            width: 60
            height: 60
            text: qsTr("Button")
            icon.color: "#5bcbcfde"
            // background: Rectangle {
            //     color: '#2e3239'
            //     opacity: 0.25
            // }
            icon.height: 80
            icon.width: 80
            icon.source: "images/add.png"
            flat: true
            display: AbstractButton.IconOnly
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Button {
            id: button3
            x: 610
            y: 235
            width: 60
            height: 60
            text: qsTr("Button")
            icon.width: 80
            icon.source: "images/history.png"
            icon.height: 80
            icon.color: "#5bcbcfde"
            flat: true
            display: AbstractButton.IconOnly
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    Rectangle {
        x: 85
        width: 300
        color: bg_color_base
        radius: 18
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.topMargin: 26
        anchors.bottomMargin: 74
        z: 2

        Text {
            id: text4
            x: 22
            y: 25
            width: 181
            height: 27
            color: color_text
            text: qsTr("Crear Simulacion")
            font.pixelSize: 22
            font.weight: Font.Bold
            font.family: "Google Sans"
        }

        Text {
            id: text5
            x: 22
            y: 72
            color: color_text
            text: qsTr("Virus:")
            font.pixelSize: 16
            font.family: "Google Sans"
        }

        TextField {
            id: textoNombre
            x: 22
            y: 103
            persistentSelection: false
            overwriteMode: false
            readOnly: false
            cursorVisible: false
            font.family: "Google Sans"
            font.pointSize: 13
            width: 225
            height: 37
            color: color_text
            placeholderTextColor: "#4dffffff"
            placeholderText: "Nombre del Virus"
            background: Rectangle {
                color: bg_color_base
                radius: 12
                border.color: "#5bcbcfde"
                border.width: 1
            }
        }

        Text {
            id: text6
            x: 22
            y: 162
            color: color_text
            text: "Tipo de Transmisión"
            font.pixelSize: 16
            font.family: "Google Sans"
        }

        ComboBox {
            id: tipo_de_contagio
            x: 22
            y: 200
            width: 225
            height: 37
            font.pointSize: 13
            font.family: "Google Sans"
            model: ["hola", "epa"]

            background: Rectangle {
                id: bg_rec
                color: bg_color_base
                radius: 12
                border.color: "#5bcbcfde"
                border.width: 1
            }
        }

        Text {
            id: text7
            x: 22
            y: 259
            color: color_text
            text: "Tasa de Letalidad"
            font.pixelSize: 16
            font.family: "Google Sans"
        }

        TextField {
            id: tasaLetalidad
            x: 22
            y: 292
            width: 83
            height: 37
            color: color_text
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignBottom
            maximumLength: 5
            readOnly: false
            persistentSelection: false
            overwriteMode: false
            font.pointSize: 13
            font.family: "Google Sans"
            cursorVisible: false
            background: Rectangle {
                id: rectangle4
                color: bg_color_base
                radius: 12
                border.color: "#5bcbcfde"
                border.width: 1
                Text {
                    x: 59
                    color: color_text
                    text: "%"
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 20
                    anchors.verticalCenterOffset: 2
                    font.family: "Google Sans"
                }
            }
        }
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

        Rectangle {
            id: rectangle5
            color: "#181a1e"
            radius: 18
            border.color: "#a4363943"
            border.width: 1
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.leftMargin: 20
            anchors.rightMargin: 20
            anchors.topMargin: 40
            anchors.bottomMargin: 45
        }

        Text {
            id: text3
            color: color_text
            text: qsTr("Sin datos activos")
            font.pixelSize: 16
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.centerIn: parent
            font.family: "Google Sans"
            x: 100
        }
    }

    Rectangle {
        // #81363943
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

    Rectangle {
        id: rectangle3
        color: "#121316"
        radius: 18
        border.color: "#81363943"
        border.width: 1
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: 99
        anchors.rightMargin: 304
        anchors.topMargin: 35
        anchors.bottomMargin: 35
        Image {
            id: image1
            width: 500
            opacity: 0.35
            source: "images/background_biohazard.png"
            fillMode: Image.PreserveAspectCrop
            anchors.centerIn: parent
        }

        Text {
            id: text2
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
