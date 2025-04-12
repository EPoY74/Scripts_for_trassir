# -*- coding: utf-8 -*-
# <h3>Shot Saver Universal</h3><br>
# <code>
# Version: v3.2.12<br>
# </code>
"""
<parameters>
    <company>DSSL</company>
    <author>A.A.Trubilin</author>
    <title>ShotSaverUniversal</title>
    <version>3.2.12</version>

    <parameter>
        <type>caption</type>
        <name>Настройки скрипта</name>
    </parameter>
    <parameter>
        <id>SELECTED_SERVER</id>
        <type>server</type>
        <name>Сервер</name>
    </parameter>
    <parameter>
        <id>SELECTED_CHANNELS</id>
        <type>objects</type>
        <name>Каналы</name>
    </parameter>
    <parameter>
        <id>SAVE_FOLDER</id>
        <type>string</type>
        <name>Путь, относительно папки скриншотов</name>
        <value>{server.name}/%Y.%m.%d/{channel.name}</value>
    </parameter>
    <parameter>
        <id>CUSTOM_FILE_NAME</id>
        <type>string</type>
        <name>Название скриншотов</name>
        <value>{channel.name} (%Y.%m.%d %H-%M-%S.%f).jpg</value>
    </parameter>
    <parameter>
        <id>SHOT_AWAITING_TIME</id>
        <type>integer</type>
        <name>Время ожидания скриншота, сек</name>
        <value>5</value>
        <min>1</min>
        <max>99</max>
    </parameter>
    <parameter>
        <id>DISABLE_POPUP</id>
        <type>boolean</type>
        <name>Отключать всплывающие окна</name>
        <value>False</value>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Режим отладки</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Скриншоты онлайн</name>
    </parameter>
    <parameter>
        <id>SSO_DELAY</id>
        <type>integer</type>
        <name>Каждые n сек</name>
        <value>0</value>
        <min>0</min>
        <max>9999999</max>
    </parameter>
    <parameter>
        <id>SSO_SCHEDULE</id>
        <type>objects</type>
        <name>По расписанию (Red)</name>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Время ожидания загрузки расписания (сек)</name>
        <id>LOAD_SCHEDULE_TIMEOUT</id>
        <value>5</value>
        <min>5</min>
        <max>99999</max>
    </parameter>
    <parameter>
        <id>SSO_BUTTON_ALL</id>
        <type>string_from_list</type>
        <name>По нажатию клавиши (для выбранных каналов)</name>
        <value></value>
        <string_list>,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12</string_list>
    </parameter>
    <parameter>
        <id>SSO_BUTTON_ONE</id>
        <type>string_from_list</type>
        <name>По нажатию клавиши (для активного канала)</name>
        <value></value>
        <string_list>,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12</string_list>
    </parameter>
    <parameter>
        <type>string</type>
        <name>По событию</name>
        <id>EVENT_TYPES</id>
        <value></value>
    </parameter>
    <parameter>
        <id>EVENT_OBJECTS</id>
        <type>objects</type>
        <name>Только события с выбранных объектов</name>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Скриншоты из архива</name>
    </parameter>
    <parameter>
        <id>SSA_INTERVAL</id>
        <type>time</type>
        <name>Интервал между скриншотами</name>
        <value>00:02:00</value>
</parameter>
    <parameter>
        <type>date</type>
        <id>SSA_DAY_START</id>
        <name>Дата начала</name>
        <value>01.05.2019</value>
    </parameter>
    <parameter>
        <type>time</type>
        <id>SSA_TIME_START</id>
        <name>Время начала</name>
        <value>10:00:00</value>
    </parameter>
    <parameter>
        <type>date</type>
        <id>SSA_DAY_STOP</id>
        <name>Дата окончания</name>
        <value>01.05.2019</value>
    </parameter>
    <parameter>
        <type>time</type>
        <id>SSA_TIME_STOP</id>
        <name>Время окончания</name>
        <value>11:00:00</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FIGURES</id>
        <name>Фигуры</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Настройка отправки</name>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>SENDING_METHOD</id>
        <name>Отправка скриншотов</name>
        <value>Отключено</value>
        <string_list>Отключено,Email,FTP</string_list>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>REMOVE</id>
        <name>Удалить после отправки</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Настройка Email</name>
    </parameter>
    <parameter>
        <id>EMAIL_ACCOUNT</id>
        <name>Учетная запись отправителя</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <id>EMAIL_SUBSCRIBERS</id>
        <name>Получатели</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>EMAIL_MAX_SIZE</id>
        <name>Максимальный размер вложения(МБ)</name>
        <value>25</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Настройка FTP</name>
    </parameter>
    <parameter>
        <type>string</type>
        <id>FTP_HOST</id>
        <name>IP адрес/имя хоста</name>
        <value>172.20.0.10</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>FTP_PORT</id>
        <name>Порт</name>
        <value>21</value>
        <min>1</min>
        <max>65535</max>
    </parameter>
    <parameter>
        <type>string</type>
        <id>FTP_USER</id>
        <name>Имя пользователя</name>
        <value>trassir</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>FTP_PASSWORD</id>
        <name>Пароль пользователя</name>
        <value>12345</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>FTP_WORK_DIR</id>
        <name>Рабочая папка</name>
        <value>/trassir/shots/</value>
    </parameter>
    <parameter>
        <id>FTP_ADD_RELATIVE_PATH</id>
        <type>boolean</type>
        <name>Учитывать относительный путь</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FTP_PASSIVE_MODE</id>
        <name>Пассивный режим FTP</name>
        <value>True</value>
    </parameter>

    <resources>
        <resource>email_sender.py</resource>
        <resource>ftp.py</resource>
        <resource>helpers.py</resource>
        <resource>schedule.py</resource>
        <resource>shot_saver.py</resource>
    </resources>

</parameters>
"""

