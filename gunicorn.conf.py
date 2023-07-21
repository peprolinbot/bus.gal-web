def on_starting(server):
    from buses import jobs
    jobs.start_scheduler()