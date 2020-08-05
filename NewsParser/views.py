import json
from django.db import connection
from datetime import date, datetime
from django.http import JsonResponse


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


def posts(request):
    order_by = request.GET.get('order', None)
    offset_val = request.GET.get('offset', 0)
    limit_val = request.GET.get('limit', 5)
    if isinstance(limit_val, str):
        if limit_val.isdigit():
            limit_val = int(limit_val)
            if limit_val < 0:
                limit_val = 5
        else:
            limit_val = 5
    if isinstance(offset_val, str):
        if offset_val.isdigit():
            offset_val = int(offset_val)
            if offset_val < 0:
                offset_val = 0
        else:
            offset_val = 0
    avail_cols = ['id', 'title', 'url', 'saved_at']
    with connection.cursor() as cursor:
        cursor.execute("select count(*) from News;")
        table_size = int(cursor.fetchone()[0])
        if order_by is not None and order_by in avail_cols:
            if offset_val > table_size:
                offset_val = 0
            if limit_val > table_size:
                limit_val = table_size
            cursor.execute(f"SELECT * FROM News ORDER BY {order_by} LIMIT  {limit_val} OFFSET {offset_val};")
        else:
            cursor.execute(f"SELECT * FROM News LIMIT  {limit_val} OFFSET {offset_val};")
        rows = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
        return JsonResponse(rows, safe=False)