resources = {
    "email_sender.py": """
        eNqVV1tr5DYUfg/kPwhDQNOdmmRpoQydJaHNQmHZl9C+pKnw2JoZtbZkJHk32aX/vedIsi3b
        mkl3ArFH5/6di86IplXaEs0vL4R/VWZ4PSpjLy8uL6x+2VxeEPjstWrIkdct14YErgO3rFaH
        A9eXF/y55K0lvznKvdZKx4LIJeQhEvzg5EhhJlrwz7+TbUSgKyQw9gmMCyUZA2p2k1/nN1nP
        n1d81x1odmVI4NqQK5OtCWOyaDhj+DbIe328KUTNPhW1qJjmB/7cgl7N81I1rag51dnjX7dP
        b27d/z9z98hW3suyLowh96jBRUvvHQCgfRUCb4FhwXtXlqqT9qOy7+FZ0VHBWTHg/wPdPMtf
        8T1hn4VkXJaq4qwt7JHiv55V7CHHOcJBtgCgtFkg4GdMdf9BUQAEH4AuqqRZZ/c/IQQ9T0g7
        /V0KZPjVsTn/1iSc3cvhbLWwgL7jm+a209LZWgT/wGUFNaB2f/PS9iog2KKrLTOdO8aC+Gq4
        hgy7fP9Lvn9HvppSi9b6gyzfK90Ulo4uRPxbrPjccGuhTA3NspXHSWmS/VILDlitI8FRbxC0
        hTV0lbeFBlbqhYOAK5jgMtSgkMIyRg2v92tS+HKIcUFCzligQFzuAHvBl2sg0F50JtkUz6yw
        tiiPDXhi2O7FcgNa3v5IviM3129/CI/eqVt0XZQNt0dVjX6ethe5CvUkle2DmOVWF8JwAlXb
        +dzT7L5p7UvPnQ2wuCEBOCP4REgyy4TH2kBCakB4ZgQ8QM7cvrS+puMmy0ghK0IdQ1/0PazB
        Xn7oRBWdz/VHpYnsscs+vmRTj6k5i7HHVxg/gaj7GjsQDO+UqmliVkGqbXkMYqMt1zhzU1CX
        hjPkNLSszdrbNolkesL/zKVnnsyD2vBFk4PtygeAlfj4tMihMEICRrLkPhxwkBoLI6TzI2SV
        ysug0L/kpq2Fpdl6Wll9dTkmLK9kgMEPgCZ/LSsnQ8uLtoVJFSQS/i6hSdTSMOlTaoYpGZmd
        TJeDVl3L9nB5YeczHAZGfOFh2uC5uxUmic+y7AGhc2RDrCJOi8nJA4gSBYUK08QfQqYIMAHX
        kUvSq4/xvtOHObijWUJrYaDJyAd4oGZncuLKoiBH6U0SDCynkeC9nBZZ2WnnJhxfT0eOqJ4j
        VFx1yK7hurCcpsFyiXQXWsVGwe3y3h2Iq0W1Y1RwD7t7VRhkpAuVqYoLi87nQksYjTR7D8we
        Ipw6Yd05ZdcBoSQM1Y4n0hPwAbdwViX8gfOQ64RLYfe6qyoy3j3gT+wTCp92T+wjP95tz9xl
        rwOT7jHcDJ12eO46S5LKt+hvWn7w/BzdBZmmn44oIZAumqGQoXTp8OXNaHpFfv425EYl21HL
        ks11VT/fTqXwxHzbaV78c/aC6BvZWZl085QCkfrl6NSUG1v2ETp78zTZvAz67udguGIsf7bb
        DOozQmr7UUko07BVum9xK07qfRpFhmsq/sbxN82VDgbwJTaA33v1V3pebd616RmqmR1FCmeU
        oDo6XU1Gar8vwyDH4DZJ6X7rnC3ZcWpAVeTEZnnhuiTBCIm4cMCez2DEnJqAYTWUlVtlGP60
        HPbTM103bNNu3TvXn/Ge5DekU9wLmF/J2KSVprCc7/9Ew3wbDCkITkY7BOZjWCxr4Nh/udOX
        +Q==
    """,
    "ftp.py": """
        eNrVWv9v27gV/z1A/gdWh6Byz1PSbsMOwWnYXS69BevaoUlxuB0KVbboWItM+iiqvszI/773
        SIoiKcl22hXYjKC1xfceyffl894jVa7WXEjC6+OjUn9dyHVVzuxPuRQ0L0p2e3y0EHxFFg2b
        S86rmhiCjcjXtRmc86qic1lyZocL+mtDp4TlK1rIZl3R4yMre8lriT+Pj6S4Pz8+IvBRcpa0
        WlNhZdxSmVX89paK4yP625yuJblSI5dCcOEyIhWs1WF8pfhIXntSjo/0N5I6j+MJDmTZR5ga
        tpBlMBo9T14kZ1FLnxR01tzG0UlNDNU5OamjKcky3GGW4TfLP9Gbu5a5bGoQ1ikhjvRD4Pwl
        qilDBcP3iOKG8AtYIbM/6mY+pzUSRyXLQJ8Njd6D8LoVrIXFnybJrLKgC5IVPGNcLkFG/CwX
        t/WUPHt2t8FvE6PmdV7XDsMGxFA25wXN1rlcxvhPS1ouwK8S3DRJQZNMRmYAP53F2w+ywl7w
        P1AzioyjRi6+wQW2NMb68TtWIsEPikx5wZSYZ5fMPpv0ZsC14zdBZSOYmsvZjGhYlteZdvl4
        wVr+KIreNky7PhgWnUnTwAAyI81fVBwgk/6NAkHemBqVCmC3NrySGz2rBCoq0wWbEqRPNbtm
        To0MR0RS5HQFS0rJjWioOwDOIWTs0Jo9y3bF5jcsUqtgXoF6yMubfyjdxZdK1bDdvuU15cWS
        zu8uOGM64jVXyz7G9FKu360rnhc3Ip/fUdFpWD8ma8FvBbgoUfSOgpWFspKVMsvimlaLKZF5
        fZfdNmUxJYuy0h44JbOKz++yuvw3zWb3knoqR75EDW1EKSVFxZ0lZwEBzCyzesk3LAMYmlOG
        lgqJ7ORoxfZ7QBMuBUjDR6FULvNKDQMtRI+KBnAIfBL3os3uejLx1TTPq8qqaYcLgn7/mrOi
        AiRccEFqycWsZLm4b8Xh55pS8l1V8yCallKu6/PT04LPYZ33cslZwsXt6YtTyB8CZJzqVJIs
        5ar6ynwH/0jcWZyF7LLS1+mwQjseY6hszleArxLVJ3jDijjuSzsNdT0hz8jzs7OJu2tArzFn
        eJL2pgt0M+5GIaPPF2YZk118h5v2hEyCCL6oShiO+exfEJutvW+u/n755t0NrOG58eXrq9c/
        vrq8efPag4/vX725+Ft2ffXPy+z7n28urxXDiz/owSy7en11c/mDSo4v86qmg/Hp23La/cSU
        7/zELJ2+eO48aWoq0ihnnN2vOCZIhxh2tynSyH224eIuK0qRvuaMOs8xAGaAMOFzlfKyVf5b
        RVkKJj9zeRDQQKctoqWok2D+8iNwQ/y5Y0FAgf4BvNAARHKCKVmhU+0613cQh2E4gWZIXEuA
        TkRJUxx56QtLmrhkckq4Qua8MrQ4MkUL5E0lz8mHF8/JB58X1aqk93hxBHO0y+/o/0M/hW6K
        cUmagIvCigNpoZDWaMNicBRrOCAAO3Bx74hCawbCWkuTGL/ls4p6Eq91SYR5Za7SiiF3tzsg
        1fWTvs5boYqKAMktJp5OIDpWuMzAuUg8gyrak6oSKnFI4E9lcVV9h1ZoPXFA0CVDNZCnhuwp
        UXQAaB/zipRQvPh+rT5Q9VGxKWsKeq8Vu+FWzO7m0PM/uM58oWAnl1KUswZAOXDsFndQi7jL
        bn+yXFHeSFLCPqGSY0XtKzFQYQdXastWY1hnsuoe/oFNMtAYm1Myh2pK0mJg4YMpp0X7bg5I
        i/pRB3nBxlRVna3qW4DCOFAnyv+ZNwTgv6kKgrBIarBj5SyRL8h2XtWqc3j4dib+HA0IwaxM
        pUOYuKitEBgXfw9z3TG+IZtlLqFypOpJwWHKJ08CuZMEcv0ql3ErMzX7VPkjy5K2mZn4fCJH
        94BKGO2myz2rAofU5p/ESxY6wQRJPlOolwZgp4cU3KUK28IhhTSpApwelwao1CBVOGyhJ7Uo
        NCTBBlfqxVpv/RoAUt3lxiatuNgx6W8ZKiHgQMzpjVksSztYAwdw2rK+OLUNtLzNx+24V0wg
        cVjfhJg0VMSENHFQaQq6FqbSdPPgYFRE325HPO0hDnw02nb+8UQ8QL8ajKvKYdt5yiCRKia2
        nc8MS9JlxXZZFgVlxoEGKW2xsfWdaZDYViBbz7QDlF5NsnV/ja7XliHbvs8+hAwTF1hs8Pdt
        nQa1Gn48paTRswgqZVhY7AbbZDqeO9MuTBL9xCHuN6fgNq579ZwvdDPAcJsDAGHXHNSAuQsK
        L8PloXz/0EEHY9ecxJPeeGIkxZ1HTh2ImrZpTG/VZLsBMRCOZas4dMaph1gDDID7OPgx7tu4
        fyRitoB9nwLlGk8p4Nv5EIYPtu5APOknROvkgaC+Kq26NkXsswZ781esUwh0NKsReau7PfJ2
        TtyRIsmvTSkDBMPzvz0eZkah4AO/AjGu1LfKceu+WxmH0jWt7sRGag+/6fuRSjVVt6YkSdwz
        sP8fJ97nQ+N+dLAvPdKfHuVTBy8CidSxDNotJXhq+btvok8N6AGX4NJtC9pD3LA80xCq/HNY
        NR04nA9Ot8kFw6Pf6CJnT9XpuXKtbupoihKhyV9w1QAHK2gP+2xszSte033RhTThPOPhgeSP
        DA/rhjgJtD9QSqny61HeaCUkalPxiL8Ei+2MpriKMdt1tjrfKTewkBJ6mH0WJfSG1f1QiTdQ
        kSrr4dFFhkcXO49bbUz4Zr22h3yKmGxKudTTBQA6cBTSHa2a85AbeED881W9J7MKe27SVJWe
        Tp/su8TeoQPQ/gS/8YwBu2wvZsK+0DKOu47TVbRntgyqLHVGO9DTnW4f4C9qK7GgM4GCPzqN
        HMUG3dvo1O3XpIZolzEICWjnjRB4bKjJoxChVKeB+2TkkwDbFf81yD89qSNyQvweaySmAGId
        9s8H+U40Qv0OgN+1Bjd6wNP0TZa18CyHAIFHzim8c4ypbjMyqW85sDcLLj7i4WhSywlPYB25
        Koz4GirwHZcB0DOIWTTBChBJqY7isdB3zuOHnPX65s1boi1ptTB15Y4sehrooOfF5t7Mv3UL
        4Af0NJAyru2ZKvqqvsXcXea3KUDRDrhMmCJG0oOnN2LuJMIK0nOcoQlGBOvbmVaqbpnWfF3R
        hRzLNl91TNsxCqUz6xvRueNtO1kEXXFJMRKAp/uxm6ntcoHFHrTuZLBRABxdRIyxPAypFj8D
        +Qh0opXzi7P791P70Nnf+xE8s0fF7l1fy2+36sjsdvN+bKW99wjMnb3agrnucaDB3vgOS9NX
        7AqOylql6l13hCOOh59xVG8/2DIkpkuIn5+dTUmVr2ZF3lnahTT9akJiNjeZ7JatQ6OrN/ZU
        Gl9iobou27XQA2vpnQbfTYof7P/MVFg2bpZYzYB1TPeprpNOoO3K1+sWBfG5BsHpfvn7oj/Y
        cVdL7qE/xMIa0/TK4967DOOO0WsjHuMB+7d5qI/YN2kmn6WKL7S69n2e/Yvb6+L21Y/2DAmx
        d31flUyet9dD6U9nfzr7/UGur3R2kOtDdd2wpXohoegFQQuUJ+J/2M+/kHEPdLthAlrVdAdI
        ha3lS1T2iVC9zgJfoYgcFN6xhkds/b+17cEte+v4I87UpRfaO4sc1s2+qxWfbhc+DXb1bWC0
        Hh5H7wbcHmpbs2h1PGJeOQs2sEfrn6Np75wUF2LOAZyU3BVR+kWL4L2LrpJRv4Myfs8pQL+7
        H27suzX03yd4q8aU+npd6J4XB162b/tJvFFFEgSfzZIyp2RjZb2kwamEf3rhybTnGM61tDKg
        AOPzleLy+4e3eF4faubqjX7xFcs/VQDYUB3VL1Ai0acXi/riwMxsQOLpSf3UgYm2QzQ44U3e
        KWW4u3Ir7N0aGbkj9S7ZXPqxDumgnujALuiAvmdvp/MwfLncK5d6NvWxahhpTLtxjW+TEI0p
        IZD0IM9/obQjMX25i3F9EH18oRKsVONeXiHm3bfvBEXe/tsXWruXL/8DXbfBrA==
    """,
    "helpers.py": """
        eNqtGVtv41j5vVL/w9FZRbJ3Ek87u0KjqCl0dtKZSr2s2lTLUKojNz5JzTi218dpp1SVgPCG
        kBYJIVjtImDfEEILT4AEvPADMvyDPOyKn8H3nYt9bCedediOJo3Pd79/x32HdN7tkGEShPG4
        S6b5qPMYT9bXwkmaZDkRN6L4nvHia1KeRsl4DMTra6MsmQCnKOLDPExiQTRCwD+eAmVBcJmI
        HB8Zu+KZAEzGSI/QR96mt0ER8LS/u3O6P2AnHxzvfThghzsH/RPAuF1fI/BDX/A4JOJlFqY5
        beuz0zj2JzwgJ8PK8WL2xWL2+8Xsk8Xsz4vZLxezTxezz4k8+s1i9rvF7NeL2W8Xsz/Al4Jm
        /qv5l//9Yv4lef3j+T9e/2j+t/m/X/+kgCoBJE6mJcHn83/N//r6Z/O/Lyex9CVBIm588Z+/
        1IiBYgXx15/98atf/POrT37+v59++vVnf8Lzu/U1kfu5AJegKz354LhwqnTrEXnipX7G4xwB
        Ez+M2SQJphFH6I3w1IPwxjx3bCYFkTeehkFbCgAGozD2o/CHEC6gPzvHIK2vBXxEroExjyF9
        OEv9/NLBD7erdA9HkCYexoX0IL5xTjUAf/LsxnrCHyQF7vjLCziydCjk42Pqlnj81ZCDhc5p
        HCLCU4nWz7IkaxN91o+LM7chQQh1kvF8msVSlrJlGAGMPJ2mUTj0c74bRjnPHJ3anno07Cil
        J9M0zbgQACSTaZSHKXh2Agf+mAtwClgi0O5hEufgTg9FIOkg84cvkQjEqcqBnM3AiiwgfhyQ
        kRREkmkOjzdG15SDSgFxRDgJIz9zNYUo2PZf+RPQwDK30+mQwSVXcrRiJaf3SB7CYWGO4YMR
        ZSyMw5wxR/BoZHtQTFNwSc1FbSLRvILKChZCPIYaMLAUQnuYxHwVmA2TaYy5u2kro/whVWlr
        q22V1IkXGJ0wO9EaAx9OM8xmLd7R6Cr3DT8v4lc8ipPieSLGlhGQxBUuvZretRRbatQDaZWN
        pvNv14+E5REOTzV+IH4py22yWcNc5Q+niSajfn+GtIRKke/HlLSWqtBk697nCtDE8uNbOG2V
        zwaZGiamZp9Dh9pPxs+hfCKrZPWzyRZMJj4J85WpJJsgSteukIjeKMkmfq4Tx3VtuR8m6TR9
        g1QoLah4aBMZSRGdXCq4VXJMAkQ53iQdDL7B3gc7+7SrFOOyxVkIuzuDe6D94+Oj45XQj3aO
        Dw3QB23yOnDv8NlK+N7h7pEBalfZ4Kf9J6fP7oEfHg1O+oPlCHd25d8bLChRoguxGqF6d1HO
        PatUOvTlc0cVeRnNgxvoZ/wN4fwIotJng72D/tHpgB3gTvJoY2NDAQ92vsv2j56xk73v9dmT
        FwO5smxukHfh49H75hd5B88OnqzsuG3seRyVbPbeipJv7rwMOTE9VuuDulpbCW4LMHd/kITx
        koahNgSe5+AU4VBYIHI+YdchMEtSuetR94zC+sF5LC6TXLBREgWQ5+elOVWulrJNva+zELo+
        u04yOSt79T6p0SCGDDbLKe40csd0Jv4rENbbhKBYXMvlxfPTlMeBU5Hjmlh8J80ScHN+U5k/
        XLqrPgx1M6o7uhrW4SUfvpQtTYD4Bg+1H0m/hwJZOHV2bnMaGApY3AqmFRIYDfKsmY9LBgZE
        iZkAmYqy8+YBoR7g0CZlU3mbl9tdPnWAJOOT5KqGvUQxRERYw8D2ai3dqvtVeJt7jCKvBcfS
        Qa5vkAnxEtnUpy7xBa5u8rhm5/UlnDXyc4kzDL0nlXRoqzJpS1IPOljER7CQv32ZvGUTbYiy
        i6Mx+Ky4x0m+XIWlu1BTTTXBG/0F9w1YfJX8eqttk2bNqhuIiaS6/DA57WQDL/s2LlF4vTmj
        cseQKPTc0lahq0lZa3/mwheEwr+IYDOS2SExSRKTKIw5LEtd+E/bNfPrIhkiQ0t8A1oFwzJU
        tnmlqYOV0YYQX0zHPRl1eDBLH1NLc3GuFFejUB0av2iX1e6R1r0RkXRroLf45Y45t3gxvHOp
        SRE87uEHFGwa+UNIZkKhUBh12wRxe1qMvFFqpsoMYGsmLbSz/dK0CpZnmnBxg1BQkG/2KQbO
        Mdj6SJx17QgbRG8YJaJS7ZpMtSWzABj0oqNoLJiB+7hEOHrRKeDoQKapQM/aUuo2kUpWxgWS
        I+aqDKu8DBTuwa3LZqJ8n1dcuGvOrAymLeVPQc5aTrH+uJ3H4pzAAeRjnLid9wXZajmjaTw8
        lMjbpANQvZy5Qnf/FUaUYquaVWPoB0HhW4tB4T/dVirJaoVPPlv+rSzf7gq8povRjSs8rPfe
        Bq+39bTMyEneo1sX2xVfi/OthxfbZB983S19LrYusu2tcLt0s/et9zbE1sNwmy5djRqWlUrU
        FG3mtuX8Chvb+9IllsfBFqz6luOLIXbmbySFJGMcpmUkq4s3zEG8hOEkrC0GNtmK2qlj3x86
        MBCaI/RLGbXWi05r0mnBxfd5t3XQbZ3Q6syrd9duI/LKW+XVG4yGxQQANcxvVLOGZyDU+t1V
        /V2We48zLdkV9e5NJZtJE9Fq2hVp5rzo4o3lPPInF4FPop7i1F0x4d16bw7jUWK3vpPcz/DC
        osccvtJwWgKG0iWPUnyTeYUz2wxBT41Ue1a1ifWGutIDtURZM47ZEGBsAgvwGqxyNuczWkLo
        eaG1vkEoVuWUh0FohrwZ0xoTIBCUzLFe5sKYVbggDUejS2AmNkeqtURAsI0f5XYtp7cktV5u
        8tz4TF3cFGQnGwsr7eVe4IgcLqLqDuhHbpeclHRtrBtkDa0APAC9VpLIvxKUHjHcj6WRtgBg
        XeFnva00EwNOLQKwz59GFfvku/DKTlF7xxYkQ8BZ7lrGAMqY7Vv75WIe5vJ1esahhPxseOlk
        dEsebjveA3frofoO5MDGKhCdUo33oWCQpKi1lhK9Ikgfa1HmqSFsuU/orZR0R65uNeVdsc9V
        pUu8nvz0xlkyTZ1NqCBN1NO/CwjaYPSV05V+24N/zYmGG7nUSP15ALa3ZX/zqb+eqy+oZxSp
        6bm8/zfsrBTPUnh5hSi6UFF0uF0Wp6hgxtEyHjhlx7JvUxYHxVhqnPFxKPD2U4ItYYD5f1UR
        Trk=
    """,
    "schedule.py": """
        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
        kIw=
    """,
    "shot_saver.py": """
        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
    """,
}
t1utils.resources_check(script_path, resources)
from shot_saver import ShotSaver, status as shot_status
from email_sender import EmailSender
from schedule import ScheduleObject
from ftp import FTPClient, status as ftp_status
import helpers
import host
from __builtin__ import object
from functools import wraps
import threading
import datetime
import os
import re

