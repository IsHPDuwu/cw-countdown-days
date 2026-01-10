import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import RinUI
import ClassWidgets.Plugins

SettingsLayout {
    SettingCard {
        Layout.fillWidth: true
        title: "目标日期与标题"
        description: "Target date and title for the countdown."

        RowLayout {
            TextField {
                Layout.fillWidth: true
                id: textField
                text: settings.target_title
                onTextChanged: {
                    settings.target_title = text
                }
            }
            CalendarDatePicker {
                id: datePicker
                selectedDate: new Date(settings.target_date)
                onSelectedDateChanged: {
                    settings.target_date = Qt.formatDate(selectedDate, "yyyy-MM-dd")
                }
            }
        }
    }

    SettingCard {
        Layout.fillWidth: true
        title: "显示小数点"
        description: "Show decimal places in the countdown."

        Switch {
            checked: settings.show_decimal
            onCheckedChanged: {
                settings.show_decimal = checked
            }
        }
    }
}