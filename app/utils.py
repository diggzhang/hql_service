def hql_commander(cursor, hql):
    cursor.execute(hql)
    fetch_row = cursor.fetchall()
    return fetch_row