GLOBALS = globals()

# Script settings
SELECTED_SERVER = GLOBALS.get("SELECTED_SERVER", "") or None
SELECTED_CHANNELS = GLOBALS.get("SELECTED_CHANNELS", "")
SAVE_FOLDER = GLOBALS.get(
    "SAVE_FOLDER", "{server.name}/%Y.%m.%d/{channel.name}"
)
CUSTOM_FILE_NAME = (
    GLOBALS.get(
        "CUSTOM_FILE_NAME", "{channel.name} (%Y.%m.%d %H-%M-%S.%f).jpg"
    )
    or None
)
SHOT_AWAITING_TIME = GLOBALS.get("SHOT_AWAITING_TIME", 5)
DISABLE_POPUP = GLOBALS.get("DISABLE_POPUP", False)
DEBUG = GLOBALS.get("DEBUG", False)

# Online screenshots
SSO_DELAY = GLOBALS.get("SSO_DELAY", 0) * 1000
SSO_SCHEDULE = GLOBALS.get("SSO_SCHEDULE", "")
LOAD_SCHEDULE_TIMEOUT = GLOBALS.get("LOAD_SCHEDULE_TIMEOUT", 5)
SSO_BUTTON_ALL = GLOBALS.get("SSO_BUTTON_ALL", "")
SSO_BUTTON_ONE = GLOBALS.get("SSO_BUTTON_ONE", "")
EVENT_TYPES = GLOBALS.get("EVENT_TYPES", "")
EVENT_OBJECTS = GLOBALS.get("EVENT_OBJECTS", "")

