from django.core.cache import cache
from django.http import HttpResponse
from django_redis import get_redis_connection
import datetime

def redis_demo(request):
    # Using Django's cache framework
    # Set a key
    now = datetime.datetime.now()
    if not cache.get('my_key'):
        cache.set('my_key', f'Hello, Redis! {now}' , timeout=60)  # Expires in 60 seconds
    redis_conn = get_redis_connection("default")

    #for trying, comment in one line, 2nd line, for deleting 3rd line.
    #redis_conn.set('my_direct_key', 'Hello from Redis client!')
    direct_value = redis_conn.get('my_direct_key')
    #redis_conn.delete('my_direct_key')

    response = (
        f"<h2>Using Django's cache framework:</h2>"
        f"Value of cache[my_key]: {cache.get('my_key')}<br>"
        f"<h2>Using Redis client directly:</h2>"
        f"Value: {direct_value}"
    )

    return HttpResponse(response)
