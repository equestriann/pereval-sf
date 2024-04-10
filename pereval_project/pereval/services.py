def upload_path(instance, file):
    return f'photos/pereval_{instance.rel_pass.id}/{file}'