# Archive screenshots
SSA_INTERVAL = int(
    (
        datetime.datetime.strptime(
            GLOBALS.get("SSA_INTERVAL", "00:01:00"), "%H:%M:%S"
        )
        - datetime.datetime(1900, 1, 1)
    ).total_seconds()
)
SSA_DAY_START = GLOBALS.get("SSA_DAY_START", "01.05.2019")
SSA_TIME_START = GLOBALS.get("SSA_TIME_START", "10:00:00")
SSA_DAY_STOP = GLOBALS.get("SSA_DAY_STOP", "01.05.2019")
SSA_TIME_STOP = GLOBALS.get("SSA_TIME_STOP", "11:00:00")
FIGURES = GLOBALS.get("FIGURES", False)

# Sender settings
SENDING_METHOD = GLOBALS.get("SENDING_METHOD", "Отключено")
REMOVE = GLOBALS.get("REMOVE", False)

# Email settings
EMAIL_ACCOUNT = GLOBALS.get("EMAIL_ACCOUNT", "")
EMAIL_SUBSCRIBERS = GLOBALS.get("EMAIL_SUBSCRIBERS", "")
EMAIL_MAX_SIZE = GLOBALS.get("EMAIL_MAX_SIZE", 25)

# FTP settings
FTP_HOST = GLOBALS.get("FTP_HOST", "172.20.0.10")
FTP_PORT = GLOBALS.get("FTP_PORT", 21)
FTP_USER = GLOBALS.get("FTP_USER", "trassir")
FTP_PASSWORD = GLOBALS.get("FTP_PASSWORD", "12345")
FTP_WORK_DIR = GLOBALS.get("FTP_WORK_DIR", "/trassir/shots/")
FTP_ADD_RELATIVE_PATH = GLOBALS.get("FTP_ADD_RELATIVE_PATH", False)
FTP_PASSIVE_MODE = GLOBALS.get("FTP_PASSIVE_MODE", True)


