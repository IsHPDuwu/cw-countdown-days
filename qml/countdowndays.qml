import QtQuick
import QtQuick.Controls
import QtQuick.Window as QQW
import QtQuick.Layouts
import RinUI
import Widgets


Widget {
    id: root
    text: settings.target_title ? qsTr("距 %1 还有").arg(settings.target_title) : qsTr("倒数日")

    RowLayout {
        anchors.centerIn: parent
        spacing: 10
        AnimatedDigits {
            id: countdown
            value: backend.calculateCountdownDays(settings.target_date, settings.show_decimal, settings.target_title)
        }
        Title {
            Layout.bottomMargin: font.pixelSize * 0.1
            text: qsTr("天")
        }
    }

    // Component.onCompleted: {
    //     Qt.callLater(function() {
    //         backend.calculateCountdownDays(settings.target_date, settings.show_decimal, settings.target_title)
    //     })
    // }
}