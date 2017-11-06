import json
import datetime
import pandas as pd
from config import RETURN_FIELDS_LIST


def hql_commander(cursor, hql):
    cursor.execute(hql)
    fetch_row = cursor.fetchall()
    return fetch_row


def hql_query_line_generator(hql_elem):
    fields_list = ','.join(RETURN_FIELDS_LIST)
    query_template = '''SELECT {fields_list}
    FROM events.frontend_event_orc
    WHERE day BETWEEN {start} and {end}
    AND event_key = "{ek}"
    AND os = "{os}"
    LIMIT 15'''.format(ek=hql_elem['eventKey'],
                       start=hql_elem['day']['start'],
                       end=hql_elem['day']['end'],
                       fields_list=fields_list,
                       os=hql_elem['os'])
    print("--==" * 12)
    print(query_template)
    print("--==" * 12)
    return query_template


def query_day_is():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    week_range = {
        'yesterday': yesterday.strftime("%Y%m%d"),
        'start': (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y%m%d"),
        'end': yesterday.strftime("%Y%m%d"),
    }
    return week_range


def convert_content_to_json(pd_dataframe):
    assert isinstance(pd_dataframe, object)
    return json.dumps(
        list(
            json.loads(
                pd.DataFrame(pd_dataframe,
                             columns=RETURN_FIELDS_LIST).to_json(orient='index')
            ).values()
        )
    )
