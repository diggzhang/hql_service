def hql_commander(cursor, hql):
    cursor.execute(hql)
    fetch_row = cursor.fetchall()
    return fetch_row

def hql_query_line_generator(hql_elem):
    query_template = '''SELECT event_key as eventKey, d_app_version as appVersion FROM events.frontend_event_orc WHERE event_key = "{ek}" AND day = {day} LIMIT 3'''.format(ek=hql_elem['eventKey'], day=hql_elem['day'])
    print("--==" * 12)
    print(query_template)
    print("--==" * 12)
    return query_template
