from datetime import timedelta
from celery.schedules import crontab


CELERY_BEAT_SCHEDULE = {

    """------------------------sterling_square app ------------------------"""
    'sterling_square.tasks.stock_scheduler': {
        'task': 'sterling_square.tasks.stock_scheduler',
        'schedule': timedelta(hours=4),
    },
    'sterling_square.tasks.update_transaction_table': {
        'task': 'sterling_square.tasks.update_transaction_table',
        'schedule': timedelta(seconds=50),
    },
    'sterling_square.tasks.update_stock_market_details': {
        'task': 'sterling_square.tasks.update_stock_market_details',
        'schedule': timedelta(seconds=60),
    },
    'sterling_square.tasks.update_gainloss_table': {
        'task': 'sterling_square.tasks.update_gainloss_table',
        'schedule': timedelta(seconds=3600),
    },
    'sterling_square.tasks.update_pos_table_latest_price': {
        'task': 'sterling_square.tasks.update_pos_table_latest_price',
        'schedule': timedelta(seconds=30),
    },


    """------------------------main app ------------------------"""
    # Run every 5 seconds
    'main.tasks.initialize_celery_singleton': {
        'task': 'main.tasks.initialize_celery_singleton',
        'schedule': timedelta(seconds=5)
    },
    # Runs every 5 seconds
    'main.tasks.update_transaction_table_2': {
        'task': 'main.tasks.update_transaction_table_2',
        'schedule': timedelta(seconds=5),
    },
    # Runs 07:30 AM from Monday to Friday
    'main.tasks.update_stock_market_details_3': {
        'task': 'main.tasks.update_stock_market_details_3',
        'schedule': crontab(minute="30", hour="7", day_of_month="*", month_of_year="*", day_of_week="1-5"),
    },
    # Runs at Every New Year. 2022 holidays will be fetched on January 1, 2022 00:00 AM
    'main.tasks.get_holidays': {
        'task': 'main.tasks.get_holidays',
        'schedule': crontab(minute="0", hour="0", day_of_month="1", month_of_year="1"),
    },
    'main.tasks.save_market_opened_object': {
        'task': 'main.tasks.save_market_opened_object',
        'schedule': crontab(minute="3", hour="0"),
    },
    'main.tasks.update_pos_table_latest_price_2': {
        'task': 'main.tasks.update_pos_table_latest_price_2',
        'schedule': timedelta(seconds=5),
    },

    # Old Portfolio intra day history will be deleted on weekdays at 11:00AM
    'main.tasks.clear_portfolio_history': {
        'task': 'main.tasks.clear_portfolio_history',
        'schedule': crontab(minute="0", hour="11", day_of_month="*", month_of_year="*", day_of_week="1-5"),
    },
    # Data will be written every 5 seconds
    'main.tasks.save_portfolio_history': {
        'task': 'main.tasks.save_portfolio_history',
        'schedule': timedelta(seconds=30),
    },

    'main.tasks.save_stock_information': {
        'task': 'main.tasks.save_stock_information',
        'schedule': timedelta(seconds=5),
    },

    'main.tasks.get_most_active': {
        'task': 'main.tasks.get_most_active',
        'schedule': crontab(minute="*/15", hour="8-23"),
    },


    """------------------------account app ------------------------"""
#    'accounts.tasks.sync_credentials': {
#        'task': 'accounts.tasks.sync_credentials',
#        'schedule': crontab(minute="30", hour="6-23", day_of_month="*", month_of_year="*", day_of_week="*"),
#    },
    'accounts.tasks.clear_old_stock_data': {
        # Remove old stock data on every weekday at 11:00AM
        'task': 'accounts.tasks.clear_old_stock_data',
        'schedule': crontab(minute="0", hour="11", day_of_month="*", month_of_year="*", day_of_week="1-5"),
    },
    'accounts.tasks.clear_old_stock_data_2': {
        # Remove old stock data on every weekday at 11:00AM
        'task': 'accounts.tasks.clear_old_stock_data_2',
        'schedule': crontab(minute="0", hour="11", day_of_month="*", month_of_year="*", day_of_week="1-5"),
    },
    'accounts.tasks.load_symbols': {
        # Remove old stock data on every weekday at 06:30AM
        'task': 'accounts.tasks.load_symbols',
        'schedule': crontab(minute="30", hour="6", day_of_month="*", month_of_year="*", day_of_week="1-5"),
    },
}
