"""Модуль c вспомогательными методами для allure."""


def add_allure_env(browser_name, device):
    with open('allure-results/environment.xml', 'w+') as file:
        file.write(f"""<environment>
            <parameter>
                <key>Browser.Name</key>
                <value>{browser_name}</value>
            </parameter>
            <parameter>
                <key>Device</key>
                <value>{device}</value>
            </parameter>
        </environment>
        """)
