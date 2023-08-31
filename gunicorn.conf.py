def on_starting(server):
    from main import jobs
    jobs.start_scheduler()