helpers.set_script_name()
logger = helpers.init_logger(
    "ShotSaver", debug=DEBUG, disable_popup=DISABLE_POPUP
)


tr = host.tr

if not SELECTED_SERVER:
    SELECTED_SERVER = host.settings("").guid

if EVENT_OBJECTS:
    EVENT_OBJECTS = EVENT_OBJECTS.split(",")


def _is_channel_enabled(sett):
    info = sett.cd("info")
    try:
        if not sett["archive_zombie_flag"]:
            if info and info["grabber_path"]:
                try:
                    grabber = host.settings(info["grabber_path"])
                except KeyError:
                    return False

                if grabber["grabber_enabled"]:
                    n = info["grabber_channel_n"]
                    return (
                        grabber["channel%02d_main_enabled" % n]
                        or grabber["channel%02d_ext_enabled" % n]
                    )
    except KeyError:
        logger.warning("Can't check is channel enebled", exc_info=True)
    return False


def _parse_channel_names(channel_names):
    if channel_names:
        return set(channel_names.split(","))


def _run_as_thread(fn):
    @wraps(fn)
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
        return t

    return run


class TRObject(object):
    spec_symbols = re.compile(r'[|\\/:*?"<>]')

    def __init__(self, sett):
        self.sett = sett
        self.name = self.spec_symbols.sub("", sett.name.strip())

    def __getattr__(self, name):
        return getattr(self.sett, name)


