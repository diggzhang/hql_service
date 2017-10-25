import datetime
from config import RETURN_FIELDS_LIST


def hql_commander(cursor, hql):
    cursor.execute(hql)
    fetch_row = cursor.fetchall()
    return fetch_row


def hql_query_line_generator(hql_elem):
    fields_list = ','.join(RETURN_FIELDS_LIST)
    query_template = '''SELECT {fields_list}
    FROM events.frontend_event_orc
    WHERE day = {day}
    AND event_key = "{ek}"
    AND u_user = "{u_user}"
    AND d_app_version = "{appv}"
    AND os = "{os}"
    LIMIT 15'''.format(ek=hql_elem['eventKey'],
                        day=hql_elem['day'],
                        appv=hql_elem['appVersion'],
                        fields_list=fields_list,
                        os=hql_elem['os'],
                        u_user=hql_elem['userId'])
    print("--==" * 12)
    print(query_template)
    print("--==" * 12)
    return query_template


def query_day_is():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    return yesterday.strftime("%Y%m%d")
