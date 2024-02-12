def ignore(fn):
    def wrapper(*args, **kwargs):
        try:
            res = fn(*args, **kwargs)

        except:
            print('err')
        return res
    return wrapper