class TRServer(TRObject):
    def __init__(self, sett):
        super(TRServer, self).__init__(sett)


class TRChannel(TRObject):
    def __init__(self, sett, server):
        super(TRChannel, self).__init__(sett)
        self.server = server

    @property
    def full_guid(self):
        return "{s.guid}_{s.server.guid}".format(s=self)


def get_channel(channel_guid):
    for _, guid, _, parent in host.objects_list("Channel"):
        if guid == channel_guid:
            server_settings = host.settings("/%s" % parent[:-1])
            channel_settings = server_settings.cd("channels").cd(guid)
            server = TRServer(server_settings)
            return TRChannel(channel_settings, server)


def get_channels(server_guid, channel_names=None):
    channels_ = []
    server = TRServer(host.settings("/%s" % server_guid))
    for sett in host.settings("/%s/channels" % server_guid).ls():
        if sett.type == "Channel":
            try:
                if channel_names is None or sett.name in channel_names:
                    if _is_channel_enabled(sett):
                        channels_.append(TRChannel(sett, server))
            except ValueError:
                logger.warning(
                    "Can't check channel, maybe user has no access",
                    exc_info=True,
                )
    return channels_


class Saver(object):
    default_shots_folder = host.settings("system_wide_options")[
        "screenshots_folder"
    ]

    def __init__(self, channel_guids, folder_tmpl, custom_file_name):
        """

        Args:
            channel_guids (List[str]): Channels guid `channelGuid_serverGuid`
        """
        self.folder_tmpl = folder_tmpl
        self.channel_guids = channel_guids
        self.ss = ShotSaver(callback=self.save_shot_callback)
        self.ftp = None
        self.ftp_add_relative_path = False
        self.email = None
        self.email_subscribers = None
        self.remove = False
        self.custom_file_name = custom_file_name
        self.shots_path_for_send_email = []
        self.working_tasks = {}

    def __get_folder(self, channel, dt=None):
        dt = dt or datetime.datetime.now()
        folder = dt.strftime(
            self.folder_tmpl.format(channel=channel, server=channel.server)
        )
        logger.debug("Folder: %s" % folder)
        return folder

    def ftp_callback(self, task_guid, state):
        logger.debug("%s: ftp %s", task_guid, state)
        if state in (ftp_status.success, ftp_status.error):
            task = self.working_tasks.pop(task_guid, None)
            host.stats()["run_count"] -= 1
            if task and self.remove:
                try:
                    os.remove(task["path"])
                except BaseException:
                    logger.exception(
                        "Unhandled exception while removing file", task
                    )

    def remove_file(self, shot_path):
        try:
            os.remove(shot_path)
            logger.debug("remove file %s" % shot_path)
        except BaseException:
            logger.exception(
                "Unhandled exception while removing file %s", shot_path
            )

    @_run_as_thread
    def sending_email(self):
        self.email.send(
            mails=self.email_subscribers,
            attachments=self.shots_path_for_send_email,
        )
        if self.remove:
            for path in self.shots_path_for_send_email:
                self.remove_file(path)
        self.shots_path_for_send_email = []

    def save_shot_callback(self, task_guid, state):
        logger.debug("%s: shot %s", task_guid, state)
        if state == shot_status.success:
            task = self.working_tasks.get(task_guid, None)
            if task:
                if self.ftp:
                    try:
                        if self.ftp_add_relative_path:
                            remote_dir = task["folder"]
                        else:
                            remote_dir = None
                        self.ftp.send(
                            task["path"],
                            remote_dir=remote_dir,
                            task_guid=task_guid,
                            callback=self.ftp_callback,
                        )
                    except IOError:
                        logger.exception(
                            "Could not send file %s", task["path"]
                        )
                elif self.email:
                    self.shots_path_for_send_email.append(task["path"])
                    self.working_tasks.pop(task_guid, None)
                    host.stats()["run_count"] -= 1
                else:
                    self.working_tasks.pop(task_guid, None)
                    host.stats()["run_count"] -= 1

        elif state == shot_status.error:
            self.working_tasks.pop(task_guid, None)
            host.stats()["run_count"] -= 1
            logger.warning("Can't save shot %s" % task_guid)
        if (
            self.email
            and not self.working_tasks
            and self.shots_path_for_send_email
        ):
            logger.debug("Time to send email")
            self.sending_email()

    def save_shots(self, channels=None, dt=None):
        channels = channels or self.channel_guids
        paths = []
        for channel in channels:
            host.stats()["run_count"] += 1
            folder = self.__get_folder(channel, dt=dt)
            file_path = os.path.join(self.default_shots_folder, folder)
            task_guid, path = self.ss.save(
                channel.full_guid,
                dt=dt,
                file_path=file_path,
                figures=FIGURES,
                file_name=self.custom_file_name,
            )
            self.working_tasks[task_guid] = {
                "path": path,
                "folder": folder,
            }
            logger.debug("%s: task created (%s)", task_guid, path)
            paths.append(path)

        return paths


