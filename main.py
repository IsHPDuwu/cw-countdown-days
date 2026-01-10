"""
Countdown Days
Class Widgets 2 倒计日插件/ Countdown Days Plugin
"""

from ClassWidgets.SDK import CW2Plugin, PluginAPI
from datetime import datetime, timedelta

from PySide6.QtCore import Slot
from loguru import logger


class Plugin(CW2Plugin):
    def __init__(self, api: PluginAPI):
        super().__init__(api)
        self.notification_provider = None
        # 请在此导入第三方库 / Import third-party libraries here

    @Slot(str, bool, str, result=float)
    def calculateCountdownDays(self, target_date: str, decimal_point: bool = False, target_title: str = ""):
        """
        计算到目标日期的倒数天数

        Args:
            target_date (str): 目标日期，格式为 "yyyy-mm-dd"
            decimal_point (bool): 是否显示小数点，默认为False
            target_title (str): 倒计日标题，用于通知显示

        Returns:
            float: 倒数天数
        """
        try:
            target = datetime.strptime(target_date, "%Y-%m-%d")
            now = self.api.runtime.current_time
            time_diff = target - now
            days_diff = time_diff.total_seconds() / (24 * 3600)

            target_date_only = target.date()
            now_date_only = now.date()
            if target_date_only == now_date_only and self.notification_provider:
                logger.info(f"倒计日提醒: {target_title} 就在今天！")
                self.notification_provider.push(
                    level=1,
                    title="倒计日提醒",
                    message=f"「{target_title}」就在今天！",
                    duration=5000,
                    closable=True
                )

            if not decimal_point:
                if days_diff > 0:
                    return max(0, int(days_diff) + 1)
                else:
                    return 0
            else:
                return max(0, round(days_diff, 2))

        except ValueError:
            raise ValueError(f"日期格式错误，请使用 'yyyy-mm-dd' 格式，当前输入: {target_date}")
        except Exception as e:
            raise Exception(f"计算倒数日期时出错: {str(e)}")

    def on_load(self):
        super().on_load()
        self.notification_provider = self.api.notification.register_provider(
            provider_id=self.pid,
            name="倒计日提醒 / Countdown Days Reminder",
            icon="icon.png",
            use_system_notify=True
        )
        self.api.widgets.register(
            widget_id='com.rinlit.countdowndays',
            name='倒计日 / Countdown Days',
            qml_path="qml/countdowndays.qml",
            backend_obj=self,
            settings_qml="qml/countdowndays-settings.qml",
            default_settings={
                "target_date": f"{datetime.now().year + 1}-01-01",  # 格式yyyy-mm-dd
                "target_title": "新年",
                "show_decimal": False,  # 是否显示小数点
            }
        )

    def on_unload(self):
        print(f"Countdown Days unloaded")