selected_channels = get_channels(
    SELECTED_SERVER, _parse_channel_names(SELECTED_CHANNELS)
)
saver = Saver(selected_channels, SAVE_FOLDER, CUSTOM_FILE_NAME)
saver.ss.timeout_sec = SHOT_AWAITING_TIME
saver.remove = REMOVE

if SENDING_METHOD == "Email":
    saver.email = EmailSender(EMAIL_ACCOUNT)
    saver.email_subscribers = EmailSender.parse_mails(EMAIL_SUBSCRIBERS)
    saver.email.max_attachments_bytes = EMAIL_MAX_SIZE * 1024 * 1024

elif SENDING_METHOD == "FTP":
    saver.ftp = FTPClient(
        FTP_HOST,
        port=FTP_PORT,
        user=FTP_USER,
        passwd=FTP_PASSWORD,
        work_dir=FTP_WORK_DIR,
        passive_mode=FTP_PASSIVE_MODE,
    )
    saver.ftp_add_relative_path = FTP_ADD_RELATIVE_PATH
else:
    pass

if SSO_DELAY:
    assert SSO_DELAY > len(selected_channels), tr(
        "Delay is too short, for {length} channels you need more than {delay_min} seconds delay".format(
            length=len(selected_channels), delay_min=SSO_DELAY
        )
    )

    def make_shots_loop(delay):
        logger.info("Save shots by delay")
        saver.save_shots()
        host.timeout(delay, lambda: make_shots_loop(delay))

    make_shots_loop(SSO_DELAY)

if SSO_SCHEDULE:

    def color_change_handler(sched):
        if sched.color == "Red":
            saver.save_shots()

    schedule = ScheduleObject(
        SSO_SCHEDULE,
        color_change_handler=color_change_handler,
        tries=LOAD_SCHEDULE_TIMEOUT,
    )

if SSO_BUTTON_ALL:
    host.activate_on_shortcut(SSO_BUTTON_ALL, saver.save_shots)

if SSO_BUTTON_ONE:

    class ActiveChannelHandler(object):
        def __init__(self, saver):
            self.saver = saver
            self.active_channel = ""

        def __call__(self, guid):
            logger.info("Focus Changed %s -> %s", self.active_channel, guid)
            self.active_channel = guid

        def save_shot(self):
            if not self.active_channel:
                host.alert(tr("Channel not selected!"))
            else:
                channel = get_channel(self.active_channel)
                if channel is not None:
                    paths = self.saver.save_shots([channel])
                    host.message(tr("Saving shot to <br><b>%s</b>") % paths[0])
                else:
                    host.error("Can't find channel %s" % self.active_channel)

    active_channel_handler = ActiveChannelHandler(saver)

    host.activate_on_gui_event("Focus Changed", active_channel_handler)
    host.activate_on_shortcut(SSO_BUTTON_ONE, active_channel_handler.save_shot)

if EVENT_TYPES:
    EVENT_TYPES = EVENT_TYPES.split(",")

    def handler(ev):
        if not EVENT_OBJECTS or ev.origin_object.name in EVENT_OBJECTS:
            saver.save_shots()

    for event_ in EVENT_TYPES:
        host.activate_on_events(event_, "", handler)

if SSA_INTERVAL:
    dt_start_ = datetime.datetime.strptime(
        "%s %s" % (SSA_DAY_START, SSA_TIME_START), "%d.%m.%Y %H:%M:%S"
    )
    dt_end_ = datetime.datetime.strptime(
        "%s %s" % (SSA_DAY_STOP, SSA_TIME_STOP), "%d.%m.%Y %H:%M:%S"
    )
    assert dt_start_ <= dt_end_, tr(
        "Datetime end must be lower than datetime start"
    )

    td = datetime.timedelta(seconds=SSA_INTERVAL)
    while dt_start_ <= dt_end_:
        saver.save_shots(dt=dt_start_)
        dt_start_ += td
